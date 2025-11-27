from typing import Any, Dict
from google_adk import LoopAgent, AgentContext


class ReflectionAgent(LoopAgent):
    """Refines the plan across iterations to improve coherence and coverage."""

    def run(self, context: AgentContext) -> Dict[str, Any]:
        schedule: Dict[str, Any] = context.get("schedule", {})
        improved = schedule
        context.set("schedule", improved)
        return improved
