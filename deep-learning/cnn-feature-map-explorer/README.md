# CNN Feature Map Explorer Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/deep-learning/cnn-feature-map-explorer)

Interactive visualizer reference: [https://mlhive.com/playground/deep-learning/cnn-feature-map-explorer](https://mlhive.com/playground/deep-learning/cnn-feature-map-explorer)

![Feature Map Explorer Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Visualizes how successive convolutional filter kernels detect hierarchical visual features:
- **Early layers**: Low-level edge and contrast detectors (Sobel, Laplacian, horizontal/vertical)
- **Deeper layers**: High-level semantic textures, combinations, and patterns.

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/deep-learning/cnn-feature-map-explorer):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ACTIVE_FILTER` | `string` | `"horizontal_edges"` | Filter preset (`"horizontal_edges"`, `"vertical_edges"`, `"sharpen"`, `"box_blur"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
