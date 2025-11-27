from src.utils import gemini_generate

class ReflectionAgent:
    def run(self, schedule):
        prompt = f"Review this schedule: {schedule}. Suggest improvements for efficiency and feasibility. Return updated JSON."
        return gemini_generate(prompt, json_output=True)
