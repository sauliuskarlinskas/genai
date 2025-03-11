import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

# Load API key from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Information to process
information = "Jaunius Pinelis is a great developer and loves to code. Lives in Vilnius, Lithuania."

# Send request
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information from user messages."},
        {"role": "user", "content": f"Here is some information: {information}"},
        {"role": "user", "content": "Who is Jaunius Pinelis?"},
    ],
)

# Extract response
event = completion.choices[0].message.content
print(event)
