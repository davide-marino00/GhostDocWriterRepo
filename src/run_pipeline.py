import time
import asyncio
import sys
import os
import traceback
from pathlib import Path

try:
    import config
except ImportError:
    print("ERROR: config.py not found. Make sure it's in the same directory.")
    sys.exit(1)

# --- Module Imports ---
script_dir = Path(__file__).parent.resolve()
if str(script_dir) not in sys.path:
    sys.path.append(str(script_dir))
try:
    import parse_pbi_model
    import parse_pbi_report
    import generate_documentation
except ImportError as e:
    print(f"ERROR: Could not import necessary script modules.")
    print(f"       Ensure parse_pbi_model.py, parse_pbi_report.py, generate_documentation.py,")
    print(f"       and pbi_data_models.py are in the directory: {script_dir}")
    print(f"Import Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred during module import: {e}")
    traceback.print_exc()
    sys.exit(1)


async def main_pipeline():
    """Runs the complete documentation generation pipeline."""
    start_pipeline_time = time.time()
    print("=============================================")
    print("=== Starting Power BI Documentation Pipeline ===")
    print("=============================================")

    # 1. Validate Configuration
    if not config.validate_config():
        print("\nConfiguration validation failed. Please correct the settings in config.py or your .env file.")
        print("--- Pipeline Halted ---")
        sys.exit(1)

    # 2. Run Model Parsing
    print("\n--- Step 1: Parsing Power BI Model (TMDL) ---")
    try:
        parse_pbi_model.run_parser()
        print("--- Model Parsing Completed Successfully ---")
    except Exception as e:
        print(f"--- ERROR during Model Parsing ---")
        print("--- Pipeline Halted ---")
        sys.exit(1)

    # 3. Run Report Parsing
    print("\n--- Step 2: Parsing Power BI Report Structure (JSON) ---")
    try:
        parse_pbi_report.run_parser()
        print("--- Report Parsing Completed Successfully ---")
    except Exception as e:
        print(f"--- ERROR during Report Parsing ---")
        print("--- Pipeline Halted ---")
        sys.exit(1)

    # 4. Run Documentation Generation (Async)
    print("\n--- Step 3: Generating Documentation (Loading JSON, Calling LLM, Assembling Markdown & JSON) ---")
    try:
        await generate_documentation.run_generation()
        print("--- Documentation Generation Completed Successfully ---")
    except Exception as e:
        print(f"--- ERROR during Documentation Generation ---")
        print("--- Pipeline Halted ---")
        sys.exit(1)

      # 5. Completion
    end_pipeline_time = time.time()
    print("\n=============================================")
    print("=== Power BI Documentation Pipeline Complete ===")
    print(f"Total Pipeline Time: {end_pipeline_time - start_pipeline_time:.2f} seconds")

    # Check config to see which files were *intended* to be generated
    generated_files = []
    if 'md' in config.OUTPUT_FORMATS:
        final_md_path = config.OUTPUT_DIR / config.OUTPUT_MARKDOWN_FILE
        generated_files.append(f"Markdown Output: {final_md_path.resolve()}")
    if 'json' in config.OUTPUT_FORMATS:
        final_json_path = config.OUTPUT_DIR / config.OUTPUT_FULL_DATA_JSON_FILE
        generated_files.append(f"JSON Data Output: {final_json_path.resolve()}")

    if generated_files:
        print("Generated Files:")
        for file_info in generated_files:
            print(f"  - {file_info}")
    else:
        print("No output files were generated based on config.OUTPUT_FORMATS.")

    print("=============================================")
    
# --- Entry Point ---
if __name__ == "__main__":
    try:
        try: loop = asyncio.get_running_loop()
        except RuntimeError: loop = asyncio.new_event_loop(); asyncio.set_event_loop(loop)
        loop.run_until_complete(main_pipeline())
    except SystemExit: 
        print("\nPipeline execution stopped due to errors.")
    except KeyboardInterrupt: 
        print("\nPipeline execution interrupted by user."); sys.exit(1)
    except Exception as main_e:
        print(f"\nAn unexpected error occurred during pipeline execution: {main_e}"); traceback.print_exc(); sys.exit(1)
    finally:
         if 'loop' in locals() and not loop.is_running():
             try: 
                loop.close(); asyncio.set_event_loop(None)
             except Exception as loop_e:
                 print(f"Error closing event loop: {loop_e}")

