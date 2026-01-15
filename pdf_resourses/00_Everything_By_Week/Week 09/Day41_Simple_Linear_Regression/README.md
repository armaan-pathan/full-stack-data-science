# Day41 – Simple Linear Regression

This folder contains my first implementation of **Simple Linear Regression (SLR)** using the **Salary_Data** dataset.  

---

## What is Simple Linear Regression?

Simple Linear Regression is used to model the relationship between a **single independent variable (X)** and a **dependent variable (y)**.  

The equation is:  
\[
y = mx + c
\]

- **c (Intercept):** Value of y when x = 0  
- **m (Slope):** Amount y changes for each unit increase in x  

In this case:
- **X:** Years of Experience  
- **y:** Salary  

---

## Files in this Folder

- `Day41_Simple_Linear_Regression.ipynb` → Jupyter notebook with explanation, theory, and code  
- `Salary_Data.csv` → dataset used (YearsExperience vs Salary)  
- `linear_regression_model.pkl` → saved model file for reuse  

---

## Workflow

1. **Theory Recap**
   - Introduction to regression and its equation
   - Why regression is important in ML

2. **Data Loading & Splitting**
   - Loaded `Salary_Data.csv`
   - Split dataset into training (80%) and test (20%)

3. **Training the Model**
   - Fitted `LinearRegression` from scikit-learn
   - Obtained slope (b1) and intercept (b0)

4. **Visualization**
   - Plotted regression line on training and test sets
   - Interpreted slope & intercept

5. **Predictions**
   - Predicted salaries for test data
   - Also made predictions for custom values (e.g., 15 and 20 years of experience)

6. **Statistical Analysis**
   - Used `describe()` → summary statistics  
   - `corr()` → correlation between Experience and Salary  
   - `skew()` → symmetry of data  
   - `sem()` → Standard Error of Mean  
   - `variation()` → Coefficient of Variation  
   - `zscore()` → detected potential outliers  

7. **Model Performance**
   - R² score on train and test sets (explains variance)  
   - Mean Squared Error (MSE) for train and test sets  

8. **Saving the Model**
   - Exported trained model using `pickle`  

---

## Key Results

- **Strong positive correlation** between experience and salary  
- **R² close to 1** → model explains most of the variance  
- **Low MSE** → predictions are very accurate  
- Regression line fits the data almost perfectly  

---

## Key Takeaways

- Regression models relationships and makes predictions for continuous values  
- SLR is the **foundation** for more advanced regression techniques  
- Always check data distribution, correlation, and skewness before modeling  
- Evaluation metrics like **R²** and **MSE** show both fit and prediction quality  
- Models can be saved and reused for deployment  

---

## Next Steps
- Day42 → Deployment of this SLR model using **Streamlit**  
