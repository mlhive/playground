# MLHive Playgrounds — Practical Code Examples

[![MLHive Interactive Playgrounds](https://img.shields.io/badge/MLHive-Interactive_Playgrounds-blue?style=for-the-badge)](https://mlhive.com/playground)

This repository contains comprehensive, production-grade, self-contained practical code examples and educational walkthroughs mirroring every interactive visualizer on [MLHive](https://mlhive.com/playground).

Each folder matches the exact link structure of the website (e.g. `/playground/deep-learning/neural-network-forward-pass` $\rightarrow$ `deep-learning/neural-network-forward-pass`), and contains:
1. **Configurable Run Parameters at the Top**: Tweak hyperparameters, thresholds, kernels, and learning rates just like using the interactive visualizer sliders!
2. **Hardcoded Presets & Datasets**: Switch between standard datasets, edge cases, and synthetic samples.
3. **Multi-Language Implementations**:
   - **Algorithms**: Full runnable solutions in **Python**, **JavaScript (Node.js)**, **Java**, **C++**, and **Go**.
   - **Machine Learning & Deep Learning**: Pure Python + NumPy/Scikit-Learn/PyTorch and Node.js solutions.
   - **Computer Vision & GenAI**: OpenCV, MediaPipe, NMS, mAP, and LLM sampling pipelines.
4. **Detailed `README.md`**: Theoretical background, mathematical formulations, complexity analysis, and direct link references to the live web visualizer.

---

## Catalog Directory (50 Playgrounds)

### 1. Algorithms and Data Structures
Direct live link: [https://mlhive.com/playground/algorithms](https://mlhive.com/playground/algorithms)

| Category | Algorithm / Playground | Live Visualizer Link | Available Languages |
| :--- | :--- | :--- | :--- |
| **Sorting** | [Bubble Sort](algorithms/sorting/bubble-sort) | [Live Page](https://mlhive.com/playground/algorithms/sorting/bubble-sort) | Python, JS, Java, C++, Go |
| **Sorting** | [Selection Sort](algorithms/sorting/selection-sort) | [Live Page](https://mlhive.com/playground/algorithms/sorting/selection-sort) | Python, JS, Java, C++, Go |
| **Sorting** | [Insertion Sort](algorithms/sorting/insertion-sort) | [Live Page](https://mlhive.com/playground/algorithms/sorting/insertion-sort) | Python, JS, Java, C++, Go |
| **Sorting** | [Merge Sort](algorithms/sorting/merge-sort) | [Live Page](https://mlhive.com/playground/algorithms/sorting/merge-sort) | Python, JS, Java, C++, Go |
| **Sorting** | [Quick Sort](algorithms/sorting/quick-sort) | [Live Page](https://mlhive.com/playground/algorithms/sorting/quick-sort) | Python, JS, Java, C++, Go |
| **Searching** | [Linear Search](algorithms/searching/linear-search) | [Live Page](https://mlhive.com/playground/algorithms/searching/linear-search) | Python, JS, Java, C++, Go |
| **Searching** | [Binary Search](algorithms/searching/binary-search) | [Live Page](https://mlhive.com/playground/algorithms/searching/binary-search) | Python, JS, Java, C++, Go |
| **Searching** | [Breadth-First Search (BFS)](algorithms/searching/bfs) | [Live Page](https://mlhive.com/playground/algorithms/searching/bfs) | Python, JS, Java, C++, Go |
| **Searching** | [Depth-First Search (DFS)](algorithms/searching/dfs) | [Live Page](https://mlhive.com/playground/algorithms/searching/dfs) | Python, JS, Java, C++, Go |
| **Graph** | [Breadth-First Search (BFS)](algorithms/graph-algorithms/bfs) | [Live Page](https://mlhive.com/playground/algorithms/graph-algorithms/bfs) | Python, JS, Java, C++, Go |
| **Graph** | [Depth-First Search (DFS)](algorithms/graph-algorithms/dfs) | [Live Page](https://mlhive.com/playground/algorithms/graph-algorithms/dfs) | Python, JS, Java, C++, Go |
| **Recursion** | [Factorial Recursion](algorithms/recursion/factorial-recursion) | [Live Page](https://mlhive.com/playground/algorithms/recursion/factorial-recursion) | Python, JS, Java, C++, Go |
| **Recursion** | [Fibonacci Recursion](algorithms/recursion/fibonacci-recursion) | [Live Page](https://mlhive.com/playground/algorithms/recursion/fibonacci-recursion) | Python, JS, Java, C++, Go |
| **Dynamic Prog.** | [Fibonacci DP](algorithms/dynamic-programming/fibonacci-dp) | [Live Page](https://mlhive.com/playground/algorithms/dynamic-programming/fibonacci-dp) | Python, JS, Java, C++, Go |
| **Dynamic Prog.** | [0/1 Knapsack](algorithms/dynamic-programming/zero-one-knapsack) | [Live Page](https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack) | Python, JS, Java, C++, Go |

---

### 2. Machine Learning & Reinforcement Learning
Direct live link: [https://mlhive.com/playground/machine-learning](https://mlhive.com/playground/machine-learning)

| Playground | Description | Live Visualizer Link | Code Available |
| :--- | :--- | :--- | :--- |
| [Linear Regression](machine-learning/linear-regression) | Gradient descent & analytical ordinary least squares | [Live Page](https://mlhive.com/playground/machine-learning/linear-regression) | Python, JS |
| [Polynomial Regression](machine-learning/polynomial-regression) | High-order curve fitting with L2 Ridge penalty | [Live Page](https://mlhive.com/playground/machine-learning/polynomial-regression) | Python |
| [K-Nearest Neighbors (KNN)](machine-learning/knn) | Distance-based majority vote classification | [Live Page](https://mlhive.com/playground/machine-learning/knn) | Python, JS |
| [Decision Tree](machine-learning/decision-tree) | Recursive Gini/Entropy information gain splits | [Live Page](https://mlhive.com/playground/machine-learning/decision-tree) | Python |
| [K-Means Clustering](machine-learning/kmeans) | Unsupervised Lloyd's algorithm with K-Means++ | [Live Page](https://mlhive.com/playground/machine-learning/kmeans) | Python, JS |
| [Support Vector Machine (SVM)](machine-learning/svm) | Maximum margin hyperplane with soft-margin hinge loss | [Live Page](https://mlhive.com/playground/machine-learning/svm) | Python |
| [Logistic Regression](machine-learning/logistic-regression) | Binary classification with sigmoid and cross-entropy | [Live Page](https://mlhive.com/playground/machine-learning/logistic-regression) | Python, JS |
| [Confusion Matrix](machine-learning/confusion-matrix) | TP/FP/TN/FN, Precision, Recall, Specificity, F1 | [Live Page](https://mlhive.com/playground/machine-learning/confusion-matrix) | Python, JS |
| [Embedding Projector](machine-learning/embedding-projector) | 2D PCA projection and cosine semantic search | [Live Page](https://mlhive.com/playground/machine-learning/embedding-projector) | Python |
| [Q-Learning Gridworld](machine-learning/q-learning) | Tabular TD learning with $\epsilon$-greedy exploration | [Live Page](https://mlhive.com/playground/machine-learning/q-learning) | Python |
| [Multi-Armed Bandits](machine-learning/reinforcement-learning/multi-armed-bandits) | Epsilon-Greedy, UCB1, and Thompson Sampling | [Live Page](https://mlhive.com/playground/machine-learning/reinforcement-learning/multi-armed-bandits) | Python |
| [Value & Policy Iteration](machine-learning/reinforcement-learning/value-policy-iteration) | Bellman optimality dynamic programming on MDPs | [Live Page](https://mlhive.com/playground/machine-learning/reinforcement-learning/value-policy-iteration) | Python |

---

### 3. Deep Learning
Direct live link: [https://mlhive.com/playground/deep-learning](https://mlhive.com/playground/deep-learning)

| Playground | Description | Live Visualizer Link | Code Available |
| :--- | :--- | :--- | :--- |
| [NN Forward Pass](deep-learning/neural-network-forward-pass) | Layer-by-layer matrix forward propagation trace | [Live Page](https://mlhive.com/playground/deep-learning/neural-network-forward-pass) | Python, JS |
| [Backpropagation](deep-learning/backpropagation) | Output and hidden error backpropagation via chain rule | [Live Page](https://mlhive.com/playground/deep-learning/backpropagation) | Python |
| [Activation Functions](deep-learning/activation-functions) | ReLU, LeakyReLU, Sigmoid, Tanh, GELU, Softmax | [Live Page](https://mlhive.com/playground/deep-learning/activation-functions) | Python |
| [CNN Operations](deep-learning/cnn-operations) | 2D Convolution, Stride, Padding, and Max Pooling | [Live Page](https://mlhive.com/playground/deep-learning/cnn-operations) | Python |
| [Dropout Layer](deep-learning/dropout-layer) | Inverted dropout scaling and Bernoulli mask | [Live Page](https://mlhive.com/playground/deep-learning/dropout-layer) | Python |
| [Normalization](deep-learning/normalization) | Batch Normalization vs Layer Normalization | [Live Page](https://mlhive.com/playground/deep-learning/normalization) | Python |
| [CNN Feature Map Explorer](deep-learning/cnn-feature-map-explorer) | Edge, blur, and sharpening filter responses | [Live Page](https://mlhive.com/playground/deep-learning/cnn-feature-map-explorer) | Python |
| [CNN Architecture Visualizer](deep-learning/cnn-visualizer) | End-to-end conv-pool-dense classification pipeline | [Live Page](https://mlhive.com/playground/deep-learning/cnn-visualizer) | Python |

---

### 4. Computer Vision
Direct live link: [https://mlhive.com/playground/computer-vision](https://mlhive.com/playground/computer-vision)

| Subgroup | Playground | Live Visualizer Link | Code Available |
| :--- | :--- | :--- | :--- |
| **OpenCV** | [Image Filters & Edge Detection](computer-vision/opencv/edge-detection) | [Live Page](https://mlhive.com/playground/computer-vision/opencv/edge-detection) | Python |
| **OpenCV** | [Contour & Shape Detection](computer-vision/opencv/contour-shape-detection) | [Live Page](https://mlhive.com/playground/computer-vision/opencv/contour-shape-detection) | Python |
| **OpenCV** | [Morphological Operations](computer-vision/opencv/morphological-operations) | [Live Page](https://mlhive.com/playground/computer-vision/opencv/morphological-operations) | Python |
| **OpenCV** | [Color Spaces & HSV Masking](computer-vision/opencv/color-spaces) | [Live Page](https://mlhive.com/playground/computer-vision/opencv/color-spaces) | Python |
| **MediaPipe** | [Hand Landmark Detection](computer-vision/mediapipe/hand-landmarks) | [Live Page](https://mlhive.com/playground/computer-vision/mediapipe/hand-landmarks) | Python |
| **MediaPipe** | [Face Detection](computer-vision/mediapipe/face-detection) | [Live Page](https://mlhive.com/playground/computer-vision/mediapipe/face-detection) | Python |
| **MediaPipe** | [Face Mesh (468 points)](computer-vision/mediapipe/face-mesh) | [Live Page](https://mlhive.com/playground/computer-vision/mediapipe/face-mesh) | Python |
| **MediaPipe** | [Pose Landmarks (33 points)](computer-vision/mediapipe/pose-landmarks) | [Live Page](https://mlhive.com/playground/computer-vision/mediapipe/pose-landmarks) | Python |
| **MediaPipe** | [Holistic Landmarker (543 points)](computer-vision/mediapipe/holistic-landmarker) | [Live Page](https://mlhive.com/playground/computer-vision/mediapipe/holistic-landmarker) | Python |
| **MediaPipe** | [Image Segmentation](computer-vision/mediapipe/image-segmentation) | [Live Page](https://mlhive.com/playground/computer-vision/mediapipe/image-segmentation) | Python |
| **MediaPipe** | [Object Detection](computer-vision/mediapipe/object-detection) | [Live Page](https://mlhive.com/playground/computer-vision/mediapipe/object-detection) | Python |
| **MediaPipe** | [Image Similarity & Visual Search](computer-vision/mediapipe/image-similarity) | [Live Page](https://mlhive.com/playground/computer-vision/mediapipe/image-similarity) | Python |
| **CV Algorithms** | [Non-Maximum Suppression (NMS)](computer-vision/algorithms/non-maximum-suppression) | [Live Page](https://mlhive.com/playground/computer-vision/algorithms/non-maximum-suppression) | Python, JS |
| **CV Algorithms** | [Detection Metrics & mAP](computer-vision/algorithms/detection-metrics) | [Live Page](https://mlhive.com/playground/computer-vision/algorithms/detection-metrics) | Python, JS |

---

### 5. Generative AI
Direct live link: [https://mlhive.com/playground/generative-ai](https://mlhive.com/playground/generative-ai)

| Playground | Description | Live Visualizer Link | Code Available |
| :--- | :--- | :--- | :--- |
| [LLM Inference Playground](generative-ai/llm-inference) | Temperature, Top-K, Top-P nucleus sampling and generation | [Live Page](https://mlhive.com/playground/generative-ai/llm-inference) | Python, JS |

---

## Setup & How to Run

### Python Setup

All examples are designed to run self-contained with standard library fallbacks, but full scientific libraries are recommended:

```bash
pip install -r requirements.txt
```

Run any example directly:
```bash
python deep-learning/neural-network-forward-pass/solution.py
python computer-vision/algorithms/non-maximum-suppression/solution.py
python algorithms/sorting/bubble-sort/solution.py
```

### JavaScript / Node.js Setup

```bash
node algorithms/sorting/bubble-sort/solution.js
node machine-learning/linear-regression/solution.js
node computer-vision/algorithms/detection-metrics/solution.js
```

---

## License & Attribution

These code examples are developed to accompany the interactive visualizers on [MLHive](https://mlhive.com).
