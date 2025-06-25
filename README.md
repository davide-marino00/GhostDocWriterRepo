# GhostDocWriter: AI-Powered Power BI Documentation

**An AI-powered tool to automatically generate documentation for your Power BI models using Azure OpenAI and TMDL metadata.**

---

## Overview
GhostDocWriter streamlines the often tedious process of documenting Power BI reports. By parsing the metadata extracted by `pbi-tools`, it leverages the power of Large Language Models to generate business-friendly descriptions for tables, columns, and complex DAX measures. This tool is designed for Power BI developers, data analysts, and consultants who need to create and maintain clear, comprehensive documentation with minimal effort.

## Features
-   **Automated Parsing:** Ingests `pbi-tools` TMDL output for data models, relationships, and measures.
-   **Report Structure Analysis:** Deconstructs report pages, visuals, and filters from the report's JSON metadata.
-   **AI-Powered Descriptions:** Utilizes Azure OpenAI to generate clear explanations for your data model components.
-   **Markdown & JSON Output:** Produces a clean, readable Markdown report for documentation portals and a comprehensive JSON file for programmatic use.

## Prerequisites
Before you begin, ensure you have the following:
* Python 3.8+ installed on your machine.
* An Azure Subscription with permissions to create and manage Azure OpenAI resources.
* A Power BI report file (`.pbix`).

## Setup and Usage

Follow these steps to get GhostDocWriter running.

### Step 1: Prepare Your Power BI File with pbi-tools
First, extract the metadata from your `.pbix` file. We will use the open-source `pbi-tools` for this.

1.  **Download and Extract pbi-tools**
    Download the latest version from the official GitHub releases: [pbi-tools Releases](https://github.com/pbi-tools/pbi-tools/releases). Extract the contents into a folder on your computer.

2.  **Extract Your .pbix File**
    Open a Terminal or PowerShell in the folder where you extracted `pbi-tools`. Run the following command, replacing the example path with the actual path to your report.

    **Example:**
    ```bash
    .\pbi-tools.exe extract "C:\Path\To\Your\Report.pbix"
    ```
    This command will create a new folder (e.g., `Report`). Move this newly created folder into the `input_folder` within the GhostDocWriter project directory.

### Step 2: Configure the Application
Provide your credentials and paths to the script using an environment file.

1.  Open the `.env` file and update it with your paths and Azure credentials. **Use forward slashes (`/`) for paths.**

    **Example `.env` file:**
    ```env
    # --- REQUIRED: Path Configuration ---
    PBI_EXTRACT_ROOT_DIR=input_folder/your_report_folder_name
    OUTPUT_DIR=output_folder

    # --- REQUIRED: Azure OpenAI Configuration ---
    AZURE_OPENAI_ENDPOINT=[https://your-resource-name.openai.azure.com/](https://your-resource-name.openai.azure.com/)
    AZURE_OPENAI_API_KEY=your_secret_key
    AZURE_OPENAI_API_VERSION=2024-12-01-preview
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your_deployment_name
    ```

### Step 3: Run the Documentation Pipeline
Finally, set up the Python environment and run the script.

1.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```
2.  **Install required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the script!** The tool is run as a module from the project root. You can choose to run only specific parts of the pipeline.

    * **To parse local files into intermediate JSON (no AI calls):**
        ```bash
        python -m src.run_pipeline parse
        ```
    * **To generate documentation from existing JSON files (requires AI config):**
        ```bash
        python -m src.run_pipeline generate
        ```
    * **To run the full end-to-end pipeline:**
        ```bash
        python -m src.run_pipeline all
        ```
    The script will generate the documentation in your specified `output_folder`.
=======
GhostDocWriter: AI-Powered Power BI Documentation
An AI-powered tool to automatically generate documentation for your Power BI models using Azure OpenAI and TMDL metadata.

Overview
GhostDocWriter streamlines the often tedious process of documenting Power BI reports. By parsing the metadata extracted by pbi-tools, it leverages the power of Large Language Models to generate business-friendly descriptions for tables, columns, and complex DAX measures. This tool is designed for Power BI developers, data analysts, and consultants who need to create and maintain clear, comprehensive documentation with minimal effort.

Features
Automated Parsing: Ingests pbi-tools TMDL output for data models, relationships, and measures.
Report Structure Analysis: Deconstructs report pages, visuals, and filters from the report's JSON metadata.
AI-Powered Descriptions: Utilizes Azure OpenAI to generate clear explanations for your data model components.
Markdown & JSON Output: Produces a clean, readable Markdown report for documentation portals and a comprehensive JSON file for programmatic use.
Setup and Usage
Follow these steps to get GhostDocWriter running.

Step 1: Prepare Your Power BI File with pbi-tools
First, extract the metadata from your .pbix file. We will use the open-source pbi-tools for this.

Download and Extract pbi-tools
Download the latest version from the official GitHub releases: pbi-tools Releases. Extract the contents into a folder on your computer.

Extract Your .pbix File
Open a Terminal or PowerShell in the folder where you extracted pbi-tools. Run the following command, replacing the example path with the actual path to your report.

Example:

Bash

.\pbi-tools.exe extract "C:\Path\To\Your\Report.pbix"
This command will create a new folder (e.g., Report). Move this newly created folder into the input_folder within the GhostDocWriter project directory.

Step 2: Configure the Application
Provide your credentials and paths to the script using an environment file.

This project uses a .env.example file as a template. Make a copy of it and name it .env:

Bash

# In the project's root folder
cp .env.example .env
Open the new .env file and update it with your paths and Azure credentials. Use forward slashes (/) for paths.

Example .env file:

Code snippet

# --- REQUIRED: Path Configuration ---
PBI_EXTRACT_ROOT_DIR=input_folder/your_report_folder_name
OUTPUT_DIR=output_folder

# --- REQUIRED: Azure OpenAI Configuration ---
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your_secret_key
AZURE_OPENAI_API_VERSION=2024-02-01
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your_deployment_name
Step 3: Run the Documentation Pipeline
Finally, set up the Python environment and run the script.

Create and activate a virtual environment:

Bash

python -m venv venv
.\venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
Install required libraries:

Bash

pip install -r requirements.txt
Run the script! The tool is run as a module from the project root. You can choose to run only specific parts of the pipeline.

To parse local files into intermediate JSON (no AI calls):
Bash

python -m src.run_pipeline parse
To generate documentation from existing JSON files (requires AI config):
Bash

python -m src.run_pipeline generate
To run the full end-to-end pipeline:
Bash

python -m src.run_pipeline all
The script will generate the documentation in your specified output_folder.
>>>>>>> 9a43eb4ce0470ac9f06cf50bbdf62fee7b0f261f
