import json
import os
import time
import re
from pathlib import Path
from typing import List, Dict, Tuple, Any, Optional
import traceback
from . import config

try:
    from .pbi_data_models import (
        ReportPage, Visual, ReportFilter, FilterTarget, VisualFieldMapping,
        DataClassEncoder # Reuse the encoder
    )
except ImportError:
    print("ERROR: Could not import data models from pbi_data_models.py.")
    print("       Ensure the file exists and is accessible.")
    raise # Stop execution if models can't be imported

def load_json_file(file_path: Path) -> Optional[Any]:
    """Safely loads a JSON file, returning None if error occurs."""
    if not file_path.is_file():
        # This is common (e.g., missing filters.json), so don't print warning by default
        # print(f"Debug: JSON file not found: {file_path}")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Strip BOM if present before parsing
            content = f.read()
            if content.startswith('\ufeff'):
                content = content.lstrip('\ufeff')
            return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Warning: Error decoding JSON from {file_path.name}: {e}")
    except Exception as e:
        print(f"Warning: Error reading file {file_path.name}: {e}")
    return None


def parse_filter_target(expression_dict: Optional[Dict[str, Any]]) -> Optional[FilterTarget]:
    """
    Parses the 'expression' object to find the target entity and property.
    """
    if not expression_dict:
        return None
    try:
        # The key can be 'Column', 'Aggregation', 'Measure', etc.
        for key in expression_dict:
            if isinstance(expression_dict[key], dict) and 'Property' in expression_dict[key]:
                prop_dict = expression_dict[key]
                property_name = prop_dict.get("Property")

                source_ref = prop_dict.get("Expression", {}).get("SourceRef", {})
                entity = source_ref.get("Entity")

                if not entity: # Add fallback to check another common location
                    entity = prop_dict.get("SourceRef", {}).get("Entity")

                if key == "Measure" and property_name:
                    property_name = f"[{property_name}]" # Format measures for clarity

                if entity and property_name:
                    return FilterTarget(entity=entity, property=property_name)
    except Exception as e:
        print(f"Warning: Exception during filter target parsing: {e}")
    return None

def _parse_condition_recursively(condition: dict) -> str:
    """Recursively parses a filter condition object into a human-readable string."""
    if not isinstance(condition, dict):
        return "(Invalid condition format)"

    # Handles logical operators like "And", "Or", "Not"
    for logical_op in ["And", "Or"]:
        if logical_op in condition:
            left = _parse_condition_recursively(condition[logical_op].get("Left", {}))
            right = _parse_condition_recursively(condition[logical_op].get("Right", {}))
            return f"({left} {logical_op.upper()} {right})"

    if "Not" in condition:
        inner = _parse_condition_recursively(condition["Not"].get("Expression", {}))
        return f"NOT ({inner})"

    # Handles "In" condition for categorical filters
    if "In" in condition:
        in_op = condition["In"]
        col_expr = in_op.get("Expressions", [{}])[0]
        target_prop = col_expr.get("Column", {}).get("Property", "?")

        values_list = []
        for value_group in in_op.get("Values", []):
            for item in value_group:
                literal_val = item.get("Literal", {}).get("Value", "?")
                if isinstance(literal_val, str):
                    values_list.append(literal_val.strip("'"))
                else:
                    values_list.append(str(literal_val))

        values_str = ", ".join([f"'{v}'" for v in values_list])
        return f"`{target_prop}` IN ({values_str})"

    # Handles "Comparison" condition for advanced filters
    if "Comparison" in condition:
        comp = condition["Comparison"]
        op_map = {0: "=", 1: "<>", 2: ">", 3: ">=", 4: "<", 5: "<="}
        op_kind = comp.get("ComparisonKind")
        op_str = op_map.get(op_kind, f"op({op_kind})")

        left_prop = comp.get("Left", {}).get("Column", {}).get("Property", "?")
        right_val = comp.get("Right", {}).get("Literal", {}).get("Value", "?")

        if isinstance(right_val, str):
            right_val = right_val.rstrip("L")

        return f"`{left_prop}` {op_str} {right_val}"

    return "(Unparsed condition)"

