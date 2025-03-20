from rich import print
import os 
from dotenv import load_dotenv
#import requests
from openai import OpenAI

import json

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    print("Please set OPENAI_API_KEY in .env file")

def get_info_about_city():
    file_path = r"C:\Users\gaidy\Documents\genai\genai\examples\function-calling\skuodas.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()  # Read entire file and remove extra spaces/newlines
        return content  # Return the raw text
    except FileNotFoundError:
        print("File not found")
        return None

#city_name = get_info_about_city()
#print(city_name)

def write_to_file(content: str, filename: str = "skuodas_output.txt"):
        with open(filename, 'w') as file:
            file.write(content)
        return os.path.abspath(filename)
#print(write_to_file("content"))


client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=openai_api_key
)

tools = [{
    "type": "function",
    "function": {
        "name": "get_info_about_city",
        "description": "Get information about city.",
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

completion=client.chat.completions.create(
      model="gpt-4o",
    messages=[{"role": "system", "content": "When was the city of Skuodas founded?"}],
    tools=tools
)
#print(completion)

tool_call = completion.choices[0].message.tool_calls[0]
#print(tool_call)
args = json.loads(tool_call.function.arguments)

result = get_info_about_city()
#print(result)

messages = []

messages.append({
   "role": "tool",
    "tool_call_id": tool_call.id,
    "content": str(result)
})

#print(messages)

comletion_2 = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools
)

#print(comletion_2)