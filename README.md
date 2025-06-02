CyberGuard AI - Your Personal Security Assistant
Version License PRs Welcome
Welcome to CyberGuard AI! An intelligent chatbot that helps you with cybersecurity questions, threat detection, and security best practices.

🌟 Features
🔍 AI-Powered Security Analysis
🛡️ Real-time Threat Detection
💬 Interactive Chat Interface
🔒 Secure Authentication
📱 Responsive Design
🎥 Demo

CyberGuard AI in action - Real-time threat detection and security analysis

🚀 Quick Start
Prerequisites
Node.js (v16 or later)
Python (v3.8 or later)
npm or yarn
Git
Installation
Clone the repository

git clone https://github.com/Uma-29/SecuBot-Crew.git
cd CyberGuardAI
Set up the Backend

# Navigate to backend directory
cd backend-node

# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration
Set up the Frontend

# Navigate to frontend directory
cd ../frontend

# Install Node.js dependencies
npm install
# or
yarn install
Running the Application
Start the Backend Server

# From the backend-node directory
node src/server.js
The backend will run on http://localhost:5000

Start the Frontend Development Server

# From the frontend directory
npm run dev
# or
yarn dev
The frontend will be available at http://localhost:3000

Access the Application

Open your browser and go to http://localhost:3000
Sign up for a new account or log in if you already have one
Start chatting with CyberGuard AI!
📂 Project Structure
CyberGuardAI/
├── backend-node/         # Node.js backend server
│   ├── src/
│   │   ├── config/     # Configuration files
│   │   ├── controllers/  # Request handlers
│   │   ├── models/      # Database models
│   │   └── server.js    # Main server file
│   └── .env.example     # Example environment variables
│
├── frontend/            # React frontend
│   ├── public/          # Static files
│   └── src/
│       ├── components/  # React components
│       ├── context/     # React context providers
│       └── pages/       # Page components
│
└── docs/               # Documentation
🔧 Configuration
Backend Configuration

Copy .env.example to .env in the backend-node directory
Update the following variables:
PORT=5000
MONGODB_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
OPENROUTER_API_KEY=your_openrouter_api_key
Frontend Configuration

Update API endpoints in frontend/src/config.js if needed
