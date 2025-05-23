'''
🚀 AI-Powered Travel Planner with Memory
========================================

📌 **Project Overview**
This project is an AI-powered travel planner that generates personalized travel 
itineraries using **CrewAI autonomous agents** with memory integration. 
It allows users to plan trips by selecting **destination, budget, number of days, 
and preferred activities**.

📌 **Solution Implementation**
✔ Uses **CrewAI agents** for domain-specific **travel recommendations**.  
✔ Integrates **FAISS (vector database)** for **past trip recall based on similarity**.  
✔ Uses **SQLite (structured database)** to **track exact travel history**.  
✔ Provides **Streamlit UI** for **interactive trip planning**.  
✔ Deployed via **Docker + AWS for scalability**.  

📌 **How It Works (Workflow Overview)**
1️⃣ User enters **travel details** in the UI (destination, budget, days, activities).  
2️⃣ AI memory system **checks for matching past trips** (FAISS + SQLite).  
3️⃣ **CrewAI processes the request**, running **three AI agents**:  
   - **Destination Agent** → Suggests places to visit.  
   - **Budget Agent** → Optimizes cost-effective travel plans.  
   - **Itinerary Agent** → Generates a structured day-by-day trip schedule.  
4️⃣ AI generates a **customized travel plan** using learned preferences.  
5️⃣ **Final itinerary and past trips are displayed on the Streamlit UI**.  

📌 **Technology Stack**
✅ **Frontend UI** → Streamlit (for user input & result display)  
✅ **Backend Logic** → CrewAI, Python (for autonomous reasoning)  
✅ **Memory System** → FAISS (AI recall) + SQLite (structured past trip storage)  
✅ **Containerization** → Docker (for cloud deployment)  
✅ **Cloud Hosting** → AWS (scalable remote access)  

📌 **Execution Instructions**
💡 **Run Locally:**  
pip install -r requirements.txt
streamlit run app.py
'''

import streamlit as st
from crewai import Crew
from dotenv import load_dotenv
from crewai_agents.destination_agent import DestinationAgent
from crewai_agents.budget_agent import BudgetAgent
from crewai_agents.itinerary_agent import ItineraryAgent
from crewai_tasks.destination_task import DestinationTask
from crewai_tasks.budget_task import BudgetTask
from crewai_tasks.itinerary_task import ItineraryTask
from memory.memory_store import MemoryStore
from memory.memory_db import MemoryDB

# Load API Keys
load_dotenv()

# Initialize memory modules
vector_memory = MemoryStore()
structured_memory = MemoryDB()

st.title("🌍 AI-Powered Travel Planner with Memory")

destination = st.text_input("Where would you like to travel?")
budget = st.number_input("Select your budget:", min_value=1000, max_value=50000, step=5000)
days = st.number_input("How many days will your trip be?", min_value=1, max_value=30, step=1)
activities = st.text_input("What activities do you like? (e.g., hiking, museums, food)")

if st.button("Generate Travel Plan"):
    user_inputs = {"destination": destination.strip(), "budget": budget, "days": days, "activities": activities.strip()}
    
    # Store trip in memory only if it's not already stored
    structured_memory.store_trip(destination, budget, days, activities)
    vector_memory.store_user_trip(user_inputs)

    # Display the current planned trip
    st.subheader("🧠 Current Planned Trip:")
    st.write(f"Destination: {destination}, Budget: {budget}, Days: {days}, Activities: {activities}")

    # Retrieve only past trips matching the destination
    past_trips_db = structured_memory.get_past_trips_by_destination(destination)

    if past_trips_db:
        st.subheader(f"🧠 Your Past Planned Trips for {destination} (Database Memory):")
        for trip in past_trips_db:
            if trip[0] != destination or trip[1] != budget or trip[2] != days or trip[3] != activities:
                st.write(f"Destination: {trip[0]}, Budget: {trip[1]}, Days: {trip[2]}, Activities: {trip[3]}")

    # CrewAI Execution
    crew = Crew(
        agents=[DestinationAgent(), BudgetAgent(), ItineraryAgent()],
        tasks=[DestinationTask(destination), BudgetTask(budget), ItineraryTask(destination, days, activities)]
    )

    travel_plan = crew.kickoff()

    if travel_plan:
        st.subheader("✈️ Your Travel Itinerary:")
        st.text_area("✈️ Travel Itinerary:", travel_plan, height=300)
    else:
        st.write("⚠️ Travel itinerary generation failed. Please try again.")
