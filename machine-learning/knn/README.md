# K-Nearest Neighbors (KNN) Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/knn)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/knn](https://mlhive.com/playground/machine-learning/knn)

![KNN Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

K-Nearest Neighbors is a non-parametric supervised classifier. For a query point $x_q$, it identifies the $K$ closest training samples according to a distance metric (e.g. Euclidean), and assigns the class with majority vote:

$$d(p, q) = \sqrt{\sum_{i=1}^m (p_i - q_i)^2}$$

$$\hat{y} = \arg\max_c \sum_{i \in N_K(x_q)} \mathbb{I}(y_i = c)$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/knn):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `K` | `int` | `3` | Number of nearest neighbors to consider |
| `DISTANCE_METRIC` | `string` | `"euclidean"` | Distance function (`"euclidean"`, `"manhattan"`) |
| `QUERY_POINT` | `tuple[float, float]` | `(3.2, 2.8)` | 2D coordinates of sample to classify |
| `PRESET` | `string` | `"two_clusters"` | Dataset preset (`"two_clusters"`, `"interleaved_moons"`, `"three_classes"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
python solution.py
node solution.js
```
