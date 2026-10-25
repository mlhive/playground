# Dropout Layer Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/deep-learning/dropout-layer)

Interactive visualizer reference: [https://mlhive.com/playground/deep-learning/dropout-layer](https://mlhive.com/playground/deep-learning/dropout-layer)

![Dropout Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Dropout is a stochastic regularization technique preventing neuron co-adaptation by randomly zeroing out activations during training.

### Inverted Dropout:

1. Generate binary Bernoulli mask $m_i \sim \text{Bernoulli}(1 - p)$
2. Apply mask and scale activations:
   $$\tilde{a}_i = \frac{m_i \odot a_i}{1 - p}$$
3. During evaluation mode, no mask or scaling is applied ($a_{\text{eval}} = a$), preserving identical expected activation magnitude!

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/deep-learning/dropout-layer):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `DROPOUT_RATE` | `float` | `0.3` | Probability $p$ of dropping each neuron |
| `MODE` | `string` | `"train"` | Execution mode (`"train"` vs `"eval"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
