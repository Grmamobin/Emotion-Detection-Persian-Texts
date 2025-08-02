from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from hazm import Normalizer

# Load everything
model = load_model("/Users/macbookpro/Desktop/EmotionDetection/accuracy-50%/emotion_model.h5")

with open("/Users/macbookpro/Desktop/EmotionDetection/accuracy-50%/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("/Users/macbookpro/Desktop/EmotionDetection/accuracy-50%/label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

normalizer = Normalizer()

def normalized_sentence(text):
    return normalizer.normalize(text)


def response_emotion(msg):
    # print(sentence)
    sentence = normalized_sentence(msg)
    sentence = tokenizer.texts_to_sequences([sentence])
    sentence = pad_sequences(sentence, maxlen=229, truncating='pre')
    result = le.inverse_transform(np.argmax(model.predict(sentence), axis=-1))[0]
    proba =  np.max(model.predict(sentence))
    return (f"{result}")
    
    