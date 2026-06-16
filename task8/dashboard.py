import streamlit as st
import requests

API_KEY="YOUR_API_KEY_HERE"

URL = "https://careers.zelbytes.com/api/iot-lab/v1/telemetry/latest"

headers = {
    "X-Iot-Lab-Key": API_KEY
}

st.title("IoT Telemetry Dashboard")

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    latest = data["latest"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Temperature (°C)", latest["temperature_c"])
        st.metric("Humidity (%)", latest["humidity_pct"])

    with col2:
        st.metric("Soil Moisture (%)", latest["soil_moisture_pct"])
        st.metric("CO₂ (ppm)", latest["co2_ppm"])

else:
    st.error(f"API Error: {response.status_co
