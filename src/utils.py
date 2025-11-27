import os
import json
from typing import Any, Dict, List
import google.generativeai as genai
from dotenv import load_dotenv


def configure_gemini() -> None:
    """
    Configures the Gemini client using environment variables.
    Expects GOOGLE_API_KEY to be present in the environment or .env file.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY", "")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not set.")
    genai.configure(api_key=api_key)


def get_model(model_name: str = "gemini-1.5-flash") -> genai.GenerativeModel:
    """
    Returns a GenerativeModel instance for the requested model name.
    """
    return genai.GenerativeModel(model_name)


def generate_json(model: genai.GenerativeModel, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    """
    Produces a JSON-compatible response via structured prompting.
    Ensures the returned content is valid JSON by enforcing format in the prompt.
    """
    prompt = (
        f"{system_prompt}\n\n"
        "Return ONLY valid JSON. Do not include commentary or markdown.\n\n"
        f"User request:\n{user_prompt}"
    )
    response = model.generate_content(prompt)
    text = response.text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        corrected = text[start:end + 1] if start != -1 and end != -1 else "{}"
        return json.loads(corrected)


def embed_texts(texts: List[str]) -> List[List[float]]:
    """
    Computes embeddings for a list of texts using Gemini's embedding model.
    Returns a list of embedding vectors.
    """
    outputs = []
    for t in texts:
        res = genai.embed_content(
            model="text-embedding-004",
            content=t,
            task_type="retrieval_document",
        )
        outputs.append(res["embedding"])
    return outputs


def embed_query(text: str) -> List[float]:
    """
    Computes an embedding vector for a query string using the same embedding model.
    """
    res = genai.embed_content(
        model="text-embedding-004",
        content=text,
        task_type="retrieval_query",
    )
    return res["embedding"]
