import streamlit as st
import requests
import pandas as pd
import time

st.title("Real-Time AI Insights")
threshold = st.sidebar.slider("Anomaly Threshold", 0, 100, 50)

if st.button("Get Live Prediction"):
response = requests.get("https://api-and-dashboard-final-capstone-project.onrender.com/predict?input_val=0.5").json()    
    
    st.metric("Latest Prediction", f"{response['prediction']:.2f}")
    
    if response['prediction'] > threshold:
        st.error("🚨 Anomaly Detected: Prediction exceeds threshold!")
