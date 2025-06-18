import asyncio
import json
import os
import time
import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import traceback

# Langchain and Azure OpenAI imports
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

# Import configuration settings
import config

# Import our data model classes
try:
    from pbi_data_models import (
        Table, Column, CalculatedColumn, Measure, Relationship, Annotation,
        ReportPage, Visual, ReportFilter, FilterTarget, VisualFieldMapping,
        DataClassEncoder # Make sure this is imported
    )
except ImportError:
    print("ERROR: Could not import data models from pbi_data_models.py.")
    raise

# --- Helper Functions ---
def slugify(text: str) -> str:
    if not text: return "section"
    text = str(text).lower()
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'[^\w\-]+', '', text)
    text = re.sub(r'\-+','-', text)
    text = text.strip('-')
    return text or "section"

def load_json_file(file_path: Path) -> Optional[Any]:
    if not file_path.is_file():
        # print(f"Info: JSON file not found, skipping: {file_path}") # Reduce noise
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('\ufeff'): content = content.lstrip('\ufeff')
            return json.loads(content)
    except json.JSONDecodeError as e: print(f"Warning: Error decoding JSON from {file_path.name}: {e}")
    except Exception as e: print(f"Warning: Error reading file {file_path.name}: {e}")
    return None

def parse_filter_target(expression_dict: Optional[Dict[str, Any]]) -> Optional[FilterTarget]:
    if not expression_dict: return None
    try:
        # Case 1: Simple Column Filter
        if "Column" in expression_dict:
            column_dict = expression_dict["Column"]; expression = column_dict.get("Expression"); source_ref = None
            if expression: 
                source_ref = expression.get("SourceRef")
            if source_ref is None:
                source_ref = column_dict.get("SourceRef")
            entity = None; property_name = column_dict.get("Property")
            if source_ref: 
                entity = source_ref.get("Entity") or source_ref.get("Source")
            if entity and property_name: 
                return FilterTarget(entity=entity, property=property_name)
        # Case 2: Aggregation Filter
        elif "Aggregation" in expression_dict:
            agg_dict = expression_dict["Aggregation"]; agg_func_map = {0: "Sum",
                                                                       1: "Avg",
                                                                       2: "Min",
                                                                       3: "Max",
                                                                       4: "Count",
                                                                       5: "CountNonNull",
                                                                       6: "Median",
                                                                       7: "StandardDeviation",
                                                                       8: "Variance"}
            agg_func_code = agg_dict.get("Function", -1);   
            agg_func_name = agg_func_map.get(agg_func_code, f"Agg{agg_func_code}")
            inner_expr = agg_dict.get("Expression")
            if inner_expr and "Column" in inner_expr:
                 column_dict = inner_expr["Column"]; expression = column_dict.get("Expression"); source_ref = None
                 if expression: 
                    source_ref = expression.get("SourceRef")
                 if source_ref is None:
                    source_ref = column_dict.get("SourceRef")
                 entity = None; property_name = column_dict.get("Property")
                 if source_ref:
                    entity = source_ref.get("Entity") or source_ref.get("Source")
                 if entity and property_name: 
                    return FilterTarget(entity=entity, property=f"{agg_func_name}({property_name})")
                 elif property_name: 
                    return FilterTarget(entity="Unknown", property=f"{agg_func_name}({property_name})")
            return FilterTarget(entity="Aggregation", property=agg_func_name)
        # Case 3: Measure Filter
        elif "Measure" in expression_dict:
             measure_dict = expression_dict["Measure"]; expression = measure_dict.get("Expression"); source_ref = None
             if expression:
                source_ref = expression.get("SourceRef")
             entity = None; property_name = measure_dict.get("Property")
             if source_ref:
                entity = source_ref.get("Entity") or source_ref.get("Source")
             if entity and property_name:
                return FilterTarget(entity=entity, property=f"[{property_name}]")
             elif property_name: 
                return FilterTarget(entity="Measure", property=f"[{property_name}]")
    except Exception as e: 
        print(f"Warning: Exception during filter target parsing: {e} - Data: {expression_dict}")
    return None

