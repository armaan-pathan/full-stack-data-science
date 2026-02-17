# Day50 – Logistic Regression with Unseen Data

## Overview
This notebook extends Day49’s Logistic Regression by applying the model to **unseen (future) data**.  
The aim is to simulate real-world scenarios where a trained model must generalize to new inputs.

## Topics Covered
- Why predicting on unseen data is important.
- Workflow for handling unseen data:
  1. Train the Logistic Regression model.
  2. Save the trained model and preprocessing scaler.
  3. Load unseen data (new dataset).
  4. Apply the same preprocessing steps (StandardScaler).
  5. Make predictions on unseen data.
- Importance of **consistent preprocessing** between training and unseen data.

## Practical Implementation
- Trained Logistic Regression model on training dataset (same as Day49).  
- Loaded a second dataset (future/unseen samples).  
- Scaled unseen data using the same StandardScaler.  
- Generated predictions for unseen inputs.  
- Compared performance with earlier test results.

## Interpretation
- Predictions (0 = Will Not Purchase, 1 = Will Purchase) were generated for each new record.  
- The model demonstrated **generalization ability** beyond training/testing split.  
- This step shows how models move closer to **deployment**.

## Summary & Key Takeaways
- Logistic Regression can be applied not just on training/testing sets, but also on **completely new data**.  
- Ensuring **preprocessing consistency** is critical.  
- If unseen data has no labels, predictions are still useful but cannot be evaluated immediately.  
- This notebook acts as a bridge from training → **real-world deployment**.
