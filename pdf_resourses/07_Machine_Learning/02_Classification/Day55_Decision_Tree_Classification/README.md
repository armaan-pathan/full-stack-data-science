# Day 55 – Decision Tree Classifier

## Overview

On Day 55, I studied the **Decision Tree Classifier**, a supervised machine learning algorithm that splits data based on feature values to make predictions. This notebook includes both the theoretical foundation and practical implementation of decision trees.

---

## Topics Covered

* Concept of **Decision Trees** and how they work
* **Entropy** and its formula
* **Information Gain (IG)** and how it guides splits
* **Gini Index & Gini Impurity** as an alternative to entropy
* **Pruning** to prevent overfitting and its parameters (`max_depth`, `min_samples_split`, `min_samples_leaf`, etc.)
* Step-by-step process of building a decision tree
* Implementing and evaluating decision trees with:

  * With and without scaling (showing scaling is not required)
  * Different tree depths (`max_depth=3` vs `max_depth=10`)

---

## Key Learnings

* Decision Trees are **scale-invariant** – accuracy remains the same with and without scaling.
* **Tree depth** has a strong impact on performance:

  * Shallow trees (depth=3) generalize better.
  * Deep trees (depth=10) can overfit and slightly reduce test accuracy.
* **Entropy, Gini, and Information Gain** are key measures to decide splits.
* **Pruning parameters** help control complexity and improve generalization.
* Decision Trees are **easy to interpret and visualize**, making them useful for explainable AI.

---

## Conclusion

This day provided both a theoretical and practical understanding of **Decision Trees**. I learned why scaling is unnecessary, how different depths affect model generalization, and how pruning helps in controlling overfitting. Decision Trees are a powerful yet interpretable algorithm, serving as a foundation for more advanced ensemble methods like Random Forests and Gradient Boosted Trees.