# --- Data Loading Function ---
def load_parsed_data(parsed_dir: Path) -> Tuple[List[Relationship], List[Table], Dict[str, Any], List[ReportPage], List[ReportFilter]]:
    """Loads all model and report layout data from intermediate JSON files. Includes visual filter debugging."""
    print(f"Loading parsed data from: {parsed_dir}")
    relationships, tables, model_summary, report_pages, report_level_filters = [], [], {}, [], []
    
    rel_file_path = parsed_dir / config.OUTPUT_RELATIONSHIPS_JSON_FILE
    try: # Relationship loading
        raw_rels = load_json_file(rel_file_path)
        if raw_rels:
            relationships = [Relationship(**rel_dict) for rel_dict in raw_rels]
        print(f"Loaded {len(relationships)} relationships from {rel_file_path.name}")
    except Exception as e:
        print(f"Error loading relationships: {e}")
    summary_file_path = parsed_dir / config.OUTPUT_MODEL_SUMMARY_JSON_FILE
    try: # Summary loading
        model_summary = load_json_file(summary_file_path) or {}
        print(f"Loaded model summary from {summary_file_path.name}")
    except Exception as e:
        print(f"Error loading model summary: {e}")
    tables_dir_path = parsed_dir / config.OUTPUT_TABLES_JSON_SUBDIR
    if tables_dir_path.is_dir():
        # Table loading loop
        print(f"Loading table data from: {tables_dir_path}")
        for table_file in tables_dir_path.glob("*.json"):
            try:
                table_dict = load_json_file(table_file)
                if not table_dict: 
                    continue
                instantiated_columns = [] # Column deserialization
                raw_columns = table_dict.get('columns', [])
                for col_dict in raw_columns:
                    raw_annotations = col_dict.pop('annotations', []);  
                    col_annotations = [Annotation(**ann_dict) for ann_dict in raw_annotations]
                    col_dict.setdefault('llm_description', None)
                    is_calc_col = col_dict.get('daxExpression') is not None and col_dict.get('sourceColumn') is None
                    if is_calc_col:
                        col_dict.setdefault('llm_dax_explanation', None); col_dict.setdefault('dataType', 'string')
                        col = CalculatedColumn(**col_dict)
                    else:
                        col_dict.pop('llm_dax_explanation', None); col_dict.pop('daxExpression', None)
                        col_dict.setdefault('dataType', 'string'); col_dict.setdefault('sourceColumn', None)
                        col = Column(**col_dict)
                    col.annotations = col_annotations; instantiated_columns.append(col)
                instantiated_measures = [] # Measure deserialization
                raw_measures = table_dict.get('measures', [])
                for mea_dict in raw_measures:
                     raw_annotations = mea_dict.pop('annotations', []); 
                     mea_annotations = [Annotation(**ann_dict) for ann_dict in raw_annotations]
                     mea_dict.setdefault('llm_description', None); mea_dict.setdefault('llm_dax_explanation', None); mea_dict.setdefault('daxExpression', '')
                     measure = Measure(**mea_dict); measure.annotations = mea_annotations; instantiated_measures.append(measure)
                raw_table_annotations = table_dict.pop('annotations', []) # Table annotation deserialization
                table_annotations = [Annotation(**ann_dict) for ann_dict in raw_table_annotations]
                table_dict.pop('columns', None); table_dict.pop('measures', None); table_dict.pop('annotations', None)
                table_dict.setdefault('llm_description', None)
                table_obj = Table(**table_dict, columns=instantiated_columns, measures=instantiated_measures, annotations=table_annotations)
                tables.append(table_obj)
            except Exception as e:
                print(f"Error loading/processing table {table_file.name}: {e}"); traceback.print_exc()
        print(f"Loaded data for {len(tables)} tables.")
    else: 
        print(f"Warning: Tables directory not found: {tables_dir_path}")

    # --- Load Report Layout Data ---
    report_layout_file_path = parsed_dir / config.OUTPUT_REPORT_LAYOUT_JSON_FILE
    print(f"\nLoading report layout data from: {report_layout_file_path.name}")
    try:
        report_layout_data = load_json_file(report_layout_file_path)
        if report_layout_data:
            # Report Level Filters (Simplified Loading)
            print("\n--- Loading Report Level Filters ---")
            raw_report_filters = report_layout_data.get('reportLevelFilters', [])
            for i, filter_dict in enumerate(raw_report_filters):
                try:
                    target_dict = filter_dict.pop('target', None); 
                    target_obj = FilterTarget(**target_dict) if target_dict else None
                    filter_dict.setdefault('level', 'Report'); filter_dict.setdefault('llm_explanation', None)
                    filt = ReportFilter(**filter_dict, target=target_obj); report_level_filters.append(filt)
                except Exception as filter_e:
                    print(f"  ERROR deserializing a report-level filter: {filter_e} - Data: {filter_dict}"); traceback.print_exc()
            print(f"Finished loading report filters. Loaded {len(report_level_filters)} filter objects.")

            # Pages (Simplified Filter Loading)
            print("\n--- Loading Pages ---")
            raw_pages = report_layout_data.get('pages', [])
            for page_dict_orig in raw_pages:
                page_dict = page_dict_orig.copy(); page_name_for_debug = page_dict.get('name', 'N/A')
                try:
                    # Page Filters
                    raw_page_filters = page_dict.pop('page_level_filters', []); page_filter_objects = []
                    for j, filter_dict in enumerate(raw_page_filters):
                         try:
                            target_dict = filter_dict.pop('target', None); target_obj = FilterTarget(**target_dict) if target_dict else None
                            filter_dict.setdefault('level', 'Page'); filter_dict.setdefault('llm_explanation', None)
                            filt = ReportFilter(**filter_dict, target=target_obj); page_filter_objects.append(filt)
                         except Exception as filter_e:
                             print(f"    ERROR deserializing a page-level filter on page '{page_name_for_debug}': {filter_e}")

                    # Visuals
                    raw_visuals = page_dict.pop('visuals', []); visual_objects = []
                    for visual_dict_orig in raw_visuals:
                        visual_dict = visual_dict_orig.copy(); visual_name_for_debug = visual_dict.get('name', 'N/A')
                        print(f"    DEBUG: Processing visual dict for '{visual_name_for_debug}': Keys={list(visual_dict.keys())}") # DEBUG Visual Dict Keys
                        try:
                            # --- Debug Visual Filters ---
                            print(f"      DEBUG: Attempting to pop 'visual_level_filters' for visual '{visual_name_for_debug}'")
                            # Pop using snake_case key
                            raw_visual_filters = visual_dict.pop('visual_level_filters', [])
                            print(f"      DEBUG: Popped 'visual_level_filters'. Found {len(raw_visual_filters)} raw visual filters.") # DEBUG Count
                            visual_filter_objects = []
                            for k, filter_dict in enumerate(raw_visual_filters):
                                print(f"        DEBUG: Deserializing visual filter {k+1}: {json.dumps(filter_dict)}") # DEBUG Raw Filter Dict
                                try:
                                    target_dict = filter_dict.pop('target', None)
                                    target_obj = FilterTarget(**target_dict) if target_dict else None
                                    filter_dict.setdefault('level', 'Visual'); filter_dict.setdefault('llm_explanation', None)
                                    filt = ReportFilter(**filter_dict, target=target_obj)
                                    print(f"        DEBUG: Created Visual ReportFilter object: {filt}") # DEBUG Created Object
                                    visual_filter_objects.append(filt)
                                except Exception as filter_e:
                                    print(f"      ERROR deserializing a visual-level filter in visual '{visual_name_for_debug}': {filter_e}")
                                    traceback.print_exc() # Show traceback for filter errors
                            print(f"      DEBUG: Finished processing visual filters for '{visual_name_for_debug}'. Created {len(visual_filter_objects)} objects.")
                            # --- End Debug Visual Filters ---

                            # Field Mappings
                            raw_field_mappings = visual_dict.pop('field_mappings', []); field_mapping_objects = []
                            for fm_dict in raw_field_mappings:
                                try:
                                    fm_dict.setdefault('role', 'Unknown'); field_mapping_objects.append(VisualFieldMapping(**fm_dict))
                                except Exception as fm_e:
                                    print(f"      ERROR processing a field mapping in visual '{visual_name_for_debug}': {fm_e}")

                            visual_dict.setdefault('llm_description', None)

                            # Create Visual Object - Pass the list we just created
                            vis_obj = Visual(**visual_dict,
                                             visual_level_filters=visual_filter_objects,
                                             field_mappings=field_mapping_objects)
                            visual_objects.append(vis_obj)
                        except Exception as visual_e:
                            print(f"    ERROR processing visual '{visual_name_for_debug}' on page '{page_name_for_debug}': {visual_e}"); traceback.print_exc()
                    # Create Page Object
                    page_obj = ReportPage(**page_dict, page_level_filters=page_filter_objects, visuals=visual_objects)
                    report_pages.append(page_obj)
                except Exception as page_e:
                    print(f"ERROR processing page dictionary for page '{page_name_for_debug}': {page_e}"); traceback.print_exc()
            print(f"\nFinished processing pages. Created {len(report_pages)} page objects.")
    except Exception as e:
        print(f"FATAL Error processing report layout file {report_layout_file_path.name}: {e}"); traceback.print_exc()
    return relationships, tables, model_summary, report_pages, report_level_filters

