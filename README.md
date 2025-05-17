# Sentiment Analysis API

This is a simple Sentiment Analyzer API built using **FastAPI** and **scikit-learn**.
You send text, and it replies whether the sentiment is **positive** or **negative**.


## Features

- REST API built with FastAPI
- Trained ML model using scikit-learn
- `.env` for config settings
- 12-Factor App principles
- CI with GitHub Actions

## How to Run

### 1. Clone the repo

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2. Create & activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up .env
ENV=development
MODEL_PATH=models/sentiment.joblib

### 5. Train the model
python scripts/train_model.py

### 6. Start the API
uvicorn app.main:app --reload

Then open http://127.0.0.1:8000



## API Endpoints

GET - / - Welcome message /n
POST - /predict - Returns sentiment analysis of input text



Example request:

POST /predict
{
  "text": "I love this app!"
}


Example response:

{
  "text": "I love this app!",
  "sentiment": "positive"
}
