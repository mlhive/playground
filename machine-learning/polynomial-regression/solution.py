"""
Polynomial Regression Implementation
Reference: https://mlhive.com/playground/machine-learning/polynomial-regression
"""

import math

# RUN CONFIGURATION & PARAMETERS
DEGREE = 3
LEARNING_RATE = 0.05
EPOCHS = 200
L2_LAMBDA = 0.001
PRESET = "cubic_curve"  # "cubic_curve", "quadratic", "sine_wave"
VERBOSE = True

DATASETS = {
    "cubic_curve": [
        (-2.0, -5.8), (-1.5, -2.1), (-1.0, 0.4), (-0.5, 1.2), (0.0, 0.8),
        (0.5, 0.5), (1.0, 1.9), (1.5, 4.8), (2.0, 9.2)
    ],
    "quadratic": [
        (-2.0, 4.2), (-1.5, 2.3), (-1.0, 1.1), (-0.5, 0.2), (0.0, 0.1),
        (0.5, 0.3), (1.0, 1.2), (1.5, 2.1), (2.0, 3.9)
    ],
    "sine_wave": [
        (-3.0, -0.2), (-2.0, -0.9), (-1.0, -0.8), (0.0, 0.0),
        (1.0, 0.8), (2.0, 0.9), (3.0, 0.1)
    ]
}

def poly_features(x: float, degree: int) -> list[float]:
    return [x ** p for p in range(1, degree + 1)]

def train_poly_regression(points: list[tuple[float, float]], degree: int, lr: float, epochs: int, l2: float):
    X_raw = [p[0] for p in points]
    y = [p[1] for p in points]
    n = len(points)

    # Feature scaling: mean and std for each power
    X_feats = [poly_features(x, degree) for x in X_raw]
    means = [sum(X_feats[i][p] for i in range(n)) / n for p in range(degree)]
    stds = [
        math.sqrt(sum((X_feats[i][p] - means[p]) ** 2 for i in range(n)) / n) or 1.0
        for p in range(degree)
    ]
    X_norm = [
        [(X_feats[i][p] - means[p]) / stds[p] for p in range(degree)]
        for i in range(n)
    ]

    weights = [0.0] * degree
    bias = sum(y) / n

    for epoch in range(1, epochs + 1):
        dw = [0.0] * degree
        db = 0.0
        loss = 0.0

        for i in range(n):
            pred = bias + sum(weights[p] * X_norm[i][p] for p in range(degree))
            err = pred - y[i]
            loss += err ** 2
            db += (2.0 / n) * err
            for p in range(degree):
                dw[p] += (2.0 / n) * err * X_norm[i][p]

        # Apply L2 regularized weight updates
        bias -= lr * db
        for p in range(degree):
            weights[p] -= lr * (dw[p] + 2 * l2 * weights[p])

        mse = loss / n
        if VERBOSE and (epoch % 40 == 0 or epoch == 1 or epoch == epochs):
            print(f"Epoch {epoch:03d} | Loss (MSE): {mse:.4f} | Weights norm: {math.sqrt(sum(w**2 for w in weights)):.4f}")

    return weights, bias, means, stds

def main():
    points = DATASETS.get(PRESET, DATASETS["cubic_curve"])
    print(f"--- Polynomial Regression (Degree = {DEGREE}) ---")
    print(f"Dataset Preset: {PRESET} ({len(points)} samples)")
    print(f"Learning Rate: {LEARNING_RATE}, Epochs: {EPOCHS}, L2: {L2_LAMBDA}\n")

    weights, bias, means, stds = train_poly_regression(points, DEGREE, LEARNING_RATE, EPOCHS, L2_LAMBDA)
    print(f"\nTrained Normalized Bias: {bias:.4f}")
    for p, w in enumerate(weights, 1):
        print(f"  Feature x^{p} weight: {w:.4f}")

if __name__ == "__main__":
    main()