# --- LLM Initialization ---
def initialize_llm() -> Optional[AzureChatOpenAI]:
    # (Implementation uses config)
    print("Initializing Azure OpenAI LLM...")
    if not all([config.AZURE_OPENAI_ENDPOINT, 
                config.AZURE_OPENAI_API_KEY, 
                config.AZURE_OPENAI_API_VERSION, 
                config.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME]):
        print("Error: Missing Azure OpenAI environment variables (loaded from config).")
        return None
    try:
        llm = AzureChatOpenAI(
            azure_deployment=config.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME,
            openai_api_version=config.AZURE_OPENAI_API_VERSION,
            azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
            openai_api_key=config.AZURE_OPENAI_API_KEY,
            temperature=config.LLM_TEMPERATURE,
            max_tokens=config.LLM_MAX_TOKENS,
            request_timeout=config.LLM_REQUEST_TIMEOUT
        )
        print("LLM initialized successfully.")
        return llm
    except Exception as e: 
        print(f"Error initializing AzureChatOpenAI: {e}"); 
        traceback.print_exc(); 
        return None

# --- Function to Load Prompt Template from File ---
def load_prompt_template(template_path: Path) -> str:
    # (Implementation uses config)
    try:
        if not template_path.is_file(): 
            raise FileNotFoundError(f"Prompt template file not found: {template_path}")
        return template_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"ERROR: Failed to load prompt template from {template_path}: {e}"); 
        return "Error: Could not load prompt template. Input: {input}"

# --- LLM Prompt Templates (Load from Files) ---
try:
    TABLE_DESC_TEMPLATE_STR = load_prompt_template(config.PROMPT_TABLE_DESC_FILE)
    TABLE_DESC_TEMPLATE = ChatPromptTemplate.from_template(TABLE_DESC_TEMPLATE_STR)
    COLUMN_DESC_TEMPLATE_STR = load_prompt_template(config.PROMPT_COLUMN_DESC_FILE)
    COLUMN_DESC_TEMPLATE = ChatPromptTemplate.from_template(COLUMN_DESC_TEMPLATE_STR)
    DAX_EXPLAIN_TEMPLATE_STR = load_prompt_template(config.PROMPT_DAX_EXPLAIN_FILE)
    DAX_EXPLAIN_TEMPLATE = ChatPromptTemplate.from_template(DAX_EXPLAIN_TEMPLATE_STR)
    MODEL_OVERVIEW_TEMPLATE_STR = load_prompt_template(config.PROMPT_MODEL_OVERVIEW_FILE)
    MODEL_OVERVIEW_TEMPLATE = ChatPromptTemplate.from_template(MODEL_OVERVIEW_TEMPLATE_STR)
    FILTER_EXPLAIN_TEMPLATE_STR = load_prompt_template(config.PROMPT_FILTER_EXPLAIN_FILE)
    FILTER_EXPLAIN_TEMPLATE = ChatPromptTemplate.from_template(FILTER_EXPLAIN_TEMPLATE_STR)
    print("Successfully loaded LLM prompt templates from files.")
except Exception as e: 
    print(f"CRITICAL ERROR during prompt template loading: {e}. Exiting."); raise e

