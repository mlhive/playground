"""
CNN Operations: 2D Convolution, Stride, Padding & Max/Avg Pooling
Reference: https://mlhive.com/playground/deep-learning/cnn-operations
"""

# RUN CONFIGURATION & PARAMETERS
STRIDE = 1
PADDING = 0
POOL_SIZE = 2
VERBOSE = True

# 5x5 Input Feature Map
INPUT_MAP = [
    [1, 2, 0, 1, 3],
    [0, 3, 2, 4, 1],
    [2, 1, 4, 2, 0],
    [3, 0, 1, 5, 2],
    [1, 2, 3, 0, 4]
]

# 3x3 Vertical Edge Filter
KERNEL = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

def pad_matrix(mat: list[list[int]], pad: int) -> list[list[int]]:
    if pad == 0:
        return mat
    rows, cols = len(mat), len(mat[0])
    padded = [[0] * (cols + 2 * pad) for _ in range(rows + 2 * pad)]
    for r in range(rows):
        for c in range(cols):
            padded[r + pad][c + pad] = mat[r][c]
    return padded

def conv2d(mat: list[list[int]], kernel: list[list[int]], stride: int, padding: int):
    padded = pad_matrix(mat, padding)
    h_in, w_in = len(padded), len(padded[0])
    k_h, k_w = len(kernel), len(kernel[0])
    
    out_h = (h_in - k_h) // stride + 1
    out_w = (w_in - k_w) // stride + 1
    output = []

    for r in range(0, out_h * stride, stride):
        row = []
        for c in range(0, out_w * stride, stride):
            val = sum(padded[r + kr][c + kc] * kernel[kr][kc] for kr in range(k_h) for kc in range(k_w))
            row.append(val)
        output.append(row)
    return output

def max_pool2d(mat: list[list[int]], pool_size: int):
    rows, cols = len(mat), len(mat[0])
    out_h = rows // pool_size
    out_w = cols // pool_size
    output = []

    for r in range(out_h):
        row = []
        for c in range(out_w):
            sub = [
                mat[r * pool_size + kr][c * pool_size + kc]
                for kr in range(pool_size)
                for kc in range(pool_size)
            ]
            row.append(max(sub))
        output.append(row)
    return output

def main():
    print("--- CNN Operations: Convolution & Pooling ---")
    print(f"Input Feature Map Size: {len(INPUT_MAP)}x{len(INPUT_MAP[0])}")
    print(f"Kernel Size: {len(KERNEL)}x{len(KERNEL[0])}, Stride: {STRIDE}, Padding: {PADDING}\n")

    conv_out = conv2d(INPUT_MAP, KERNEL, STRIDE, PADDING)
    print(f"Convolution Output ({len(conv_out)}x{len(conv_out[0])}):")
    for row in conv_out:
        print("  " + " ".join(f"{v:3d}" for v in row))

    pool_out = max_pool2d(conv_out, POOL_SIZE)
    print(f"\nMax Pooling 2x2 Output ({len(pool_out)}x{len(pool_out[0])}):")
    for row in pool_out:
        print("  " + " ".join(f"{v:3d}" for v in row))

if __name__ == "__main__":
    main()
