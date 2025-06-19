import json
import os
import re
from pathlib import Path
from typing import List, Dict, Tuple, Any, Optional
import traceback # Keep traceback
from . import config

try:
    from .pbi_data_models import (
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

def _split_relationship_chunks(content: str) -> list[str]:
    """
    Splits the content of a model/relationships file into a list of 
    individual relationship definition blocks.
    """
    # Regex to find the start of a new relationship definition.
    # We will split the file content before each match of this pattern.
    rel_start_pattern = re.compile(r"^\s*relationship\s+[\w-]+", re.MULTILINE)
    
    # Find all the starting points of relationship definitions
    matches = list(rel_start_pattern.finditer(content))
    if not matches:
        return []

    # Split the content at the start of each match
    chunks = []
    for i in range(len(matches)):
        start_pos = matches[i].start()
        end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)
        chunk = content[start_pos:end_pos].strip()
        if chunk:
            chunks.append(chunk)
            
    return chunks

def parse_relationships(relationship_files: list[Path]) -> list[Relationship]:
    """
    Parses relationship definitions from the provided TMDL file(s) by
    splitting the content into chunks and parsing each chunk individually.
    """
    all_relationships: list[Relationship] = []
    processed_rel_ids = set()

    for file_path in relationship_files:
        print(f"Parsing relationships from: {file_path.name}...")
        try:
            content = file_path.read_text(encoding='utf-8-sig')
            relationship_chunks = _split_relationship_chunks(content)

            for chunk in relationship_chunks:
                lines = chunk.splitlines()
                def_line = lines[0]
                body_lines = lines[1:]

                rel_match = re.match(r"^\s*relationship\s+([\w-]+)", def_line)
                if not rel_match:
                    continue

                rel_id = rel_match.group(1)
                if rel_id in processed_rel_ids:
                    continue
                
                properties, _ = parse_properties_and_annotations(body_lines)
                
                from_col_ref = properties.get('fromColumn')
                to_col_ref = properties.get('toColumn')

                if not from_col_ref or not to_col_ref:
                    print(f"Warning: Skipping relationship '{rel_id}' due to missing fromColumn/toColumn.")
                    continue

                from_table, from_column = parse_table_column_ref(from_col_ref)
                to_table, to_column = parse_table_column_ref(to_col_ref)

                if not from_table or not to_table:
                    print(f"Warning: Skipping relationship '{rel_id}' due to parsing error in column references.")
                    continue

                rel_obj = Relationship(
                    fromTable=from_table,
                    fromColumn=from_column,
                    toTable=to_table,
                    toColumn=to_column,
                    isActive=properties.get('isActive', 'true').lower() != 'false',
                    crossFilteringBehavior=properties.get('crossFilteringBehavior', 'singleDirection')
                )
                all_relationships.append(rel_obj)
                processed_rel_ids.add(rel_id)

        except Exception as e:
            print(f"Error parsing relationship file {file_path.name}: {e}")
            traceback.print_exc()

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
        if not line_stripped or line_stripped.startswith('--'):
            continue # Skip empty/comment lines

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
    Parses a single table TMDL file into a Table object by splitting it
    into object chunks and parsing each chunk individually.
    """
    print(f"Parsing table file: {table_file_path.name}...")
    try:
        content = table_file_path.read_text(encoding='utf-8-sig') # 'utf-8-sig' handles BOM automatically
    except Exception as e:
        print(f"Error reading table file {table_file_path.name}: {e}")
        raise IOError(f"Could not read table file {table_file_path.name}") from e

    object_chunks = _split_tmdl_objects(content)
    
    # The first object must be the table definition
    if not object_chunks or object_chunks[0][0] != 'table':
        raise ValueError(f"Could not find table definition in {table_file_path.name}")

    table_type, table_chunk = object_chunks.pop(0)
    
    # --- Parse Table Properties ---
    table_name_match = re.search(r"^\s*table\s+(?:(['\"])(.+?)\1|([\w\.-]+))", table_chunk, re.MULTILINE)
    table_name = table_name_match.group(2) or table_name_match.group(3)
    table_obj = Table(name=table_name)
    
    table_body_lines = table_chunk.splitlines()[1:]
    properties, annotations = parse_properties_and_annotations(table_body_lines)
    table_obj.isHidden = properties.get('isHidden', 'false').lower() == 'true'
    table_obj.description = properties.get('description')
    table_obj.annotations.extend(annotations)

    # --- Parse Column and Measure Objects ---
    for obj_type, chunk in object_chunks:
        parsed_data = _parse_object_chunk(obj_type, chunk)
        if not parsed_data:
            continue
            
        obj_properties = parsed_data.get('properties', {})
        obj_annotations = parsed_data.get('annotations', [])
        obj_description = obj_properties.get('description')

        if parsed_data.get('is_measure'):
            measure = Measure(
                name=parsed_data['name'],
                daxExpression=parsed_data.get('daxExpression', ''),
                formatString=obj_properties.get('formatString'),
                isHidden=obj_properties.get('isHidden', 'false').lower() == 'true',
                description=obj_description,
                annotations=obj_annotations
            )
            table_obj.measures.append(measure)
        
        elif parsed_data.get('is_calc_col'):
            calc_col = CalculatedColumn(
                name=parsed_data['name'],
                daxExpression=parsed_data.get('daxExpression', ''),
                dataType=obj_properties.get('dataType', 'string'),
                formatString=obj_properties.get('formatString'),
                isHidden=obj_properties.get('isHidden', 'false').lower() == 'true',
                summarizeBy=obj_properties.get('summarizeBy', 'none'),
                description=obj_description,
                annotations=obj_annotations
            )
            table_obj.columns.append(calc_col)

        elif parsed_data['type'] == 'column':
            col = Column(
                 name=parsed_data['name'],
                 dataType=obj_properties.get('dataType', 'string'),
                 sourceColumn=obj_properties.get('sourceColumn'),
                 formatString=obj_properties.get('formatString'),
                 isHidden=obj_properties.get('isHidden', 'false').lower() == 'true',
                 summarizeBy=obj_properties.get('summarizeBy', 'none'),
                 description=obj_description,
                 annotations=obj_annotations
            )
            table_obj.columns.append(col)

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

def _split_tmdl_objects(content: str) -> list[tuple[str, str]]:
    """
    Splits the content of a TMDL file into a list of object chunks.
    
    This function uses a regular expression to find the start of each object
    (table, column, measure) and splits the file content based on these
    definitions.

    Returns:
        A list of tuples, where each tuple contains the object type 
        (e.g., 'table', 'column') and the text block for that object.
    """
    # Regex to find the start of a new object definition (table, column, or measure)
    # It looks for the start of a line, optional indentation, the keyword, and a name.
    object_start_pattern = re.compile(r"^(?P<indent>\s*)(?P<type>table|column|measure)\s+(?:['\"].+?['\"]|[\w\.-]+)", re.MULTILINE)
    
    # Find all starting positions of objects
    matches = list(object_start_pattern.finditer(content))
    if not matches:
        return []

    objects = []
    for i, match in enumerate(matches):
        # The start of the current chunk is the start of the current match
        start_pos = match.start()
        # The end of the chunk is the start of the next match, or the end of the file
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        
        # The content of the chunk
        chunk = content[start_pos:end_pos].strip()
        
        # The type of the object (e.g., 'table', 'column')
        obj_type = match.group('type')
        
        objects.append((obj_type, chunk))
        
    return objects


def _parse_object_chunk(obj_type: str, chunk: str) -> dict[str, Any]:
    """
    Parses a single TMDL object text chunk into a dictionary of properties.

    This replaces the old 'process_object' helper. It's responsible for 
    parsing one self-contained block of text for a single column or measure.
    """
    lines = chunk.splitlines()
    def_line = lines[0]
    body_lines = lines[1:]
    
    parsed_data = {'type': obj_type}
    name = ""
    is_calc_col = False
    is_measure = False
    single_line_dax = None
    dax_part = None

    # --- Parse Definition Line ---
    if obj_type == 'column':
        col_match = re.match(r"^\s*column\s+(?:(['\"])(.+?)\1|([\w\.-]+))(?:\s*=\s*(.*))?$", def_line.strip())
        if not col_match: return None
        name = col_match.group(2) or col_match.group(3)
        dax_part = col_match.group(4)
        if dax_part is not None:
            is_calc_col = True
            if not dax_part.strip().startswith("```"):
                single_line_dax = dax_part.strip()

    elif obj_type == 'measure':
        mea_match = re.match(r"^\s*measure\s+(?:(['\"])(.+?)\1|([\w\.-]+))\s*=\s*(.*)$", def_line.strip())
        if not mea_match: return None
        name = mea_match.group(2) or mea_match.group(3)
        dax_part = mea_match.group(4)
        is_measure = True
        if not dax_part.strip().startswith("```"):
            single_line_dax = dax_part.strip()
    
    parsed_data['name'] = name

    # --- Parse Properties and Annotations from the object's body ---
    properties, annotations = parse_properties_and_annotations(body_lines)
    parsed_data['properties'] = properties
    parsed_data['annotations'] = annotations
    
    # --- Determine DAX Expression ---
    dax_expression = None
    if single_line_dax:
        dax_expression = single_line_dax
    elif dax_part: # Check for multiline
        full_block_text = dax_part + "\n" + "\n".join(body_lines)
        multiline_dax = parse_multiline_dax(full_block_text)
        dax_expression = multiline_dax

    if dax_expression:
        parsed_data['daxExpression'] = dax_expression

    # Reclassify calculated columns if they have a sourceColumn property
    if is_calc_col and 'sourceColumn' in properties:
        is_calc_col = False
    
    parsed_data['is_calc_col'] = is_calc_col
    parsed_data['is_measure'] = is_measure

    return parsed_data


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
                    continue
                
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
