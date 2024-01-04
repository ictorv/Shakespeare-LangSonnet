import tensorflow
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import json
import numpy as np
import pickle

# with open('./handle/token_dict.json', 'r') as json_file:
#     dictkn = json.load(json_file)

with open('./models/tokenizer.pickle', 'rb') as handletkn:
    tokenizer = pickle.load(handletkn)

model=load_model('./models/model_sp.h5')
print(len(tokenizer.word_index))
def inp(faqs):
    text=faqs
    for i in range (100):
        token_text=tokenizer.texts_to_sequences([text])[0]
        
        pad_token_text=pad_sequences([token_text],maxlen=10,padding='pre')
        prd=np.argmax(model.predict(pad_token_text))
        
        # print(prd)
        for word,pos in tokenizer.word_index.items():
            if pos==prd:
                text=text+ " " + word
                # print(text)
    return text

# val=inp("Hello from other side")
# print(val)
