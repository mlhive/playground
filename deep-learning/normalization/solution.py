"""
Batch Normalization and Layer Normalization
Reference: https://mlhive.com/playground/deep-learning/normalization
"""

import math

# RUN CONFIGURATION & PARAMETERS
NORM_TYPE = "batch_norm"  # "batch_norm" or "layer_norm"
EPSILON = 1e-5
GAMMA = 1.0
BETA = 0.0

# Batch of 4 samples, 3 features each
BATCH_DATA = [
    [2.0, 1.0, 6.0],
    [3.0, 0.0, 4.0],
    [5.0, 2.0, 5.0],
    [7.0, 3.0, 2.0],
]

def batch_norm(batch: list[list[float]], eps: float, gamma: float, beta: float):
    n_samples = len(batch)
    n_features = len(batch[0])
    
    # Compute mean and variance along feature columns (axis 0)
    means = [sum(batch[i][j] for i in range(n_samples)) / n_samples for j in range(n_features)]
    vars_ = [
        sum((batch[i][j] - means[j]) ** 2 for i in range(n_samples)) / n_samples
        for j in range(n_features)
    ]

    normalized = []
    for i in range(n_samples):
        row = [
            gamma * ((batch[i][j] - means[j]) / math.sqrt(vars_[j] + eps)) + beta
            for j in range(n_features)
        ]
        normalized.append(row)
    return normalized, means, vars_

def layer_norm(batch: list[list[float]], eps: float, gamma: float, beta: float):
    n_features = len(batch[0])
    normalized = []

    for row in batch:
        mean = sum(row) / n_features
        var = sum((x - mean) ** 2 for x in row) / n_features
        norm_row = [gamma * ((x - mean) / math.sqrt(var + eps)) + beta for x in row]
        normalized.append(norm_row)
    return normalized

def main():
    print(f"--- Normalization Visualizer ({NORM_TYPE.replace('_', ' ').title()}) ---")
    print(f"Batch Size: {len(BATCH_DATA)}, Features: {len(BATCH_DATA[0])}")
    print(f"Gamma: {GAMMA}, Beta: {BETA}, Epsilon: {EPSILON}\n")

    if NORM_TYPE == "batch_norm":
        out, means, vars_ = batch_norm(BATCH_DATA, EPSILON, GAMMA, BETA)
        print("Column Means:    ", [round(m, 3) for m in means])
        print("Column Variances:", [round(v, 3) for v in vars_])
    else:
        out = layer_norm(BATCH_DATA, EPSILON, GAMMA, BETA)

    print("\nNormalized Matrix:")
    for row in out:
        print("  " + "  ".join(f"{x:+6.3f}" for x in row))

if __name__ == "__main__":
    main()