def parse_filters(filter_list_json: Optional[List[Dict[str, Any]]], level: str) -> List[ReportFilter]:
    """Parses a list of filter definitions from JSON using robust helpers."""
    filters = []
    if not filter_list_json:
        return filters

    for i, filter_dict in enumerate(filter_list_json):
        try:
            target = parse_filter_target(filter_dict.get('expression'))
            definition_summary = "(No definition found)"

            if 'filter' in filter_dict and 'Where' in filter_dict['filter']:
                conditions = [_parse_condition_recursively(wc.get("Condition", {})) for wc in filter_dict['filter']['Where']]
                definition_summary = " AND ".join(conditions)
            elif target:
                definition_summary = "(All values)"

                # --- START OF NEW DEBUGGING BLOCK ---
            print(f"\n--- DEBUGGING PARSED FILTER: {filter_dict.get('name')} ---")
            print(f"  - Target Object: {target}")
            print(f"  - Parsed Definition: {definition_summary}")
            # --- END OF NEW DEBUGGING BLOCK ---

            filt = ReportFilter(
                name=filter_dict.get('name'),
                filter_type=filter_dict.get('type'),
                level=level,
                target=target,
                filter_definition=definition_summary
            )
            filters.append(filt)
        except Exception as e:
            print(f"Warning: Failed to parse filter item {i+1} at level {level}: {e}")
            traceback.print_exc()
            continue
    return filters


def _parse_mappings_from_transforms(visual_transforms: Optional[Dict[str, Any]]) -> List[VisualFieldMapping]:
    """Primary Strategy: Parses field mappings from the dataTransforms.json 'selects' array."""
    mappings = []
    if not visual_transforms or 'selects' not in visual_transforms:
        return mappings

    for select_item in visual_transforms.get('selects', []):
        try:
            field_role = next((role for role, active in select_item.get('roles', {}).items() if active), "Unknown")
            query_name = select_item.get('queryName')
            display_name = select_item.get('displayName')

            if not query_name:
                continue

            mappings.append(VisualFieldMapping(
                role=str(field_role),
                query_ref=query_name,
                display_name=display_name
            ))
        except Exception as e:
            print(f"    WARNING: Error processing select item in dataTransforms: {e}")
            continue
    return mappings

def _parse_mappings_from_config(visual_config: Optional[Dict[str, Any]]) -> List[VisualFieldMapping]:
    """Fallback Strategy: Parses field mappings from the config.json 'projections' object."""
    mappings = []
    if not visual_config or 'projections' not in visual_config.get('singleVisual', {}):
        return mappings

    projections = visual_config['singleVisual'].get('projections', {})
    column_properties = visual_config['singleVisual'].get('columnProperties', {})

    for role, fields_in_role in projections.items():
        if not isinstance(fields_in_role, list):
            continue
        
        for field_projection in fields_in_role:
            try:
                if not isinstance(field_projection, dict):
                    continue
                
                query_ref = field_projection.get('queryRef')
                if not query_ref:
                    continue

                # Use the display name from columnProperties if available, otherwise default to the query reference
                display_name = column_properties.get(query_ref, {}).get('displayName', query_ref)
                
                mappings.append(VisualFieldMapping(
                    role=str(role),
                    query_ref=query_ref,
                    display_name=display_name
                ))
            except Exception as e:
                print(f"    WARNING: Error processing projection for role '{role}': {e}")
                continue
    return mappings


# --- Main Field Mapping Function (Orchestrator) ---

def parse_field_mappings(
    visual_config: Optional[Dict[str, Any]],
    visual_transforms: Optional[Dict[str, Any]]
) -> List[VisualFieldMapping]:
    """
    Parses field mappings for a visual, trying the primary strategy (dataTransforms)
    first, and then falling back to the secondary strategy (config).
    """
    mappings = _parse_mappings_from_transforms(visual_transforms)
    
    if not mappings:
        mappings = _parse_mappings_from_config(visual_config)
        
    if not mappings:
        non_data_visual_types = ['image', 'shape', 'textbox', 'actionButton']
        
        visual_type = ""
        if visual_config:
            visual_type = visual_config.get('singleVisual', {}).get('visualType', "")

        if visual_type not in non_data_visual_types:
            visual_name = visual_config.get('name', 'Unknown') if visual_config else "Unknown"
            print(f"    >>>> WARNING: No field mappings extracted for visual {visual_name} (Type: {visual_type}) <<<<")

    return mappings


