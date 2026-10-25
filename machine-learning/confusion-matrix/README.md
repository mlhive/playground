# Confusion Matrix & ROC / PR Explorer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/confusion-matrix)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/confusion-matrix](https://mlhive.com/playground/machine-learning/confusion-matrix)

![Confusion Matrix Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

A Confusion Matrix evaluates the performance of a classification model by cross-tabulating true versus predicted labels.

| | Actual Positive | Actual Negative |
| :--- | :--- | :--- |
| **Predicted Positive** | True Positive (**TP**) | False Positive (**FP**) |
| **Predicted Negative** | False Negative (**FN**) | True Negative (**TN**) |

### Core Evaluation Metrics:

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
$$\text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall (Sensitivity)} = \frac{TP}{TP + FN}$$
$$\text{Specificity} = \frac{TN}{TN + FP}, \quad F_1 = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/confusion-matrix):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `THRESHOLD` | `float` | `0.5` | Cutoff probability to classify as positive |
| `PRESET` | `string` | `"balanced"` | Dataset preset (`"balanced"`, `"imbalanced"`, `"high_confidence"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
python solution.py
node solution.js
```
