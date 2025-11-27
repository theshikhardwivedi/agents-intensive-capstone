import os
import google.generativeai as genai
import json

def configure_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not set.")
    genai.configure(api_key=api_key)

def gemini_generate(prompt, model="gemini-pro", json_output=False):
    response = genai.GenerativeModel(model).generate_content(prompt)
    text = response.text
    if json_output:
        return json.loads(text)
    return text
