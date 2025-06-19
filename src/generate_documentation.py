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
from . import config
from . import markdown_generator



try:
    from .pbi_data_models import (
        Table, Column, CalculatedColumn, Measure, Relationship, Annotation,
        ReportPage, Visual, ReportFilter, FilterTarget, VisualFieldMapping,
        DataClassEncoder # Make sure this is imported
    )
except ImportError:
    print("ERROR: Could not import data models from pbi_data_models.py.")
    raise



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


# --- Data Loading Helper Functions ---

def _load_relationships(parsed_dir: Path) -> List[Relationship]:
    """Loads relationship data from the intermediate JSON file."""
    rel_file_path = parsed_dir / config.OUTPUT_RELATIONSHIPS_JSON_FILE
    raw_rels = load_json_file(rel_file_path)
    if not raw_rels:
        return []
    
    try:
        relationships = [Relationship(**rel_dict) for rel_dict in raw_rels]
        print(f"Loaded {len(relationships)} relationships from {rel_file_path.name}")
        return relationships
    except Exception as e:
        print(f"Error deserializing relationships: {e}")
        return []

def _load_model_summary(parsed_dir: Path) -> Dict[str, Any]:
    """Loads the model summary data from its intermediate JSON file."""
    summary_file_path = parsed_dir / config.OUTPUT_MODEL_SUMMARY_JSON_FILE
    model_summary = load_json_file(summary_file_path) or {}
    if model_summary:
        print(f"Loaded model summary from {summary_file_path.name}")
    return model_summary

def _load_all_tables(parsed_dir: Path) -> List[Table]:
    """Loads and deserializes all table data from their JSON files."""
    tables = []
    tables_dir_path = parsed_dir / config.OUTPUT_TABLES_JSON_SUBDIR
    if not tables_dir_path.is_dir():
        print(f"Warning: Tables directory not found: {tables_dir_path}")
        return []

    print(f"Loading table data from: {tables_dir_path}")
    for table_file in tables_dir_path.glob("*.json"):
        try:
            table_dict = load_json_file(table_file)
            if not table_dict:
                continue
            
            # Deserialize columns, measures, and annotations
            raw_columns = table_dict.get('columns', [])
            instantiated_columns = [Column(**col) for col in raw_columns] # Simplified for this example
            
            raw_measures = table_dict.get('measures', [])
            instantiated_measures = [Measure(**mea) for mea in raw_measures]

            raw_table_annotations = table_dict.pop('annotations', [])
            table_annotations = [Annotation(**ann) for ann in raw_table_annotations]
            
            # Create Table object
            table_dict.pop('columns', None); table_dict.pop('measures', None)
            table_obj = Table(
                **table_dict, 
                columns=instantiated_columns, 
                measures=instantiated_measures, 
                annotations=table_annotations
            )
            tables.append(table_obj)
        except Exception as e:
            print(f"Error loading/processing table {table_file.name}: {e}")
            traceback.print_exc()
            
    print(f"Loaded data for {len(tables)} tables.")
    return tables


def _load_report_layout(parsed_dir: Path) -> Tuple[List[ReportPage], List[ReportFilter]]:
    """Loads all report page and report-level filter data."""
    report_pages: List[ReportPage] = []
    report_level_filters: List[ReportFilter] = []
    
    report_layout_file_path = parsed_dir / config.OUTPUT_REPORT_LAYOUT_JSON_FILE
    print(f"\nLoading report layout data from: {report_layout_file_path.name}")
    report_layout_data = load_json_file(report_layout_file_path)

    if not report_layout_data:
        return report_pages, report_level_filters

    # Load Report Level Filters
    raw_report_filters = report_layout_data.get('reportLevelFilters', [])
    for filter_dict in raw_report_filters:
        try:
            target_obj = FilterTarget(**filter_dict.pop('target', {}))
            report_level_filters.append(ReportFilter(**filter_dict, target=target_obj))
        except Exception as e:
            print(f"ERROR deserializing a report-level filter: {e} - Data: {filter_dict}")
    
    # Load Pages and their contents
    raw_pages = report_layout_data.get('pages', [])
    for page_dict in raw_pages:
        try:
            # Page Filters
            raw_page_filters = page_dict.pop('page_level_filters', [])
            page_filter_objects = [ReportFilter(**f) for f in raw_page_filters] # Simplified
            
            # Visuals
            raw_visuals = page_dict.pop('visuals', [])
            visual_objects = [Visual(**v) for v in raw_visuals] # Simplified
            
            page_obj = ReportPage(
                **page_dict, 
                page_level_filters=page_filter_objects, 
                visuals=visual_objects
            )
            report_pages.append(page_obj)
        except Exception as e:
            print(f"ERROR processing page dictionary: {e}")

    print(f"Finished loading report layout. Loaded {len(report_level_filters)} report filters and {len(report_pages)} pages.")
    return report_pages, report_level_filters


