# Basics of Machine Learning

## Overview

The **Basics** folder introduces the **foundational concepts of Machine Learning**.
It covers the essential preprocessing and feature engineering steps that are required before building ML models.

These notebooks are designed to help beginners understand how raw data is transformed into a usable form for algorithms.

---

## Contents

### [Day39 – Introduction to Machine Learning](Day39_Introduction_to_Machine_Learning.ipynb)

* What is Machine Learning?
* Types of ML: **Supervised, Unsupervised, Reinforcement Learning**.
* General ML workflow: **Data → Preprocessing → Training → Testing → Prediction**.

---

### [Day40 – Data Preprocessing in ML](Day40_Data_Preprocessing_in_Machine_Learning.ipynb)

* Why preprocessing is essential.
* Steps covered:

  * Handling missing values
  * Encoding categorical features
  * Splitting data into training and testing sets
  * Feature scaling basics
* Implemented preprocessing using a sample dataset.

---

### [Day45 – Feature Scaling in ML](Day45_Feature_Scaling_in_Machine_Learning.ipynb)

* Importance of scaling numerical features.
* Techniques covered:

  * **Normalization (Min–Max Scaling)** → range \[0,1], does not assume Gaussian distribution.
  * **Standardization (Z-score Scaling)** → mean=0, variance=1, follows Gaussian distribution.
* Practical implementation with examples.
* When to use normalization vs standardization.

---

### [Day51 – Principal Component Analysis (PCA) in ML](Day51_PCA_in_Machine_Learning.ipynb)

* **Dimensionality reduction technique** that transforms high-dimensional data into fewer principal components while retaining most of the variance.
* Why PCA is useful: reduces redundancy, speeds up computation, and avoids overfitting.
* Step-by-step working of PCA (standardization → covariance → eigenvalues/eigenvectors → projection).
* Applied PCA on a dataset and trained **Logistic Regression** on reduced features.
* Key results:

  * \~90% variance retained using 12 principal components.
  * Achieved maximum accuracy of **0.8227**.

---

## Datasets

All datasets used in these notebooks are stored in the [`datasets/`](datasets) folder for easy reference.

---

## Key Takeaways

* Preprocessing is the **foundation of any ML project**.
* Proper handling of missing values, encoding, and scaling ensures models learn effectively.
* Feature scaling improves training stability and convergence.
* PCA helps reduce dimensionality, simplify models, and retain most of the useful information.

---

This folder builds the base required for working on advanced topics in **Regression, Classification, and Clustering** in later sections.
