from google.adk.agents import SequentialAgent

class ExtractorAgent:
    def run(self, context):
        return {'tasks': context.get('pdf_text', '').split('\n')[:10]}

class PriorityAgent:
    def run(self, context):
        tasks = context.get('tasks', [])
        return {'prioritized': sorted([t for t in tasks if t.strip()])}

class SchedulerAgent:
    def run(self, context):
        prioritized = context.get('prioritized', [])
        return {'schedule': [(task, f'Day {i+1}') for i, task in enumerate(prioritized)]}

def run_orchestrator(pdf_text: str):
    orchestrator = SequentialAgent([
        ExtractorAgent(),
        PriorityAgent(),
        SchedulerAgent()
    ])
    context = {'pdf_text': pdf_text}
    return orchestrator.run(context)
