# Color Spaces & HSV Masking Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/computer-vision/opencv/color-spaces)

Interactive visualizer reference: [https://mlhive.com/playground/computer-vision/opencv/color-spaces](https://mlhive.com/playground/computer-vision/opencv/color-spaces)

![Color Spaces Preview](https://mlhive.com/playground/computer-vision.png)

---

## Overview

Inspects color representations across standard computer vision color spaces and isolates target objects using HSV (Hue, Saturation, Value) color range masking.

- **RGB / BGR**: Additive primary color channels. Sensitive to illumination changes.
- **HSV / HSL**: Decouples chromatic content (**Hue**) and color purity (**Saturation**) from brightness (**Value**). Ideal for color segmentation.
- **Grayscale**: Luminance only:
  $$Y = 0.299 R + 0.587 G + 0.114 B$$

### Reference Images:
- Peppers: [https://mlhive.com/playground/opencv/color-spaces/peppers.webp](https://mlhive.com/playground/opencv/color-spaces/peppers.webp)
- Color Blocks: [https://mlhive.com/playground/opencv/color-spaces/color-blocks.svg](https://mlhive.com/playground/opencv/color-spaces/color-blocks.svg)

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/computer-vision/opencv/color-spaces):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `HUE_MIN` | `int` | `170` | Lower hue threshold (0-180 in OpenCV) |
| `HUE_MAX` | `int` | `10` | Upper hue threshold (wraps around for Red) |
| `SAT_MIN` | `int` | `100` | Minimum saturation |
| `SAT_MAX` | `int` | `255` | Maximum saturation |
| `VAL_MIN` | `int` | `60` | Minimum brightness value |
| `VAL_MAX` | `int` | `255` | Maximum brightness value |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
