import json
import os
import time
import re
from pathlib import Path
from typing import List, Dict, Tuple, Any, Optional
import traceback
import config

try:
    from pbi_data_models import (
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

# Enhanced parse_filter_target function
def parse_filter_target(expression_dict: Optional[Dict[str, Any]]) -> Optional[FilterTarget]:
    """
    Parses the 'expression' object within a filter definition.
    Handles simple Column references and basic Aggregations.
    """
    if not expression_dict:
        return None
    try:
        # Case 1: Simple Column Filter (Most common)
        if "Column" in expression_dict:
            column_dict = expression_dict["Column"]
            expression = column_dict.get("Expression")
            source_ref = None
            if expression: 
                source_ref = expression.get("SourceRef")
            if source_ref is None:
                source_ref = column_dict.get("SourceRef") # Fallback

            entity = None
            if source_ref: 
                entity = source_ref.get("Entity") or source_ref.get("Source")
            property_name = column_dict.get("Property")
            if entity and property_name:
                return FilterTarget(entity=entity, property=property_name)

        # Case 2: Aggregation Filter (e.g., Sum(SalesAmount) > 50)
        elif "Aggregation" in expression_dict:
            agg_dict = expression_dict["Aggregation"]
            agg_func_map = {0: "Sum", 1: "Avg", 2: "Min", 3: "Max",
                            4: "Count", 5: "CountNonNull", 6: "Median",
                            7: "StandardDeviation", 8: "Variance"}
            agg_func_code = agg_dict.get("Function", -1)
            agg_func_name = agg_func_map.get(agg_func_code, f"Agg{agg_func_code}")

            # Try to find the underlying column being aggregated
            inner_expr = agg_dict.get("Expression")
            if inner_expr and "Column" in inner_expr:
                 column_dict = inner_expr["Column"]
                 expression = column_dict.get("Expression")
                 source_ref = None
                 if expression: 
                    source_ref = expression.get("SourceRef")
                 if source_ref is None:
                     source_ref = column_dict.get("SourceRef") # Fallback

                 entity = None
                 if source_ref: 
                    entity = source_ref.get("Entity") or source_ref.get("Source")

                 property_name = column_dict.get("Property")

                 if entity and property_name:
                     # Represent the target as "Agg(Entity.Property)"
                     agg_target_prop = f"{agg_func_name}({property_name})"
                     return FilterTarget(entity=entity, property=agg_target_prop)
                 elif property_name: # Found property but no entity
                      agg_target_prop = f"{agg_func_name}({property_name})"
                      return FilterTarget(entity="Unknown", property=agg_target_prop)

            # Fallback if inner column not found - just use Aggregation function name
            return FilterTarget(entity="Aggregation", property=agg_func_name)

        # Case 3: Measure Filter (Basic handling)
        elif "Measure" in expression_dict:
             measure_dict = expression_dict["Measure"]
             expression = measure_dict.get("Expression")
             source_ref = None
             if expression:
                 source_ref = expression.get("SourceRef")

             entity = None
             if source_ref:
                 entity = source_ref.get("Entity") or source_ref.get("Source")
             property_name = measure_dict.get("Property") # This is the Measure name

             if entity and property_name:
                 return FilterTarget(entity=entity, property=f"[{property_name}]") # Indicate measure with []
             elif property_name:
                  return FilterTarget(entity="Measure", property=f"[{property_name}]")

    except Exception as e:
        print(f"Warning: Exception during filter target parsing: {e} - Data: {expression_dict}")
        # traceback.print_exc() # Optional: uncomment for more detail
    return None # Return None if structure doesn't match known patterns

def parse_filters(filter_list_json: Optional[List[Dict[str, Any]]], level: str) -> List[ReportFilter]:
    """Parses a list of filter definitions from JSON."""
    filters = []
    if not filter_list_json:
        return filters

    for i, filter_dict in enumerate(filter_list_json):
        try:
            # Use the enhanced target parser
            target = parse_filter_target(filter_dict.get('expression'))

            # Create the filter object - ensure all expected fields are present
            filt = ReportFilter(
                name=filter_dict.get('name'),
                filter_type=filter_dict.get('type'), # Extract type
                level=level,
                target=target, # Use potentially improved target
                filter_definition=filter_dict.get('filter') # Store raw filter logic
                # llm_explanation is added later
            )
            filters.append(filt)
        except Exception as e:
            print(f"Warning: Failed to parse filter item {i+1} at level {level}: {e} - Data: {filter_dict}")
            traceback.print_exc()
            continue
    return filters

# Use the version with extensive debugging prints
def parse_field_mappings(visual_config: Optional[Dict[str, Any]],
                         visual_transforms: Optional[Dict[str, Any]]) -> List[VisualFieldMapping]:
    """
    Parses field mappings from visual config (config.json) and dataTransforms (dataTransforms.json).
    Prefers using dataTransforms.selects if available, otherwise falls back to config.projections.
    Includes extensive debugging prints.
    """
    mappings = []
    visual_name_for_debug = visual_config.get('name') if visual_config else "Unknown"
    print(f"\n    --- Debugging parse_field_mappings for Visual: {visual_name_for_debug} ---")

    # --- Check Inputs ---
    has_transforms = visual_transforms is not None
    has_selects = has_transforms and 'selects' in visual_transforms and visual_transforms['selects']
    has_config = visual_config is not None
    has_projections = has_config and 'projections' in visual_config.get('singleVisual', {})

    print(f"    DEBUG: Has visual_transforms? {has_transforms}")
    print(f"    DEBUG: Has non-empty 'selects' in visual_transforms? {bool(has_selects)}") # Print True/False
    print(f"    DEBUG: Has visual_config? {has_config}")
    print(f"    DEBUG: Has 'projections' in visual_config? {has_projections}")

    # --- Primary Method: Use dataTransforms.json ---
    if has_transforms and has_selects:
        print(f"    DEBUG: Entering PRIMARY path (using dataTransforms.selects)")
        selects_list = visual_transforms.get('selects', [])
        print(f"    DEBUG: Found {len(selects_list)} items in 'selects' array.")
        for i, select_item in enumerate(selects_list):
            # Limit printing very large select items
            select_item_str = json.dumps(select_item)
            if len(select_item_str) > 500:
                select_item_str = select_item_str[:500] + "..."
            print(f"      DEBUG: Processing select item {i+1}: {select_item_str}")
            try:
                # Extract the primary role
                field_role = next(
                    (role for role, is_active in select_item.get('roles', {}).items() if is_active), "Unknown")
                query_name = select_item.get('queryName')
                display_name = select_item.get('displayName')

                print(f"        DEBUG: Extracted Role='{field_role}', Query='{query_name}', Display='{display_name}'")

                if not query_name:
                     print(f"        WARNING: Missing queryName in select item {i+1}. Skipping.")
                     continue

                mapping = VisualFieldMapping(
                    role=str(field_role), # Ensure string
                    query_ref=query_name,
                    display_name=display_name
                )
                print(f"        DEBUG: Created Mapping Object: {mapping}")
                mappings.append(mapping)
            except Exception as e:
                 print(f"    WARNING: Error processing select item {i+1} in dataTransforms for visual {visual_name_for_debug}: {e} - Data: {select_item}")
                 traceback.print_exc() # Show details

    # --- Fallback Method: Use config.json ---
    elif has_config and has_projections:
        print(f"    DEBUG: Entering FALLBACK path (using config.json projections)")
        projections = visual_config['singleVisual'].get('projections', {})
        column_properties = visual_config['singleVisual'].get('columnProperties', {})
        print(f"    DEBUG: Projections found: {list(projections.keys())}")

        for role, fields_in_role in projections.items():
            if isinstance(fields_in_role, list):
                print(f"      DEBUG: Processing role '{role}' with {len(fields_in_role)} fields.")
                for j, field_projection in enumerate(fields_in_role):
                    # Limit printing large projection items
                    field_proj_str = json.dumps(field_projection)
                    if len(field_proj_str) > 500:
                        field_proj_str = field_proj_str[:500] + "..."
                    print(f"        DEBUG: Processing field projection {j+1} in role '{role}': {field_proj_str}")
                    if not isinstance(field_projection, dict):
                         print(f"        WARNING: Field projection item {j+1} in role '{role}' is not a dict. Skipping.")
                         continue

                    query_ref = field_projection.get('queryRef')
                    print(f"          DEBUG: Found queryRef: {query_ref}")

                    if query_ref:
                        display_name = query_ref # Default
                        if column_properties and query_ref in column_properties:
                             prop_display_name = column_properties[query_ref].get('displayName')
                             if prop_display_name:
                                 display_name = prop_display_name
                                 print(f"          DEBUG: Found displayName in columnProperties: {display_name}")
                        try:
                            mapping = VisualFieldMapping(
                                role=str(role), # Ensure string
                                query_ref=query_ref,
                                display_name=display_name
                            )
                            print(f"          DEBUG: Created Mapping Object: {mapping}")
                            mappings.append(mapping)
                        except Exception as e:
                            print(f"    WARNING: Error creating VisualFieldMapping from projection for visual {visual_name_for_debug}: {e} - Role: {role}, Data: {field_projection}")
                            traceback.print_exc() # Show details
                    else:
                        print(f"        WARNING: No queryRef found in field projection {j+1} for role '{role}'.")
            else:
                 print(f"      WARNING: Content for role '{role}' is not a list. Skipping role.")

    # --- No Mappings Found Path ---
    else:
         print(f"    DEBUG: NEITHER dataTransforms/selects NOR config/projections found usable data for visual {visual_name_for_debug}")

    # --- Final Result ---
    print(f"    --- Finished parse_field_mappings for Visual: {visual_name_for_debug} ---")
    print(f"    DEBUG: Final mappings list count: {len(mappings)}")
    if not mappings:
         print(f"    >>>> WARNING: No field mappings extracted for visual {visual_name_for_debug} <<<<")
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


def parse_visual(visual_dir: Path) -> Optional[Visual]:
    """Parses JSON files within a visual's directory using config constants. Includes filter debugging."""
    visual_name_for_debug = visual_dir.name
    print(f"    Parsing visual: {visual_name_for_debug}")

    # Use config constants for filenames
    container_json_path = visual_dir / config.VISUAL_CONTAINER_JSON_FILE
    config_json_path = visual_dir / config.VISUAL_CONFIG_JSON_FILE
    filters_json_path = visual_dir / config.VISUAL_FILTERS_JSON_FILE # Path to visual filters
    transforms_json_path = visual_dir / config.VISUAL_DATATRANSFORMS_JSON_FILE

    container_json = load_json_file(container_json_path)
    config_json = load_json_file(config_json_path)
    transforms_json = load_json_file(transforms_json_path)

    print(f"      DEBUG (parse_visual): Checking for filters file: {filters_json_path}")
    filters_json = load_json_file(filters_json_path) # Load the visual's filters.json
    visual_level_filters = [] # Initialize empty list

    if filters_json is not None:
        print(f"      DEBUG (parse_visual): Found and loaded filters file for {visual_name_for_debug}. Content type: {type(filters_json)}")
        if isinstance(filters_json, list):
            print(f"      DEBUG (parse_visual): Calling parse_filters for {len(filters_json)} items.")
            visual_level_filters = parse_filters(filters_json, 'Visual')
            print(f"      DEBUG (parse_visual): parse_filters returned {len(visual_level_filters)} filter objects.")
        else:
            print(f"      WARNING (parse_visual): Expected list in filters file, got {type(filters_json)}. Skipping filters.")
    else:
        print(f"      DEBUG (parse_visual): No filters file found or loaded for {visual_name_for_debug}.")

    if not config_json: # Config is essential
        print(f"    Warning: Missing or invalid {config.VISUAL_CONFIG_JSON_FILE} for visual {visual_name_for_debug}. Skipping visual.")
        return None

    # Extract field mappings (keep existing logic with its own debug prints)
    field_mappings = parse_field_mappings(config_json, transforms_json)

    try:
        # Create the Visual object, passing the visual_level_filters list we created
        visual = Visual(
            name=config_json.get('name'),
            visual_type=config_json.get('singleVisual', {}).get('visualType'),
            title=parse_visual_title(config_json),
            x=container_json.get('x') if container_json else None,
            y=container_json.get('y') if container_json else None,
            width=container_json.get('width') if container_json else None,
            height=container_json.get('height') if container_json else None,
            visual_level_filters=visual_level_filters, # Pass the potentially populated list
            field_mappings=field_mappings
        )
        print(f"      DEBUG (parse_visual): Successfully created Visual object for {visual_name_for_debug} with {len(visual.visual_level_filters)} filters attached.") # Confirm filters attached
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
