# Day 56 – Ensemble Learning

## Overview

On **Day 56**, I studied **Ensemble Learning**, a machine learning technique that combines multiple weak learners to create a stronger model.
The idea is similar to a group of experts making decisions together — their combined knowledge is usually better than relying on a single expert.

This notebook first covers the **theory of ensemble methods** and then implements different approaches (Bagging, Boosting, Voting, Stacking) on the dataset to compare their performance.

---

## Contents

### 1. Theory

* Explained the concept of **weak vs strong learners**.
* Why ensemble methods are used to improve accuracy, stability, and generalization.
* Detailed discussion of ensemble techniques:

  * **Bagging (Random Forest)**
  * **Boosting (AdaBoost, XGBoost, LightGBM)**
  * **Voting Classifier**
  * **Stacking Classifier**
* Covered concepts of bias–variance tradeoff and how ensembles prevent overfitting.
* Random Forest parameters and boosting algorithms were explained in detail.

---

### 2. Code Implementation

* **Bagging – Random Forest**: trained multiple decision trees in parallel, reducing variance.
* **Boosting – AdaBoost, XGBoost, LightGBM**: sequentially improved performance by focusing on misclassified samples.
* **Voting Classifier**: combined Logistic Regression, SVM, and Decision Tree using both hard and soft voting.
* **Stacking Classifier**: combined KNN, SVM, and Decision Tree as base learners, with Logistic Regression as a meta-learner.
* Evaluated all models with **accuracy, confusion matrix, and classification report**.

---

### 3. Results & Comparison

* Created a **comparison table** of model accuracies.
* Visualized results with a **bar chart** to make performance differences clear.
* Observed that:

  * **AdaBoost achieved the highest accuracy (0.94)**.
  * Random Forest and Stacking also performed strongly.
  * Voting classifier gave lower accuracy, showing that simple combinations don’t always outperform.

---

## Key Takeaways

* **Ensemble Learning** combines multiple models to create more robust predictions.
* **Bagging** reduces variance; **Boosting** reduces bias.
* **Voting** and **Stacking** combine diverse models, but effectiveness depends on base learners.
* Ensemble methods also help in **preventing overfitting**.
* On this dataset, **AdaBoost was the best performer**, while Random Forest and Stacking also gave reliable results.
* Ensemble techniques often outperform single classifiers in real-world problems.

---

**Conclusion:**
This day gave me practical insights into how ensemble learning works, both in theory and implementation. Comparing bagging, boosting, voting, and stacking showed me the strengths and weaknesses of each method, and why ensembles are a powerful tool in machine learning.
