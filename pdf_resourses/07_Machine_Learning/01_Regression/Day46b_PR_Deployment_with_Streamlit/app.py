import streamlit as st
import numpy as np
import pickle

# Load saved polynomial model
with open("polynomial_model.pkl", "rb") as f:
    saved_objects = pickle.load(f)

poly = saved_objects["poly"]
model = saved_objects["model"]

# App title and description
st.title("Polynomial Regression – Employee Salary Prediction")
st.write("""
This simple app predicts **Employee Salary** based on the **Employee Level** using a Polynomial Regression.""")

# User input
level_value = st.number_input("Enter Employee Level:", min_value=1, max_value=10, value=3)

# Predict button
if st.button("Predict Salary"):
    # Transform input
    level_transformed = poly.transform(np.array([[level_value]]))
    prediction = model.predict(level_transformed)
    
    # Show result
    st.success(f"Predicted Salary for Level {level_value}: **₹{prediction[0]:,.2f}**")
