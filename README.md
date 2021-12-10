# sentimany

Just a simple sentiment tool. It just grabs a set of pre-made sentiment models that you can quickly use to attach sentiment scores to text. None of these sentiment models will be perfect, as none of them actually understand language, but they may serve well in human-in-the-loop kinds of labelling situations. Currently the tool only supports English models.

## Quickstart 

The goal is to whip up some sentiment models real quick. A demo is shown below.

```python
import pandas as pd
from sentimany.sentiment import (
    vader_sentiment,
    textblob_sentiment,
    onnx_sentiment,
    roberta_sentiment,
    nlptown_sentiment,
)

# Add some text to a pandas dataframe
texts = [
    "i like dogs",
    "i hate cats",
    "stroopwafels are amazing",
    "mcdondals is horrible",
]
df = pd.DataFrame({"text": texts})

# Apply each sentiment model and attach it as a new column
(df
  .assign(vader = lambda d: vader_sentiment(d['text']), 
          textblob = lambda d: textblob_sentiment(d['text']),
          imdb_onnx = lambda d: onnx_sentiment(d['text'], "onnx/imdb-reviews.onnx"),
          amazon_onnx = lambda d: onnx_sentiment(d['text'], "onnx/amazon-reviews.onnx"),
          roberta = lambda d: roberta_sentiment(d['text']), 
          nlptown = lambda d: nlptown_sentiment(d['text'])))
```

This would result in a table that looks something like; 

| text                     |   vader |   textblob |   imdb_onnx |   amazon_onnx |   roberta |   nlptown |
|:-------------------------|--------:|-----------:|------------:|--------------:|----------:|----------:|
| i like dogs              |  0.6806 |        0.5 |      0.5667 |        0.577  |    0.9979 |    0.7335 |
| i hate cats              |  0.214  |        0.1 |      0.6835 |        0.3837 |    0.0016 |    0.3544 |
| stroopwafels are amazing |  0.793  |        0.8 |      0.7374 |        0.8058 |    0.9985 |    0.9323 |
| mcdondals is horrible    |  0.2288 |        0   |      0.1983 |        0.1522 |    0.0006 |    0.0605 |

## Good to know 

This is a repo made for utility for myself. Feel free to re-use, but don't expect maintenance in the long term. 

More-over though, keep in mind that sentiment models are imperfect and brittle. In particular check [this short blogpost](https://koaning.io/til/2021-09-27-sentiment/) and [this huggingface stream](https://www.youtube.com/watch?v=0K5ybetv-dA&ab_channel=HuggingFace) for more details.
