import json
import time
import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# Import the data models and config from our other project files
from . import config
from .pbi_data_models import (
    Table, Column, CalculatedColumn, Measure, Relationship, Annotation,
    ReportPage, Visual, ReportFilter, FilterTarget, VisualFieldMapping
)

# --- Helper Functions ---
def slugify(text: str) -> str:
    if not text: return "section"
    text = str(text).lower()
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'[^\w\-]+', '', text)
    text = re.sub(r'\-+','-', text)
    text = text.strip('-')
    return text or "section"

# --- Markdown Assembly Helper Functions ---

def _format_filter(filt: ReportFilter) -> str:
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


def _format_mapping(mapping: VisualFieldMapping) -> str:
     """Formats the VisualFieldMapping object into a readable string."""
     display = mapping.display_name or mapping.query_ref or "N/A";
     role_str = str(mapping.role) if mapping.role else 'N/A'
     query_ref_info = f" (Query: `{mapping.query_ref}`)" if mapping.display_name and mapping.query_ref and mapping.display_name != mapping.query_ref else ""
     return f"`{display}`{query_ref_info} (Role: {role_str})"


def _write_table_of_contents(f, tables: List[Table], report_pages: List[ReportPage], report_level_filters: List[ReportFilter]):
    """Writes the Table of Contents section to the markdown file."""
    f.write("## Table of Contents\n\n")
    f.write("- [Overview](#overview)\n")
    f.write("- [Data Model](#data-model)\n")
    f.write("  - [Relationships](#relationships)\n")
    f.write("  - [Tables](#tables)\n")
    sorted_visible_tables = sorted([t for t in tables if not t.isHidden], key=lambda t: t.name.lower())
    for table in sorted_visible_tables:
         f.write(f"    - [{table.name}](#{slugify(f'table-{table.name}')})\n")

    f.write("- [Report Structure](#report-structure)\n")
    if report_level_filters:
        f.write("  - [Report Level Filters](#report-level-filters)\n")

    sorted_pages_toc = sorted(report_pages, key=lambda p: p.ordinal)
    if sorted_pages_toc:
         f.write("  - [Report Pages](#report-pages)\n")
         for page in sorted_pages_toc:
             page_title_toc = page.display_name or page.name or f"Page_{page.ordinal}"
             page_anchor = slugify(f"page-{page_title_toc}")
             f.write(f"    - [{page_title_toc}](#{page_anchor})\n")
    f.write("\n---\n\n")


def _write_overview(f, overview: str):
    """Writes the Overview section."""
    f.write("## <a name=\"overview\"></a>Overview\n\n")
    f.write(f"{overview}\n\n")
    f.write("---\n\n")


def _write_relationships(f, relationships: List[Relationship], tables: List[Table]):
    """Writes the Data Model Relationships section."""
    f.write("## <a name=\"data-model\"></a>Data Model\n\n")
    f.write("### <a name=\"relationships\"></a>Relationships\n\n")
    if not relationships:
        f.write("_No relationships were found or parsed._\n\n")
        f.write("---\n\n")
        return

    active_rels = [r for r in relationships if r.isActive]
    inactive_rels = [r for r in relationships if not r.isActive]
    sorted_rels = sorted(active_rels, key=lambda r: (r.fromTable.lower(), r.fromColumn.lower())) + \
                  sorted(inactive_rels, key=lambda r: (r.fromTable.lower(), r.fromColumn.lower()))
    
    if sorted_rels:
        f.write("The following relationships link the tables:\n\n")
        for rel in sorted_rels:
            from_table_hidden = any(t.name == rel.fromTable and t.isHidden for t in tables)
            to_table_hidden = any(t.name == rel.toTable and t.isHidden for t in tables)
            hidden_note = " (Involves hidden table)" if from_table_hidden or to_table_hidden else ""
            details = []
            if not rel.isActive: details.append("**Inactive**")
            if rel.crossFilteringBehavior != 'singleDirection': details.append(f"Filter: {rel.crossFilteringBehavior}")
            details_str = f" ({', '.join(details)})" if details else ""
            f.write(f"* `{rel.fromTable}`.[`{rel.fromColumn}`] -> `{rel.toTable}`.[`{rel.toColumn}`]{details_str}{hidden_note}\n")
        f.write("\n")
    else:
        f.write("_No relationships were found or parsed._\n\n")
    f.write("---\n\n")


