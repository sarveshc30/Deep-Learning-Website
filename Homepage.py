import streamlit as st
import Spam_Detection
import Movie_Classification
import Customer_Churn

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; font-size: 40px;'>Home Page</h1>", unsafe_allow_html=True)

# Initialize session state keys if not already set
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

def validate_user(email, password):
    # Dummy validation: replace with your actual validation logic.
    if email == "admin@example.com" and password == "admin123":
        return True
    return False

# Login Page
if st.session_state.page == "login":
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if validate_user(email, password):
            st.session_state.logged_in = True
            st.session_state.page = "home"
            st.success("Logged in successfully!")
        else:
            st.error("Invalid email or password.")
    if st.button("Sign Up"):
        st.info("Sign up functionality is not implemented yet.")

# Home Page with project options
if st.session_state.page == "home":
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.info("""
        #### Spam Classification \n
        With the increasing reliance on digital communication, spam messages have become a major nuisance, often leading to
        fraud, phishing, and privacy breaches. This project aims to develop an intelligent system that can accurately
        classify SMS messages as spam or legitimate, significantly enhancing cybersecurity and protecting users from
        potential threats and online risks.
        """)
        if st.button('Go to Spam Detector'):
            st.session_state.page = "spam"

    with col2:
        st.success("""
        #### Movie Genre Classification \n
        The entertainment industry generates vast amounts of content, making it essential to categorize movies efficiently.
        This project involves leveraging machine learning techniques to classify movies into appropriate genres based on
        attributes like descriptions, reviews, and metadata. Such a system enhances recommendation engines, making content
        discovery more seamless for users.
        """)
        if st.button('Go to Movie Classifier'):
            st.session_state.page = "movie"
    with col3:
        st.error("""
        #### Customer Churn \n
        Businesses thrive on customer retention, and predicting churn is essential for maintaining long-term relationships.
        This project focuses on building predictive models that analyze customer behavior and identify patterns indicating
        potential churn. By enabling businesses to take proactive measures, such as personalized engagement strategies,
        this system helps improve customer satisfaction and loyalty.
        """)
        if st.button('Go to Churn Model'):
            st.session_state.page = "churn"

# Spam Detection Page
if st.session_state.page == "spam":
    if Spam_Detection.spam():
        st.session_state.page = "home"

# Movie Classification Page
elif st.session_state.page == "movie":
    if Movie_Classification.movie():
        st.session_state.page = "home"

# Customer Churn Page
elif st.session_state.page == "churn":
    if Customer_Churn.churn():
        st.session_state.page = "home"
