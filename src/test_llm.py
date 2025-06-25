import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# --- 1. Load Environment Variables ---
print("Attempting to load .env file...")
if load_dotenv():
    print(".env file loaded successfully.")
else:
    print("ERROR: .env file not found. Make sure this script is in the project root.")
    exit()

# --- 2. Read Credentials from Environment ---
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

print("\n--- Using the following configuration ---")
print(f"Endpoint:         '{azure_endpoint}'")
print(f"Deployment Name:  '{deployment_name}'")
print(f"API Version:      '{api_version}'")
print("--------------------------------------\n")

# --- 3. Check if all required variables are present ---
if not all([azure_endpoint, api_key, api_version, deployment_name]):
    print("FATAL ERROR: One or more required Azure environment variables are missing in the .env file.")
    exit()

# --- 4. Initialize the LLM Client and Test the Connection ---
try:
    print("Initializing AzureChatOpenAI client...")
    llm = AzureChatOpenAI(
        azure_deployment=deployment_name,
        openai_api_version=api_version,
        azure_endpoint=azure_endpoint,
        openai_api_key=api_key,
        request_timeout=30 # Set a timeout
    )
    print("Client initialized successfully.")

    print("\nAttempting to invoke the model with a simple prompt...")
    # Make a simple, single call to the LLM
    response = llm.invoke("Hello, say 'test successful'.")

    print("\n✅ --- SUCCESS! --- ✅")
    print("Received a valid response from the model:")
    print(f"Response: '{response.content}'")

except Exception as e:
    print("\n❌ --- FAILED! --- ❌")
    print("An error occurred while trying to connect to or invoke the Azure OpenAI service.")
    print("\n--- Full Error Details ---")
    print(e)
    print("--------------------------")