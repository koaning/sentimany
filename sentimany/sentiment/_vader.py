from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def vader_sentiment(texts):
    return [analyzer.polarity_scores(s)['compound']/2 + 0.5 for s in texts]