# --- Main Data Loading Function (Orchestrator) ---

def load_parsed_data(parsed_dir: Path) -> Tuple[List[Relationship], List[Table], Dict[str, Any], List[ReportPage], List[ReportFilter]]:
    """
    Loads all model and report layout data from intermediate JSON files
    by orchestrating calls to specific data-loading helpers.
    """
    print(f"Loading all parsed data from: {parsed_dir}")
    
    # Call each helper function to load a specific part of the data
    relationships = _load_relationships(parsed_dir)
    tables = _load_all_tables(parsed_dir)
    model_summary = _load_model_summary(parsed_dir)
    report_pages, report_level_filters = _load_report_layout(parsed_dir)
    
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

# --- LLM Enrichment Helper Functions ---

async def _enrich_item(chain: RunnableSequence, params: dict, target_obj: Any, field_name: str, semaphore: asyncio.Semaphore):
    """
    Acquires a semaphore, calls an LLM chain for a single item, and assigns the result.
    This was formerly the nested helper _enrich_item_with_semaphore.
    """
    result_text = f"(Enrichment skipped for {field_name})"
    try:
        async with semaphore:
            # print(f"    Attempting LLM call for {field_name} on {getattr(target_obj, 'name', 'N/A')}")
            result = await chain.ainvoke(params)
            result_text = str(result).strip()
    except Exception as e:
        result_text = f"(Error during enrichment for {field_name}: {e})"
        print(f"    ERROR enriching {field_name} for {getattr(target_obj, 'name', 'N/A')}: {e}")
    finally:
        setattr(target_obj, field_name, result_text)

def _schedule_table_enrichment_tasks(table: Table, chains: dict, semaphore: asyncio.Semaphore) -> list:
    """Creates all the async enrichment tasks for a single table."""
    if table.isHidden:
        return []

    print(f"\nProcessing Visible Table: {table.name}")
    all_tasks = []
    
    # --- Table Description Task ---
    visible_cols = [col for col in table.columns if not col.isHidden]
    example_cols_str = ", ".join([f"{col.name} ({col.dataType})" for col in visible_cols[:10]]) or "N/A"
    all_tasks.append(_enrich_item(
        chains['table'], 
        {"table_name": table.name, "column_examples": example_cols_str},
        table, "llm_description", semaphore
    ))

    # --- Column and Calculated Column Tasks ---
    for column in visible_cols:
        all_tasks.append(_enrich_item(
            chains['column'],
            {"column_name": column.name, "data_type": column.dataType, "table_name": table.name,
             "table_description": lambda t=table: t.llm_description or "N/A"},
            column, "llm_description", semaphore
        ))
        if isinstance(column, CalculatedColumn) and column.daxExpression:
            all_tasks.append(_enrich_item(
                chains['dax'],
                {"item_name": f"Calculated Column: {column.name}", "dax_code": column.daxExpression},
                column, "llm_dax_explanation", semaphore
            ))

    # --- Measure Tasks ---
    visible_measures = [m for m in table.measures if not m.isHidden]
    for measure in visible_measures:
        if measure.daxExpression:
            all_tasks.append(_enrich_item(
                chains['dax'],
                {"item_name": f"Measure: {measure.name}", "dax_code": measure.daxExpression},
                measure, "llm_dax_explanation", semaphore
            ))
        else:
            measure.llm_dax_explanation = "(No DAX expression found)"
            
    return all_tasks


