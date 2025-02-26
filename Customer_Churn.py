import streamlit as st
import tensorflow as tf
import numpy as np
import pickle



@st.cache_resource
def load_model():
    return tf.keras.models.load_model(r'models/Churn.keras')


@st.cache_resource
def load_scaler():
    with open(r'models/churn_scaler.pkl', 'rb') as file:
        return pickle.load(file)


def get_value(name, mini, maxi):
    return st.number_input(f"Enter {name} between {mini} & {maxi}", min_value=mini, max_value=maxi, step=1, value=None, placeholder="")


def churn():
    st.title("Customer Churn Prediction")
    input_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    input_data[0] = get_value('Credit Score', 350, 850)
    input_data[1] = get_value("Age", 18, 92)
    input_data[2] = get_value('Tenure', 2, 10)
    input_data[3] = get_value('Balance', 0, 250000)
    input_data[4] = get_value('No of Products', 0, 4)

    credit_card = st.selectbox('Does Customer have credit card?', ('Yes', 'No'))
    if credit_card == 'Yes':
        input_data[5] = 1
    else:
        input_data[5] = 0

    credit_card = st.selectbox('Is Customer an active member?', ('Yes', 'No'))
    if credit_card == 'Yes':
        input_data[6] = 1
    else:
        input_data[6] = 0

    input_data[7] = get_value('Salary', 12, 199990)

    country = st.selectbox('Select Country', ('Germany', 'Spain', 'France'))
    input_data[8] = (country == 'Germany')
    input_data[9] = (country == 'Spain')

    gender = st.selectbox('Select Gender', ('Male', 'Female'))
    input_data[10] = (gender == 'Male')

    scaler = load_scaler()
    model = load_model()
    input_array = np.array(input_data).reshape(1, -1)
    scaled_input = scaler.transform(input_array)

    if st.button('Predict'):
        results = model.predict(scaled_input)[0][0]
        if results < 0.5:
            st.header('It is likely the customer will leave')
        else:
            st.header('It is likely the customer will stay')
