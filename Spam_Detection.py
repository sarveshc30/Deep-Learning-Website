import streamlit as st
import tensorflow as tf
import json
import numpy as np


def spam():
    #Website Code
    st.title("Spam Classifier")
    input_sms = st.text_input("Enter Message")


    #Preprocessing Text
    #Load JSON from the directory
    with open(r'models\spam_tokenizer.json', "r") as infile:
        loaded_tokenizer_json = json.load(infile)

    # Reconstruct tokenizer
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(loaded_tokenizer_json)


    def text_processing(text):
        sequences = tokenizer.texts_to_sequences(text)
        padded = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=220, padding='post')
        return np.array(padded)


    #Prediction
    model_input = text_processing([input_sms])
    model = tf.keras.models.load_model('models/Spam_model.keras', compile=False)


    #Button Function

    if st.button('Predict'):
        results = model.predict(model_input)[0][0]

        print(results)

        if results < 0.5:
            st.header('Not Spam')
        else:
            st.header('Spam')
