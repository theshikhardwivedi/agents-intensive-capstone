from src.utils import gemini_generate

class SchedulerAgent:
    def run(self, prioritized_tasks):
        prompt = f"Create a structured schedule for these tasks: {prioritized_tasks}. Include start_time, end_time, and dependencies. Return JSON."
        return gemini_generate(prompt, json_output=True)
