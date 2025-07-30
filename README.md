EMOTION DETECTION BOT
A full-stack web app that detects emotions from text input and responds with supportive or motivational messages based on the detected emotion.
Features :
 Detects emotions like joy, sadness, anger, fear, etc.
 Provides instant motivational or empathetic responses
 Machine learning model built with Scikit-learn using the GoEmotions dataset
 Frontend built with React
 Backend built with Express (Node.js)
 Dark mode UI
How to Run Locally :
 1. Clone the repo
 git clone https://github.com/Sampathnaidu28/emotion-detection-bot.git
 cd emotion-detection-bot
 2. Install and run the backend
 cd server
 npm install
 npm start
 3. Install and run the frontend
 cd ../client
 npm install
 npm start
App will run at:
 http://localhost:3000

 
PROJECT STRUCTURE
motion-detection-bot/
├── client/ → React frontend
│ ├── src/
│ └── ...
├── server/ → Express backend
│ ├── model/
│ ├── routes/
│ └── ...
├── model.pkl → Trained emotion detection model
├── README.md
└── ...

DATASET
Uses the GoEmotions dataset by Google

Trained using Scikit-learn pipelines and saved as model.pkl

How it Works :
 User enters a message
 The message is sent to the backend via API
 The backend uses the trained model to predict the emotion
 Based on the emotion, the app displays a relevant supportive or motivational message

AUTHOR:
Sampath Naidu
GitHub: https://github.com/Sampathnaidu28
