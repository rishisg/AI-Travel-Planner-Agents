# 2️⃣ budget_task.py (Budget Optimization)

from crewai import Task
from crewai_agents.budget_agent import BudgetAgent

class BudgetTask(Task):
    def __init__(self, budget):
        super().__init__(
            name="Optimize Travel Budget",
            description=f"Suggest cost-effective travel plans for a budget of {budget}.",
            expected_output="A financial breakdown of affordable travel expenses.",
            agent=BudgetAgent()  # Assign agent here
        )
