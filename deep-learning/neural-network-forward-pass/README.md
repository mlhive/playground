# Neural Network Forward Pass Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/deep-learning/neural-network-forward-pass)

Interactive visualizer reference: [https://mlhive.com/playground/deep-learning/neural-network-forward-pass](https://mlhive.com/playground/deep-learning/neural-network-forward-pass)

![Forward Pass Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

The forward pass computes layer-by-layer activations in a Feedforward Neural Network (Multilayer Perceptron). For layer $l$:

1. **Linear Transformation (Weighted Sum)**:
   $$z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}$$
2. **Non-linear Activation**:
   $$a^{[l]} = g^{[l]}(z^{[l]})$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/deep-learning/neural-network-forward-pass):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `LAYER_SIZES` | `list[int]` | `[3, 4, 2, 1]` | Network architecture (input, hidden, output) |
| `ACTIVATION` | `string` | `"relu"` | Hidden activation (`"relu"`, `"sigmoid"`, `"tanh"`, `"linear"`) |
| `WEIGHT_PRESET` | `string` | `"he"` | Initialization scheme (`"he"`, `"xavier"`, `"small"`) |
| `INPUT_VALUES` | `list[float]` | `[0.75, -0.3, 0.5]` | Feature vector fed into input layer |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
python solution.py
node solution.js
```
