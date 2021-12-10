from transformers import pipeline


_star_mapping = {
        '1 star': 0.0,
        '2 stars': 0.25,
        '3 stars': 0.5,
        '4 stars': 0.75,
        '5 stars': 1.0
    }

def _translate_preds(d):
    return sum([_star_mapping[s['label']] * s['score'] for s in d])

_roberta_sentiment = pipeline("sentiment-analysis", 
                              model="siebert/sentiment-roberta-large-english")

_nlp_town_sentiment = pipeline("sentiment-analysis", 
                               model="nlptown/bert-base-multilingual-uncased-sentiment")

def roberta_sentiment(texts):
    scores = _roberta_sentiment(list(texts), return_all_scores=True)
    return [[i['score'] for i in s if i['label'] == 'POSITIVE'][0] for s in scores]


def nlptown_sentiment(texts):
    scores = _nlp_town_sentiment(list(texts), return_all_scores=True)
    return [_translate_preds(s) for s in scores]
