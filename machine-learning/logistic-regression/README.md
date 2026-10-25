# Logistic Regression Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/logistic-regression)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/logistic-regression](https://mlhive.com/playground/machine-learning/logistic-regression)

![Logistic Regression Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Logistic Regression models the probability of a binary outcome using the sigmoid function:

$$\sigma(z) = \frac{1}{1 + e^{-z}}, \quad z = w^T x + b$$

The parameters are optimized by minimizing Binary Cross-Entropy (Log Loss):

$$J(w, b) = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/logistic-regression):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LEARNING_RATE` | `float` | `0.1` | Step size for gradient descent |
| `EPOCHS` | `int` | `200` | Number of training iterations |
| `THRESHOLD` | `float` | `0.5` | Classification decision boundary threshold |
| `PRESET` | `string` | `"study_hours"` | Dataset preset (`"study_hours"`, `"2d_blobs"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
python solution.py
node solution.js
```
