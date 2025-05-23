# AI Agents
# 📌 Purpose: Define AI-powered agents specializing in different aspects 
# of travel planning.
# 1️⃣ destination_agent.py (Destination Expert)

from crewai import Agent

class DestinationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Destination Expert",
            role="Travel Guide",
            goal="Find the best destinations for personalized travel.",
            backstory="Experienced in travel recommendations and cultural insights.",
            model="gpt-4-turbo"
        )
