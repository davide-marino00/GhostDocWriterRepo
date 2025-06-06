# parse_pbi_model.py - REFACTORED to use config.py

import json
import os
import re
from pathlib import Path
from typing import List, Dict, Tuple, Any, Optional
import traceback # Keep traceback

# Import configuration settings
import config

# Import our data model classes and the custom encoder
# Ensure pbi_data_models.py is in the same directory or Python path
try:
    from pbi_data_models import (
        Table, Column, CalculatedColumn, Measure, Relationship, Annotation,
        DataClassEncoder
    )
except ImportError:
    print("ERROR: Could not import data models from pbi_data_models.py.")
    print("       Ensure the file exists and is accessible.")
    raise # Stop execution if models can't be imported

# --- Configuration: Hardcoded Paths --- REMOVED (Now in config.py)
# --- Constants --- REMOVED (Now in config.py)


# --- Helper Function for Parsing Table/Column References ---
def parse_table_column_ref(ref_string: str) -> Tuple[str | None, str | None]:
    """ Parses 'Table'.'Column' or Table.Column, handling quotes. Uses greedy match. """
    # Regex to capture: OptionalQuote1, TableName (greedy), OptionalQuote1, Dot, OptionalQuote2, ColumnName (greedy), OptionalQuote2
    match = re.match(r"^\s*(['\"]?)(.+)\1\s*\.\s*(['\"]?)(.+)\3\s*$", ref_string)
    if match:
        table_name = match.group(2)
        column_name = match.group(4)
        return table_name, column_name
    else:
        # Don't print warning here, let the calling function decide if it's an error
        # print(f"Warning: Could not parse table/column reference: {ref_string}")
        return None, None


# --- File Discovery Function ---
def find_tmdl_files(input_root_dir: Path) -> Tuple[List[Path], List[Path]]:
    """
    Finds relationship and table TMDL files within the pbi-tools output structure.
    Uses constants from the config module.
    Returns paths to potential relationship files (relationships.tmdl, model.tmdl)
    and table TMDL files.
    """
    # Use config variables for directory/file names
    model_path = input_root_dir / config.MODEL_DIR_NAME
    relationship_files = []
    table_files = []

    if not model_path.is_dir():
        # Raise a specific error if the essential Model directory is missing
        raise FileNotFoundError(f"'{config.MODEL_DIR_NAME}' directory not found in '{input_root_dir}'")

    # Look for relationship file(s) using config constants
    potential_rel_file = model_path / config.RELATIONSHIP_TMDL_FILE
    if potential_rel_file.is_file():
        relationship_files.append(potential_rel_file)

    potential_model_file = model_path / config.MODEL_TMDL_FILE
    if potential_model_file.is_file():
         # Add model.tmdl only if it's different from relationships.tmdl and hasn't been added
        if potential_model_file not in relationship_files:
            relationship_files.append(potential_model_file)

    # Look for table files using config constants
    tables_path = model_path / config.TABLES_TMDL_SUBDIR
    if tables_path.is_dir():
        for item in tables_path.iterdir():
            # Check if it's a file and has the .tmdl extension
            if item.is_file() and item.suffix.lower() == '.tmdl':
                table_files.append(item)
    else:
        # This might be acceptable if a model has no tables, so just print a warning
        print(f"Warning: '{config.TABLES_TMDL_SUBDIR}' directory not found in '{model_path}'. No table files loaded.")

    print(f"Found {len(relationship_files)} potential relationship file(s).")
    print(f"Found {len(table_files)} table TMDL files.")
    return relationship_files, table_files


# --- Parsing Functions ---

