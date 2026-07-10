from textblob import TextBlob
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Sentiment Prediction API"
)

# ---------- Sentiment Function ----------

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "text": text,
        "polarity": round(polarity, 4),
        "sentiment": sentiment
    }

# ---------- Models ----------

class TweetInput(BaseModel):
    text: str
    author: Optional[str] = "Anonymous"

class SentimentResult(BaseModel):
    text: str
    author: str
    sentiment: str
    polarity: float

# ---------- Endpoint ----------

@app.post("/analyze_tweets/")
def analyze_tweets(tweets: List[TweetInput]):

    results = []

    for tweet in tweets:

        result = analyze_sentiment(tweet.text)

        results.append({
            "text": result["text"],
            "author": tweet.author,
            "sentiment": result["sentiment"],
            "polarity": result["polarity"]
        })

    return {
        "total_tweets": len(results),
        "results": results
    }