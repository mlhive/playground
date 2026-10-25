"""
Neural Network Forward Pass (Pure Python & NumPy-free)
Reference: https://mlhive.com/playground/deep-learning/neural-network-forward-pass
"""

import math

# RUN CONFIGURATION & PARAMETERS
LAYER_SIZES = [3, 4, 2, 1]
ACTIVATION = "relu"  # "relu", "sigmoid", "tanh", "linear"
WEIGHT_PRESET = "he" # "he", "xavier", "small"
INPUT_VALUES = [0.75, -0.3, 0.5]
VERBOSE = True

def activate(z: float, act_fn: str) -> float:
    if act_fn == "sigmoid":
        return 1.0 / (1.0 + math.exp(-max(min(z, 20.0), -20.0)))
    if act_fn == "tanh":
        return math.tanh(z)
    if act_fn == "linear":
        return z
    # ReLU
    return max(0.0, z)

def init_weights(fan_in: int, fan_out: int, preset: str):
    if preset == "he":
        scale = math.sqrt(2.0 / fan_in)
    elif preset == "small":
        scale = 0.25
    else:  # xavier
        scale = math.sqrt(2.0 / (fan_in + fan_out))
    
    # Deterministic pseudo-weights matching playground
    W = []
    for j in range(fan_out):
        row = []
        for i in range(fan_in):
            raw = math.sin((j + 1) * 1.5 + (i + 1) * 2.3)
            row.append(round(raw * scale, 4))
        W.append(row)
    b = [round(math.cos((j + 1) * 0.7) * 0.1, 4) for j in range(fan_out)]
    return W, b

def forward_pass(inputs: list[float], layers: list[int], act_fn: str):
    a = inputs[:]
    trace = [("Layer 0 (Input)", a)]

    for l_idx in range(len(layers) - 1):
        fan_in = layers[l_idx]
        fan_out = layers[l_idx + 1]
        is_output_layer = (l_idx == len(layers) - 2)
        layer_act = "sigmoid" if is_output_layer else act_fn

        W, b = init_weights(fan_in, fan_out, WEIGHT_PRESET)

        z_next = []
        a_next = []
        for j in range(fan_out):
            # z_j = sum(W_ji * a_i) + b_j
            z_j = sum(W[j][i] * a[i] for i in range(fan_in)) + b[j]
            a_j = activate(z_j, layer_act)
            z_next.append(z_j)
            a_next.append(a_j)

        layer_name = f"Layer {l_idx + 1} ({'Output' if is_output_layer else 'Hidden'})"
        trace.append((layer_name, a_next))
        a = a_next

    return a, trace

def main():
    print("--- Neural Network Forward Pass Visualizer ---")
    print(f"Architecture: {' -> '.join(str(s) for s in LAYER_SIZES)}")
    print(f"Hidden Activation: {ACTIVATION}, Init: {WEIGHT_PRESET}")
    print(f"Inputs: {INPUT_VALUES}\n")

    output, trace = forward_pass(INPUT_VALUES, LAYER_SIZES, ACTIVATION)

    for name, activations in trace:
        formatted = ", ".join(f"{v:+.4f}" for v in activations)
        print(f"{name:20s} | Activations: [{formatted}]")

    print(f"\nFinal Network Output Prediction: {output[0]:.4f}")

if __name__ == "__main__":
    main()
