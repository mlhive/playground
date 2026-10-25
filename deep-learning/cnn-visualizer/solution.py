"""
End-to-End CNN Pipeline & Tensor Shape Tracking
Reference: https://mlhive.com/playground/deep-learning/cnn-visualizer
"""

INPUT_SHAPE = (32, 32, 3) # Height, Width, Channels
NUM_CLASSES = 10

CNN_PIPELINE = [
    {"name": "Input Layer", "out_shape": (32, 32, 3), "params": 0},
    {"name": "Conv2D (16 @ 3x3)", "out_shape": (30, 30, 16), "params": (3*3*3 + 1) * 16},
    {"name": "ReLU Activation", "out_shape": (30, 30, 16), "params": 0},
    {"name": "MaxPool2D (2x2)", "out_shape": (15, 15, 16), "params": 0},
    {"name": "Conv2D (32 @ 3x3)", "out_shape": (13, 13, 32), "params": (3*3*16 + 1) * 32},
    {"name": "ReLU Activation", "out_shape": (13, 13, 32), "params": 0},
    {"name": "MaxPool2D (2x2)", "out_shape": (6, 6, 32), "params": 0},
    {"name": "Flatten", "out_shape": (6 * 6 * 32,), "params": 0},
    {"name": "Dense Output (10)", "out_shape": (NUM_CLASSES,), "params": (1152 + 1) * NUM_CLASSES},
    {"name": "Softmax", "out_shape": (NUM_CLASSES,), "params": 0},
]

def main():
    print("--- CNN Architecture Visualizer ---")
    print(f"Input Image Tensor: {INPUT_SHAPE}\n")
    print(f"{'Layer':26s} | {'Output Shape':16s} | Param Count")
    print("-" * 58)

    total_params = 0
    for stage in CNN_PIPELINE:
        name = stage["name"]
        shape_str = str(stage["out_shape"])
        params = stage["params"]
        total_params += params
        print(f"{name:26s} | {shape_str:16s} | {params:8d}")

    print("-" * 58)
    print(f"Total Trainable Parameters: {total_params:,}")

if __name__ == "__main__":
    main()
