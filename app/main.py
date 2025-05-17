from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from app.utils import load_model, predict_sentiment


load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")
ENV = os.getenv("ENV", "development")

app = FastAPI()

model, vectorizer = load_model(MODEL_PATH)

class TextInput(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API!",
            "env": ENV
            }

@app.post("/predict")
def predict(input: TextInput):
    sentiment = predict_sentiment(input.text, model, vectorizer)
    return {"text": input.text, "sentiment": sentiment}