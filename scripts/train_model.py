from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Sample training data
texts = ["I love it",
        "This is amazing",
         "I hate this",
         "So bad",
         "I enjoy it",
         "Worst ever",
         "Not good",
         "Fantastic",
         "Terrible",
         "I like it",
         "I'm frustrated and unhappy",
         "Completely disappointed",
         "This is the worst thing ever",
         "I'm so happy and satisfied"]
labels = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1]  # 1 = positive, 0 = negative

# Vectorize the data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train the model
model = LogisticRegression()
model.fit(X, labels)

# Save both model and vectorizer
os.makedirs("models", exist_ok=True)
joblib.dump({
    "model": model,
    "vectorizer": vectorizer
}, "models/sentiment.joblib")

print("Model and vectorizer saved to models/sentiment.joblib")
