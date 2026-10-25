# Support Vector Machine (SVM) Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/svm)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/svm](https://mlhive.com/playground/machine-learning/svm)

![SVM Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Support Vector Machine constructs an optimal separating hyperplane maximizing the geometric margin between two classes:

$$\min_{w, b, \xi} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^n \xi_i$$

$$\text{subject to } y_i (w^T \phi(x_i) + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$

### Kernels:
- **Linear**: $K(x, x') = x^T x'$
- **RBF**: $K(x, x') = \exp(-\gamma \|x - x'\|^2)$
- **Polynomial**: $K(x, x') = (x^T x' + 1)^d$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/svm):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `C` | `float` | `1.0` | Regularization / margin hardness penalty |
| `KERNEL` | `string` | `"linear"` | Kernel type (`"linear"`, `"rbf"`) |
| `GAMMA` | `float` | `0.5` | Kernel bandwidth coefficient for RBF |
| `LEARNING_RATE` | `float` | `0.001` | Step size for subgradient descent optimizer |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
