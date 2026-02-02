# Day46 – Polynomial Regression

## Overview
On Day46, I learned about **Polynomial Regression**, an extension of Linear Regression where the relationship between the independent variable and target is modeled as an nth-degree polynomial.  
This helps to capture **non-linear patterns** in data.

Dataset used: `emp_sal.csv`  
- **Feature (X):** Level of the employee  
- **Target (y):** Salary  

---

## Key Learnings
- Concept of **Polynomial Regression** and how it differs from Linear Regression.  
- Importance of **choosing the right degree** to avoid underfitting or overfitting.  
- Training and comparing models with polynomial degrees from 2 to 6.  
- Observing how higher degrees fit the training data better but may risk overfitting.  

---

## Implementation Steps
1. **Load dataset** and understand features.  
2. **Train Linear Regression** (baseline).  
3. **Apply PolynomialFeatures (degree 2–6)** and train models.  
4. **Compare curves and predictions** across different degrees.  
5. **Interpret results** — polynomial regression can fit complex curves but must balance bias–variance.  

---

## Summary
- Polynomial regression can model **non-linear relationships**.  
- Higher-degree polynomials provide more flexibility but risk **overfitting**.  
- Final model (degree 5) was trained and saved for later deployment.  

---
