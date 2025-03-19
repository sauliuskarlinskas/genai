from rich import print
import os 
from dotenv import load_dotenv
import requests
from openai import OpenAI

import json

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    print("Please set OPENAI_API_KEY in .env file")