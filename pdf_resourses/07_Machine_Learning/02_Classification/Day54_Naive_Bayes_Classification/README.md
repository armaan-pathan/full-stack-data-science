# Day 54 – Naive Bayes Classifier

## Overview

On Day 54, I studied the **Naive Bayes Classifier**, a family of probabilistic algorithms based on Bayes’ Theorem. This notebook includes both theoretical explanation and practical implementation of Naive Bayes variants.

---

## Topics Covered

* Conditional probability and Bayes’ Theorem
* Working of the **Naive Bayes algorithm**
* Real-world applications of Naive Bayes (e.g., spam detection)
* Implementing and comparing three variants of Naive Bayes:

  * **GaussianNB** (continuous features)
  * **MultinomialNB** (count-based features)
  * **BernoulliNB** (binary features)
* Testing each variant under three preprocessing scenarios:

  * Without scaling
  * With **StandardScaler**
  * With **Normalizer**
* Analyzing performance using **accuracy, confusion matrix, and classification report**
* Explanation of why **MultinomialNB fails with StandardScaler**

---

## Key Learnings

* **GaussianNB** works best for continuous features and benefits from scaling.
* **MultinomialNB** is designed for non-negative count data (e.g., word counts) and fails when features are standardized (negative values).
* **BernoulliNB** is suited for binary features and can collapse into predicting only one class without proper preprocessing.
* **Scaling choice matters**: StandardScaler generally helps GaussianNB, while Normalizer can harm performance.
* Always check confusion matrices and class-level metrics, not just overall accuracy.

---

## Conclusion

This day provided a complete understanding of **Naive Bayes classifiers** — from theory and variants to practical implementation and scaling effects. By the end of this notebook, I could clearly see when to use **Gaussian, Multinomial, or Bernoulli Naive Bayes**, and why preprocessing plays a critical role in their performance.
