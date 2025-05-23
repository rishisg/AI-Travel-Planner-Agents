📌 Project Documentation: AI-Powered Travel Planner Using CrewAI & AWS Docker Deployment
1️⃣ Project Overview
🛠 Assignment Title:
Development of a Domain-Specific Agentic AI Application Using CrewAI & Deploying as Docker on AWS

🎯 Objective:
To design and implement a domain-specific agentic AI application leveraging the CrewAI platform, demonstrating effective collaboration among autonomous agents to solve complex, real-world problems with enhanced capabilities like reasoning, memory, and tool usage.

🌍 Project Summary:
This AI-powered travel planner helps users plan personalized trips based on budget, duration, and activity preferences using CrewAI autonomous agents and GPT-4 Turbo. The application is containerized using Docker and deployed on AWS EC2, ensuring scalability, security, and high availability.

🚀 Live Deployment: http://your-public-ip:8501

2️⃣ Problem Statement
❌ Challenges in Traditional Travel Planning:
✔ Time-consuming & complex—users must manually research destinations, costs, itineraries, and activities. ✔ Lack of personalization—existing tools provide generic results rather than personalized trip suggestions. ✔ Difficulty in budgeting—no AI-driven insights for selecting cost-effective destinations. ✔ Fragmented information sources—users must navigate multiple platforms to build an itinerary.

3️⃣ Solution Approach
✅ AI-Powered Travel Planning
✔ CrewAI Agents work together to suggest destinations, estimate costs, and plan itineraries. ✔ GPT-4 Turbo provides intelligent recommendations based on user input. ✔ FAISS-based Memory System stores past user trips for enhanced personalization. ✔ Docker ensures portability & AWS provides scalability for global access.

4️⃣ Technology Stack
Technology	Purpose
Python 3.11	Core application development
OpenAI GPT-4 Turbo	AI-powered travel insights
CrewAI	Autonomous agents for travel planning
Streamlit	Interactive UI for users
Docker	Containerized deployment
AWS EC2	Cloud hosting platform
FAISS	Memory system for past trip tracking
SQLite	Structured database for trip storage
WinSCP & Putty	File transfer & SSH login
Route 53 (Optional)	Custom domain management
5️⃣ System Architecture
🌍 High-Level Architecture
mermaid
graph TD
    A[User Input: Destination, Budget, Days, Activities] --> B[AI Agents Process Input]
    B --> C[Destination AI Agent Suggests Places]
    B --> D[Budget AI Agent Estimates Costs]
    B --> E[Itinerary AI Agent Plans Schedule]
    C --> F[Final AI-Generated Travel Plan]
    D --> F
    E --> F
    F --> G[User Receives Personalized Itinerary]
🔹 Key Components:
✔ Frontend: Streamlit UI for user interaction ✔ AI Agents: CrewAI-based reasoning & planning ✔ Database: SQLite & FAISS memory storage ✔ Cloud Hosting: AWS EC2 with Docker containers

6️⃣ Application Design
🔹 AI Agent Configuration
Each CrewAI agent specializes in different aspects of travel planning:

1️⃣ Destination Agent → Suggests ideal travel destinations 2️⃣ Budget Agent → Estimates costs based on budget constraints 3️⃣ Itinerary Agent → Plans the trip schedule & activities

📌 CrewAI Agent Example

python
from crewai import Agent

class DestinationAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Destination Expert",
            role="Travel Guide",
            goal="Find the best destinations for personalized travel.",
            model="gpt-4-turbo"
        )
7️⃣ Testing & Validation
✔ Unit Testing CrewAI Agents
Each AI agent undergoes unit testing to verify correct reasoning:

python
import unittest
from crewai_agents.destination_agent import DestinationAgent

class TestDestinationAgent(unittest.TestCase):
    def test_suggest_destination(self):
        agent = DestinationAgent()
        result = agent.suggest_place("Adventure Travel")
        self.assertIn("Hiking", result)
✔ Manual UI Testing
✅ Input different budgets, preferences & verify output accuracy ✅ Check responsiveness & loading speed ✅ Ensure AI memory retrieves past trips correctly

8️⃣ Deployment on AWS EC2 (Docker)
1️⃣ Launch AWS EC2 Instance
✔ Choose Ubuntu 22.04 ✔ Select t2.micro (Free-tier eligible) ✔ Configure Security Groups to allow port 8501

2️⃣ Connect to EC2 & Install Docker
bash
ssh -i your-key.pem ubuntu@your-public-ip
sudo apt update && sudo apt install docker.io -y
sudo systemctl enable docker && sudo systemctl start docker
sudo usermod -aG docker ubuntu && newgrp docker
3️⃣ Transfer Project Files via SCP/WinSCP
bash
scp -i your-key.pem -r /local-folder-path ubuntu@your-public-ip:/home/ubuntu/travel-planner
4️⃣ Build & Run Docker Container
bash
cd /home/ubuntu/travel-planner
docker build -t travel-planner-ai .
docker run -d --restart unless-stopped --env-file .env -p 8501:8501 travel-planner-ai
5️⃣ Retrieve Public IP & Access App
bash
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 3600"`
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4
✔ Open http://your-public-ip:8501 in a browser! 🎉

9️⃣ Future Improvements
🔹 OAuth-based User Authentication 🔹 Real-time Travel Cost API Integration 🔹 Custom Domain Setup (mytravelapp.com) 🔹 Improved UX with Maps & Interactive Charts

📄 Conclusion
This domain-specific AI-powered travel planner successfully leverages CrewAI, GPT-4 Turbo, FAISS memory, Docker, and AWS to create an automated, intelligent travel assistant.

🎉 Your project is now globally accessible, scalable, and ready for further enhancements! 🚀🔥