def parse_relationships(relationship_files: List[Path]) -> List[Relationship]:
    """
    Parses relationship definitions from the provided TMDL file(s) using line-by-line processing.
    Handles potential definitions across multiple files and avoids duplicates.
    """
    all_relationships: List[Relationship] = []
    processed_rel_ids = set() # To avoid duplicates if defined in multiple files

    # Regex to find the start of a relationship definition line
    rel_start_pattern = re.compile(r"^\s*relationship\s+([\w-]+)")
    # Pattern for individual property lines (key: value)
    prop_pattern = re.compile(r"^\s*(\w+):\s*(.*)")

    for file_path in relationship_files:
        print(f"Parsing relationships from: {file_path.name}...")
        try:
            content = file_path.read_text(encoding='utf-8')
            # Strip potential BOM from the start of the content
            if content.startswith('\ufeff'):
                content = content.lstrip('\ufeff')

            lines = content.splitlines()
            current_rel_id = None
            current_props = {}
            is_in_block = False # Flag to indicate if we are inside a relationship's property block

            def process_collected_relationship(rel_id, props_dict):
                # Helper to create Relationship object from collected properties
                if not rel_id or not props_dict: return None
                if rel_id in processed_rel_ids:
                    # Silently skip duplicates found across files, only process the first time.
                    return None

                from_col_ref = props_dict.get('fromColumn')
                to_col_ref = props_dict.get('toColumn')

                if not from_col_ref or not to_col_ref:
                    print(f"Warning: Skipping relationship '{rel_id}' due to missing fromColumn/toColumn in parsed properties.")
                    return None

                from_table, from_column = parse_table_column_ref(from_col_ref)
                to_table, to_column = parse_table_column_ref(to_col_ref)

                if not from_table or not from_column or not to_table or not to_column:
                     print(f"Warning: Skipping relationship '{rel_id}' due to parsing error in column references ('{from_col_ref}', '{to_col_ref}').")
                     return None

                is_active = props_dict.get('isActive', 'true').lower() != 'false'
                cross_filter = props_dict.get('crossFilteringBehavior', 'singleDirection')

                processed_rel_ids.add(rel_id) # Mark as processed
                return Relationship(
                    fromTable=from_table, fromColumn=from_column,
                    toTable=to_table, toColumn=to_column,
                    isActive=is_active, crossFilteringBehavior=cross_filter
                )
            # --- End of helper ---

            for line in lines:
                line_stripped = line.strip()
                if not line_stripped: # Blank line potentially ends a block
                    if is_in_block:
                         # Process the completed relationship block
                        rel_obj = process_collected_relationship(current_rel_id, current_props)
                        if rel_obj: all_relationships.append(rel_obj)
                        # Reset state after processing
                        is_in_block = False
                        current_rel_id = None
                        current_props = {}
                    continue # Skip blank line

                rel_match = rel_start_pattern.match(line) # Check if line starts a new relationship

                if rel_match:
                    # Found the start of a new relationship definition
                    # Process the PREVIOUS relationship's properties first (if any)
                    if current_rel_id:
                         rel_obj = process_collected_relationship(current_rel_id, current_props)
                         if rel_obj: all_relationships.append(rel_obj)

                    # Start collecting for the new relationship
                    current_rel_id = rel_match.group(1)
                    current_props = {}
                    is_in_block = True # We are now inside a block (or starting one)

                elif is_in_block and (line.startswith(' ') or line.startswith('\t')):
                    # This line is indented and we are inside a block - potential property
                    prop_match = prop_pattern.match(line_stripped)
                    if prop_match:
                        key = prop_match.group(1)
                        value = prop_match.group(2).strip()
                        # Handle quoted values (remove leading/trailing quotes if present)
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                        elif value.startswith("'") and value.endswith("'"):
                            value = value[1:-1]
                        current_props[key] = value
                    else:
                        # Line is indented but doesn't match property pattern - ignore? Or log?
                        pass # Ignore lines like comments within the block

                elif not line.startswith(' ') and not line.startswith('\t') and is_in_block :
                     # Line is not indented, and not blank, and not a new definition
                     # Assume it marks the end of the previous block
                    rel_obj = process_collected_relationship(current_rel_id, current_props)
                    if rel_obj: all_relationships.append(rel_obj)
                     # Reset state
                    is_in_block = False
                    current_rel_id = None
                    current_props = {}

            # Process the very last relationship collected after the loop finishes
            if current_rel_id:
                rel_obj = process_collected_relationship(current_rel_id, current_props)
                if rel_obj: all_relationships.append(rel_obj)

        except FileNotFoundError:
            # This shouldn't happen if find_tmdl_files worked, but handle defensively
            print(f"Warning: Relationship file not found during parsing: {file_path}")
        except Exception as e:
            print(f"Error parsing relationship file {file_path.name}: {e}")
            traceback.print_exc() # Show details for relationship parsing errors

    print(f"Successfully parsed {len(all_relationships)} relationships.")
    return all_relationships


