# MediaPipe Pose Landmark Detection Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/computer-vision/mediapipe/pose-landmarks)

Interactive visualizer reference: [https://mlhive.com/playground/computer-vision/mediapipe/pose-landmarks](https://mlhive.com/playground/computer-vision/mediapipe/pose-landmarks)

![MediaPipe Preview](https://mlhive.com/playground/computer-vision.png)

---

## Overview

Tracks 33 full-body landmarks (shoulders, elbows, wrists, hips, knees, ankles) providing 3D human pose reconstruction and biomechanical angle analysis.

### Model Pipeline:
- **On-Device Inference**: WebAssembly and WebGPU / CPU acceleration via MediaPipe Tasks Vision.
- **Normalized Coordinates**: Outputs coordinates normalized to $[0.0, 1.0]$ with depth $Z$ relative to center.

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/computer-vision/mediapipe/pose-landmarks):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MIN_DETECTION_CONFIDENCE` | `float` | `0.5` | Minimum score threshold for detection stage |
| `DELEGATE` | `string` | `"CPU"` | Execution hardware delegate (`"CPU"`, `"GPU"`) |
| `RUN_MODE` | `string` | `"IMAGE"` | Media input stream mode (`"IMAGE"`, `"VIDEO"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
