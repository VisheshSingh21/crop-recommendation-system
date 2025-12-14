import streamlit as st
import numpy as np
import pickle


# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


st.set_page_config(page_title="Crop Recommendation", page_icon="🌾", layout="centered")


# Custom CSS
st.markdown("""
<style>
.main {
background-color: #f4f9f4;
}
.title {
color: #2e7d32;
text-align: center;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1 class='title'>🌱 Smart Crop Recommendation System</h1>", unsafe_allow_html=True)
st.write("Enter soil and climate parameters to get the best crop recommendation.")


# Input fields
N = st.number_input("Nitrogen (N)", 0, 150)
P = st.number_input("Phosphorus (P)", 0, 150)
K = st.number_input("Potassium (K)", 0, 150)
temperature = st.slider("Temperature (°C)", 0.0, 90.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0)
ph = st.slider("Soil pH", 0.0, 14.0)
rainfall = st.slider("Rainfall (mm)", 0.0, 300.0)


if st.button("🌾 Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.success(f"✅ Recommended Crop: {prediction[0]}")
