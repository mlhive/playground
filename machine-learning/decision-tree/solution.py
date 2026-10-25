"""
Decision Tree Classifier (Pure Python Implementation)
Reference: https://mlhive.com/playground/machine-learning/decision-tree
"""

import math
from collections import Counter

# RUN CONFIGURATION & PARAMETERS
MAX_DEPTH = 3
CRITERION = "gini"  # "gini" or "entropy"
MIN_SAMPLES_SPLIT = 2
PRESET = "checkerboard"
VERBOSE = True

DATASETS = {
    "checkerboard": [
        (1.0, 1.0, 0), (1.5, 1.2, 0), (1.2, 1.8, 0),
        (3.0, 1.0, 1), (3.5, 1.2, 1), (3.2, 1.8, 1),
        (1.0, 3.0, 1), (1.5, 3.2, 1), (1.2, 3.8, 1),
        (3.0, 3.0, 0), (3.5, 3.2, 0), (3.2, 3.8, 0),
    ],
    "linear_split": [
        (1.0, 2.0, 0), (1.5, 1.8, 0), (2.0, 1.2, 0), (2.2, 2.5, 0),
        (3.5, 4.0, 1), (4.0, 3.5, 1), (4.5, 4.2, 1), (5.0, 3.8, 1)
    ]
}

def impurity(labels: list[int], criterion: str) -> float:
    if not labels:
        return 0.0
    total = len(labels)
    counts = Counter(labels)
    if criterion == "entropy":
        return -sum((c / total) * math.log2(c / total) for c in counts.values())
    # Gini
    return 1.0 - sum((c / total) ** 2 for c in counts.values())

class Node:
    def __init__(self, depth=0):
        self.depth = depth
        self.feature = None
        self.threshold = None
        self.left = None
        self.right = None
        self.prediction = None

def build_tree(data: list[tuple[float, float, int]], depth: int = 0) -> Node:
    labels = [p[2] for p in data]
    node = Node(depth)

    # Base cases
    if len(set(labels)) == 1 or depth >= MAX_DEPTH or len(data) < MIN_SAMPLES_SPLIT:
        node.prediction = Counter(labels).most_common(1)[0][0]
        return node

    current_impurity = impurity(labels, CRITERION)
    best_gain = -1.0
    best_split = None

    for feature_idx in (0, 1):
        values = sorted(set(p[feature_idx] for p in data))
        thresholds = [(values[i] + values[i + 1]) / 2.0 for i in range(len(values) - 1)]

        for thr in thresholds:
            left = [p for p in data if p[feature_idx] <= thr]
            right = [p for p in data if p[feature_idx] > thr]

            if not left or not right:
                continue

            p_l = len(left) / len(data)
            p_r = len(right) / len(data)
            gain = current_impurity - (p_l * impurity([p[2] for p in left], CRITERION) +
                                       p_r * impurity([p[2] for p in right], CRITERION))

            if gain > best_gain:
                best_gain = gain
                best_split = (feature_idx, thr, left, right)

    if not best_split or best_gain <= 0.0:
        node.prediction = Counter(labels).most_common(1)[0][0]
        return node

    f_idx, thr, left_data, right_data = best_split
    node.feature = f_idx
    node.threshold = thr
    node.left = build_tree(left_data, depth + 1)
    node.right = build_tree(right_data, depth + 1)
    return node

def print_tree(node: Node, indent=""):
    if node.prediction is not None:
        print(f"{indent}└── Predict Class: {node.prediction}")
    else:
        feat_name = "X" if node.feature == 0 else "Y"
        print(f"{indent}├── [{feat_name} <= {node.threshold:.2f}]")
        print_tree(node.left, indent + "│   ")
        print(f"{indent}└── [{feat_name} > {node.threshold:.2f}]")
        print_tree(node.right, indent + "    ")

def main():
    data = DATASETS.get(PRESET, DATASETS["checkerboard"])
    print(f"--- Decision Tree Classifier ---")
    print(f"Preset: {PRESET} ({len(data)} samples)")
    print(f"Max Depth: {MAX_DEPTH}, Criterion: {CRITERION}\n")

    root = build_tree(data)
    print("Decision Tree Hierarchy:")
    print_tree(root)

if __name__ == "__main__":
    main()
