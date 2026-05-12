import streamlit as st
import pandas as pd
import joblib

model = joblib.load("mymodel.pkl")

st.title("Taxi Trip Duration Estimator")

passenger_count = st.number_input("Number of Passengers", min_value=1)
hour = st.number_input("Hour of the Day", min_value=0, max_value=23)
day_of_week = st.number_input("Day of the Week", min_value=0, max_value=6)
month = st.number_input("Month", min_value=1, max_value=12)
distance_km = st.number_input("Distance in KM", min_value=0.0)

if st.button("Predict"):
    features = pd.DataFrame({
        "passenger_count": [passenger_count],
        "hour": [hour],
        "day_of_week": [day_of_week],
        "month": [month],
        "distance_km": [distance_km]})
    
    predicition = model.predict(features)
    st.success(f"Estimated Trip Duration: {round(predicition[0], 2)} minutes")
        

