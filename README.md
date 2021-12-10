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
  .assign(sent_vader = lambda d: vader_sentiment(d['text']), 
          sent_textblob = lambda d: textblob_sentiment(d['text']),
          sent_imdb_onnx = lambda d: onnx_sentiment(d['text'], "onnx/imdb-reviews.onnx"),
          sent_amazon_onnx = lambda d: onnx_sentiment(d['text'], "onnx/amazon-reviews.onnx"),
          sent_roberta = lambda d: roberta_sentiment(d['text']), 
          sent_nlptown = lambda d: nlptown_sentiment(d['text'])))
```

This would result in a table that looks something like; 

|    | text                     |   sent_vader |   sent_textblob |   sent_imdb_onnx |   sent_amazon_onnx |   sent_roberta |   sent_nlptown |
|---:|:-------------------------|-------------:|----------------:|-----------------:|-------------------:|---------------:|---------------:|
|  0 | i like dogs              |      0.6806  |             0.5 |         0.566716 |           0.576971 |    0.997911    |      0.733527  |
|  1 | i hate cats              |      0.21405 |             0.1 |         0.683531 |           0.383669 |    0.00162992  |      0.354395  |
|  2 | stroopwafels are amazing |      0.79295 |             0.8 |         0.737425 |           0.805838 |    0.998491    |      0.932349  |
|  3 | mcdondals is horrible    |      0.22885 |             0   |         0.198283 |           0.152206 |    0.000595081 |      0.0605446 |

## Good to know 

This is a repo made for utility for myself. Feel free to re-use, but don't expect maintenance in the long term. 

More-over though, keep in mind that sentiment models are imperfect and brittle. In particular check [this short blogpost](https://koaning.io/til/2021-09-27-sentiment/) and [this huggingface stream](https://www.youtube.com/watch?v=0K5ybetv-dA&ab_channel=HuggingFace) for more details.
