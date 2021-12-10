import numpy as np
import onnxruntime as rt


def onnx_sentiment(texts, model_path):
    sess = rt.InferenceSession(model_path)
    input_name = sess.get_inputs()[0].name
    
    _, probas = sess.run(None, {input_name: np.array([texts])})
    return probas[:, 1]
