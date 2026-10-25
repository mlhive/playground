# Activation Functions Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/deep-learning/activation-functions)

Interactive visualizer reference: [https://mlhive.com/playground/deep-learning/activation-functions](https://mlhive.com/playground/deep-learning/activation-functions)

![Activation Functions Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Non-linear activation functions enable neural networks to learn non-linear representations and complex decision boundaries.

| Function | Formula | Range | Common Use |
| :--- | :--- | :--- | :--- |
| **ReLU** | $\max(0, x)$ | $[0, \infty)$ | Default hidden layers |
| **LeakyReLU** | $\max(\alpha x, x)$ | $(-\infty, \infty)$ | Prevents dying ReLU |
| **Sigmoid** | $\frac{1}{1 + e^{-x}}$ | $(0, 1)$ | Binary classification output |
| **Tanh** | $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ | $(-1, 1)$ | Zero-centered hidden |
| **GELU** | $x \Phi(x) \approx 0.5x(1 + \tanh(\sqrt{2/\pi}(x + 0.044715x^3)))$ | $(-0.17, \infty)$ | Transformers / LLMs |
| **Softmax** | $\frac{e^{x_i}}{\sum_j e^{x_j}}$ | $(0, 1)$ | Multi-class probabilities |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
