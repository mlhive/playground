"""
Backpropagation & Gradient Descent (2-Layer Neural Network)
Reference: https://mlhive.com/playground/deep-learning/backpropagation
"""

import math
import random

# RUN CONFIGURATION & PARAMETERS
LEARNING_RATE = 0.2
EPOCHS = 80
PRESET = "xor"
VERBOSE = True

DATASETS = {
    "xor": [
        ([0.0, 0.0], 0.0),
        ([0.0, 1.0], 1.0),
        ([1.0, 0.0], 1.0),
        ([1.0, 1.0], 0.0),
    ]
}

def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(min(z, 20.0), -20.0)))

def d_sigmoid(a: float) -> float:
    return a * (1.0 - a)

def train_mlp():
    random.seed(42)
    # Architecture: 2 -> 3 -> 1
    # Hidden weights (3 neurons, 2 inputs each)
    W1 = [[random.uniform(-0.5, 0.5) for _ in range(2)] for _ in range(3)]
    b1 = [0.0] * 3
    # Output weights (1 neuron, 3 hidden inputs)
    W2 = [[random.uniform(-0.5, 0.5) for _ in range(3)]]
    b2 = [0.0]

    dataset = DATASETS[PRESET]

    for epoch in range(1, EPOCHS + 1):
        total_loss = 0.0

        for x, target in dataset:
            # 1. Forward Pass
            # Hidden layer
            z1 = [sum(W1[j][i] * x[i] for i in range(2)) + b1[j] for j in range(3)]
            a1 = [sigmoid(z) for z in z1]

            # Output layer
            z2 = sum(W2[0][j] * a1[j] for j in range(3)) + b2[0]
            pred = sigmoid(z2)

            loss = (pred - target) ** 2
            total_loss += loss

            # 2. Backward Pass
            # Output gradient
            delta2 = 2.0 * (pred - target) * d_sigmoid(pred)

            # Hidden gradients
            delta1 = [
                (W2[0][j] * delta2) * d_sigmoid(a1[j])
                for j in range(3)
            ]

            # 3. Parameter Updates
            for j in range(3):
                W2[0][j] -= LEARNING_RATE * delta2 * a1[j]
            b2[0] -= LEARNING_RATE * delta2

            for j in range(3):
                for i in range(2):
                    W1[j][i] -= LEARNING_RATE * delta1[j] * x[i]
                b1[j] -= LEARNING_RATE * delta1[j]

        mse = total_loss / len(dataset)
        if VERBOSE and (epoch % 15 == 0 or epoch == 1 or epoch == EPOCHS):
            print(f"Epoch {epoch:03d} | MSE Loss: {mse:.4f}")

    return W1, b1, W2, b2

def main():
    print(f"--- Backpropagation MLP Visualizer ---")
    print(f"Problem: {PRESET.upper()}, Architecture: 2 -> 3 -> 1")
    print(f"Learning Rate: {LEARNING_RATE}, Epochs: {EPOCHS}\n")

    W1, b1, W2, b2 = train_mlp()

    print("\nFinal Predictions on Dataset:")
    for x, target in DATASETS[PRESET]:
        z1 = [sum(W1[j][i] * x[i] for i in range(2)) + b1[j] for j in range(3)]
        a1 = [sigmoid(z) for z in z1]
        z2 = sum(W2[0][j] * a1[j] for j in range(3)) + b2[0]
        pred = sigmoid(z2)
        print(f"  Input: {x} | Target: {target:.0f} | Prediction: {pred:.4f} (Round: {round(pred)})")

if __name__ == "__main__":
    main()
