# CNN Architecture Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/deep-learning/cnn-visualizer)

Interactive visualizer reference: [https://mlhive.com/playground/deep-learning/cnn-visualizer](https://mlhive.com/playground/deep-learning/cnn-visualizer)

![CNN Architecture Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Inspects an end-to-end Convolutional Neural Network forward propagation pipeline:
1. **Input**: $32 \times 32 \times 3$ image
2. **Conv1**: $16$ filters of $3 \times 3$ ($30 \times 30 \times 16$)
3. **ReLU + MaxPool1**: $2 \times 2$ downsampling ($15 \times 15 \times 16$)
4. **Conv2**: $32$ filters of $3 \times 3$ ($13 \times 13 \times 32$)
5. **ReLU + MaxPool2**: $2 \times 2$ ($6 \times 6 \times 32$)
6. **Flatten**: $1152$ feature vector
7. **Dense + Softmax**: Class probability distribution over $10$ classes.

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/deep-learning/cnn-visualizer):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `INPUT_CHANNELS` | `int` | `3` | RGB image channels |
| `NUM_CLASSES` | `int` | `10` | Classification output categories |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