# --- Async Overview Generation Function ---
async def generate_model_overview(llm: AzureChatOpenAI,
                                 tables: List[Table],
                                 relationships: List[Relationship]) -> str:
    # (Implementation uses loaded template)
    print("\n--- Generating Model Overview ---")
    overview = "(Overview generation failed)"
    if not llm: 
        return "(LLM not available for overview)"
    output_parser = StrOutputParser()
    if "Error: Could not load" in MODEL_OVERVIEW_TEMPLATE_STR: 
        return "(Overview generation skipped: Error loading prompt template)"
    overview_chain: RunnableSequence = MODEL_OVERVIEW_TEMPLATE | llm | output_parser
    if not tables: 
        return "(Cannot generate overview: No table information available)"
    try:
        table_names = sorted([t.name for t in tables if not t.isHidden])
        table_list_str = ", ".join([f"'{name}'" for name in table_names])
        rel_summaries = []
        for i, rel in enumerate(relationships):
            from_table_visible = any(t.name == rel.fromTable and not t.isHidden for t in tables); 
            to_table_visible = any(t.name == rel.toTable and not t.isHidden for t in tables)
            if rel.isActive and from_table_visible and to_table_visible:
                if len(rel_summaries) >= 10: rel_summaries.append("..."); 
                break
                rel_summaries.append(f"'{rel.fromTable}' -> '{rel.toTable}' (on {rel.fromColumn}/{rel.toColumn})")
        relationship_summary_str = "\n".join(f"- {s}" for s in rel_summaries) or "- (No active relationships between visible tables found)"
        print("  Invoking LLM for overview (async)...")
        overview = await overview_chain.ainvoke({"table_list": table_list_str,"relationship_summary": relationship_summary_str})
        overview = overview.strip(); print(f"  Overview generated: {overview[:150]}...")
    except Exception as e: 
        print(f"  Error generating model overview: {e}"); overview = f"(Error generating overview: {e})"
    return overview

# --- Async Enrichment Function ---
async def enrich_data_with_llm(llm: AzureChatOpenAI, tables: List[Table]):
    """Enriches MODEL data. Uses config for concurrency limit."""
    print("\n--- Enriching MODEL data with LLM (Async + Semaphore) ---")
    if not llm:
        print("  LLM not available, skipping enrichment."); return
    if any("Error: Could not load" in tpl for tpl in [TABLE_DESC_TEMPLATE_STR, COLUMN_DESC_TEMPLATE_STR, DAX_EXPLAIN_TEMPLATE_STR]):
        print("  Skipping enrichment due to errors loading prompt templates.")
        return

    # Use config variable for concurrency
    semaphore = asyncio.Semaphore(config.LLM_CONCURRENCY_LIMIT)
    print(f"  Concurrency limited to: {config.LLM_CONCURRENCY_LIMIT} parallel LLM calls")

    output_parser = StrOutputParser()
    table_chain: RunnableSequence = TABLE_DESC_TEMPLATE | llm | output_parser
    column_chain: RunnableSequence = COLUMN_DESC_TEMPLATE | llm | output_parser
    dax_chain: RunnableSequence = DAX_EXPLAIN_TEMPLATE | llm | output_parser

    # Corrected nested helper function
    async def _enrich_item_with_semaphore(chain: RunnableSequence, params: dict, target_obj: Any, field_name: str):
        """Acquires semaphore, calls LLM chain, handles errors, assigns result."""
        result_text = f"(Enrichment skipped for {field_name})" # Default value
        try:
            async with semaphore: # Indented within try
                # print(f"    Attempting LLM call for {field_name} on {getattr(target_obj, 'name', 'N/A')}") # Debug
                result = await chain.ainvoke(params)
                result_text = str(result).strip()
                # print(f"    Finished LLM call for {field_name} on {getattr(target_obj, 'name', 'N/A')}") # Debug
        except Exception as e:
            result_text = f"(Error during enrichment for {field_name}: {e})"
            print(f"    ERROR enriching {field_name} for {getattr(target_obj, 'name', 'N/A')}: {e}")
        finally:
             setattr(target_obj, field_name, result_text)

    all_tasks = []
    for i, table in enumerate(tables):
        if table.isHidden: continue
        print(f"\nProcessing Visible Table {i+1}/{len(tables)}: {table.name}")
        # Schedule Table Description Task
        visible_cols = [col for col in table.columns if not col.isHidden]; 
        example_cols = [f"{col.name} ({col.dataType})" for col in visible_cols[:10]]; 
        example_cols_str = ", ".join(example_cols) if example_cols else "N/A"
        all_tasks.append(_enrich_item_with_semaphore(
            table_chain, {"table_name": table.name, 
                          "column_examples": example_cols_str}, 
                          table, "llm_description"))
        # Schedule Column/Measure Tasks
        for column in visible_cols:
            all_tasks.append(_enrich_item_with_semaphore(
                column_chain, 
                {"column_name": column.name,
                 "data_type": column.dataType,
                 "table_name": table.name,
                 "table_description": lambda t=table: t.llm_description or "N/A"},
                 column, "llm_description"))
            if isinstance(column, CalculatedColumn) and column.daxExpression: 
                all_tasks.append(_enrich_item_with_semaphore(
                    dax_chain, {"item_name": f"Calculated Column: {column.name}",
                                "dax_code": column.daxExpression},
                                column, "llm_dax_explanation"))
        visible_measures = [m for m in table.measures if not m.isHidden]
        for measure in visible_measures:
            if measure.daxExpression:
                all_tasks.append(_enrich_item_with_semaphore(
                    dax_chain, {"item_name": f"Measure: {measure.name}",
                                "dax_code": measure.daxExpression},
                                measure, "llm_dax_explanation"))
            else:
                measure.llm_dax_explanation = "(No DAX expression found)"
    # Run all collected tasks concurrently
    if all_tasks: 
        print(f"\nRunning {len(all_tasks)} enrichment tasks concurrently across all tables (Limit: {config.LLM_CONCURRENCY_LIMIT})..."); 
        await asyncio.gather(*all_tasks); 
        print(f"Finished all concurrent enrichment tasks.")
    else: 
        print("No enrichment tasks to run.")
    print("\n--- LLM Model Enrichment Complete ---")

