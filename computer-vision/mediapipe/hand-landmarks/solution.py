"""
MediaPipe Hand Landmark Detection Demonstration
Reference: https://mlhive.com/playground/computer-vision/mediapipe/hand-landmarks
"""

import math

# RUN CONFIGURATION & PARAMETERS
MIN_DETECTION_CONFIDENCE = 0.5
DELEGATE = "CPU"  # "CPU" or "GPU"
RUN_MODE = "IMAGE"

LANDMARK_NAMES = [
    "WRIST", "THUMB_CMC", "THUMB_MCP", "THUMB_IP", "THUMB_TIP",
    "INDEX_FINGER_MCP", "INDEX_FINGER_PIP", "INDEX_FINGER_DIP", "INDEX_FINGER_TIP",
    "MIDDLE_FINGER_MCP", "MIDDLE_FINGER_PIP", "MIDDLE_FINGER_DIP", "MIDDLE_FINGER_TIP",
    "RING_FINGER_MCP", "RING_FINGER_PIP", "RING_FINGER_DIP", "RING_FINGER_TIP",
    "PINKY_MCP", "PINKY_PIP", "PINKY_DIP", "PINKY_TIP"
]

def simulate_hand_detection():
    # Synthetic normalized (x, y, z) landmarks for an open hand
    return [
        (0.50, 0.85, 0.00), (0.42, 0.75, -0.02), (0.35, 0.65, -0.04), (0.30, 0.55, -0.05), (0.26, 0.48, -0.06),
        (0.42, 0.50, -0.01), (0.40, 0.38, -0.02), (0.39, 0.28, -0.03), (0.38, 0.20, -0.04),
        (0.50, 0.48, 0.00),  (0.50, 0.35, -0.01), (0.50, 0.24, -0.02), (0.50, 0.15, -0.03),
        (0.58, 0.50, 0.00),  (0.60, 0.38, -0.01), (0.61, 0.28, -0.02), (0.62, 0.20, -0.03),
        (0.65, 0.55, 0.01),  (0.68, 0.45, 0.00),  (0.70, 0.38, -0.01), (0.72, 0.30, -0.02)
    ]

def main():
    print(f"--- MediaPipe Hand Landmark Detection ---")
    print(f"Confidence Threshold: {MIN_DETECTION_CONFIDENCE}, Delegate: {DELEGATE}")
    print(f"Run Mode: {RUN_MODE}\n")

    try:
        import mediapipe as mp
        print("MediaPipe library detected: Ready for live webcam/image inference.")
    except ImportError:
        print("MediaPipe library not installed: Running self-contained mathematical simulation.")

    print("\nSimulated Detection Results:")
    if "hand-landmarks" == "image-similarity":
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
    elif "hand-landmarks" == "image-segmentation":
        mask = simulate_segmentation_mask()
        print("Foreground Person Segmentation Mask (threshold >= 0.5):")
        for row in mask:
            print("  " + "".join("##" if v >= 0.5 else ".." for v in row))
    elif "hand-landmarks" == "object-detection":
        objs = simulate_object_detection()
        for o in objs:
            print(f"  Detected '{o['class']}' (confidence: {o['score']:.2f}) at box: {o['box']}")
    elif "hand-landmarks" == "face-detection":
        face = simulate_face_detection()
        print(f"  Face Box: {face['box']} (confidence: {face['score']:.2f})")
        print(f"  6 Facial Keypoints:")
        for name, pt in zip(KEYPOINT_NAMES, face["keypoints"]):
            print(f"    {name:20s}: (x={pt[0]:.2f}, y={pt[1]:.2f})")
    elif "hand-landmarks" == "pose-landmarks":
        shoulder = (0.45, 0.35)
        elbow = (0.40, 0.50)
        wrist = (0.48, 0.45)
        angle = calculate_angle(shoulder, elbow, wrist)
        print(f"  Tracked 33 3D Pose Landmarks.")
        print(f"  Sample Right Elbow Curl Angle: {angle:.1f} degrees")
    else:
        print(f"  Successfully extracted landmark topology (21 points).")

if __name__ == "__main__":
    main()
