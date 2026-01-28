# Day43 – Multiple Linear Regression

This folder contains my work on **Multiple Linear Regression (MLR)**.  
It extends the concept of Simple Linear Regression (Day41) by using **multiple independent variables** to predict a dependent variable.  
The notebook includes both **theory** and **practical implementation** so that beginners can easily follow along.

---

## What is Multiple Linear Regression?

Multiple Linear Regression (MLR) models the relationship between **two or more independent variables (X₁, X₂, …, Xₙ)** and a **dependent variable (y)**.  

Equation:
\[
y = b_0 + b_1x_1 + b_2x_2 + ... + b_nx_n
\]

- **b0 (intercept):** base value when all X = 0  
- **b1, b2, … (coefficients):** how much y changes when that variable increases by 1 unit (while keeping others constant)  

---

## Dataset Information

The dataset contains information about a company’s **spending and research activities** with the goal of predicting **Profit**.  

### Features:
- **Digital Marketing** → Money spent on online marketing  
- **Promotions** → Expenses related to promotions/advertisements  
- **Research** → Spending on R&D activities  

### Target:
- **Profit** → The company’s profit (dependent variable)

---

## Workflow in this Notebook

1. **Introduction**  
   - Recap of regression concepts  
   - Difference between simple and multiple regression  

2. **Data Preprocessing**  
   - Used `pd.get_dummies()` (if needed for categorical data)  
   - Reshaped arrays into proper format (X, y)  

3. **Applying Multiple Linear Regression**  
   - Trained Linear Regression model using scikit-learn  
   - Compared predicted vs actual values  

4. **Model Parameters**  
   - Intercept (b₀) and coefficients (b₁, b₂, …)  
   - Constructed regression equation  

5. **Model Performance**  
   - R² score (train & test sets)  
   - Mean Squared Error (MSE)  

6. **Ordinary Least Squares (OLS)**  
   - Used `statsmodels.api` to obtain detailed statistics (p-values, confidence intervals, F-statistic, etc.)  

7. **Backward Elimination**  
   - Performed feature selection using p-values  
   - Iteratively removed insignificant variables to refine the model  

8. **API & statsmodels.api**  
   - Learned about APIs in ML  
   - Used `statsmodels.api` for statistical analysis  

---

## Key Results

- Found strong relationships between independent variables and Profit  
- Model explained a significant portion of the variance (high R² value)  
- OLS summary provided detailed statistical insights  
- Backward Elimination helped identify the most important predictors  

---

## Key Takeaways

- MLR allows using multiple predictors for more accurate predictions  
- Preprocessing (encoding, reshaping) is essential before training  
- Scikit-learn gives a quick model fit, while `statsmodels.api` provides detailed statistical analysis  
- Backward Elimination is a powerful technique for feature selection  
- Understanding coefficients makes the model more interpretable  

---

## Files in this Folder

- `Day43_Multiple_Linear_Regression.ipynb` → Jupyter notebook with theory, code, and results  
- `multiple_linear_regression_model.pkl` → saved trained model (for deployment)  
- `Investment.csv` → dataset used for this project  
