# 3️⃣ itinerary_agent.py (Itinerary Planner)

from crewai import Agent

class ItineraryAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Itinerary Planner",
            role="Travel Scheduler",
            goal="Create structured day-by-day plans with optimal activities.",
            backstory="Has extensive knowledge of trip logistics."
        )
