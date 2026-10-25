"""
OpenCV Morphological Operations (Erosion, Dilation, Opening, Closing)
Reference: https://mlhive.com/playground/computer-vision/opencv/morphological-operations
"""

# RUN CONFIGURATION & PARAMETERS
OPERATION = "open"  # "open", "close", "dilate", "erode", "gradient"
KERNEL_SHAPE = "rectangle"  # "rectangle", "cross", "ellipse"
KERNEL_SIZE = 5
ITERATIONS = 1
IMAGE_URL = "https://mlhive.com/playground/opencv/morphological-operations/holes.svg"

def make_kernel(size: int, shape: str):
    kernel = [[1] * size for _ in range(size)]
    if shape == "cross":
        mid = size // 2
        for r in range(size):
            for c in range(size):
                kernel[r][c] = 1 if (r == mid or c == mid) else 0
    return kernel

def erode_binary(mat: list[list[int]], kernel: list[list[int]]) -> list[list[int]]:
    h, w = len(mat), len(mat[0])
    k_size = len(kernel)
    pad = k_size // 2
    out = [[0] * w for _ in range(h)]

    for r in range(pad, h - pad):
        for c in range(pad, w - pad):
            match = True
            for kr in range(k_size):
                for kc in range(k_size):
                    if kernel[kr][kc] == 1 and mat[r - pad + kr][c - pad + kc] == 0:
                        match = False
                        break
                if not match:
                    break
            out[r][c] = 1 if match else 0
    return out

def dilate_binary(mat: list[list[int]], kernel: list[list[int]]) -> list[list[int]]:
    h, w = len(mat), len(mat[0])
    k_size = len(kernel)
    pad = k_size // 2
    out = [[0] * w for _ in range(h)]

    for r in range(pad, h - pad):
        for c in range(pad, w - pad):
            hit = False
            for kr in range(k_size):
                for kc in range(k_size):
                    if kernel[kr][kc] == 1 and mat[r - pad + kr][c - pad + kc] == 1:
                        hit = True
                        break
                if hit:
                    break
            out[r][c] = 1 if hit else 0
    return out

def apply_morphology(mat: list[list[int]], op: str, kernel: list[list[int]]):
    if op == "erode":
        return erode_binary(mat, kernel)
    elif op == "dilate":
        return dilate_binary(mat, kernel)
    elif op == "open":
        # Erosion followed by Dilation
        return dilate_binary(erode_binary(mat, kernel), kernel)
    elif op == "close":
        # Dilation followed by Erosion
        return erode_binary(dilate_binary(mat, kernel), kernel)
    elif op == "gradient":
        dil = dilate_binary(mat, kernel)
        ero = erode_binary(mat, kernel)
        h, w = len(mat), len(mat[0])
        return [[dil[r][c] - ero[r][c] for c in range(w)] for r in range(h)]
    return mat

def main():
    print(f"--- Morphological Operations Visualizer ---")
    print(f"Operation: {OPERATION.upper()}, Kernel: {KERNEL_SHAPE} ({KERNEL_SIZE}x{KERNEL_SIZE})")
    print(f"Sample asset: {IMAGE_URL}\n")

    # 10x10 binary grid with a shape + noise speckles
    grid = [[0] * 10 for _ in range(10)]
    for r in range(3, 8):
        for c in range(3, 8):
            grid[r][c] = 1
    # Noise speckle
    grid[1][1] = 1
    # Small hole inside
    grid[5][5] = 0

    kernel = make_kernel(3, KERNEL_SHAPE)
    result = apply_morphology(grid, OPERATION, kernel)

    print("Initial Binary Grid:")
    for row in grid:
        print("  " + "".join("#" if v else "." for v in row))

    print(f"\nResult after Morphology '{OPERATION}':")
    for row in result:
        print("  " + "".join("#" if v else "." for v in row))

if __name__ == "__main__":
    main()
