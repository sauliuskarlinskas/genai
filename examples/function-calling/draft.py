from rich import print
import os
from dotenv import load_dotenv
import json
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get OpenAI API key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    print("Please set OPENAI_API_KEY in .env file")
    exit()

# Function to retrieve city info from a file
def get_info_about_city():
    file_path = r"C:\Users\gaidy\Documents\genai\genai\examples\function-calling\skuodas.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()  # Read entire file and remove extra spaces/newlines
        return content  # Return the raw text
    except FileNotFoundError:
        print("File not found")
        return None

# Function to write content to a file
def write_to_file(content: str, filename: str = "skuodas_output.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return os.path.abspath(filename)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=openai_api_key
)

# Define available tools
tools = [{
    "type": "function",
    "function": {
        "name": "get_info_about_city",
        "description": "Get information about the city.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    }
}, {
    "type": "function",
    "function": {
        "name": "write_to_file",
        "description": "Write content to a file and return the absolute path.",
        "parameters": {
            "type": "object",
            "properties": {
                "content": {"type": "string"}
            },
            "required": ["content"],
            "additionalProperties": False
        },
        "strict": True
    }
}]

# Step 1: Ask OpenAI a question about Skuodas
messages = [{"role": "user", "content": "What is the origin of name Skuodas?"}]

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools
)

# Step 2: Extract tool call
tool_calls = completion.choices[0].message.tool_calls

if tool_calls:
    tool_call = tool_calls[0]  # Get the first tool call

    # Step 3: Check which tool is being called
    if tool_call.function.name == "get_info_about_city":
        city_info = get_info_about_city()
        
        # Step 4: Send retrieved info back to OpenAI
        messages.append({
            "role": "assistant",
            "tool_calls": tool_calls  # Properly linking tool call
        })
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": city_info
        })

        # Step 5: Ask OpenAI to interpret the city info
        completion_2 = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools
        )

        final_response = completion_2.choices[0].message.content

        if final_response:
            file_path = write_to_file(final_response)
            print(f"Answer written to file: {file_path}")
        else:
            print("No valid response received.")
