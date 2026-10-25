# Backpropagation Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/deep-learning/backpropagation)

Interactive visualizer reference: [https://mlhive.com/playground/deep-learning/backpropagation](https://mlhive.com/playground/deep-learning/backpropagation)

![Backpropagation Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Backpropagation computes the gradient of the loss function with respect to weights and biases by repeatedly applying the chain rule backward from the output layer:

1. **Output Error**:
   $$\delta^{[L]} = \nabla_a L \odot g'(z^{[L]})$$
2. **Backpropagate Error to Layer $l$**:
   $$\delta^{[l]} = ((W^{[l+1]})^T \delta^{[l+1]}) \odot g'(z^{[l]})$$
3. **Parameter Gradients**:
   $$\frac{\partial L}{\partial W^{[l]}} = \delta^{[l]} (a^{[l-1]})^T, \quad \frac{\partial L}{\partial b^{[l]}} = \delta^{[l]}$$
4. **SGD Weight Update**:
   $$W^{[l]} \leftarrow W^{[l]} - \alpha \frac{\partial L}{\partial W^{[l]}}$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/deep-learning/backpropagation):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LEARNING_RATE` | `float` | `0.2` | Optimization step size $\alpha$ |
| `EPOCHS` | `int` | `80` | Training iterations |
| `PRESET` | `string` | `"xor"` | Problem dataset (`"xor"`, `"and"`, `"or"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
