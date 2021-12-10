from transformers import AutoTokenizer, AutoModelForSequenceClassification


import numpy as np
import onnxruntime as rt


def onnx_sentiment(texts, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    return


