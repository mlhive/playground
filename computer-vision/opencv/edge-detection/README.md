# Image Filters & Edge Detection Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/computer-vision/opencv/edge-detection)

Interactive visualizer reference: [https://mlhive.com/playground/computer-vision/opencv/edge-detection](https://mlhive.com/playground/computer-vision/opencv/edge-detection)

![Edge Detection Preview](https://mlhive.com/playground/computer-vision.png)

---

## Overview

Edge detection identifies points in an image where the brightness changes sharply. Common algorithms include:

- **Sobel Operator**: Computes first-order spatial gradients in $X$ and $Y$:
  $$G_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix} * I, \quad G_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix} * I$$
  $$G = \sqrt{G_x^2 + G_y^2}$$

- **Laplacian**: Computes second-order derivative:
  $$\nabla^2 I = \frac{\partial^2 I}{\partial x^2} + \frac{\partial^2 I}{\partial y^2}$$

- **Canny Edge Detector**: Multi-stage algorithm featuring Gaussian smoothing, gradient calculation, non-maximum suppression, and hysteresis thresholding.

### Reference Images:
- Architecture: [https://mlhive.com/playground/opencv/edge-detection/architecture.webp](https://mlhive.com/playground/opencv/edge-detection/architecture.webp)
- Portrait: [https://mlhive.com/playground/opencv/edge-detection/portrait.webp](https://mlhive.com/playground/opencv/edge-detection/portrait.webp)
- Street: [https://mlhive.com/playground/opencv/edge-detection/street.webp](https://mlhive.com/playground/opencv/edge-detection/street.webp)

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/computer-vision/opencv/edge-detection):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `METHOD` | `string` | `"canny"` | Edge detector (`"canny"`, `"sobel"`, `"laplacian"`) |
| `CANNY_THRESHOLD1` | `int` | `50` | Hysteresis lower threshold |
| `CANNY_THRESHOLD2` | `int` | `150` | Hysteresis upper threshold |
| `BLUR_KERNEL_SIZE` | `int` | `5` | Pre-filtering Gaussian blur kernel |

---

## Implementations

- **Python**: [`solution.py`](./solution.py) (uses `opencv-python` with standalone synthetic fallback)

### How to Run

```bash
python solution.py
```