# In generate_documentation.py

async def enrich_filters_with_llm(llm: AzureChatOpenAI, report_filters: List[ReportFilter], pages: List[ReportPage]):
    print("\n--- Enriching Filters with LLM Explanations (Async + Semaphore) ---")
    if not llm: 
        print("  LLM not available, skipping filter enrichment."); 
        return
    if "Error: Could not load" in FILTER_EXPLAIN_TEMPLATE_STR:
        print("  Skipping filter enrichment due to error loading prompt template.")
        return

    # Use the same semaphore logic as data enrichment
    semaphore = asyncio.Semaphore(config.LLM_CONCURRENCY_LIMIT)
    print(f"  Concurrency limited to: {config.LLM_CONCURRENCY_LIMIT} parallel LLM calls")

    output_parser = StrOutputParser()
    filter_chain: RunnableSequence = FILTER_EXPLAIN_TEMPLATE | llm | output_parser

    # Nested helper function (similar to data enrichment)
    async def _enrich_filter_with_semaphore(filt: ReportFilter):
        # Only enrich if there's a definition and no explanation yet
        if not filt.filter_definition or filt.llm_explanation:
            return # Skip if no definition or already has explanation

        # Optionally, only enrich 'Advanced' types or complex ones
        # if filt.filter_type != 'Advanced': return

        target_desc = "this filter"
        if filt.target and filt.target.entity and filt.target.property:
            target_desc = f"the target `{filt.target.entity}`.`{filt.target.property}`"
        elif filt.target and filt.target.entity:
             target_desc = f"the target entity `{filt.target.entity}`"

        # Convert definition dict to JSON string for the prompt
        try:
            filter_def_str = json.dumps(filt.filter_definition, indent=2)
        except Exception:
             filter_def_str = str(filt.filter_definition) # Fallback

        params = {
            "target_description": target_desc,
            "filter_definition_json": filter_def_str
        }
        result_text = f"(Explanation generation skipped for filter on {target_desc})"
        try:
            async with semaphore:
                # print(f"    Attempting LLM call for filter explanation on {target_desc}") # Debug
                result = await filter_chain.ainvoke(params)
                result_text = str(result).strip()
                # print(f"    Finished LLM call for filter explanation on {target_desc}") # Debug
        except Exception as e:
            result_text = f"(Error generating explanation for filter on {target_desc}: {e})"
            print(f"    ERROR enriching filter explanation for {target_desc}: {e}")
        finally:
             filt.llm_explanation = result_text # Assign successful explanation or error message

    # Collect all filter enrichment tasks
    all_tasks = []
    print("  Scheduling report-level filter enrichment...")
    for filt in report_filters:
        all_tasks.append(_enrich_filter_with_semaphore(filt))

    print("  Scheduling page and visual-level filter enrichment...")
    for page in pages:
        for filt in page.page_level_filters:
             all_tasks.append(_enrich_filter_with_semaphore(filt))
        for visual in page.visuals:
            for filt in visual.visual_level_filters:
                 all_tasks.append(_enrich_filter_with_semaphore(filt))

    # Run all collected tasks concurrently
    if all_tasks:
        print(f"\nRunning {len(all_tasks)} filter enrichment tasks concurrently (Limit: {config.LLM_CONCURRENCY_LIMIT})...")
        await asyncio.gather(*all_tasks)
        print(f"Finished all concurrent filter enrichment tasks.")
    else:
        print("No filter enrichment tasks to run.")
    print("\n--- LLM Filter Enrichment Complete ---")

