import os
from dotenv import load_dotenv
from crewai import Crew, Agent, Task

# Load environment variables from .env
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Print the API key to verify if it is correctly loaded
print(f"Loaded OpenAI API Key: {api_key}")

# Define a sample CrewAI agent
destination_agent = Agent(
    name="Destination Expert",
    role="Travel Guide",
    goal="Find the best destinations for personalized travel.",
    backstory="Experienced in travel recommendations and cultural insights.",
    model="gpt-4-turbo",
    openai_api_key=api_key  # Ensure API key is passed explicitly
)

# ✅ Corrected: Assign an agent to the task
destination_task = Task(
    description="Suggest top travel destinations based on user preferences.",
    expected_output="A list of recommended destinations based on budget and activities.",
    agent=destination_agent  # 🔥 Fix: Assigning the correct agent
)

# Initialize Crew with agents and tasks
crew = Crew(agents=[destination_agent], tasks=[destination_task])

# Run the CrewAI process and print results
travel_plan = crew.kickoff()
print("\nGenerated Travel Plan:")
print(travel_plan)
