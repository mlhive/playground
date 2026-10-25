# Object Detection Metrics & mAP Explorer Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/computer-vision/algorithms/detection-metrics)

Interactive visualizer reference: [https://mlhive.com/playground/computer-vision/algorithms/detection-metrics](https://mlhive.com/playground/computer-vision/algorithms/detection-metrics)

![Detection Metrics Preview](https://mlhive.com/playground/computer-vision.png)

---

## Overview

Evaluates object detection performance by matching predicted bounding boxes against ground truth annotations at an IoU threshold (e.g. $\ge 0.50$).

### Metrics:

- **True Positive (TP)**: Detection with $\text{IoU} \ge \text{IoU\_threshold}$ matching an unmatched ground truth box of the same class.
- **False Positive (FP)**: Detection with $\text{IoU} < \text{IoU\_threshold}$ or duplicate detection on an already matched ground truth.
- **False Negative (FN)**: Ground truth box left unmatched.
- **Average Precision (AP)**: Area under the Precision-Recall curve (11-point interpolation or all-point area).
- **mAP**: Mean of AP across all classes.

### Reference Image:
- Street Scene: [https://mlhive.com/playground/detection-metrics/street-scene.webp](https://mlhive.com/playground/detection-metrics/street-scene.webp)

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/computer-vision/algorithms/detection-metrics):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `IOU_THRESHOLD` | `float` | `0.5` | Matching threshold between prediction and ground truth |
| `CONFIDENCE_THRESHOLD` | `float` | `0.4` | Minimum confidence cutoff for predictions |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
python solution.py
node solution.js
```
