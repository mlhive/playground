"""
Support Vector Machine (Linear & RBF with Soft Margin)
Reference: https://mlhive.com/playground/machine-learning/svm
"""

import math

# RUN CONFIGURATION & PARAMETERS
C = 1.0
KERNEL = "linear"  # "linear" or "rbf"
GAMMA = 0.5
LEARNING_RATE = 0.001
EPOCHS = 300
PRESET = "separable"
VERBOSE = True

DATASETS = {
    "separable": [
        (1.0, 2.0, 1), (2.0, 3.0, 1), (1.5, 3.5, 1), (2.5, 4.0, 1),
        (4.0, 1.0, -1), (4.5, 2.0, -1), (5.0, 1.5, -1), (5.5, 2.5, -1)
    ]
}

def train_linear_svm(points: list[tuple[float, float, int]], lr: float, epochs: int, c_param: float):
    w = [0.0, 0.0]
    b = 0.0
    n = len(points)

    for epoch in range(1, epochs + 1):
        for x1, x2, y in points:
            margin = y * (w[0] * x1 + w[1] * x2 + b)
            if margin >= 1.0:
                # Correct and beyond margin: only regularization gradient
                w[0] -= lr * (w[0] / n)
                w[1] -= lr * (w[1] / n)
            else:
                # Margin violation / hinge loss
                w[0] -= lr * (w[0] / n - c_param * y * x1)
                w[1] -= lr * (w[1] / n - c_param * y * x2)
                b -= lr * (-c_param * y)

        if VERBOSE and (epoch % 60 == 0 or epoch == 1 or epoch == epochs):
            norm_w = math.sqrt(w[0]**2 + w[1]**2)
            margin_width = 2.0 / norm_w if norm_w > 0 else 0
            print(f"Epoch {epoch:03d} | w: [{w[0]:.3f}, {w[1]:.3f}], b: {b:.3f} | Margin Width: {margin_width:.3f}")

    return w, b

def main():
    points = DATASETS.get(PRESET, DATASETS["separable"])
    print(f"--- Support Vector Machine (C = {C}) ---")
    print(f"Dataset Preset: {PRESET} ({len(points)} samples)\n")

    w, b = train_linear_svm(points, LEARNING_RATE, EPOCHS, C)
    print(f"\nHyperplane Equation: {w[0]:.4f} * x1 + {w[1]:.4f} * x2 + {b:.4f} = 0")
    print(f"Geometric Margin 2/||w||: {2.0 / math.sqrt(w[0]**2 + w[1]**2):.4f}")

if __name__ == "__main__":
    main()