# --- Main LLM Enrichment Function (Orchestrator) ---

async def enrich_data_with_llm(llm: AzureChatOpenAI, tables: List[Table]):
    """
    Enriches table, column, and measure data with descriptions and explanations
    from an LLM, managing concurrency.
    """
    print("\n--- Enriching MODEL data with LLM (Async + Semaphore) ---")
    if not llm:
        print("  LLM not available, skipping enrichment.")
        return
        
    if any("Error: Could not load" in tpl for tpl in [TABLE_DESC_TEMPLATE_STR, COLUMN_DESC_TEMPLATE_STR, DAX_EXPLAIN_TEMPLATE_STR]):
        print("  Skipping enrichment due to errors loading prompt templates.")
        return

    # --- Setup Chains and Concurrency Limiter ---
    output_parser = StrOutputParser()
    chains = {
        'table': TABLE_DESC_TEMPLATE | llm | output_parser,
        'column': COLUMN_DESC_TEMPLATE | llm | output_parser,
        'dax': DAX_EXPLAIN_TEMPLATE | llm | output_parser
    }
    semaphore = asyncio.Semaphore(config.LLM_CONCURRENCY_LIMIT)
    print(f"  Concurrency limited to: {config.LLM_CONCURRENCY_LIMIT} parallel LLM calls")

    # --- Schedule All Tasks ---
    all_enrichment_tasks = []
    for table in tables:
        table_tasks = _schedule_table_enrichment_tasks(table, chains, semaphore)
        all_enrichment_tasks.extend(table_tasks)

    # --- Run All Tasks Concurrently ---
    if all_enrichment_tasks:
        print(f"\nRunning {len(all_enrichment_tasks)} enrichment tasks concurrently across all tables...")
        await asyncio.gather(*all_enrichment_tasks)
        print("Finished all concurrent enrichment tasks.")
    else:
        print("No enrichment tasks to run.")
        
    print("\n--- LLM Model Enrichment Complete ---")



# --- Filter Enrichment Helper Functions ---

async def _enrich_single_filter(filt: ReportFilter, chain: RunnableSequence, semaphore: asyncio.Semaphore):
    """
    Enriches a single filter object with an LLM-generated explanation.
    This was formerly the nested helper _enrich_filter_with_semaphore.
    """
    # Skip if there's no definition to explain, or if it already has one.
    if not filt.filter_definition or filt.llm_explanation:
        return

    target_desc = "this filter"
    if filt.target and filt.target.entity and filt.target.property:
        target_desc = f"the target `{filt.target.entity}`.`{filt.target.property}`"
    elif filt.target and filt.target.entity:
        target_desc = f"the target entity `{filt.target.entity}`"

    try:
        filter_def_str = json.dumps(filt.filter_definition, indent=2)
    except Exception:
        filter_def_str = str(filt.filter_definition)

    params = {
        "target_description": target_desc,
        "filter_definition_json": filter_def_str
    }
    await _enrich_item(chain, params, filt, "llm_explanation", semaphore)


# --- Main Filter Enrichment Function (Orchestrator) ---

