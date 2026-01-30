# Day44 – Regularization Techniques (Ridge, Lasso, Elastic Net)

In this notebook, I focused on the problem of **overfitting and underfitting** in machine learning models, and explored **regularization techniques** as solutions. The experiments were carried out on the **Car MPG dataset** using Linear Regression as a baseline and then applying Ridge, Lasso, and Elastic Net regression.

---

## Key Topics Covered
- **Overfitting vs Underfitting**
  - Understood the **bias–variance tradeoff**
  - Overfitting → low bias, high variance  
  - Underfitting → high bias, low variance  
  - Best fit → balance between bias & variance  

- **Dataset**
  - Used the **Car MPG dataset**
  - Features included: horsepower, weight, cylinders, etc.  
  - Target variable: **Miles Per Gallon (MPG)**

- **Baseline Model**
  - Implemented **Linear Regression**  
  - Achieved good results but showed signs of overfitting  

- **Ridge Regression (L2 Regularization)**
  - Shrinks coefficients but does not eliminate them  
  - Reduces model variance and improves generalization  

- **Lasso Regression (L1 Regularization)**
  - Shrinks some coefficients to zero  
  - Works as a **feature selection technique**  

- **Elastic Net Regression (L1 + L2)**
  - Combines Ridge and Lasso benefits  
  - Balances coefficient shrinkage and feature elimination  

- **Model Evaluation**
  - Compared models using:
    - **R² Score (train & test)**
    - **Mean Squared Error (MSE)**
  - Visualized coefficient differences between Linear, Ridge, and Lasso models  

---

## Results
- **Linear Regression** achieved a good baseline performance but was prone to overfitting.  
- **Ridge Regression** improved generalization by reducing large coefficients.  
- **Lasso Regression** eliminated irrelevant features, performing feature selection.  
- **Elastic Net** provided a balance of Ridge and Lasso, giving stable and interpretable results.  

---

## Key Takeaways
- **Regularization** is essential to handle overfitting and improve model stability.  
- **Ridge (L2):** reduces large coefficients but keeps all features.  
- **Lasso (L1):** eliminates unimportant features by shrinking coefficients to zero.  
- **Elastic Net:** combines both Ridge and Lasso advantages.  
- These techniques are widely used in real-world ML to improve generalization.  

