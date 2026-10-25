"""
Logistic Regression Binary Classifier
Reference: https://mlhive.com/playground/machine-learning/logistic-regression
"""

import math

# RUN CONFIGURATION & PARAMETERS
LEARNING_RATE = 0.1
EPOCHS = 200
THRESHOLD = 0.5
PRESET = "study_hours"
VERBOSE = True

DATASETS = {
    # (study_hours, pass_fail)
    "study_hours": [
        (0.5, 0), (1.0, 0), (1.5, 0), (2.0, 0), (2.5, 0),
        (3.0, 0), (3.5, 1), (4.0, 1), (4.5, 1), (5.0, 1),
        (5.5, 1), (6.0, 1)
    ]
}

def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(min(z, 20.0), -20.0)))

def train_logistic(data: list[tuple[float, int]], lr: float, epochs: int):
    X = [p[0] for p in data]
    y = [p[1] for p in data]
    n = len(data)

    w = 0.0
    b = 0.0

    for epoch in range(1, epochs + 1):
        dw = 0.0
        db = 0.0
        loss = 0.0

        for xi, yi in zip(X, y):
            pred = sigmoid(w * xi + b)
            # Binary Cross Entropy
            loss += - (yi * math.log(max(pred, 1e-12)) + (1 - yi) * math.log(max(1.0 - pred, 1e-12)))
            err = pred - yi
            dw += (1.0 / n) * err * xi
            db += (1.0 / n) * err

        w -= lr * dw
        b -= lr * db

        if VERBOSE and (epoch % 40 == 0 or epoch == 1 or epoch == epochs):
            print(f"Epoch {epoch:03d} | Log Loss: {loss/n:.4f} | w: {w:.4f}, b: {b:.4f}")

    return w, b

def main():
    data = DATASETS.get(PRESET, DATASETS["study_hours"])
    print(f"--- Logistic Regression ---")
    print(f"Preset: {PRESET} ({len(data)} samples)")
    print(f"Learning Rate: {LEARNING_RATE}, Threshold: {THRESHOLD}\n")

    w, b = train_logistic(data, LEARNING_RATE, EPOCHS)

    print(f"\nTrained Sigmoid Model: P(y=1) = sigmoid({w:.4f} * x + {b:.4f})")
    print(f"Decision Boundary (P=0.5): x = {-b / w:.2f}")

    print("\nSample Predictions:")
    for test_x in [1.0, 3.0, 3.5, 5.0]:
        p = sigmoid(w * test_x + b)
        cls = 1 if p >= THRESHOLD else 0
        print(f"  Study {test_x:3.1f} hrs -> Probability = {p:.4f} -> Class {cls}")

if __name__ == "__main__":
    main()
