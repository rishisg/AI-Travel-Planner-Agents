# 3️⃣ itinerary_task.py (Full Travel Schedule)

from crewai import Task
from crewai_agents.itinerary_agent import ItineraryAgent

class ItineraryTask(Task):
    def __init__(self, destination, days, activities):
        super().__init__(
            name="Generate Travel Itinerary",
            description=f"Create a {days}-day itinerary for {destination} including activities: {activities}.",
            expected_output="A detailed day-by-day travel schedule.",
            agent=ItineraryAgent()  # Assign agent here
        )
