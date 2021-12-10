import numpy as np
import onnxruntime as rt


def onnx_sentiment(texts, model_path, label_name=1):
    sess = rt.InferenceSession(model_path)
    input_name = sess.get_inputs()[0].name
    
    predictions = [sess.run(None, {input_name: np.array([[t]])})[1][0] for t in texts]
    
    # We'll assume that the label for positive = label_name, this is a convention
    return [p[label_name] for p in predictions]
