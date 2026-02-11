# Import Libraries
import streamlit as st
import numpy as np
import pickle

# Load the saved model and scaler
model = pickle.load(open(r'C:\Arman\FSDS GenAI 2025\Practicals\07_Machine_Learning\02_Classification\Day50_LR_Deployment_with_Streamlit\logistic_regression_model.pkl', 'rb'))
scaler = pickle.load(open(r'C:\Arman\FSDS GenAI 2025\Practicals\07_Machine_Learning\02_Classification\Day50_LR_Deployment_with_Streamlit\logistic_regression_scaler.pkl', 'rb'))

# App Title
st.set_page_config(page_title="Logistic Regression App", page_icon="", layout="centered")
st.title("Logistic Regression Prediction App")
st.markdown(
    """
    This app uses a **Logistic Regression model** trained on customer data  
    to predict whether a person will **purchase a product** based on their **Age** and **Estimated Salary**.
    """
)

# Sidebar for Inputs
st.sidebar.header("Enter Input Features")
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=25, step=1)
salary = st.sidebar.number_input("Estimated Salary", min_value=10000, max_value=150000, value=60000, step=1000)

# Predict Button
if st.sidebar.button("Predict"):
    user_input = np.array([[age, salary]])
    scaled_input = scaler.transform(user_input)
    prediction = model.predict(scaled_input)

    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.success("The model predicts: **Will Purchase**")
    else:
        st.error("The model predicts: **Will Not Purchase**")

