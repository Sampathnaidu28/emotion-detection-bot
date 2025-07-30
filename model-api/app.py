from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

# Allow CORS (React calls this from another port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once at startup
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

class UserText(BaseModel):
    text: str

@app.post("/predict")
async def predict_emotion(data: UserText):
    result = classifier(data.text)[0]
    top_emotion = max(result, key=lambda x: x['score'])
    return {"emotion": top_emotion['label']}
