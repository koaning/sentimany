# sentimany

Just a simple sentiment tool. It just grabs a set of pre-made sentiment models that you can quickly use to attach sentiment scores to text. None of these sentiment models will be perfect, as none of them actually understand language, but they may serve well in human-in-the-loop kinds of labelling situations. Currently the tool only supports English models.

- [vader](https://github.com/cjhutto/vaderSentiment)
- [textblob](https://textblob.readthedocs.io/en/dev/quickstart.html)
- [depeche mood](https://textacy.readthedocs.io/en/0.11.0/api_reference/datasets_resources.html#textacy.resources.depeche_mood.DepecheMood)

```python
import pandas as pd
from sentimany.sentiment import vader_sentiment, textblob_sentiment

df = pd.DataFrame({"text": ["i like dogs", "i hate cats", 
                           "stroopwafels are amazing", "mcdondals is horrible"]})

(df
  .assign(sent_vader = lambda d: vader_sentiment(d['text']), 
          sent_textblob = lambda d: textblob_sentiment(d['text'])))
```
