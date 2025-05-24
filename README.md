# 🚨 CyberGuard AI – Cybersecurity Awareness Chatbot

CyberGuard AI is an intelligent, AI-driven cybersecurity chatbot that enables users to detect, understand, and respond to digital threats in real time. It combines a conversational interface with powerful threat analysis capabilities using advanced AI models and real-time threat intelligence APIs.

---

## 🌐 Features

- 🔒 **Real-Time Threat Detection** – Detects phishing links, malware, and malicious files  
- 💬 **Conversational Chatbot** – Interacts through a secure, user-friendly chat interface  
- 🧠 **AI-Powered Analysis** – Uses Llama 3.1 (local or cloud-based) for intelligent security insights  
- 📦 **File and URL Scanning** – Analyzes uploads using VirusTotal and code-level parsing  
- 📩 **Incident Reporting** – Reports cyber incidents via email to designated authorities  
- 📊 **Threat Classification** – Categorizes threats as High, Medium, or Low with recommendations  
- 📱 **Responsive UI** – Mobile-friendly interface with dark/light theme support  

---

## 🛠️ Tech Stack

### Frontend:
- React.js  
- Tailwind CSS  
- Socket.IO (client)  
- React Markdown + Prism.js  

### Backend:
- Node.js + Express.js  
- Socket.IO (server)  
- RESTful APIs  
- Email (SMTP) integration  

### AI & Security:
- Meta Llama 3.1 via Hugging Face or OpenRouter  
- VirusTotal API  
- PhishTank API  
- Have I Been Pwned API (optional)  

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites
- Node.js (v16+)
- Python (v3.9+)
- NPM (v8+)
- Git
- API keys for OpenRouter, VirusTotal, Hugging Face, etc.

---

### 📁 Clone the Repository

```bash
git clone https://github.com/your-repo/CyberGuardAI.git
cd CyberGuardAI

 Frontend Setup
cd frontend
npm install
cp .env.example .env
npm run dev

 Backend Setup
cd ../backend-node
npm install
cp .env.example .env
npm start

Python Component Setup
cd ..
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

Environment Configuration
# OpenRouter Configuration
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL_NAME=nvidia/llama-3.1-nemotron-ultra-253b-v1:free

# Local Model Configuration
HUGGINGFACE_TOKEN=your_huggingface_token_here
LOCAL_MODEL_NAME=meta-llama/Meta-Llama-3.1-8B-Instruct

# VirusTotal Configuration
VIRUSTOTAL_API_KEY=your_virustotal_api_key_here

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password_here
FROM_EMAIL=your_email@gmail.com
SECURITY_EMAIL=your_security_email@example.com

# API Server
PORT=8000
HOST=0.0.0.0
