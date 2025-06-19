GhostDocWriter: AI-Powered Power BI Documentation
=================================================

**An AI-powered tool to automatically generate documentation for your Power BI models using Azure OpenAI and TMDL metadata.**

Overview
--------

GhostDocWriter streamlines the often tedious process of documenting Power BI reports. By parsing the metadata extracted by pbi-tools, it leverages the power of Large Language Models to generate business-friendly descriptions for tables, columns, and complex DAX measures. This tool is designed for Power BI developers, data analysts, and consultants who need to create and maintain clear, comprehensive documentation with minimal effort.

Features
--------

*   **Automated Parsing:** Ingests pbi-tools TMDL output for data models, relationships, and measures.
    
*   **Report Structure Analysis:** Deconstructs report pages, visuals, and filters from the report's JSON metadata.
    
*   **AI-Powered Descriptions:** Utilizes Azure OpenAI to generate clear explanations for your data model components.
    
*   **Markdown & JSON Output:** Produces a clean, readable Markdown report for documentation portals and a comprehensive JSON file for programmatic use.
    

Prerequisites
-------------

Before you begin, ensure you have the following:

*   Python 3.8+ installed on your machine.
    
*   An Azure Subscription with permissions to create and manage Azure OpenAI resources.
    
*   A Power BI report file (.pbix).
    

Setup and Usage
---------------

Follow these steps to get GhostDocWriter running.

### Step 1: Prepare Your Power BI File with pbi-tools

First, extract the metadata from your .pbix file. We will use the open-source pbi-tools for this.

1.  **Download and Extract pbi-tools**Download the latest version from the official GitHub releases: [pbi-tools v1.2.0](https://github.com/pbi-tools/pbi-tools/releases/download/1.2.0/pbi-tools.1.2.0.zip). Extract the contents into a folder on your computer.
    
2.  **Example for Windows:**Bash.\\pbi-tools.exe extract "C:\\Users\\yourusername\\Documents\\yourreport.pbix"This command will create a new folder (e.g., yourreport). Move this newly created folder into the input\_folder within the GhostDocWriter project directory.
    

### Step 2: Set Up Azure OpenAI Service

Next, deploy a model in Azure to get the necessary credentials.

1.  Log in to the Azure Portal, search for "Azure OpenAI", and create a resource.
    
2.  In your new Azure OpenAI resource, navigate to the **Deployments** section.
    
3.  Deploy a new model:
    
    *   **Model:** gpt-4o-mini
        
    *   **Deployment name:** gpt-4o-mini (the script uses this name).
        
    *   **Model Version:** 2024-07-18
        
4.  Navigate to the **Keys and Endpoint** section in your resource page to find your credentials. You will need the **Endpoint** URL and one of the secret **Keys** (KEY 1 or KEY 2).
    

### Step 3: Configure the Application

Provide your credentials to the script using an environment file.

1.  Bash# In the project's root foldercp .env.example .env
    
2.  **Example .env file:**
3.  Code snippet# --- REQUIRED: Path Configuration ---PBI\_EXTRACT\_ROOT\_DIR=input\_folder/yourreportOUTPUT\_DIR=output\_folder# --- REQUIRED: Azure OpenAI Configuration ---AZURE\_OPENAI\_ENDPOINT=https://your-service.openai.azure.com/AZURE\_OPENAI\_API\_KEY=your-secret-key-from-azureAZURE\_OPENAI\_API\_VERSION=2024-07-18AZURE\_OPENAI\_CHAT\_DEPLOYMENT\_NAME=gpt-4o-mini# --- OPTIONAL: Output Filename Configuration ---FINAL\_MARKDOWN\_FILENAME=Ghostwritten.mdFINAL\_JSON\_FILENAME=Ghostwritten.json**Note:** Do not use quotes (" or ') around the values in the .env file.
    

### Step 4: Run the Documentation Pipeline

Finally, set up the Python environment and run the script.

1.  Bashpython -m venv venv.\\venv\\Scripts\\activate # On Windows# source venv/bin/activate # On macOS/Linux
    
2.  Bashpip install -r requirements.txt
    
3.  The script will generate the documentation in your specified output\_folder.
    
    *   python -m src.run\_pipeline parse
        
    *   python -m src.run\_pipeline generate
        
    *   python -m src.run\_pipeline all
