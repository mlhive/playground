# Embedding Explorer & Projector Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/embedding-projector)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/embedding-projector](https://mlhive.com/playground/machine-learning/embedding-projector)

![Embedding Projector Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

The Embedding Projector visualizes high-dimensional representation vectors in 2D space using dimension-reduction techniques (Principal Component Analysis - PCA, and Cosine Similarity nearest neighbor search).

### Principal Component Analysis (PCA)

1. Center data matrix $X \in \mathbb{R}^{n \times d}$:
   $$\tilde{X} = X - \mu$$
2. Compute covariance matrix:
   $$\Sigma = \frac{1}{n} \tilde{X}^T \tilde{X}$$
3. Compute eigenvectors and project onto top 2 components:
   $$Z = \tilde{X} V_{1:2}$$

### Cosine Similarity

$$\text{similarity}(u, v) = \frac{u \cdot v}{\|u\| \|v\|}$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/embedding-projector):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `METHOD` | `string` | `"PCA"` | Projection technique (`"PCA"`, `"CosineNN"`) |
| `QUERY_WORD` | `string` | `"king"` | Word to search nearest neighbors for |
| `TOP_K` | `int` | `3` | Number of nearest neighbors to retrieve |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
