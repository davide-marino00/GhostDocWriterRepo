# ****GhostDocWriter: AI-Powered Power BI Documentation****
This guide provides all the necessary steps to set up and run ****GhostDocWriter****, a tool that automatically generates documentation for your Power BI reports using Azure OpenAI.

### *Prerequisites*
Before you begin, ensure you have the following:

Python 3.8+ installed on your machine.
An Azure Subscription with permissions to create and manage Azure OpenAI/AI Foundry resources.
A Power BI report file (.pbix).


### **Part 1: Prepare Your Power BI File**
The first step is to extract the metadata from your .pbix file into a folder structure that the script can read. We will use the open-source pbi-tools for this.

Download and Extract pbi-tools

Download the latest version from the official GitHub releases:       
https://github.com/pbi-tools/pbi-tools/releases/download/1.2.0/pbi-tools.1.2.0.zip    
Extract the contents of the zip file into a folder on your computer.    

Extract Your .pbix File  
Open a Terminal (or PowerShell) directly in the folder where you extracted pbi-tools.
(for Terminal, right click on the folder canvas where pbi-tools resides)
Run the following command, replacing <path-to-your-pbix-file> with the actual path to your report.
<!-- end list -->


#### Example for Windows

>.\pbi-tools.exe extract "C:\Users\yourusername\Documents\yourreport.pbix"

The command will create a new folder with the same name as your report (e.g., Documents\Sales Report).
Move this newly created folder into the *input_folder* within the ****GhostDocWriter**** project directory.

### **Part 2: Set Up Azure OpenAI Service**
Next, you need to deploy a model in Azure and get the necessary credentials to connect your script to it. 
Log in to the Azure Portal.
Search for "Azure OpenAI" or "AI Foundry" and create an instance.
Access the instance, on the left side of the AI Foundry UI you will find the "Deployments" section. click on it.
Deploy a model (base model):
Choose a **gpt-4o-mini** model. Deployment name: use **gpt-4o-mini**. This name is what your script will use to call the model.  
Make sure the Model Version is **'2024-07-18'**

Find Your Credentials:
Go back to your Azure OpenAI resource page in the Azure Portal.
On the left-hand menu, under Resource Management, click Keys and Endpoint.
or From Azure AIFoundry instance, on the left-hand menu click Deployments --> then your click on your model.

Here you will find two critical pieces of information:
Endpoint: The URL for your service (e.g., https://your-service.openai.azure.com/).
Key: Two secret keys are provided (KEY 1 and KEY 2). You only need to copy one.

**Part 3: Configure the Application**
Now, you will provide the credentials from Azure to the ****GhostDocWriter**** script using an environment file.
Locate the .env file in the **GhostDocWriter** project directory.
Update the file with the values you just retrieved. The file should look like this:

#### REQUIRED: Path Configuration 
PBI_EXTRACT_ROOT_DIR=input_folder/yourreport  
OUTPUT_DIR=ouput_folder  

#### REQUIRED: Azure OpenAI Configuration    
AZURE_OPENAI_ENDPOINT=https://your-service.openai.azure.com/  
AZURE_OPENAI_API_KEY=your-secret-key-from-azure  
AZURE_OPENAI_API_VERSION=2024-07-18  
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-mini  

**Note**: .env file do not use "" or '' for values


### **Part 4: Run the Documentation Pipeline**
The final step is to set up the Python environment and run the script.
Open a Terminal in the root directory of the **GhostDocWriter** project.
Create a Virtual Environment to keep your project dependencies isolated.

> python -m venv venv

Activate the Environment.
On Windows:
> .\venv\Scripts\activate
On macOS / Linux:
> source venv/bin/activate

*You will know it's active when you see (venv) at the beginning of your terminal prompt.*

**Install Required Libraries using the provided requirements.txt file.**

>pip install -r requirements.txt

**Run the Script!**

>python run_pipeline.py

The script will now execute, generating the documentation in your specified output_folder.

**Advanced Configuration (Optional)**
By default, the script generates a Markdown (.md) file. You can change this to output a JSON file (useful for integrations like Jira) or both.

*Open the config.py file.*         
Locate the line               
OUTPUT_FORMATS = ['md'] (around line 47).      
Modify the list to suit your needs:       
For JSON only:        
> OUTPUT_FORMATS = ['json']

For both Markdown and JSON:         
> OUTPUT_FORMATS = ['md', 'json']    

Customizing Filenames
You can change the names of output files in the .env file. Just ensure the file extensions (.md, .json) are kept.
