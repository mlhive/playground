# Contour & Shape Detection Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/computer-vision/opencv/contour-shape-detection)

Interactive visualizer reference: [https://mlhive.com/playground/computer-vision/opencv/contour-shape-detection](https://mlhive.com/playground/computer-vision/opencv/contour-shape-detection)

![Contour Detection Preview](https://mlhive.com/playground/computer-vision.png)

---

## Overview

Contour detection identifies boundaries of shapes with continuous intensity. Using the Douglas-Peucker polygon approximation algorithm (`cv2.approxPolyDP`), shapes are classified based on vertex counts:

- **3 vertices**: Triangle
- **4 vertices**: Quadrilateral (Square if aspect ratio $\approx 1.0$, otherwise Rectangle)
- **5 vertices**: Pentagon
- **6+ vertices**: Polygon or Circle (circularity $4\pi \frac{A}{P^2} \approx 1.0$)

### Reference Images:
- Geometric Shapes: [https://mlhive.com/playground/opencv/contour-shape-detection/geometric-shapes.svg](https://mlhive.com/playground/opencv/contour-shape-detection/geometric-shapes.svg)
- Noisy Shapes: [https://mlhive.com/playground/opencv/contour-shape-detection/noisy-shapes.svg](https://mlhive.com/playground/opencv/contour-shape-detection/noisy-shapes.svg)
- Objects: [https://mlhive.com/playground/opencv/contour-shape-detection/objects.svg](https://mlhive.com/playground/opencv/contour-shape-detection/objects.svg)

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/computer-vision/opencv/contour-shape-detection):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `BINARY_THRESHOLD` | `int` | `127` | Grayscale intensity cutoff for binary mask |
| `EPSILON_FACTOR` | `float` | `0.04` | Approximation accuracy $\epsilon = \text{factor} \times \text{arcLength}$ |
| `MIN_CONTOUR_AREA` | `int` | `100` | Minimum area threshold to reject noise |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
