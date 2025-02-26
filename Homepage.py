import streamlit as st
import Spam_Detection
import Movie_Classification
import Customer_Churn
st.set_page_config(layout="wide")
st.html("<h1 style='text-align: center;'><font size='40'>Home Page</font></h1>")
st.html("<h1 style='text-align: center;'><font size='20'> </font></h1>")

if "session" not in st.session_state:
    st.session_state.session = 0

col1, col2, col3 = st.columns([2, 2, 2], gap="large")

with col1:
    st.info("""
    #### Spam Classification \n
    With the increasing reliance on digital communication, spam messages have become a major nuisance, often leading to
    fraud, phishing, and privacy breaches. This project aims to develop an intelligent system that can accurately
    classify SMS messages as spam or legitimate, significantly enhancing cybersecurity and protecting users from
    potential threats and online risks.
    """)
    if st.button('Go to Spam Detector'):
        st.session_state.session = 1

with col2:
    st.success("""
    #### Movie Genre Classification \n
    The entertainment industry generates vast amounts of content, making it essential to categorize movies efficiently.
    This project involves leveraging machine learning techniques to classify movies into appropriate genres based on
    attributes like descriptions, reviews, and metadata. Such a system enhances recommendation engines, making content
    discovery more seamless for users.
    """)
    if st.button('Go to Movie Classifier'):
        st.session_state.session = 2

with col3:
    st.error("""
    #### Customer Churn \n
    Businesses thrive on customer retention, and predicting churn is essential for maintaining long-term relationships.
    This project focuses on building predictive models that analyze customer behavior and identify patterns indicating
    potential churn. By enabling businesses to take proactive measures, such as personalized engagement strategies,
    this system helps improve customer satisfaction and loyalty.
    """)
    if st.button('Go to Churn Model'):
        st.session_state.session = 3

# Add some space at the bottom
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

if st.session_state.session == 1:
    Spam_Detection.spam()
elif st.session_state.session == 2:
    Movie_Classification.movie()
elif st.session_state.session == 3:
    Customer_Churn.churn()
