# Polynomial Regression Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/polynomial-regression)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/polynomial-regression](https://mlhive.com/playground/machine-learning/polynomial-regression)

![Polynomial Regression Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Polynomial Regression extends linear models by transforming input features into powers $x, x^2, \dots, x^d$:

$$y = w_0 + w_1 x + w_2 x^2 + \dots + w_d x^d$$

This allows fitting non-linear curves while keeping linear mathematical structure with respect to weights. Regularization (L2 / Ridge) helps control overfitting at higher degrees:

$$J(w) = \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i)^2 + \lambda \sum_{j=1}^d w_j^2$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/polynomial-regression):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DEGREE` | `int` | `3` | Degree of the polynomial (1 to 5) |
| `LEARNING_RATE` | `float` | `0.05` | Learning rate for feature-normalized gradient descent |
| `EPOCHS` | `int` | `200` | Iterations of training |
| `L2_LAMBDA` | `float` | `0.001` | Ridge regularization coefficient |
| `PRESET` | `string` | `"cubic_curve"` | Dataset shape (`"cubic_curve"`, `"quadratic"`, `"sine_wave"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
