from google.adk.agents import SequentialAgent, TaskAgent

extractor_agent = TaskAgent(
    name="ExtractorAgent",
    description="Extract tasks from PDF text",
    task=lambda context: {'tasks': context['pdf_text'].split('\n')[:10]}
)

priority_agent = TaskAgent(
    name="PriorityAgent",
    description="Sort tasks alphabetically",
    task=lambda context: {'prioritized': sorted([t for t in context['tasks'] if t.strip()])}
)

scheduler_agent = TaskAgent(
    name="SchedulerAgent",
    description="Assign tasks to sequential days",
    task=lambda context: {'schedule': [(task, f'Day {i+1}') for i, task in enumerate(context['prioritized'])]}
)

orchestrator = SequentialAgent(agents=[extractor_agent, priority_agent, scheduler_agent])

context = {'pdf_text': pdf_text}
result = orchestrator.run(context)

print("Workflow Result:")
for task, day in result['schedule']:
    print(f"{day}: {task}")