async def enrich_filters_with_llm(llm: AzureChatOpenAI, report_filters: List[ReportFilter], pages: List[ReportPage]):
    """
    Enriches all filter objects (report, page, and visual level) with
    LLM-generated explanations.
    """
    print("\n--- Enriching Filters with LLM Explanations (Async + Semaphore) ---")
    if not llm:
        print("  LLM not available, skipping filter enrichment.")
        return
    if "Error: Could not load" in FILTER_EXPLAIN_TEMPLATE_STR:
        print("  Skipping filter enrichment due to error loading prompt template.")
        return

    # --- Setup Chain and Concurrency Limiter ---
    output_parser = StrOutputParser()
    filter_chain: RunnableSequence = FILTER_EXPLAIN_TEMPLATE | llm | output_parser
    semaphore = asyncio.Semaphore(config.LLM_CONCURRENCY_LIMIT)
    print(f"  Concurrency limited to: {config.LLM_CONCURRENCY_LIMIT} parallel LLM calls")

    # --- Collect All Filters ---
    all_filters_to_process = []
    all_filters_to_process.extend(report_filters)
    for page in pages:
        all_filters_to_process.extend(page.page_level_filters)
        for visual in page.visuals:
            all_filters_to_process.extend(visual.visual_level_filters)
            
    if not all_filters_to_process:
        print("No filters found to enrich.")
        print("\n--- LLM Filter Enrichment Complete ---")
        return
        
    # --- Schedule and Run All Tasks ---
    print(f"Scheduling {len(all_filters_to_process)} filter enrichment tasks...")
    enrichment_tasks = [_enrich_single_filter(filt, filter_chain, semaphore) for filt in all_filters_to_process]

    await asyncio.gather(*enrichment_tasks)
    print("Finished all concurrent filter enrichment tasks.")
    print("\n--- LLM Filter Enrichment Complete ---")



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


# Replace your old run_generation function with this one:
async def run_generation():
    """
    Main execution function for the documentation generation step.
    It loads data, runs AI enrichment, and then calls generators for
    each required output format (Markdown, JSON).
    """
    start_time = time.time()
    print(f"--- Starting Documentation Generation (generate_documentation.py) ---")
    
    # --- Setup ---
    parsed_dir = config.OUTPUT_DIR
    output_md_file = config.OUTPUT_DIR / config.FINAL_MARKDOWN_FILENAME
    output_json_file = config.OUTPUT_DIR / config.OUTPUT_FULL_DATA_JSON_FILE
    generate_md = 'md' in config.OUTPUT_FORMATS
    generate_json = 'json' in config.OUTPUT_FORMATS

    if not generate_md and not generate_json:
        print("WARNING: No output formats selected in config.OUTPUT_FORMATS. Skipping generation.")
        return

    # --- Step 1: Load Data ---
    print("\nStep G1: Loading Parsed JSON Data...")
    relationships, tables, model_summary, report_pages, report_level_filters = load_parsed_data(parsed_dir)
    if not tables and not report_pages:
        print("Error: No table or report page data loaded. Exiting generation step.")
        return

    # --- Step 2: AI Enrichment ---
    print("\nStep G2: Initializing LLM...")
    llm = initialize_llm()

    print("\nStep G3: Generating Model Overview...")
    overview_text = await generate_model_overview(llm, tables, relationships)

    print("\nStep G4: Enriching Model Data...")
    await enrich_data_with_llm(llm, tables)

    print("\nStep G4.5: Enriching Filter Definitions...")
    await enrich_filters_with_llm(llm, report_level_filters, report_pages)

    # --- Step 3: Output Generation ---
    if generate_md:
        print("\nStep G5: Assembling Final Markdown Report...")
        # This now calls the function in our new module
        markdown_generator.create_markdown_file(
            output_path=output_md_file,
            overview=overview_text,
            relationships=relationships,
            tables=tables,
            report_pages=report_pages,
            report_level_filters=report_level_filters
        )
    else:
        print("\nStep G5: Skipping Markdown Report generation (not in config.OUTPUT_FORMATS).")

    if generate_json:
        print("\nStep G6: Writing Full Data JSON Output...")
        write_full_json_output(
            output_path=output_json_file,
            overview=overview_text,
            relationships=relationships,
            tables=tables,
            report_pages=report_pages,
            report_level_filters=report_level_filters
        )
    else:
        print("\nStep G6: Skipping Full Data JSON generation (not in config.OUTPUT_FORMATS).")
        
    end_time = time.time()
    print(f"\n--- Documentation Generation Step Complete ---")
    print(f"Generation Time: {end_time - start_time:.2f} seconds")

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