# --- Helper functions for table parsing ---

def parse_multiline_dax(text_block: str) -> Optional[str]:
    """Extracts DAX expression enclosed in triple backticks."""
    match = re.search(r"```\s*\n(.*?)\n\s*```", text_block, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def parse_properties_and_annotations(lines: List[str]) -> Tuple[Dict[str, str], List[Annotation]]:
    """Parses indented property lines and annotation lines."""
    properties = {}
    annotations = []
    prop_pattern = re.compile(r"^\s*(\w+):\s*(.*)") # Simple key: value
    ann_pattern = re.compile(r"^\s*annotation\s+(['\"]?)(.+?)\1\s*=\s*(.*)") # Annotation key = value (handle quotes in name)

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith('--'): continue # Skip empty/comment lines

        ann_match = ann_pattern.match(line_stripped)
        if ann_match:
            ann_name = ann_match.group(2).strip()
            ann_value = ann_match.group(3).strip()
            # Handle quoted values
            if ann_value.startswith('"') and ann_value.endswith('"'):
                ann_value = ann_value[1:-1]
            elif ann_value.startswith("'") and ann_value.endswith("'"):
                 ann_value = ann_value[1:-1]
            annotations.append(Annotation(name=ann_name, value=ann_value))
        else:
            prop_match = prop_pattern.match(line_stripped)
            if prop_match:
                key = prop_match.group(1)
                value = prop_match.group(2).strip()
                 # Handle quoted values
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                properties[key] = value

    return properties, annotations


# --- Main Table Parsing Function ---

def parse_table_file(table_file_path: Path) -> Table:
    """
    Parses a single table TMDL file into a Table object.
    """
    print(f"Parsing table file: {table_file_path.name}...")
    try:
        content = table_file_path.read_text(encoding='utf-8')
        if content.startswith('\ufeff'):
            content = content.lstrip('\ufeff')
    except Exception as e:
        print(f"Error reading table file {table_file_path.name}: {e}")
        # Return a placeholder or raise error? Raising is probably better.
        raise IOError(f"Could not read table file {table_file_path.name}") from e

    # Find table name first
    table_name_match = re.search(r"^\s*table\s+(?:(['\"])(.+?)\1|([\w\.-]+))", content, re.MULTILINE)
    if not table_name_match:
        raise ValueError(f"Could not find table definition in {table_file_path.name}")
    table_name = table_name_match.group(2) or table_name_match.group(3)
    table_obj = Table(name=table_name)

    lines = content.splitlines()
    current_object_lines = []
    current_object_type = None # 'table', 'column', 'measure'
    current_object_def_line = ""
    current_indentation = ""

    def process_object(obj_type: Optional[str], def_line: str, obj_lines: List[str], table_obj: Table):
        # Helper to process collected data for a table, column, or measure
        if not obj_type: return

        name = ""
        is_calc_col = False
        is_measure = False
        single_line_dax = None
        dax_part = None

        # --- Parse Definition Line ---
        if obj_type == 'table':
            # Table properties are processed at the end of its block
            properties, annotations = parse_properties_and_annotations(obj_lines)
            table_obj.isHidden = properties.get('isHidden', 'false').lower() == 'true'
            table_obj.description = properties.get('description')
            table_obj.annotations.extend(annotations)
            # Extract description from specific annotation if present
            desc_annotation = next((a for a in annotations if a.name == 'PBI_ObjectProcessingOrder'), None) # Or common name like 'Description'
            if desc_annotation: table_obj.description = desc_annotation.value
            return

        elif obj_type == 'column':
            # Handle quoted names: column 'Column Name' or column ColumnName
            col_match = re.match(r"^\s*column\s+(?:(['\"])(.+?)\1|([\w\.-]+))(?:\s*=\s*(.*))?$", def_line.strip())
            if not col_match: print(f"Warning: Could not parse column definition line: {def_line}"); return
            name = col_match.group(2) or col_match.group(3) # Get quoted or unquoted name
            dax_part = col_match.group(4)
            if dax_part is not None:
                is_calc_col = True
                if not dax_part.strip().startswith("```"): single_line_dax = dax_part.strip()

        elif obj_type == 'measure':
            # Handle quoted names: measure 'Measure Name' or measure MeasureName
            mea_match = re.match(r"^\s*measure\s+(?:(['\"])(.+?)\1|([\w\.-]+))\s*=\s*(.*)$", def_line.strip())
            if not mea_match: print(f"Warning: Could not parse measure definition line: {def_line}"); return
            name = mea_match.group(2) or mea_match.group(3) # Get quoted or unquoted name
            dax_part = mea_match.group(4)
            is_measure = True
            if not dax_part.strip().startswith("```"): single_line_dax = dax_part.strip()

        # --- Parse Properties and Annotations from the object's body ---
        properties, annotations = parse_properties_and_annotations(obj_lines)

        # Extract description from specific annotation if present
        obj_description = properties.get('description') # Check direct property first
        if not obj_description:
             desc_annotation = next((a for a in annotations if a.name == 'PBI_ObjectProcessingOrder'), None) # Or common name like 'Description'
             if desc_annotation: obj_description = desc_annotation.value

        # --- Determine DAX Expression ---
        dax_expression = None
        if single_line_dax:
            dax_expression = single_line_dax
        else:
            # Combine definition line DAX part (if multiline start) and body lines
            full_block_text = (dax_part if dax_part else "") + "\n" + "\n".join(obj_lines)
            multiline_dax_from_block = parse_multiline_dax(full_block_text)
            dax_expression = multiline_dax_from_block

        # --- Create Object ---
        if is_measure:
            if dax_expression is None: dax_expression = "" # Measures must have expression
            measure = Measure(
                name=name, daxExpression=dax_expression,
                formatString=properties.get('formatString'),
                isHidden=properties.get('isHidden', 'false').lower() == 'true',
                description=obj_description, # Use extracted description
                annotations=annotations
            )
            table_obj.measures.append(measure)
        elif is_calc_col:
            # If sourceColumn property exists, it's NOT a calculated column, reclassify
            if 'sourceColumn' in properties:
                is_calc_col = False
            else:
                if dax_expression is None: dax_expression = "" # Calc columns must have expression
                calc_col = CalculatedColumn(
                    name=name, daxExpression=dax_expression,
                    dataType=properties.get('dataType', 'string'), # Default if missing
                    formatString=properties.get('formatString'),
                    isHidden=properties.get('isHidden', 'false').lower() == 'true',
                    summarizeBy=properties.get('summarizeBy', 'none'),
                    description=obj_description, # Use extracted description
                    annotations=annotations
                )
                table_obj.columns.append(calc_col)

        # Handle regular columns (either originally or after reclassification)
        if obj_type == 'column' and not is_calc_col:
            col = Column(
                 name=name, dataType=properties.get('dataType', 'string'), # Default if missing
                 sourceColumn=properties.get('sourceColumn'), # Might be None
                 formatString=properties.get('formatString'),
                 isHidden=properties.get('isHidden', 'false').lower() == 'true',
                 summarizeBy=properties.get('summarizeBy', 'none'),
                 description=obj_description, # Use extracted description
                 annotations=annotations
            )
            # Add a check: regular columns usually need a sourceColumn
            if col.sourceColumn is None:
                 print(f"Warning: Column '{name}' in table '{table_obj.name}' lacks 'sourceColumn'. Check definition.")
            table_obj.columns.append(col)
    # --- End of process_object helper ---

    # --- Main Loop Logic for table parsing ---
    # Pattern to find start of table, column, or measure definition (handling quoted names)
    definition_pattern = re.compile(r"^(\s*)(table|column|measure)\s+(?:['\"].+?['\"]|[\w\.-]+)(.*)")

    line_iter = iter(lines)
    current_line = None
    eof = False
    table_properties_processed = False # Flag to process table properties only once

    while not eof:
        line_to_process = current_line if current_line is not None else next(line_iter, None)
        current_line = None # Reset peeked line
        if line_to_process is None:
             eof = True # End of file reached
             # Process the very last object before breaking
             process_object(current_object_type, current_object_def_line, current_object_lines, table_obj)
             break # Exit loop

        cleaned_line = line_to_process.lstrip('\ufeff') # Strip BOM just in case
        line_stripped_no_indent = cleaned_line.strip()

        # Skip blank lines and comments
        if not line_stripped_no_indent or line_stripped_no_indent.startswith('--'):
            continue

        match = definition_pattern.match(cleaned_line)

        # Check if the line starts a new definition (table, column, measure)
        if match:
            indent, obj_type = match.group(1), match.group(2)

            # If we encounter a column or measure, process the preceding object (which could be table props or another col/measure)
            if current_object_type is not None:
                 process_object(current_object_type, current_object_def_line, current_object_lines, table_obj)
                 if current_object_type == 'table': table_properties_processed = True


            # Start collecting for the new object
            current_object_type = obj_type
            current_object_def_line = cleaned_line
            current_object_lines = []
            current_indentation = indent

            # Special case: if it's the table definition itself, mark type but continue collecting lines
            if obj_type == 'table':
                 current_object_type = 'table' # Set type but don't process immediately

        # If it's not a new definition start, check if it belongs to the current object block
        elif current_object_type is not None:
            # Check if the line's indentation is greater than the definition line's indentation
            # This handles simple indented properties/annotations
            if cleaned_line.startswith(current_indentation + ' ') or cleaned_line.startswith(current_indentation + '\t'):
                current_object_lines.append(cleaned_line)
            # Handle multi-line DAX which might not be indented relative to the start definition
            elif (current_object_type == 'measure' or '=\s*```' in current_object_def_line) \
                 and not cleaned_line.startswith(current_indentation): # Rough check for DAX continuation
                 current_object_lines.append(cleaned_line)

            # If line is not indented and not part of current block, process the completed block
            else:
                 process_object(current_object_type, current_object_def_line, current_object_lines, table_obj)
                 if current_object_type == 'table': table_properties_processed = True
                 # Reset state, but keep the current line to process in the next iteration
                 current_object_type = None
                 current_object_def_line = ""
                 current_object_lines = []
                 current_indentation = ""
                 current_line = line_to_process # Re-process this line

    # Ensure table properties are processed if they were the last block
    if current_object_type == 'table' and not table_properties_processed:
         process_object(current_object_type, current_object_def_line, current_object_lines, table_obj)


    print(f"Finished parsing table '{table_obj.name}'. Found {len(table_obj.columns)} columns and {len(table_obj.measures)} measures.")
    return table_obj


# --- Output Function ---
def write_json_output(output_dir: Path, data: Any, filename: str):
    """Writes Python data (dataclasses) to a JSON file using DataClassEncoder."""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / filename
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            # Use the imported DataClassEncoder
            json.dump(data, f, cls=DataClassEncoder, indent=2, ensure_ascii=False)
        print(f"Successfully wrote {output_path}")
    except TypeError as e:
        # Provide more context on TypeError during JSON serialization
        print(f"Error writing JSON file {output_path}: TypeError - {e}")
        print("This might indicate an issue with serializing a specific data type within your dataclasses.")
        # Consider adding more detailed logging of the 'data' object here if needed, but be careful with large objects
        traceback.print_exc()
    except Exception as e:
        print(f"Error writing JSON file {output_path}: {e}")
        traceback.print_exc()


# --- Main Execution Function (New Wrapper) ---
def run_parser():
    """Main function to orchestrate the model parsing process."""
    # Use config variables for paths
    input_root_dir = config.PBI_EXTRACT_ROOT_DIR
    output_root_dir = config.OUTPUT_DIR

    print(f"--- Starting TMDL Parsing (parse_pbi_model.py) ---")
    print(f"Input Directory: {input_root_dir.resolve()}")
    print(f"Output Directory: {output_root_dir.resolve()}")

    try:
        relationship_files, table_files = find_tmdl_files(input_root_dir)
        relationships = parse_relationships(relationship_files)
        # Use config constants for output filenames
        write_json_output(output_root_dir, relationships, config.OUTPUT_RELATIONSHIPS_JSON_FILE)

        parsed_tables: List[Table] = []
        if table_files:
            # Use config constant for output subdir
            output_tables_dir = output_root_dir / config.OUTPUT_TABLES_JSON_SUBDIR
            for table_file in table_files:
                try:
                    table = parse_table_file(table_file)
                    parsed_tables.append(table)
                    # Ensure filename is filesystem-safe (replace invalid chars)
                    safe_table_name = re.sub(r'[\\/*?:"<>|]', '_', table.name)
                    write_json_output(output_tables_dir, table, f"{safe_table_name}.json")
                except Exception as e:
                    # Log error for specific table and continue with others
                    print(f"ERROR parsing table file {table_file.name}: {e}")
                    traceback.print_exc() # Print traceback for table errors
                    continue # Skip faulty table file

        # Check if any tables were successfully parsed before creating summary
        if not parsed_tables and table_files:
             print("WARNING: No tables were successfully parsed, but table files were found.")
        elif not table_files:
             print("INFO: No table files found to parse.")

        model_summary = {
            "tables": [t.name for t in parsed_tables], # Only include successfully parsed tables
            "relationship_count": len(relationships)
        }
        # Use config constant for output filename
        write_json_output(output_root_dir, model_summary, config.OUTPUT_MODEL_SUMMARY_JSON_FILE)

        print(f"\n--- Model Parsing Complete ---")
        print(f"Processed {len(relationships)} relationships.")
        print(f"Processed {len(parsed_tables)} tables.")
        print(f"Output written to: {output_root_dir.resolve()}")

    except FileNotFoundError as e:
        # Handle critical error where input directory/structure is wrong
        print(f"ERROR: Required directory not found: {e}")
        print("Please ensure 'PBI_EXTRACT_ROOT_DIR' in config.py points to the correct extraction folder.")
        raise # Re-raise the exception so the orchestrator knows it failed
    except Exception as e:
        # Catch any other unexpected errors during parsing
        print(f"An unexpected error occurred during model parsing: {e}")
        traceback.print_exc()
        raise # Re-raise the exception

# --- Entry Point ---
if __name__ == "__main__":
    # This allows running the script directly for testing
    print("Running parse_pbi_model.py independently...")
    try:
        run_parser()
        print("\nIndependent run completed.")
    except Exception as e:
         # Error should have been printed within run_parser
         print(f"\nIndependent run failed: {e}")
         # Exit with a non-zero code to indicate failure
         exit(1)
