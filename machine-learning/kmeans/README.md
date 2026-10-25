# K-Means Clustering Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/kmeans)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/kmeans](https://mlhive.com/playground/machine-learning/kmeans)

![K-Means Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

K-Means is an unsupervised clustering algorithm that partitions $n$ observations into $K$ clusters. Each observation belongs to the cluster with the nearest mean (centroid).

### Algorithm Steps:
1. **Initialize centroids**: Random or K-Means++
2. **Assignment step**: Assign each sample $x_i$ to nearest cluster centroid $\mu_k$:
   $$c_i = \arg\min_k \| x_i - \mu_k \|^2$$
3. **Update step**: Recompute centroids:
   $$\mu_k = \frac{1}{|C_k|} \sum_{i \in C_k} x_i$$
4. Repeat until convergence or `MAX_ITERS` reached.

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/kmeans):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `K` | `int` | `3` | Number of clusters to form |
| `INIT` | `string` | `"kmeans++"` | Centroid initialization (`"kmeans++"`, `"random"`) |
| `MAX_ITERS` | `int` | `50` | Maximum clustering iterations |
| `PRESET` | `string` | `"three_blobs"` | Dataset geometry (`"three_blobs"`, `"four_clusters"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
python solution.py
node solution.js
```
