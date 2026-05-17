import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏡 House Price Prediction App")

st.write("Enter house details to predict the price")

st.write("Model Used: Random Forest Regressor")
st.write("R² Score: 0.84")

# Inputs
st.sidebar.header("Enter House Features")
st.sidebar.markdown("---")

st.sidebar.header("About Project")
st.sidebar.write("Machine Learning based House Price Prediction System using Random Forest Regression.")


overall_qual = st.slider("Overall Quality (1-10)", 1, 10, 5)
area = st.number_input("Living Area (sq ft)", value=1000)
garage = st.number_input("Garage Capacity (cars)", value=1)
basement = st.number_input("Basement Area (sq ft)", value=500)
year = st.number_input("Year Built", value=2000)

# Prediction
if st.button("Predict Price"):
    features = np.array([[overall_qual, area, garage, basement, year]])
    
    prediction = model.predict(features)

    final_price = np.exp(prediction[0])

    st.success(f"Estimated House Price: ${final_price:,.2f}")

st.write("""
This app predicts house prices based on:
- Overall Quality
- Living Area
- Garage Capacity
- Basement Area
- Year Built
""")