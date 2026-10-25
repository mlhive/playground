"""
Linear Regression Implementation (Gradient Descent & Analytical OLS)
Reference: https://mlhive.com/playground/machine-learning/linear-regression
"""

import math

# ==========================================
# RUN CONFIGURATION & PARAMETERS
# ==========================================
LEARNING_RATE = 0.01
EPOCHS = 100
PRESET = "linear_trend"  # "linear_trend", "steep_slope", "noisy_scatter", "custom"
INITIAL_W = 0.0
INITIAL_B = 0.0
VERBOSE = True

DATASETS = {
    "linear_trend": [
        (1.0, 2.5), (2.0, 3.8), (3.0, 5.2), (4.0, 6.9), (5.0, 8.1),
        (6.0, 9.8), (7.0, 11.2), (8.0, 12.9), (9.0, 14.5), (10.0, 16.2)
    ],
    "steep_slope": [
        (1.0, 4.2), (2.0, 8.5), (3.0, 13.1), (4.0, 17.0), (5.0, 21.8),
        (6.0, 26.2), (7.0, 30.5), (8.0, 34.9), (9.0, 39.1), (10.0, 44.0)
    ],
    "noisy_scatter": [
        (1.0, 3.2), (2.0, 2.8), (3.0, 6.1), (4.0, 5.5), (5.0, 7.8),
        (6.0, 7.2), (7.0, 10.5), (8.0, 9.8), (9.0, 13.1), (10.0, 12.4)
    ],
    "custom": [
        (1.0, 1.0), (2.0, 3.0), (3.0, 2.0), (4.0, 5.0), (5.0, 4.0)
    ]
}

def compute_mse(X: list[float], y: list[float], w: float, b: float) -> float:
    n = len(X)
    return sum((w * xi + b - yi) ** 2 for xi, yi in zip(X, y)) / n

def train_linear_regression(points: list[tuple[float, float]], lr: float, epochs: int, verbose: bool = True):
    X = [p[0] for p in points]
    y = [p[1] for p in points]
    n = len(points)
    
    w = INITIAL_W
    b = INITIAL_B
    history = []
    
    for epoch in range(1, epochs + 1):
        # Forward pass: predictions
        y_pred = [w * xi + b for xi in X]
        errors = [yp - yi for yp, yi in zip(y_pred, y)]
        
        # Gradients
        dw = (2.0 / n) * sum(err * xi for err, xi in zip(errors, X))
        db = (2.0 / n) * sum(errors)
        
        # Updates
        w -= lr * dw
        b -= lr * db
        
        loss = compute_mse(X, y, w, b)
        history.append(loss)
        
        if verbose and (epoch % 10 == 0 or epoch == 1 or epoch == epochs):
            print(f"Epoch {epoch:03d} | Loss (MSE): {loss:.4f} | w: {w:.4f}, b: {b:.4f}")
            
    return w, b, history

def analytical_ols(points: list[tuple[float, float]]) -> tuple[float, float]:
    X = [p[0] for p in points]
    y = [p[1] for p in points]
    n = len(points)
    mean_x = sum(X) / n
    mean_y = sum(y) / n
    
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(X, y))
    denominator = sum((xi - mean_x) ** 2 for xi in X)
    
    w_ols = numerator / denominator
    b_ols = mean_y - w_ols * mean_x
    return w_ols, b_ols

def main():
    points = DATASETS.get(PRESET, DATASETS["linear_trend"])
    print(f"--- Linear Regression Demonstration ---")
    print(f"Dataset Preset: {PRESET} ({len(points)} samples)")
    print(f"Learning Rate: {LEARNING_RATE}, Epochs: {EPOCHS}\n")
    
    w, b, history = train_linear_regression(points, LEARNING_RATE, EPOCHS, verbose=VERBOSE)
    w_ols, b_ols = analytical_ols(points)
    
    print(f"\n--- Trained Model Equation ---")
    print(f"Gradient Descent: y = {w:.4f} * x + {b:.4f}")
    print(f"Analytical OLS:   y = {w_ols:.4f} * x + {b_ols:.4f}")
    print(f"Initial Loss: {history[0]:.4f} -> Final Loss: {history[-1]:.4f}")

if __name__ == "__main__":
    main()
