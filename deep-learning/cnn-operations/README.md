# CNN Operations Visualizer (Convolution & Pooling)

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/deep-learning/cnn-operations)

Interactive visualizer reference: [https://mlhive.com/playground/deep-learning/cnn-operations](https://mlhive.com/playground/deep-learning/cnn-operations)

![CNN Operations Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Convolutional Neural Networks (CNNs) process spatial grid data through sliding kernels and spatial downsampling:

### 2D Convolution:

$$S(i, j) = (I * K)(i, j) = \sum_m \sum_n I(i + m, j + n) K(m, n)$$

### Output Dimension Formula:

$$O = \left\lfloor \frac{W - K + 2P}{S} \right\rfloor + 1$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/deep-learning/cnn-operations):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `KERNEL_SIZE` | `int` | `3` | Dimension of the 3x3 filter |
| `STRIDE` | `int` | `1` | Step size of convolution window |
| `PADDING` | `int` | `0` | Zero-padding border pixels |
| `POOLING_TYPE` | `string` | `"max"` | Subsampling function (`"max"`, `"average"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
