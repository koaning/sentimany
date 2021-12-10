from textblob import TextBlob

def textblob_sentiment(texts):
    return [TextBlob(t).polarity/2 + 0.5 for t in texts]
