#  Day 52 – K-Nearest Neighbors (KNN) Classification

## Overview

On this day, I studied and implemented **K-Nearest Neighbors (KNN) Classification**.
The focus was on understanding how KNN works, experimenting with different values of `k`, and exploring why **feature scaling** is essential in distance-based algorithms.

---

## Topics Covered

* Concept of **K-Nearest Neighbors (KNN)**:

  * How it works (step-by-step process).
  * Role of the `k` parameter.
  * Distance metrics (Euclidean, Manhattan).
* **Advantages and limitations** of KNN.
* Importance of **feature scaling** in KNN.
* Implementation of KNN on a dataset:

  * With different values of `k` (3, 4, 5).
  * With and without feature scaling.
* Evaluation using **accuracy** and **confusion matrices**.
* Comparison of results for different settings.

---

## Key Learnings

* KNN predicts class labels based on the majority of nearest neighbors.
* The choice of `k` influences model performance:

  * Small `k` → risk of overfitting.
  * Large `k` → risk of underfitting.
* **Scaling features is crucial** since KNN relies on distance.
* In this notebook, best accuracy (**0.93**) was achieved with scaled data at k = 3–5.
* Without scaling, accuracy dropped to **0.78**, highlighting why preprocessing matters.

---

This day’s work built a strong foundation in **KNN Classification**, showing how a simple distance-based algorithm can achieve strong results when combined with proper preprocessing.
