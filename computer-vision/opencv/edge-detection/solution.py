"""
OpenCV Image Filters & Edge Detection
Reference: https://mlhive.com/playground/computer-vision/opencv/edge-detection
"""

# RUN CONFIGURATION & PARAMETERS
METHOD = "canny"  # "canny", "sobel", "laplacian", "gaussian"
CANNY_THRESHOLD1 = 50
CANNY_THRESHOLD2 = 150
BLUR_KERNEL_SIZE = 5
IMAGE_URL = "https://mlhive.com/playground/opencv/edge-detection/architecture.webp"

def create_synthetic_image():
    """Generates a synthetic 128x128 test image with geometric edges."""
    import numpy as np
    img = np.zeros((128, 128), dtype=np.uint8)
    # White rectangle
    img[20:70, 20:70] = 255
    # Diagonal ramp
    for i in range(50, 110):
        img[i, 40:i] = 180
    # Circle
    y, x = np.ogrid[:128, :128]
    mask = (x - 90)**2 + (y - 90)**2 <= 25**2
    img[mask] = 220
    return img

def process_edges(img):
    try:
        import cv2
        has_cv2 = True
    except ImportError:
        has_cv2 = False

    if has_cv2:
        import cv2
        blurred = cv2.GaussianBlur(img, (BLUR_KERNEL_SIZE, BLUR_KERNEL_SIZE), 0)
        if METHOD == "canny":
            edges = cv2.Canny(blurred, CANNY_THRESHOLD1, CANNY_THRESHOLD2)
        elif METHOD == "sobel":
            sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
            edges = cv2.magnitude(sobelx, sobely)
        elif METHOD == "laplacian":
            edges = cv2.Laplacian(blurred, cv2.CV_64F)
        else:
            edges = blurred
        return edges, has_cv2
    else:
        # Fallback pure-numpy edge filter
        import numpy as np
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        h, w = img.shape
        edges = np.zeros((h-2, w-2), dtype=float)
        for r in range(h - 2):
            for c in range(w - 2):
                edges[r, c] = abs(np.sum(img[r:r+3, c:c+3] * sobel_x))
        return edges, has_cv2

def main():
    print(f"--- OpenCV Edge Detection Visualizer ---")
    print(f"Algorithm: {METHOD.upper()}")
    print(f"Canny Thresholds: [{CANNY_THRESHOLD1}, {CANNY_THRESHOLD2}]")
    print(f"Blur Kernel: {BLUR_KERNEL_SIZE}x{BLUR_KERNEL_SIZE}")
    print(f"Sample hosted image link: {IMAGE_URL}\n")

    img = create_synthetic_image()
    edges, has_cv = process_edges(img)

    print(f"Input Image Size: {img.shape}")
    print(f"Processed Edge Map Shape: {edges.shape}")
    print(f"Using OpenCV library: {has_cv}")
    print(f"Detected Edge Pixels count: {(edges > 0).sum()} / {edges.size}")

if __name__ == "__main__":
    main()
