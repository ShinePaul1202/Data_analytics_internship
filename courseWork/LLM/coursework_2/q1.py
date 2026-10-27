
import pandas as pd
from transformers import pipeline

# Load the dataset
df=pd.read_csv("reviews.csv")

# Check required columns
if not {"Product", "Review"}.issubset(df.columns):
    raise ValueError("CSV must contain Product and Review columns.")

# Load the pretrained sentiment analysis pipeline
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Handle missing reviews
df["Review"]=df["Review"].fillna("").astype(str)

# Predict sentiment for each review
results = sentiment_analyzer(
    df["Review"].tolist(),
    batch_size=16,
    truncation=True
)

# Add predictions and confidence scores
df["Sentiment"]=[
    result["label"] for result in results
]
df["Confidence"] = [
    round(result["score"], 4) for result in results
]

# Display the results
print(df[["Product", "Review", "Sentiment", "Confidence"]])

# Save the results
df.to_csv("reviews_with_sentiment.csv", index=False)

print("\nSentiment analysis completed successfully.")
print("Results saved to reviews_with_sentiment.csv")
