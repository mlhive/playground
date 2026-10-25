# Decision Tree Classifier Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/decision-tree)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/decision-tree](https://mlhive.com/playground/machine-learning/decision-tree)

![Decision Tree Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Decision Trees partition the feature space into axis-aligned rectangular regions. At each node, the feature and threshold that maximize information gain or minimize impurity are selected.

### Impurity Measures

- **Gini Impurity**:
  $$I_G(p) = 1 - \sum_{k=1}^K p_k^2$$
- **Entropy**:
  $$H(p) = -\sum_{k=1}^K p_k \log_2(p_k)$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/decision-tree):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MAX_DEPTH` | `int` | `3` | Maximum allowed tree depth |
| `CRITERION` | `string` | `"gini"` | Split criterion (`"gini"` or `"entropy"`) |
| `MIN_SAMPLES_SPLIT` | `int` | `2` | Minimum sample count required to split a node |
| `PRESET` | `string` | `"checkerboard"` | Dataset geometry (`"checkerboard"`, `"linear_split"`, `"circles"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
