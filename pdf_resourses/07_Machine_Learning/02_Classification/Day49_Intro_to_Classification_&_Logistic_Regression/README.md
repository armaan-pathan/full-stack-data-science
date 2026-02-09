# Day49 – Introduction to Classification & Logistic Regression

## Overview
This notebook introduces **Classification in Machine Learning** and explains the foundation of **Logistic Regression**.  
It covers the theory of classification, differences from regression, logistic regression working, and key evaluation metrics.

## Topics Covered
- What is **Classification** and where it is used.
- **Regression vs Classification** – key differences.
- Logistic Regression explained in detail:
  - Sigmoid function
  - Why Logistic Regression is actually a classification algorithm
  - Steps to build a classification model
- **Confusion Matrix** explained with a COVID-19 doctor–patient example.
- Performance metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
- **Bias–Variance Tradeoff** – checking training vs testing accuracy.

## Practical Implementation
- Built a Logistic Regression model on a dataset.  
- Tried different scenarios:
  - Without scaling (random_state=0, test_size=0.25)
  - With StandardScaler (random_state=0, test_size=0.20 → best accuracy = 0.92)
  - With Normalizer (random_state=0, test_size=0.25)
  - With StandardScaler and different random states (51, 100).
- Compared performance across experiments.

## Results
| Experiment | Scaling Method   | Random State | Test Size | Accuracy |
|------------|-----------------|--------------|-----------|----------|
| 1          | None            | 0            | 0.25      | 0.89     |
| 2          | StandardScaler  | 0            | 0.20      | **0.92** |
| 3          | Normalizer      | 0            | 0.25      | 0.68     |
| 4          | StandardScaler  | 51           | 0.25      | 0.85     |
| 5          | StandardScaler  | 100          | 0.25      | 0.87     |

The **best accuracy was 0.92** with StandardScaler and test_size=0.20.

## Summary & Key Takeaways
- Classification predicts **categories** (e.g., Yes/No), unlike regression which predicts continuous values.  
- Logistic Regression is a **classification algorithm** despite its name.  
- Confusion Matrix & metrics help evaluate beyond accuracy.  
- Preprocessing (scaling/normalizing) significantly affects results.  
- Logistic Regression generalized well without major overfitting/underfitting.