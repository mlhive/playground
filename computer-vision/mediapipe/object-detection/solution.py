"""
MediaPipe Object Detection Demonstration
Reference: https://mlhive.com/playground/computer-vision/mediapipe/object-detection
"""

import math

# RUN CONFIGURATION & PARAMETERS
MIN_DETECTION_CONFIDENCE = 0.5
DELEGATE = "CPU"  # "CPU" or "GPU"
RUN_MODE = "IMAGE"

def simulate_object_detection():
    return [
        {"class": "laptop", "score": 0.94, "box": (0.20, 0.35, 0.40, 0.35)},
        {"class": "coffee cup", "score": 0.88, "box": (0.65, 0.50, 0.15, 0.20)},
        {"class": "book", "score": 0.75, "box": (0.10, 0.60, 0.25, 0.25)},
    ]

def main():
    print(f"--- MediaPipe Object Detection ---")
    print(f"Confidence Threshold: {MIN_DETECTION_CONFIDENCE}, Delegate: {DELEGATE}")
    print(f"Run Mode: {RUN_MODE}\n")

    try:
        import mediapipe as mp
        print("MediaPipe library detected: Ready for live webcam/image inference.")
    except ImportError:
        print("MediaPipe library not installed: Running self-contained mathematical simulation.")

    print("\nSimulated Detection Results:")
    if "object-detection" == "image-similarity":
        query_key = "red_sneakers_1"
        query_vec = CATALOG_EMBEDDINGS[query_key]
        print(f"Query Image: '{query_key}'\nVisual Search Catalog Ranking:")
        ranked = []
        for name, vec in CATALOG_EMBEDDINGS.items():
            if name != query_key:
                score = cosine_similarity(query_vec, vec)
                ranked.append((name, score))
        ranked.sort(key=lambda x: -x[1])
        for idx, (name, s) in enumerate(ranked, 1):
            print(f"  {idx}. {name:16s} | Cosine Similarity: {s:.4f}")
    elif "object-detection" == "image-segmentation":
        mask = simulate_segmentation_mask()
        print("Foreground Person Segmentation Mask (threshold >= 0.5):")
        for row in mask:
            print("  " + "".join("##" if v >= 0.5 else ".." for v in row))
    elif "object-detection" == "object-detection":
        objs = simulate_object_detection()
        for o in objs:
            print(f"  Detected '{o['class']}' (confidence: {o['score']:.2f}) at box: {o['box']}")
    elif "object-detection" == "face-detection":
        face = simulate_face_detection()
        print(f"  Face Box: {face['box']} (confidence: {face['score']:.2f})")
        print(f"  6 Facial Keypoints:")
        for name, pt in zip(KEYPOINT_NAMES, face["keypoints"]):
            print(f"    {name:20s}: (x={pt[0]:.2f}, y={pt[1]:.2f})")
    elif "object-detection" == "pose-landmarks":
        shoulder = (0.45, 0.35)
        elbow = (0.40, 0.50)
        wrist = (0.48, 0.45)
        angle = calculate_angle(shoulder, elbow, wrist)
        print(f"  Tracked 33 3D Pose Landmarks.")
        print(f"  Sample Right Elbow Curl Angle: {angle:.1f} degrees")
    else:
        print(f"  Successfully extracted landmark topology (0 points).")

if __name__ == "__main__":
    main()
