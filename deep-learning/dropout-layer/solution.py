"""
Inverted Dropout Layer Implementation
Reference: https://mlhive.com/playground/deep-learning/dropout-layer
"""

import random

# RUN CONFIGURATION & PARAMETERS
DROPOUT_RATE = 0.3
MODE = "train"  # "train" or "eval"
ACTIVATIONS = [1.5, 2.8, -0.4, 3.2, 0.9, 4.1, 1.8, 2.2]

def dropout(activations: list[float], p: float, mode: str = "train"):
    if mode != "train" or p == 0.0:
        return activations, [1] * len(activations)

    keep_prob = 1.0 - p
    scale = 1.0 / keep_prob
    mask = [1 if random.random() < keep_prob else 0 for _ in activations]
    output = [act * m * scale for act, m in zip(activations, mask)]
    return output, mask

def main():
    random.seed(42)
    print("--- Inverted Dropout Layer ---")
    print(f"Mode: {MODE}, Dropout Rate p = {DROPOUT_RATE}")
    print(f"Input Activations:  {ACTIVATIONS}\n")

    out, mask = dropout(ACTIVATIONS, DROPOUT_RATE, MODE)

    dropped = mask.count(0)
    print(f"Binary Mask:        {mask}")
    print(f"Dropped Neurons:    {dropped} / {len(ACTIVATIONS)} ({dropped / len(ACTIVATIONS) * 100:.1f}%)")
    print(f"Scaled Activations: {[round(x, 4) for x in out]}")

if __name__ == "__main__":
    main()
