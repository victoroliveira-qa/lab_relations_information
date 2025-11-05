from google import genai
from config.settings import GEMINI_API_KEY

def gemini_generate(prompt: str, model="gemini-2.5-flash") -> str:

    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(model=model, contents=prompt)
    return response.text.strip()
