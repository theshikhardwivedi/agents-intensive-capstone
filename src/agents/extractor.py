from src.utils import gemini_generate

class ExtractorAgent:
    def run(self, input_text):
        prompt = f"Extract actionable tasks from the following text:\n{input_text}\nReturn as JSON list."
        return gemini_generate(prompt, json_output=True)
