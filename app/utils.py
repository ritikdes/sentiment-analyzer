import numpy as np
import joblib
import os

def load_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")
    model_data = joblib.load(model_path)
    return model_data["model"], model_data["vectorizer"]

def predict_sentiment(text, model, vectorizer):
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return "positive" if prediction == 1 else "negative"