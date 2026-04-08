# Classification in Machine Learning

## Overview

The **Classification** folder contains all notebooks and projects related to **classification algorithms in Machine Learning**.

Unlike regression (which predicts continuous values), classification is about predicting **categories or classes** (e.g., Yes/No, Spam/Not Spam, Purchase/Not Purchase).

This section begins with the foundation of classification, covers **Logistic Regression**, extends it to unseen data, demonstrates **deployment using Streamlit**, and further explores advanced algorithms and evaluation methods.

---

## Contents

### [Day49 – Introduction to Classification & Logistic Regression](Day49_Intro_to_Classification_&_Logistic_Regression)

* Theory of **Classification** and its importance.
* Difference between **Classification and Regression**.
* Logistic Regression explained in detail (Sigmoid, probabilities, why it’s classification not regression).
* **Confusion Matrix** explained with COVID doctor–patient example.
* Performance metrics: Accuracy, Precision, Recall, F1-score.
* **Bias–Variance** concept with train/test accuracies.
* Multiple experiments: without scaling, StandardScaler, Normalizer, and different random states.
* **Best Accuracy achieved: 0.92** (StandardScaler, random_state=0, test_size=0.20).

---

### [Day50 – Logistic Regression with Unseen Data](Day50a_Logistic_Regression_on_Unseen_Data)

* Extended Logistic Regression to predict on **unseen/future data**.
* Workflow: Train → Save → Load unseen dataset → Preprocess → Predict.
* Emphasized **preprocessing consistency** between training and new data.
* Predictions generated for unseen dataset → showing how models generalize in real-world scenarios.
* Acts as a bridge towards **deployment**.

---

### [Day50 – Logistic Regression Deployment with Streamlit](Day50b_LR_Deployment_with_Streamlit)

* Built a **Streamlit web app** for Logistic Regression.
* User enters **Age** and **Estimated Salary** to predict:

  * Will Purchase
  * Will Not Purchase
* Inputs placed in sidebar, clean UI with footer branding.
* App demonstrates how ML models move from **Jupyter notebooks → real-world interactive apps**.

---

### [Day52 – K-Nearest Neighbors (KNN) Classification](Day52_K-Nearest_Neighbors_(KNN)_Classification)

* Introduction to **KNN Classification**, a distance-based supervised learning algorithm.
* Explained how KNN works step by step: choosing `k`, calculating distances, finding nearest neighbors, and majority voting.
* Discussed the **importance of feature scaling** for KNN since it relies on distance.
* Experiments performed with different values of `k` (3, 4, 5) using scaled data → **accuracy = 0.93**.
* Compared with **no scaling (k=3)** → accuracy dropped to **0.78**, showing why preprocessing is crucial.
* Confusion matrices analyzed to understand misclassifications.
* Key learning: KNN is simple, effective, but highly dependent on **k-value choice** and **scaling**.

---

### [Day53 – Support Vector Machine (SVM) Classification](Day53_Support_Vector_Machine(SVM)_Classification)

* Introduced **Support Vector Machine (SVM)**: an algorithm that finds the optimal hyperplane to separate classes.  
* Explained concepts of **support vectors, margin, and kernel trick**.  
* Implemented SVM with different kernels (`linear`, `rbf`).  
* Compared performance **with and without scaling**, showing that SVM is highly sensitive to feature scaling.  
* Evaluated results using confusion matrices, ROC curve, and AUC score.  
* Extended experiments to **future predictions**, applying the trained model on unseen data.  

---

### [Day54 – Naive Bayes Classification](Day54_Naive_Bayes_Classification)

* Covered the theory of **Naive Bayes**:
  - Conditional probability and Bayes’ Theorem  
  - Assumption of feature independence  
  - Real-world use cases (spam filtering, sentiment analysis)  
  - Types: **GaussianNB**, **MultinomialNB**, **BernoulliNB**  
