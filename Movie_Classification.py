import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import pickle


@st.cache_resource
def load_movie_model():
    return tf.keras.models.load_model('models/Movie_Classifier.keras')


@st.cache_resource
def load_tokenizer():
    with open(r'models/Movie_Tokenizer.pkl', 'rb') as file:
        return pickle.load(file)


def movie():
    st.title("Movie Classifier")
    input_summary = st.text_input("Enter Movie Summary")

    tokenizer = load_tokenizer()
    model = load_movie_model()

    def text_processing(text):
        sequences = tokenizer.texts_to_sequences([text])
        padded = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=500, padding='post')
        return np.array(padded)

    if st.button('Predict'):
        legend = pd.read_csv('models/Movie_Genre_Encoding.csv', header=None)
        model_input = text_processing(input_summary)
        result = model.predict(model_input)
        st.header(legend[0][np.argmax(result)])
