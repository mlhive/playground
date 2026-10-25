# Linear Regression Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/linear-regression)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/linear-regression](https://mlhive.com/playground/machine-learning/linear-regression)

![Linear Regression Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Linear Regression models the relationship between a scalar response $y$ and one or more explanatory variables $x$ using a linear equation:

$$y = wx + b$$

The parameters (weight $w$ and bias $b$) are optimized to minimize the Mean Squared Error (MSE) loss:

$$J(w, b) = \frac{1}{2n} \sum_{i=1}^n (wx_i + b - y_i)^2$$

### Gradient Updates

$$\frac{\partial J}{\partial w} = \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i) x_i$$
$$\frac{\partial J}{\partial b} = \frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i)$$

Parameters are iteratively updated using Gradient Descent:

$$w \leftarrow w - \alpha \frac{\partial J}{\partial w}, \quad b \leftarrow b - \alpha \frac{\partial J}{\partial b}$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/linear-regression):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LEARNING_RATE` | `float` | `0.01` | Step size for gradient descent updates |
| `EPOCHS` | `int` | `100` | Number of optimization iterations |
| `PRESET` | `string` | `"linear_trend"` | Dataset preset (`"linear_trend"`, `"steep_slope"`, `"noisy_scatter"`, `"custom"`) |
| `VERBOSE` | `bool` | `True` | Prints loss and parameter trajectory every few epochs |

---

## Implementations

- **Python**: [`solution.py`](./solution.py) (Pure NumPy gradient descent + analytical Ordinary Least Squares)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
# Python
python solution.py

# Node.js
node solution.js
```
