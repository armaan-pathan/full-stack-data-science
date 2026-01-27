# Day42 – Simple Linear Regression Deployment with Streamlit

This project demonstrates how to **deploy a trained Simple Linear Regression model** using **Streamlit**.  
The model was trained on the **Salary_Data dataset** (YearsExperience → Salary) in [Day41 – Simple Linear Regression](../Day41_Simple_Linear_Regression)


---

## Project Overview
- **Model:** Linear Regression (from scikit-learn)  
- **Input:** Years of Experience  
- **Output:** Predicted Salary  
- **Deployment Tool:** Streamlit  

---

## Files in this Folder
- `app.py` → Streamlit app script  
- `linear_regression_model.pkl` → pre-trained model (saved from Day41)  
- `slr_with_streamlit.pdf` → demo output of the app  
- `requirements.txt` → dependencies to run the app  

---

## How to Run
1. Clone the repo and navigate to this folder
   ```bash
   cd 42_SLR_Deployment_Streamlit

2. Install dependencies
   ```bash
    pip install -r requirements.txt

4. Run the app
   ```bash
    streamlit run app.py
