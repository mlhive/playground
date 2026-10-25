# Normalization Visualizer (Batch Norm & Layer Norm)

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/deep-learning/normalization)

Interactive visualizer reference: [https://mlhive.com/playground/deep-learning/normalization](https://mlhive.com/playground/deep-learning/normalization)

![Normalization Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Normalization stabilizes deep neural network training by mitigating internal covariate shift:

1. **Mean & Variance**:
   $$\mu = \frac{1}{m} \sum_{i=1}^m x_i, \quad \sigma^2 = \frac{1}{m} \sum_{i=1}^m (x_i - \mu)^2$$
2. **Standardization**:
   $$\hat{x}_i = \frac{x_i - \mu}{\sqrt{\sigma^2 + \epsilon}}$$
3. **Affine Transformation**:
   $$y_i = \gamma \hat{x}_i + \beta$$

- **BatchNorm**: Normalizes across batch dimension for each channel.
- **LayerNorm**: Normalizes across feature dimensions for each individual sample.

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/deep-learning/normalization):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `NORM_TYPE` | `string` | `"batch_norm"` | Normalization type (`"batch_norm"`, `"layer_norm"`) |
| `EPSILON` | `float` | `1e-5` | Small constant for numerical stability |
| `GAMMA` | `float` | `1.0` | Learnable scale parameter |
| `BETA` | `float` | `0.0` | Learnable shift parameter |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
