import streamlit as st
import requests
import pandas as pd
import time

st.title("Real-Time AI Insights")
threshold = st.sidebar.slider("Anomaly Threshold", 0, 100, 50)

if st.button("Get Live Prediction"):

    url = "https://api-and-dashboard-final-capstone-project.onrender.com/predict?input_val=0.5"
    response = requests.get(url).json()


    raw_prediction = response['prediction']
    
    if isinstance(raw_prediction, list):
        prediction_value = raw_prediction[0]
    else:
        prediction_value = raw_prediction
    
    st.metric("Latest Prediction", f"{prediction_value:.2f}")
    
    if prediction_value > threshold:
        st.error("🚨 Anomaly Detected: Prediction exceeds threshold!")