def _write_tables_section(f, tables: List[Table]):
    """Writes the documentation for all visible tables, their columns, and measures."""
    f.write("### <a name=\"tables\"></a>Tables\n\n")
    sorted_visible_tables = sorted([t for t in tables if not t.isHidden], key=lambda t: t.name.lower())
    if not sorted_visible_tables:
        f.write("_No visible table details were loaded or parsed._\n\n")
        f.write("---\n\n")
        return

    for table in sorted_visible_tables:
        table_slug = slugify(f"table-{table.name}")
        f.write(f"#### <a name=\"{table_slug}\"></a>Table: `{table.name}`\n\n")
        desc = table.llm_description or table.description or "_No description available._"
        f.write(f"{desc}\n\n")

        # --- Columns ---
        visible_columns = sorted(
            [col for col in table.columns if not col.isHidden and not isinstance(col, CalculatedColumn)], key=lambda c:
             c.name.lower())
        if visible_columns:
            f.write("##### Columns\n\n")
            f.write("| Name | Data Type | Description (Generated) |\n")
            f.write("|------|-----------|-------------------------|\n")
            for col in visible_columns:
                col_desc = col.llm_description or col.description or " "
                col_desc_escaped = col_desc.replace('|', '\\|').replace('\n', ' ')
                f.write(f"| `{col.name}` | `{col.dataType}` | {col_desc_escaped} |\n")
            f.write("\n")

        # --- Calculated Columns ---
        visible_calc_columns = sorted(
            [col for col in table.columns if not col.isHidden and isinstance(col, CalculatedColumn)], key=lambda c:
              c.name.lower())
        if visible_calc_columns:
           f.write("##### Calculated Columns\n\n")
           for col in visible_calc_columns:
                f.write(f"**`{col.name}`** (`{col.dataType}`)\n\n")
                if col.llm_description or col.description:
                    f.write(f"- **Description:** {col.llm_description or col.description}\n")
                if col.daxExpression:
                    f.write(f"- **DAX Expression:**\n```dax\n{col.daxExpression.strip()}\n```\n")
                if col.llm_dax_explanation:
                    f.write(f"- **DAX Explanation (Generated):** {col.llm_dax_explanation}\n")
                f.write("\n")
                   
        # --- Measures ---
        visible_measures = sorted(
            [m for m in table.measures if not m.isHidden],
            key=lambda m:
            m.name.lower())
        if visible_measures:
           f.write("##### Measures\n\n")
           for measure in visible_measures:
                f.write(f"**`{measure.name}`**\n\n")
                if measure.llm_description:
                    f.write(f"- **Description (Generated):** {measure.llm_description}\n")
                if measure.daxExpression:
                    f.write(f"- **DAX Expression:**\n```dax\n{measure.daxExpression.strip()}\n```\n")
                if measure.llm_dax_explanation:
                    f.write(f"- **DAX Explanation (Generated):** {measure.llm_dax_explanation}\n")
                f.write("\n")
        f.write("---\n\n")


def _write_report_structure_section(f, report_level_filters: List[ReportFilter], report_pages: List[ReportPage]):
    """Writes the entire Report Structure section, including filters and pages."""
    f.write("## <a name=\"report-structure\"></a>Report Structure\n\n")
    
    # Report Level Filters
    if report_level_filters:
        f.write("### <a name=\"report-level-filters\"></a>Report Level Filters\n\n")
        f.write("The following filters are applied to the entire report:\n\n")
        for filt in report_level_filters:
            f.write(f"- {_format_filter(filt)}\n")
        f.write("\n")
    else:
        f.write("_No report-level filters found._\n\n")
        
    # Report Pages
    if not report_pages:
        f.write("_No page details were loaded or parsed._\n\n")
        return
        
    f.write("### <a name=\"report-pages\"></a>Report Pages\n\n")
    sorted_pages_body = sorted(
        report_pages, key=lambda p:
        (p.display_name or p.name or "").lower())
    
    for page in sorted_pages_body:
        page_title = page.display_name or page.name or "Unnamed Page"
        page_slug = slugify(f"page-{page_title}")
        f.write(f"#### <a name=\"{page_slug}\"></a>Page: {page_title}\n\n")
        f.write(f"*Internal Name: `{page.name}`, Ordinal: {page.ordinal}*\n\n")
        
        # Page Filters
        if page.page_level_filters:
            f.write("##### Page Level Filters\n\n")
            for filt in page.page_level_filters:
                f.write(f"- {_format_filter(filt)}\n")
            f.write("\n")
            
        # Visuals on Page
        if page.visuals:
            f.write("##### Visuals on this Page\n\n")
            sorted_visuals = sorted(
                page.visuals, key=lambda v:
                (v.y or 0, v.x or 0))
            for visual in sorted_visuals:
                visual_title = visual.title or visual.visual_type or visual.name or "Unnamed Visual"
                f.write(f"**{visual_title}**\n\n")
                f.write(f"- Type: `{visual.visual_type}`\n")
                f.write(f"- Name: `{visual.name}`\n")
                if visual.llm_description:
                    f.write(f"- Description (Generated): {visual.llm_description}\n")
                
                if visual.field_mappings:
                    f.write("- Fields Used:\n")
                    for mapping in visual.field_mappings:
                        f.write(f"  - {_format_mapping(mapping)}\n")
                else:
                    f.write("- Fields Used: _(None detected)_\n")
                    
                if visual.visual_level_filters:
                    f.write("- Visual Level Filters:\n")
                    for filt in visual.visual_level_filters:
                        f.write(f"  - {_format_filter(filt)}\n")
                f.write("\n")
        else:
            f.write("_No visuals found on this page._\n\n")
    f.write("\n---\n\n")

def create_markdown_file(
    output_path: Path,
    overview: str,
    relationships: List[Relationship],
    tables: List[Table],
    report_pages: List[ReportPage],
    report_level_filters: List[ReportFilter]
):
    """
    Assembles the final Markdown report from all the parsed and enriched data.

    This function coordinates calls to various helper functions to write each
    section of the report in the correct order.
    """
    print(f"\n--- Assembling Markdown report: {output_path} ---")
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            # Write the main report header
            f.write("# Power BI Model & Report Documentation\n\n")
            f.write(f"*Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}*\n\n")

            # Write each major section using a dedicated helper function
            _write_table_of_contents(f, tables, report_pages, report_level_filters)
            _write_overview(f, overview)
            _write_relationships(f, relationships, tables)
            _write_tables_section(f, tables)
            _write_report_structure_section(f, report_level_filters, report_pages)

        print(f"Documentation successfully written to {output_path}")

    except Exception as e:
        print(f"FATAL ERROR writing documentation file: {e}")
        traceback.print_exc()