def parse_visual_title(visual_config: Optional[Dict[str, Any]]) -> Optional[str]:
    """Extracts visual title from config JSON."""
    if not visual_config: 
        return None
    try:
        title_objects = visual_config.get("singleVisual", {}).get("vcObjects", {}).get("title", [])
        if not title_objects or not isinstance(title_objects, list):
            return None
        title_obj = title_objects[0]
        properties = title_obj.get("properties", {})
        show_prop = properties.get("show", {}).get("expr", {}).get("Literal", {}).get("Value")
        if show_prop != "true": 
            return None
        title_text_val = properties.get("text", {}).get("expr", {}).get("Literal", {}).get("Value")
        if isinstance(title_text_val, str) and title_text_val.startswith("'") and title_text_val.endswith("'"):
             return title_text_val[1:-1]
        return title_text_val
    except Exception as e:
        visual_name_for_debug = visual_config.get('name', 'Unknown')
        print(f"Warning: Could not parse visual title for visual {visual_name_for_debug}: {e}")
    return None

def _load_visual_files(visual_dir: Path) -> dict:
    """Loads all necessary JSON files for a single visual into a dictionary."""
    # Use config constants for filenames
    container_json_path = visual_dir / config.VISUAL_CONTAINER_JSON_FILE
    config_json_path = visual_dir / config.VISUAL_CONFIG_JSON_FILE
    filters_json_path = visual_dir / config.VISUAL_FILTERS_JSON_FILE
    transforms_json_path = visual_dir / config.VISUAL_DATATRANSFORMS_JSON_FILE

    return {
        "container": load_json_file(container_json_path),
        "config": load_json_file(config_json_path),
        "filters": load_json_file(filters_json_path),
        "transforms": load_json_file(transforms_json_path),
    }


def parse_visual(visual_dir: Path) -> Optional[Visual]:
    """
    Parses all data for a single visual and instantiates a Visual object.
    This function first loads all data, then processes it.
    """
    visual_name_for_debug = visual_dir.name
    print(f"    Parsing visual: {visual_name_for_debug}")

    # Step 1: Load all raw data from files
    json_data = _load_visual_files(visual_dir)
    
    config_json = json_data.get("config")
    if not config_json:
        print(f"    Warning: Missing or invalid {config.VISUAL_CONFIG_JSON_FILE} for visual {visual_name_for_debug}. Skipping visual.")
        return None

    # Step 2: Parse each part of the raw data
    container_json = json_data.get("container")
    visual_level_filters = parse_filters(json_data.get("filters"), 'Visual')
    field_mappings = parse_field_mappings(config_json, json_data.get("transforms"))
    visual_title = parse_visual_title(config_json)

    # Step 3: Build the final Visual object
    try:
        visual = Visual(
            name=config_json.get('name'),
            visual_type=config_json.get('singleVisual', {}).get('visualType'),
            title=visual_title,
            x=container_json.get('x') if container_json else None,
            y=container_json.get('y') if container_json else None,
            width=container_json.get('width') if container_json else None,
            height=container_json.get('height') if container_json else None,
            visual_level_filters=visual_level_filters,
            field_mappings=field_mappings
        )
        return visual
    except Exception as e:
         print(f"    ERROR: Failed to instantiate Visual object for {visual_dir.name}: {e}")
         traceback.print_exc()
         return None


def parse_page(page_dir: Path) -> Optional[ReportPage]:
    """Parses JSON files within a page's directory using config constants."""
    print(f"  Parsing page: {page_dir.name}")
    # Use config constants
    section_json = load_json_file(page_dir / config.SECTION_JSON_FILE)
    filters_json = load_json_file(page_dir / config.SECTION_FILTERS_FILE)

    if not section_json:
        print(f"  Warning: Missing or invalid {config.SECTION_JSON_FILE} in {page_dir.name}. Skipping page.")
        return None

    # Parse page-level filters first
    page_level_filters = parse_filters(filters_json, 'Page')

    # Parse visuals within the page
    visuals = []
    # Use config constant
    visuals_dir = page_dir / config.VISUAL_CONTAINERS_SUBDIR
    if visuals_dir.is_dir():
        # Sort visual directories alpha-numerically for consistent order (optional)
        visual_subdirs = sorted([d for d in visuals_dir.iterdir() if d.is_dir()])
        for visual_subdir in visual_subdirs:
            visual_obj = parse_visual(visual_subdir)
            if visual_obj:
                visuals.append(visual_obj)
    else:
         print(f"  Info: No '{config.VISUAL_CONTAINERS_SUBDIR}' directory found in {page_dir.name}.")

    try:
        page = ReportPage(
            name=section_json.get('name'),
            display_name=section_json.get('displayName'),
            ordinal=section_json.get('ordinal', 0),
            width=section_json.get('width'),
            height=section_json.get('height'),
            page_level_filters=page_level_filters, # Pass the parsed list
            visuals=visuals # Pass the parsed list
        )
        print(f"  Finished parsing page '{page.display_name or page.name}'. Found {len(page.visuals)} visuals.")
        return page
    except Exception as e:
        print(f"  ERROR: Failed to instantiate ReportPage object for {page_dir.name}: {e}")
        traceback.print_exc()
        return None