* Implemented all three variants under different preprocessing:
  - Without scaling  
  - With StandardScaler  
  - With Normalizer  
* Observed that:
  - **GaussianNB** and **BernoulliNB** worked well with/without scaling.  
  - **MultinomialNB** failed with StandardScaler (since it requires non-negative inputs).  
* Clear comparison across approaches highlighted how preprocessing impacts performance.  

---

### [Day55 – Decision Tree Classification](Day55_Decision_Tree_Classification)

* Introduced **Decision Tree Classifier**: a model that splits data into branches based on feature thresholds.  
* Explained concepts of **Entropy, Information Gain, Gini impurity, and Pruning**.  
* Implemented Decision Trees:
  - With and without scaling (showing scaling has no effect).  
  - With `max_depth=3` and `max_depth=10` to compare generalization vs overfitting.  
* Results showed:
  - Accuracy remained the same with and without scaling → proving Decision Trees are **scale-invariant**.  
  - Shallow trees (depth=3) generalized better.  
  - Deeper trees (depth=10) slightly overfit, reducing accuracy.  

---

### [Day56 – Ensemble Learning](Day56_Ensemble_Learning)

* Studied **Ensemble Learning**, which combines multiple weak learners to form a stronger model.
* Explained the difference between **weak learners** and **strong learners**.
* Covered major ensemble methods:

  * **Bagging** → Random Forest Classifier
  * **Boosting** → AdaBoost, XGBoost, LightGBM
  * **Voting & Stacking** classifiers
* Implemented and compared these ensemble models on the dataset.
* Created a **bar chart comparison** of accuracies across models:

  * Random Forest = 0.92
  * AdaBoost = 0.94
  * XGBoost = 0.90
  * LightGBM = 0.89
  * Voting Classifier = 0.89
  * Stacking Classifier = 0.91
* Observed that **AdaBoost performed best**, but all ensemble methods improved model robustness compared to individual classifiers.

---

### [Day57 – Cross-Validation & ROC/AUC](Day57_Cross_Validation_and_ROC_AUC)

* Focused on **advanced evaluation techniques** for classification.
* Learned about **Cross-Validation** and why it provides more reliable performance estimates than a single train/test split.
* Implemented **Stratified k-Fold Cross-Validation** and evaluated both accuracy and ROC-AUC scores across folds.
* Studied **ROC (Receiver Operating Characteristic) curves** to visualize trade-offs between True Positive Rate and False Positive Rate.
* Calculated the **AUC (Area Under Curve)** as a single numeric performance measure.
* Results showed **high accuracy with AUC > 0.90**, confirming excellent class separation ability.

---
## Key Takeaways from Classification

* Classification is about predicting **categories** instead of numbers.
* Logistic Regression, despite its name, is a **classification algorithm**.
* Preprocessing (scaling/normalization) impacts accuracy for certain models.
* Confusion matrix & metrics (Precision, Recall, F1-score) give deeper insights than accuracy alone.
* Models must generalize well → tested with **unseen data**.
* Deployment with **Streamlit** shows how end-users can interact with ML models.
* K-Nearest Neighbors (KNN) is a simple distance-based algorithm where predictions depend on the majority class of neighbors.
* The choice of k-value impacts performance (small k → overfitting, large k → underfitting).
* Feature scaling is critical for KNN: accuracy improved from 0.78 (unscaled) to 0.93 (scaled).
* **SVM** is powerful in high-dimensional spaces, requires scaling, and benefits from kernel functions.
* **Naive Bayes** is fast, works well with independence assumptions, but preprocessing choices matter.
* **Decision Trees** are interpretable, do not require scaling, and must be pruned to avoid overfitting.
* **Ensemble Learning** (Bagging, Boosting, Voting, Stacking) combines multiple learners for stronger performance, often preventing overfitting.
* **Cross-Validation & ROC/AUC** provide more reliable and deeper evaluation of model performance compared to accuracy alone.

---
