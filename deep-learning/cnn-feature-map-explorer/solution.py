"""
CNN Feature Map Explorer
Reference: https://mlhive.com/playground/deep-learning/cnn-feature-map-explorer
"""

ACTIVE_FILTER = "horizontal_edges"

FILTERS = {
    "horizontal_edges": [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ],
    "vertical_edges": [
        [-1,  0,  1],
        [-2,  0,  2],
        [-1,  0,  1]
    ],
    "sharpen": [
        [ 0, -1,  0],
        [-1,  5, -1],
        [ 0, -1,  0]
    ],
    "box_blur": [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]
}

SAMPLE_IMAGE_CHANNEL = [
    [10, 10, 10, 80, 80, 80],
    [10, 10, 10, 80, 80, 80],
    [10, 10, 10, 80, 80, 80],
    [80, 80, 80, 80, 80, 80],
    [80, 80, 80, 80, 80, 80],
    [80, 80, 80, 80, 80, 80],
]

def apply_filter(img: list[list[float]], kernel: list[list[float]]):
    h, w = len(img), len(img[0])
    kh, kw = len(kernel), len(kernel[0])
    out = []
    for r in range(h - kh + 1):
        row = []
        for c in range(w - kw + 1):
            val = sum(img[r + kr][c + kc] * kernel[kr][kc] for kr in range(kh) for kc in range(kw))
            row.append(round(val, 2))
        row.append(row[-1]) # pad border
        out.append(row)
    return out

def main():
    kernel = FILTERS[ACTIVE_FILTER]
    print(f"--- CNN Feature Map Explorer ---")
    print(f"Selected Filter: {ACTIVE_FILTER}\n")

    fmap = apply_filter(SAMPLE_IMAGE_CHANNEL, kernel)
    print(f"Feature Map Activation Response ({len(fmap)}x{len(fmap[0])}):")
    for row in fmap:
        print("  " + " ".join(f"{v:6.1f}" for v in row))

if __name__ == "__main__":
    main()
