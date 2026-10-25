# Non-Maximum Suppression (NMS) Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/computer-vision/algorithms/non-maximum-suppression)

Interactive visualizer reference: [https://mlhive.com/playground/computer-vision/algorithms/non-maximum-suppression](https://mlhive.com/playground/computer-vision/algorithms/non-maximum-suppression)

![NMS Preview](https://mlhive.com/playground/computer-vision.png)

---

## Overview

Non-Maximum Suppression (NMS) is an essential post-processing step in object detection pipelines (YOLO, Faster R-CNN, SSD) that eliminates redundant, overlapping bounding boxes detecting the same object.

### Algorithm Steps:
1. Filter out candidate boxes with $\text{confidence} < \text{confidence\_threshold}$.
2. Sort remaining candidate boxes in descending order of score.
3. Select box $B$ with highest confidence score and add to kept set.
4. Remove any pending box $B'$ having $\text{IoU}(B, B') > \text{iou\_threshold}$.
5. Repeat until no candidate boxes remain.

### Intersection over Union (IoU):

$$\text{IoU}(A, B) = \frac{\text{Area}(A \cap B)}{\text{Area}(A \cup B)}$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/computer-vision/algorithms/non-maximum-suppression):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `CONFIDENCE_THRESHOLD` | `float` | `0.3` | Minimum detection score cutoff |
| `IOU_THRESHOLD` | `float` | `0.5` | Overlap threshold above which lower-scoring boxes are suppressed |
| `CLASS_AWARE` | `bool` | `True` | When true, suppression is performed independently per object class |
| `PRESET` | `string` | `"duplicate_detections"` | Scenario preset (`"duplicate_detections"`, `"crowded_scene"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
python solution.py
node solution.js
```
