# Day50 – Logistic Regression Deployment with Streamlit

## Overview
This project demonstrates how to deploy a trained **Logistic Regression model** using **Streamlit**.  
The app allows users to input their **Age** and **Estimated Salary** and predicts whether they will purchase a product.

## Features
- User-friendly **Streamlit web app**.  
- Sidebar inputs for:
  - Age
  - Estimated Salary
- Prediction results:
  - Will Purchase
  - Will Not Purchase


## How to Run
1. Clone this repository and navigate to the project folder.
2. Install requirements:
   ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
4. Enter inputs in the sidebar and click Predict.

## Files

`app.py` → Streamlit frontend code.

`logistic_regression_model.pkl` → Trained Logistic Regression model.

`logistic_regression_scaler.pkl` → StandardScaler fitted on training data.

`requirements.txt` → Dependencies to run the project.

## Summary & Key Takeaways

- Logistic Regression model deployed using Streamlit.
- End-users can interact with the model via a simple web interface.
- Demonstrates how ML models move from Jupyter experiments → real-world applications.