# --- Report Assembly Function ---
def assemble_report(
    output_path: Path,
    overview: str,
    relationships: List[Relationship],
    tables: List[Table],
    report_pages: List[ReportPage],
    report_level_filters: List[ReportFilter]
):
    print(f"\n--- Assembling Markdown report: {output_path} ---")

    # Replace the existing format_filter helper function with this one:
    
    def format_filter(filt: ReportFilter) -> str:
        """Formats the ReportFilter object into a readable string, prioritizing LLM explanation."""
        target_str = "Unknown Target"
        if filt.target and filt.target.entity and filt.target.property:
             target_str = f"`{filt.target.entity}`.`{filt.target.property}`"
        elif filt.target and filt.target.entity:
             target_str = f"`{filt.target.entity}` (Property missing)"
        elif filt.name: # Fallback to filter name
             target_str = f"(Name: `{filt.name}`)"

        filter_type_str = str(filt.filter_type) if filt.filter_type else 'N/A'

        if filt.llm_explanation and "Error" not in filt.llm_explanation and "skipped" not in filt.llm_explanation:
             # Use the LLM explanation directly if available and seems valid
             definition_summary = f"Explanation: {filt.llm_explanation}"
             return f"Filter on {target_str} (Type: {filter_type_str}, {definition_summary})"

        # --- Fallback to Parsing Definition ---
        definition_summary = "N/A"
        if filt.filter_definition and isinstance(filt.filter_definition, dict):
            try:
                where_clauses = filt.filter_definition.get("Where", [])
                conditions = []
                for clause in where_clauses:
                    condition_obj = clause.get("Condition", {})
                    condition_summary = "(Unparsed condition)"
                    is_negated = False
                    if "Not" in condition_obj:
                        is_negated = True
                        condition_obj = condition_obj.get("Not", {}).get("Expression", {})

                    comparison = condition_obj.get("Comparison")
                    in_cond = condition_obj.get("In")

                    if comparison and isinstance(comparison, dict):
                        comp_kind = comparison.get("ComparisonKind", -1)
                        left_expr_str = "N/A"; left_obj = comparison.get("Left", {})
                        if "Column" in left_obj:
                            left_expr_str = left_obj.get("Column", {}).get("Property", "N/A")
                        elif "Measure" in left_obj:
                            measure_prop = left_obj.get('Measure', {}).get('Property', 'N/A'); left_expr_str = f"[{measure_prop}]"
                        elif "Aggregation" in left_obj:
                             agg_dict = left_obj["Aggregation"];    
                             agg_func_map = {0: "Sum", 1: "Avg", 2: "Min", 3: "Max", 4: "Count", 5: "CountNonNull"}
                             agg_func_code = agg_dict.get("Function", -1); 
                             agg_func_name = agg_func_map.get(agg_func_code, f"Agg{agg_func_code}")
                             inner_prop = agg_dict.get("Expression",{}).get("Column",{}).get("Property", "?");  
                             left_expr_str = f"{agg_func_name}({inner_prop})"

                        right_val = comparison.get("Right", {}).get("Literal", {}).get("Value", "N/A")
                        right_val_str = "null" if isinstance(right_val, str) and right_val.lower() == 'null' else f"`{right_val}`"
                        op_map = {0: "=", 1: "<>", 2: ">", 3: ">=", 4: "<", 5: "<="};   
                        op = op_map.get(comp_kind, f"Kind({comp_kind})")
                        condition_summary = f"`{left_expr_str}` {op} {right_val_str}"

                    elif in_cond and isinstance(in_cond, dict):
                        left_expr_obj = in_cond.get("Expressions", [{}])[0]; 
                        left_expr_str = "N/A"
                        if "Column" in left_expr_obj:
                            left_expr_str = left_expr_obj.get("Column", {}).get("Property", "N/A")
                        elif "Measure" in left_expr_obj:
                            measure_prop = left_expr_obj.get('Measure', {}).get('Property', 'N/A');
                            left_expr_str = f"[{measure_prop}]"
                        values = in_cond.get("Values", [[]])[0]; 
                        value_str = ", ".join([f"`{v.get('Literal',{}).get('Value', '?')}`" for v in values[:5]])
                        if len(values) > 5: 
                            value_str += ", ..."; 
                            condition_summary = f"`{left_expr_str}` IN ({value_str})"

                    if is_negated and condition_summary != "(Unparsed condition)": 
                        condition_summary = f"NOT ({condition_summary})"
                    conditions.append(condition_summary)

                if conditions:
                    definition_summary = " AND ".join(conditions)
                else:
                    definition_summary = "(Could not parse conditions)"

            except Exception as e:
                print(f"WARNING: Error parsing filter definition for filter '{filt.name}': {e}");   
                filter_def_str_raw = json.dumps(filt.filter_definition)
                if len(filter_def_str_raw) > 100:
                    filter_def_str_raw = filter_def_str_raw[:100] + "...";  
                    definition_summary = f"(Raw JSON: `{filter_def_str_raw}`)"
        elif filt.filter_definition:
            definition_summary = f"(Non-dict definition: `{str(filt.filter_definition)[:100]}`)"

        # Assemble final string using parsed definition if LLM explanation wasn't available/used
        return f"Filter on {target_str} (Type: {filter_type_str}, Definition: {definition_summary})"


    def format_mapping(mapping: VisualFieldMapping) -> str:
         """Formats the VisualFieldMapping object into a readable string."""
         display = mapping.display_name or mapping.query_ref or "N/A";  
         role_str = str(mapping.role) if mapping.role else 'N/A'
         query_ref_info = f" (Query: `{mapping.query_ref}`)" if mapping.display_name and mapping.query_ref and mapping.display_name != mapping.query_ref else ""
         return f"`{display}`{query_ref_info} (Role: {role_str})"

    try: # Main report writing block
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Power BI Model & Report Documentation\n\n")
            f.write(f"*Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n")

            # --- Table of Contents ---
            f.write("## Table of Contents\n\n")
            f.write("- [Overview](#overview)\n")
            f.write("- [Data Model](#data-model)\n")
            f.write("  - [Relationships](#relationships)\n")
            f.write("  - [Tables](#tables)\n")
            sorted_visible_tables = sorted([t for t in tables if not t.isHidden], key=lambda t:
                                            t.name.lower())
            # Use a simple loop for table links
            for table in sorted_visible_tables:
                 f.write(f"    - [{table.name}](#{slugify(f'table-{table.name}')})\n")

            f.write("- [Report Structure](#report-structure)\n")
            if report_level_filters:
                f.write("  - [Report Level Filters](#report-level-filters)\n")

            sorted_pages_toc = sorted(report_pages, key=lambda p: p.ordinal)
            if sorted_pages_toc:
                 f.write("  - [Report Pages](#report-pages)\n")
                 # Use a standard for loop
                 for page in sorted_pages_toc:
                     page_title_toc = page.display_name or page.name or f"Page_{page.ordinal}"
                     page_anchor = slugify(f"page-{page_title_toc}")
                     f.write(f"    - [{page_title_toc}](#{page_anchor})\n")

            f.write("\n---\n\n")

            # --- Overview Section ---
            f.write("## <a name=\"overview\"></a>Overview\n\n"); 
            f.write(f"{overview}\n\n"); 
            f.write("---\n\n")

            # --- Data Model Section ---
            f.write("## <a name=\"data-model\"></a>Data Model\n\n");    
            f.write("### <a name=\"relationships\"></a>Relationships\n\n")
            # Relationship rendering logic
            if relationships:
                 active_rels = [r for r in relationships if r.isActive];    
                 inactive_rels = [r for r in relationships if not r.isActive];  
                 sorted_rels = sorted(
                     active_rels, key=lambda r:
                      (r.fromTable.lower(), r.fromColumn.lower())) + sorted(
                          inactive_rels, key=lambda r:
                          (r.fromTable.lower(), r.fromColumn.lower()))
                 if sorted_rels:
                     f.write("The following relationships link the tables:\n\n")
                     for rel in sorted_rels:
                        from_table_hidden = any(t.name == rel.fromTable and t.isHidden for t in tables);    
                        to_table_hidden = any(t.name == rel.toTable and t.isHidden for t in tables); 
                        hidden_note = " (Involves hidden table)" if from_table_hidden or to_table_hidden else "";   
                        details = []; [details.append("**Inactive**") for _ in [1] if not rel.isActive];    
                        [details.append(f"Filter: {rel.crossFilteringBehavior}") for _ in [1] if rel.crossFilteringBehavior != 'singleDirection'];  	
                        details_str = f" ({', '.join(details)})" if details else "";    
                        f.write(f"* `{rel.fromTable}`.[`{rel.fromColumn}`] -> `{rel.toTable}`.[`{rel.toColumn}`]{details_str}{hidden_note}\n")
                     f.write("\n")
                 else: f.write("_No relationships were found or parsed._\n\n")
            else: f.write("_No relationships were found or parsed._\n\n"); 
            f.write("---\n\n")
            f.write("### <a name=\"tables\"></a>Tables\n\n") # Tables rendering
            if sorted_visible_tables:
                 for table in sorted_visible_tables:
                     table_slug = slugify(f"table-{table.name}"); 
                     f.write(f"#### <a name=\"{table_slug}\"></a>Table: `{table.name}`\n\n"); 
                     desc = table.llm_description or table.description or "_No description available._";    
                     f.write(f"{desc}\n\n")

                     # --- Columns (Corrected Loop) ---
                     visible_columns = sorted(
                         [col for col in table.columns if not col.isHidden and not isinstance(col, CalculatedColumn)], key=lambda c:
                          c.name.lower())
                     if visible_columns:
                         f.write("##### Columns\n\n")
                         f.write("| Name | Data Type | Description (Generated) |\n")
                         f.write("|------|-----------|-------------------------|\n")
                         # Use a standard for loop to avoid backslash in f-string expression
                         for col in visible_columns:
                             col_desc = col.llm_description or col.description or " "
                             # Escape pipe characters for Markdown table
                             col_desc_escaped = col_desc.replace('|', '\\|').replace('\n', ' ') # Also replace newlines
                             f.write(f"| `{col.name}` | `{col.dataType}` | {col_desc_escaped} |\n")
                         f.write("\n")
                     # --- End Corrected Loop ---

                     # Calculated Columns...
                     visible_calc_columns = sorted(
                         [col for col in table.columns if not col.isHidden and isinstance(col, CalculatedColumn)], key=lambda c:
                           c.name.lower())
                     if visible_calc_columns: 
                        f.write("##### Calculated Columns\n\n");    
                        [(f.write(f"**`{col.name}`** (`{col.dataType}`)\n\n"),
                          [f.write(f"- **Description:** {col_desc}\n") for col_desc in [col.llm_description or col.description] if col_desc],
                           [f.write(f"- **DAX Expression:**\n```dax\n{col.daxExpression.strip()}\n```\n") for _ in [1] if col.daxExpression],
                            [f.write(f"- **DAX Explanation (Generated):** {dax_expl}\n") for dax_expl in [col.llm_dax_explanation] if dax_expl],
                            f.write("\n") ) for col in visible_calc_columns]
                        
                     # Measures...
                     visible_measures = sorted(
                         [m for m in table.measures if not m.isHidden], 
                         key=lambda m:
                         m.name.lower())
                     if visible_measures:
                        f.write("##### Measures\n\n");  
                        [(f.write(f"**`{measure.name}`**\n\n"),
                          [f.write(f"- **Description (Generated):** {mea_desc}\n") for mea_desc in [measure.llm_description] if mea_desc],
                          [f.write(f"- **DAX Expression:**\n```dax\n{measure.daxExpression.strip()}\n```\n") for _ in [1] if measure.daxExpression],
                          [f.write(f"- **DAX Explanation (Generated):** {dax_expl}\n") for dax_expl in [measure.llm_dax_explanation] if dax_expl],
                          f.write("\n")) for measure in visible_measures]
                     f.write("---\n\n")
            else: f.write("_No visible table details were loaded or parsed._\n\n")

            # --- Report Structure Section ---
            f.write("## <a name=\"report-structure\"></a>Report Structure\n\n")
            # Report Level Filters...
            if report_level_filters: 
                f.write("### <a name=\"report-level-filters\"></a>Report Level Filters\n\n"); 
                f.write("The following filters are applied to the entire report:\n\n"); 
                [f.write(f"- {format_filter(filt)}\n") for filt in report_level_filters];   
                f.write("\n")
            else:
                f.write("_No report-level filters found._\n\n")
            # Report Pages...
            if report_pages:
                 f.write("### <a name=\"report-pages\"></a>Report Pages\n\n");  
                 sorted_pages_body = sorted(
                     report_pages, key=lambda p:
                     (p.display_name or p.name or "").lower())
                 for page in sorted_pages_body:
                     page_title = page.display_name or page.name or "Unnamed Page"; 
                     page_slug = slugify(f"page-{page_title}"); 
                     f.write(f"#### <a name=\"{page_slug}\"></a>Page: {page_title}\n\n");   
                     f.write(f"*Internal Name: `{page.name}`, Ordinal: {page.ordinal}*\n\n")
                     # Page Filters...
                     if page.page_level_filters:
                        f.write("##### Page Level Filters\n\n");    
                        [f.write(f"- {format_filter(filt)}\n") for filt in page.page_level_filters]; 
                        f.write("\n")
                     # Visuals...
                     if page.visuals:
                         f.write("##### Visuals on this Page\n\n"); 
                         sorted_visuals = sorted(
                             page.visuals, key=lambda v:
                             (v.y or 0, v.x or 0))
                         for visual in sorted_visuals:
                             visual_title = visual.title or visual.visual_type or visual.name or "Unnamed Visual";  
                             f.write(f"**{visual_title}**\n\n");    
                             f.write(f"- Type: `{visual.visual_type}`\n");  
                             f.write(f"- Name: `{visual.name}`\n")
                             if visual.llm_description: 
                                 f.write(f"- Description (Generated): {visual.llm_description}\n")
                             if visual.field_mappings: 
                                f.write("- Fields Used:\n");    
                                [f.write(f"  - {format_mapping(mapping)}\n") for mapping in visual.field_mappings]
                             else: 
                                 f.write("- Fields Used: _(None detected)_\n")
                             if visual.visual_level_filters: 
                                f.write("- Visual Level Filters:\n"); 
                                [f.write(f"  - {format_filter(filt)}\n") for filt in visual.visual_level_filters]
                             f.write("\n")
                     else: 
                        f.write("_No visuals found on this page._\n\n"); 
                        f.write("\n---\n\n")
            else:
                f.write("_No page details were loaded or parsed._\n\n")

        print(f"Documentation successfully written to {output_path}")
    except Exception as e:
        print(f"FATAL ERROR writing documentation file: {e}")
        traceback.print_exc()

