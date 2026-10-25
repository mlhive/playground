"""
Neural Network Activation Functions & Derivatives
Reference: https://mlhive.com/playground/deep-learning/activation-functions
"""

import math

# Sample test inputs
TEST_VALUES = [-3.0, -1.0, 0.0, 1.0, 3.0]

def relu(x: float) -> float:
    return max(0.0, x)

def d_relu(x: float) -> float:
    return 1.0 if x > 0 else 0.0

def leaky_relu(x: float, alpha: float = 0.01) -> float:
    return x if x > 0 else alpha * x

def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(min(x, 20.0), -20.0)))

def d_sigmoid(x: float) -> float:
    s = sigmoid(x)
    return s * (1.0 - s)

def tanh(x: float) -> float:
    return math.tanh(x)

def d_tanh(x: float) -> float:
    t = math.tanh(x)
    return 1.0 - t ** 2

def gelu(x: float) -> float:
    return 0.5 * x * (1.0 + math.tanh(math.sqrt(2.0 / math.pi) * (x + 0.044715 * (x ** 3))))

def softmax(logits: list[float]) -> list[float]:
    shift = max(logits)  # numerical stability
    exps = [math.exp(z - shift) for z in logits]
    sum_exps = sum(exps)
    return [e / sum_exps for e in exps]

def main():
    print("--- Activation Functions Comparison ---")
    print(f"{'Input':8s} | {'ReLU':8s} | {'Sigmoid':8s} | {'Tanh':8s} | {'GELU':8s}")
    print("-" * 52)
    for x in TEST_VALUES:
        print(f"{x:+8.2f} | {relu(x):8.4f} | {sigmoid(x):8.4f} | {tanh(x):+8.4f} | {gelu(x):+8.4f}")

    logits = [2.0, 1.0, 0.1]
    probs = softmax(logits)
    print(f"\nSoftmax on Logits {logits} -> Probabilities: {[round(p, 4) for p in probs]}")

if __name__ == "__main__":
    main()
