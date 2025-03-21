
import os
from google import genai
from dotenv import load_dotenv
import PIL.Image

#path to the image as2023
image = PIL.Image.open(r"C:\Users\gaidy\Documents\genai\genai\examples\google-ai\as2023.jpg")

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=gemini_api_key,
    )
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Apibūdink žmogų nuotraukoje", image])

print(response.text)

