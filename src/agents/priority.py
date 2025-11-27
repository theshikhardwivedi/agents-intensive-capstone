from src.utils import gemini_generate

class PriorityAgent:
    def run(self, tasks, context):
        prompt = f"Given these tasks: {tasks} and context: {context}, rank tasks by priority. Return JSON with 'task' and 'priority'."
        return gemini_generate(prompt, json_output=True)
