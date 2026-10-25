# Morphological Operations Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/computer-vision/opencv/morphological-operations)

Interactive visualizer reference: [https://mlhive.com/playground/computer-vision/opencv/morphological-operations](https://mlhive.com/playground/computer-vision/opencv/morphological-operations)

![Morphology Preview](https://mlhive.com/playground/computer-vision.png)

---

## Overview

Morphological operations process binary images based on shape geometry using a structuring element (kernel):

- **Erosion**: Strips boundary pixels ($A \ominus B$). Removes small noise.
- **Dilation**: Expands boundaries ($A \oplus B$). Bridges small gaps and fills holes.
- **Opening**: Erosion followed by Dilation ($A \circ B = (A \ominus B) \oplus B$). Cleans small foreground specks.
- **Closing**: Dilation followed by Erosion ($A \bullet B = (A \oplus B) \ominus B$). Fills small holes and cracks.
- **Morphological Gradient**: Difference between Dilation and Erosion ($A \oplus B - A \ominus B$). Highlights object outlines.

### Reference Images:
- Holes: [https://mlhive.com/playground/opencv/morphological-operations/holes.svg](https://mlhive.com/playground/opencv/morphological-operations/holes.svg)
- Noisy Shapes: [https://mlhive.com/playground/opencv/morphological-operations/noisy-shapes.svg](https://mlhive.com/playground/opencv/morphological-operations/noisy-shapes.svg)
- Touching Shapes: [https://mlhive.com/playground/opencv/morphological-operations/touching-shapes.svg](https://mlhive.com/playground/opencv/morphological-operations/touching-shapes.svg)

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/computer-vision/opencv/morphological-operations):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `OPERATION` | `string` | `"open"` | Operation (`"open"`, `"close"`, `"dilate"`, `"erode"`, `"gradient"`) |
| `KERNEL_SHAPE` | `string` | `"rectangle"` | Structuring element shape (`"rectangle"`, `"cross"`, `"ellipse"`) |
| `KERNEL_SIZE` | `int` | `5` | Dimensions of structuring element ($5 \times 5$) |
| `ITERATIONS` | `int` | `1` | Number of times the operation is applied |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
