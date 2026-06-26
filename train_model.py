import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

data = pd.read_csv("emotion_dataset.csv")

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

model.fit(data["text"], data["emotion"])

joblib.dump(model, "emotion_model.pkl")

print("Model trained successfully!")