# --- Function to Write Full Data JSON Output ---
def write_full_json_output(output_path: Path, 
                           overview: str, 
                           relationships: List[Relationship], 
                           tables: List[Table], 
                           report_pages: List[ReportPage],
                           report_level_filters: List[ReportFilter]):
    # (Implementation uses config and DataClassEncoder)
    print(f"\n--- Writing full data JSON output to: {output_path} ---")
    full_data = {"model_overview": overview,
                 "relationships": relationships,
                 "tables": tables,
                 "report_level_filters": report_level_filters,
                 "pages": report_pages}
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(full_data, f, cls=DataClassEncoder, indent=2, ensure_ascii=False)
        print(f"Successfully wrote full data JSON to {output_path}")
    except TypeError as e: 
        print(f"ERROR writing full data JSON file {output_path}: TypeError - {e}"); print("This might indicate an issue with serializing a specific data type."); traceback.print_exc()
    except Exception as e: 
        print(f"ERROR writing full data JSON file {output_path}: {e}"); traceback.print_exc()


# --- Main Execution Function ---
async def run_generation():
    # (Implementation uses config and calls conditional output functions)
    start_time = time.time(); print(f"--- Starting Documentation Generation (generate_documentation.py) ---")
    parsed_dir = config.OUTPUT_DIR; 
    output_md_file = config.OUTPUT_DIR / config.OUTPUT_MARKDOWN_FILE; 
    output_json_file = config.OUTPUT_DIR / config.OUTPUT_FULL_DATA_JSON_FILE
    generate_md = 'md' in config.OUTPUT_FORMATS; 
    generate_json = 'json' in config.OUTPUT_FORMATS
    if not generate_md and not generate_json: 
        ("WARNING: No output formats selected in config.OUTPUT_FORMATS. Skipping generation."); return
    print("\nStep G1: Loading Parsed JSON Data..."); 
    relationships, tables, model_summary, report_pages, report_level_filters = load_parsed_data(parsed_dir)
    if not tables and not report_pages:
        print("Error: No table or report page data loaded. Exiting generation step."); return
    print("\nStep G2: Initializing LLM..."); 
    llm = initialize_llm()
    print("\nStep G3: Generating Model Overview..."); 
    overview_text = await generate_model_overview(llm, tables, relationships)
    print("\nStep G4: Enriching Model Data..."); 
    await enrich_data_with_llm(llm, tables)
    print("\nStep G4.5: Enriching Filter Definitions...")
    await enrich_filters_with_llm(llm, report_level_filters, report_pages)
    if generate_md:
        print("\nStep G5: Assembling Final Markdown Report..."); 
        assemble_report(output_path=output_md_file,
                        overview=overview_text,
                        relationships=relationships,
                        tables=tables,
                        report_pages=report_pages,
                        report_level_filters=report_level_filters)
    else: 
        print("\nStep G5: Skipping Markdown Report generation (not in config.OUTPUT_FORMATS).")
    if generate_json:
        print("\nStep G6: Writing Full Data JSON Output...");   
        write_full_json_output(
            output_path=output_json_file,
            overview=overview_text,
            relationships=relationships,
            tables=tables,
            report_pages=report_pages,
            report_level_filters=report_level_filters)
    else: 
        print("\nStep G6: Skipping Full Data JSON generation (not in config.OUTPUT_FORMATS).")
    end_time = time.time(); 
    print(f"\n--- Documentation Generation Step Complete ---"); 
    print(f"Generation Time: {end_time - start_time:.2f} seconds")
    if generate_md: 
        print(f"Markdown Output: {output_md_file}")
    if generate_json: 
        print(f"JSON Output:     {output_json_file}")

# --- Entry Point ---
if __name__ == "__main__":
    # (Implementation handles asyncio loop)
    print("Running generate_documentation.py independently...")
    try:
        try: 
            loop = asyncio.get_running_loop()
        except RuntimeError: 
            loop = asyncio.new_event_loop(); 
            asyncio.set_event_loop(loop)
        loop.run_until_complete(run_generation())
    except Exception as main_e:
        print(f"\nAn error occurred during independent execution: {main_e}"); traceback.print_exc(); exit(1)
    finally:
         if 'loop' in locals() and not loop.is_running():
             try: 
                loop.close(); asyncio.set_event_loop(None)
             except Exception as loop_e:
                 print(f"Error closing event loop: {loop_e}")

