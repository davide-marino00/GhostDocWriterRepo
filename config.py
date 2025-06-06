import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# --- Load Environment Variables ----
print("Attempting to load environment variables from .env file...")
# Look for .env in the same directory as this script.
dotenv_path = Path(__file__).parent / '.env'
if dotenv_path.is_file():
    load_dotenv(dotenv_path=dotenv_path, override=True, verbose=True)
    print(".env file loaded.")
else:
    print(".env file not found, relying on system environment variables.")


# --- Path Configuration (Loaded from Environment - REQUIRED) ---
SCRIPT_DIR = Path(__file__).parent.resolve()
input_path_str = os.getenv("PBI_EXTRACT_ROOT_DIR")
output_path_str = os.getenv("OUTPUT_DIR")

# If paths are set, make them absolute based on the script's location.
PBI_EXTRACT_ROOT_DIR = (SCRIPT_DIR / input_path_str).resolve() if input_path_str else None
OUTPUT_DIR = (SCRIPT_DIR / output_path_str).resolve() if output_path_str else None

# --- Filename Configuration (Loaded from Environment with Defaults) ---
# All filenames and directory names are now loaded from .env for full control.
# Sensible defaults are provided so the script works out-of-the-box.
MODEL_DIR_NAME = os.getenv("MODEL_DIR_NAME", "Model")
TABLES_TMDL_SUBDIR = os.getenv("TABLES_TMDL_SUBDIR", "tables")
RELATIONSHIP_TMDL_FILE = os.getenv("RELATIONSHIP_TMDL_FILE", "relationships.tmdl")
MODEL_TMDL_FILE = os.getenv("MODEL_TMDL_FILE", "model.tmdl")
REPORT_DIR_NAME = os.getenv("REPORT_DIR_NAME", "Report")
SECTIONS_SUBDIR = os.getenv("SECTIONS_SUBDIR", "sections")
VISUAL_CONTAINERS_SUBDIR = os.getenv("VISUAL_CONTAINERS_SUBDIR", "visualContainers")

# Intermediate JSON output filenames
OUTPUT_TABLES_JSON_SUBDIR = os.getenv("OUTPUT_TABLES_JSON_SUBDIR", "tables")
OUTPUT_RELATIONSHIPS_JSON_FILE = os.getenv("OUTPUT_RELATIONSHIPS_JSON_FILE", "relationships.json")
OUTPUT_MODEL_SUMMARY_JSON_FILE = os.getenv("OUTPUT_MODEL_SUMMARY_JSON_FILE", "model_summary.json")
OUTPUT_REPORT_LAYOUT_JSON_FILE = os.getenv("OUTPUT_REPORT_LAYOUT_JSON_FILE", "report_layout.json")

OUTPUT_FORMATS = ['md']

# Final documentation filenames
FINAL_MARKDOWN_FILENAME = os.getenv("FINAL_MARKDOWN_FILENAME", "Ghostwritten.md")
FINAL_JSON_FILENAME = os.getenv("FINAL_JSON_FILENAME", "Ghostwritten.json")

OUTPUT_MARKDOWN_FILE = OUTPUT_DIR / FINAL_MARKDOWN_FILENAME if OUTPUT_DIR else None
OUTPUT_FULL_DATA_JSON_FILE = OUTPUT_DIR / FINAL_JSON_FILENAME if OUTPUT_DIR else None

# --- Azure OpenAI Configuration (Loaded from Environment - REQUIRED) ---
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

# --- LLM Configuration (Loaded from Environment with Defaults) ---
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.1))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", 512))
LLM_REQUEST_TIMEOUT = int(os.getenv("LLM_REQUEST_TIMEOUT", 60))
LLM_CONCURRENCY_LIMIT = int(os.getenv("LLM_CONCURRENCY_LIMIT", 3))

# --- Prompt Template Files ---
PROMPT_TEMPLATE_DIR = SCRIPT_DIR
PROMPT_TABLE_DESC_FILE = PROMPT_TEMPLATE_DIR / "prompt_table_desc.txt"
PROMPT_COLUMN_DESC_FILE = PROMPT_TEMPLATE_DIR / "prompt_column_desc.txt"
PROMPT_DAX_EXPLAIN_FILE = PROMPT_TEMPLATE_DIR / "prompt_dax_explain.txt"
PROMPT_MODEL_OVERVIEW_FILE = PROMPT_TEMPLATE_DIR / "prompt_model_overview.txt"
PROMPT_FILTER_EXPLAIN_FILE = PROMPT_TEMPLATE_DIR / "prompt_filter_explain.txt"

