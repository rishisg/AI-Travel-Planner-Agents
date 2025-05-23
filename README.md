# 🛫 AI-Powered Travel Planner  

## 🌍 **Overview**  
The **AI-Powered Travel Planner** is an intelligent, automated travel assistant that helps users **plan personalized trips** based on their budget, interests, and duration. Built using **CrewAI, OpenAI GPT-4 Turbo, Streamlit, and AWS**, this AI-driven tool generates **customized itineraries** and suggests destinations based on user preferences.  

🚀 **Live Demo:** [http://your-public-ip:8501](http://your-public-ip:8501)  
💻 **Deployed on:** AWS EC2  

---

## 🚀 **Problem Statement**  
Planning a trip can be **stressful and time-consuming**, requiring extensive research on:  
✔ Best destinations for a given budget  
✔ Activities based on personal interests  
✔ Hotels, transportation, and itinerary suggestions  

❌ Traditional methods involve **manual searches**, lack personalization, and can be overwhelming.  

---

## ✅ **Solution**  
The **AI-Powered Travel Planner** automates this process using **GPT-4 Turbo & CrewAI agents**, generating **tailored travel plans instantly!**  

🔹 **User enters trip details** (budget, duration, preferred activities)  
🔹 AI **suggests optimal destinations** based on preferences  
🔹 AI **creates a personalized itinerary**  
🔹 The system **remembers past trips** for smarter recommendations  

🔹 **Live Demo:** [http://your-public-ip:8501](http://your-public-ip:8501)  

---

## 🛠 **Technology Stack**  
| Technology | Purpose |
|------------|---------|
| **Python 3.11** | Core development language |
| **OpenAI GPT-4 Turbo** | AI-powered responses & recommendations |
| **CrewAI** | Multi-agent collaboration framework |
| **Streamlit** | Frontend UI for user interaction |
| **Docker** | Containerization for deployment |
| **AWS EC2** | Cloud hosting |
| **FAISS** | Memory storage for past trips |
| **SQLite** | Structured trip database |
| **WinSCP & Putty** | File transfer & SSH login |
| **Route 53** _(Optional)_ | Domain name management |

---

## 🔄 **Workflow Diagram**
```mermaid
graph TD
    A(User Input: Destination, Budget, Days, Activities) --> B[AI Agents Process Input]
    B --> C[Destination AI Agent Suggests Places]
    B --> D[Budget AI Agent Estimates Costs]
    B --> E[Itinerary AI Agent Plans Schedule]
    C --> F[Final AI-Generated Travel Plan]
    D --> F
    E --> F
    F --> G(User Receives Personalized Itinerary)

🚀 Deployment Steps on AWS EC2
1️⃣ Launch AWS EC2 Instance
✔ Select Ubuntu 22.04 ✔ Choose t2.micro (Free-tier eligible) ✔ Configure security groups (port 8501 for public access)

2️⃣ Connect to EC2 & Install Docker

ssh -i your-key.pem ubuntu@your-public-ip
sudo apt update && sudo apt install docker.io -y
sudo systemctl enable docker && sudo systemctl start docker
sudo usermod -aG docker ubuntu && newgrp docker

3️⃣ Transfer Project Files via WinSCP/SCP
scp -i your-key.pem -r /local-folder-path ubuntu@your-public-ip:/home/ubuntu/travel-planner

4️⃣ Build & Run Docker Container
cd /home/ubuntu/travel-planner
docker build -t travel-planner-ai .
docker run -d --restart unless-stopped --env-file .env -p 8501:8501 travel-planner-ai

5️⃣ Retrieve Public IP & Access App
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 3600"`
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4

✔ Open http://your-public-ip:8501 in your browser! 🎉

📌 Future Improvements
✔ Add OAuth-based user authentication ✔ Improve UX with interactive UI elements ✔ Integrate real-time travel costs & hotel APIs ✔ Set up custom domain (e.g., mytravelapp.com)