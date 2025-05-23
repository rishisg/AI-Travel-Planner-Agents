# 2️⃣ budget_agent.py (Budget Planner)

from crewai import Agent

class BudgetAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Budget Planner",
            role="Financial Travel Advisor",
            goal="Optimize travel expenses based on budget constraints.",
            backstory="Expert in cost-effective travel solutions."
        )