# --- Script Parsing Constants (Loaded from Environment with Defaults) ---
# These filenames, used for parsing the PBI structure, are now configurable.
REPORT_CONFIG_FILE = os.getenv("REPORT_CONFIG_FILE", "config.json")
REPORT_FILTERS_FILE = os.getenv("REPORT_FILTERS_FILE", "filters.json")
REPORT_JSON_FILE = os.getenv("REPORT_JSON_FILE", "report.json")
SECTION_CONFIG_FILE = os.getenv("SECTION_CONFIG_FILE", "config.json")
SECTION_FILTERS_FILE = os.getenv("SECTION_FILTERS_FILE", "filters.json")
SECTION_JSON_FILE = os.getenv("SECTION_JSON_FILE", "section.json")
VISUAL_CONTAINER_JSON_FILE = os.getenv("VISUAL_CONTAINER_JSON_FILE", "visualContainer.json")
VISUAL_CONFIG_JSON_FILE = os.getenv("VISUAL_CONFIG_JSON_FILE", "config.json")
VISUAL_FILTERS_JSON_FILE = os.getenv("VISUAL_FILTERS_JSON_FILE", "filters.json")
VISUAL_DATATRANSFORMS_JSON_FILE = os.getenv("VISUAL_DATATRANSFORMS_JSON_FILE", "dataTransforms.json")


# --- Validation ---
def validate_config():
    """Checks if essential configuration values are set."""
    print("\n--- Validating Configuration ---")
    valid = True

    # Check Required Paths
    print("Checking Required Paths from .env file...")
    if not input_path_str or not PBI_EXTRACT_ROOT_DIR:
        print("  ERROR: PBI_EXTRACT_ROOT_DIR is not set in your .env file.")
        valid = False
    elif not PBI_EXTRACT_ROOT_DIR.is_dir():
        print(f"  ERROR: Input directory '{PBI_EXTRACT_ROOT_DIR}' not found.")
        valid = False
    else:
        print(f"  OK: Input directory found at '{PBI_EXTRACT_ROOT_DIR}'.")

    if not output_path_str or not OUTPUT_DIR:
        print("  ERROR: OUTPUT_DIR is not set in your .env file.")
        valid = False
    elif not OUTPUT_DIR.exists():
        print(f"  INFO: Output directory '{OUTPUT_DIR}' does not exist. It will be created.")
    else:
        print(f"  OK: Output directory found at '{OUTPUT_DIR}'.")

    # Check Required Azure Credentials
    print("Checking Azure OpenAI Credentials from .env file...")
    creds = {"Endpoint": AZURE_OPENAI_ENDPOINT, "API Key": AZURE_OPENAI_API_KEY, "API Version": AZURE_OPENAI_API_VERSION, "Chat Deployment Name": AZURE_OPENAI_CHAT_DEPLOYMENT_NAME}
    missing_creds = [name for name, value in creds.items() if not value]
    if missing_creds:
        print(f"  ERROR: Missing Azure OpenAI environment variables: {', '.join(missing_creds)}")
        valid = False
    else:
        print(f"  OK: Azure OpenAI Credentials loaded.")
        print(f"      Using Endpoint: {AZURE_OPENAI_ENDPOINT}")

    # Check Prompt Template Files
    print("Checking Prompt Template Files...")
    prompt_files = {
        "Table Description": PROMPT_TABLE_DESC_FILE, "Column Description": PROMPT_COLUMN_DESC_FILE,
        "DAX Explanation": PROMPT_DAX_EXPLAIN_FILE, "Model Overview": PROMPT_MODEL_OVERVIEW_FILE
    }
    missing_prompts = [f"{name} ({path.name})" for name, path in prompt_files.items() if not path.is_file()]
    if missing_prompts:
        print(f"  ERROR: Missing prompt template files: {', '.join(missing_prompts)}")
        valid = False
    else:
        print("  OK: All required prompt template files found.")


    print("--- Validation Complete ---")
    if not valid:
        print("\nConfiguration is invalid. Please check your .env file and folder structure.")
        sys.exit(1)
    return valid

if __name__ == "__main__":
    validate_config()