"""
OpenCV Contour & Shape Detection
Reference: https://mlhive.com/playground/computer-vision/opencv/contour-shape-detection
"""

import math

BINARY_THRESHOLD = 127
EPSILON_FACTOR = 0.04
MIN_CONTOUR_AREA = 100
IMAGE_URL = "https://mlhive.com/playground/opencv/contour-shape-detection/geometric-shapes.svg"

def classify_shape(vertices: int, area: float, perimeter: float) -> str:
    if vertices == 3:
        return "Triangle"
    elif vertices == 4:
        return "Rectangle/Square"
    elif vertices == 5:
        return "Pentagon"
    else:
        # Circularity metric: 4 * pi * Area / Perimeter^2
        circularity = (4 * math.pi * area) / (perimeter ** 2) if perimeter > 0 else 0
        if circularity > 0.80:
            return "Circle"
        return f"{vertices}-gon"

def run_contour_analysis():
    # Synthetic shape contours to demonstrate algorithm
    shapes = [
        {"name": "Shape A", "vertices": 3, "area": 450.0, "perimeter": 105.0},
        {"name": "Shape B", "vertices": 4, "area": 900.0, "perimeter": 120.0},
        {"name": "Shape C", "vertices": 5, "area": 620.0, "perimeter": 95.0},
        {"name": "Shape D", "vertices": 16, "area": 1256.0, "perimeter": 126.0}, # Circle
    ]
    return shapes

def main():
    print("--- OpenCV Contour & Shape Detection ---")
    print(f"Binary Threshold: {BINARY_THRESHOLD}")
    print(f"Epsilon Factor: {EPSILON_FACTOR}")
    print(f"Reference hosted image: {IMAGE_URL}\n")

    shapes = run_contour_analysis()
    print(f"{'Contour':10s} | {'Vertices':8s} | {'Area':8s} | {'Perimeter':10s} | Classified Shape")
    print("-" * 62)
    for s in shapes:
        classification = classify_shape(s["vertices"], s["area"], s["perimeter"])
        print(f"{s['name']:10s} | {s['vertices']:8d} | {s['area']:8.1f} | {s['perimeter']:10.1f} | {classification}")

if __name__ == "__main__":
    main()