# --- Main Execution Function (New Wrapper) ---
def run_parser():
    """Main function to orchestrate the report structure parsing."""
    start_time = time.time()
    print(f"--- Starting Report Structure Parsing (parse_pbi_report.py) ---")

    # Use config variables for paths
    input_root_dir = config.PBI_EXTRACT_ROOT_DIR
    output_dir = config.OUTPUT_DIR
    output_file_path = output_dir / config.OUTPUT_REPORT_LAYOUT_JSON_FILE

    # Use config constant for report directory name
    report_dir = input_root_dir / config.REPORT_DIR_NAME
    if not report_dir.is_dir():
        # Raise specific error if Report directory is missing
        error_msg = f"'{config.REPORT_DIR_NAME}' directory not found in '{input_root_dir}'"
        print(f"Error: {error_msg}. Exiting.")
        raise FileNotFoundError(error_msg)

    # --- Main Try Block ---
    try:
        # 1. Parse Report-Level Filters
        # Use config constant for filename
        report_filters_json = load_json_file(report_dir / config.REPORT_FILTERS_FILE)
        report_level_filters = parse_filters(report_filters_json, 'Report')
        print(f"Parsed {len(report_level_filters)} report-level filters.")

        # 2. Parse Pages and their Visuals
        parsed_pages: List[ReportPage] = []
        # Use config constant for sections subdir name
        sections_dir = report_dir / config.SECTIONS_SUBDIR
        if sections_dir.is_dir():
            # Sort page directories alpha-numerically for consistent order
            page_dirs = sorted(
                [d for d in sections_dir.iterdir() if d.is_dir()])
            print(f"Found {len(page_dirs)} page directories in '{sections_dir.name}'.")
            for page_dir in page_dirs:
                # Add inner try-except for individual page parsing
                try:
                    page_obj = parse_page(page_dir)
                    if page_obj:
                        parsed_pages.append(page_obj)
                except Exception as page_parse_error:
                    print(f"ERROR: Failed to parse page directory {page_dir.name}: {page_parse_error}")
                    traceback.print_exc() # Log error and continue with next page
                    continue
        else:
            print(f"Warning: Sections directory not found: {sections_dir}")

        # Check if any pages were successfully parsed
        if not parsed_pages and sections_dir.is_dir() and page_dirs:
             print("WARNING: No pages were successfully parsed, although page directories were found.")

        # 3. Assemble Final Output Structure
        report_layout_data = {
             "reportLevelFilters": report_level_filters,
             "pages": parsed_pages
        }

        # 4. Write Output JSON
        print(f"\nWriting report layout data to {output_file_path}...")
        output_dir.mkdir(parents=True, exist_ok=True) # Ensure output dir exists
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(report_layout_data, f, cls=DataClassEncoder, indent=2, ensure_ascii=False)
        print(f"Successfully wrote {output_file_path}")

        end_time = time.time()
        print(f"\n--- Report Parsing Complete ---")
        print(f"Processed {len(report_level_filters)} report-level filters.")
        print(f"Processed {len(parsed_pages)} pages.")
        total_visuals = sum(len(p.visuals) for p in parsed_pages)
        print(f"Processed {total_visuals} visuals across all pages.")
        print(f"Total Time: {end_time - start_time:.2f} seconds")
        print(f"Output written to: {output_file_path.resolve()}")

    # --- Catch Errors during run_parser ---
    except FileNotFoundError as e:
        # Specific handling for missing critical directories/files
        print(f"ERROR: A required file or directory was not found: {e}")
        traceback.print_exc()
        raise # Re-raise exception so the orchestrator knows it failed
    except Exception as e:
        # Catch any other unexpected errors during parsing
        print(f"An unexpected error occurred during report parsing: {e}")
        traceback.print_exc()
        raise # Re-raise exception

# --- Entry Point ---
if __name__ == "__main__":
    # This allows running the script directly for testing
    print("Running parse_pbi_report.py independently...")
    try:
        run_parser()
        print("\nIndependent run completed.")
    except Exception as e:
         # Error should have been printed within run_parser
         print(f"\nIndependent run failed.")
         # Exit with a non-zero code to indicate failure
         exit(1)
