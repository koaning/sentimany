# sentimany

Just a simple sentiment tool. It just grabs a set of pre-made sentiment models that you can quickly use to attach sentiment scores to text. None of these sentiment models will be perfect, as none of them actually understand language, but they may serve well in human-in-the-loop kinds of labelling situations. Currently the tool aims at English models, although some tools with also work on custom models.

```python
import pandas as pd
from sentimany.sentiment import (
    vader_sentiment,
    textblob_sentiment,
    onnx_sentiment,
    roberta_sentiment,
    nlptown_sentiment,
)

texts = [
    "i like dogs",
    "i hate cats",
    "stroopwafels are amazing",
    "mcdondals is horrible",
]
df = pd.DataFrame({"text": texts})

(df
  .assign(sent_vader = lambda d: vader_sentiment(d['text']), 
          sent_textblob = lambda d: textblob_sentiment(d['text']),
          sent_imdb_onnx = lambda d: onnx_sentiment(d['text'], "onnx/imdb-reviews.onnx"),
          sent_amazon_onnx = lambda d: onnx_sentiment(d['text'], "onnx/amazon-reviews.onnx"),
          sent_roberta = lambda d: roberta_sentiment(d['text']), 
          sent_nlptown = lambda d: nlptown_sentiment(d['text'])))
```
