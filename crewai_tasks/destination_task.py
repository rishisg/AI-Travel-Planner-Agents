# ✅ crewai_tasks/ (Agent Tasks)
# 📌 Purpose: Assign specific tasks to AI agents.
# 1️⃣ destination_task.py (Destination Selection)

from crewai import Task
from crewai_agents.destination_agent import DestinationAgent  # Import the agent

class DestinationTask(Task):
    def __init__(self, destination):
        super().__init__(
            name="Find Travel Destination",
            description=f"Suggest the best places to visit in {destination}.",
            expected_output="A list of top attractions and activities.",
            agent=DestinationAgent()  # Assign agent here
        )
