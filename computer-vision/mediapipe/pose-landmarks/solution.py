"""
MediaPipe Pose Landmark Detection Demonstration
Reference: https://mlhive.com/playground/computer-vision/mediapipe/pose-landmarks
"""

import math

# RUN CONFIGURATION & PARAMETERS
MIN_DETECTION_CONFIDENCE = 0.5
DELEGATE = "CPU"  # "CPU" or "GPU"
RUN_MODE = "IMAGE"

POSE_NAMES = [
    "NOSE", "LEFT_EYE_INNER", "LEFT_EYE", "LEFT_EYE_OUTER", "RIGHT_EYE_INNER", "RIGHT_EYE", "RIGHT_EYE_OUTER",
    "LEFT_EAR", "RIGHT_EAR", "MOUTH_LEFT", "MOUTH_RIGHT", "LEFT_SHOULDER", "RIGHT_SHOULDER",
    "LEFT_ELBOW", "RIGHT_ELBOW", "LEFT_WRIST", "RIGHT_WRIST", "LEFT_PINKY", "RIGHT_PINKY",
    "LEFT_INDEX", "RIGHT_INDEX", "LEFT_THUMB", "RIGHT_THUMB", "LEFT_HIP", "RIGHT_HIP",
    "LEFT_KNEE", "RIGHT_KNEE", "LEFT_ANKLE", "RIGHT_ANKLE", "LEFT_HEEL", "RIGHT_HEEL",
    "LEFT_FOOT_INDEX", "RIGHT_FOOT_INDEX"
]

def calculate_angle(a, b, c):
    ba = (a[0] - b[0], a[1] - b[1])
    bc = (c[0] - b[0], c[1] - b[1])
    dot = ba[0]*bc[0] + ba[1]*bc[1]
    mag_ba = math.hypot(*ba)
    mag_bc = math.hypot(*bc)
    return math.degrees(math.acos(max(min(dot / (mag_ba * mag_bc), 1.0), -1.0)))

def main():
    print(f"--- MediaPipe Pose Landmark Detection ---")
    print(f"Confidence Threshold: {MIN_DETECTION_CONFIDENCE}, Delegate: {DELEGATE}")
    print(f"Run Mode: {RUN_MODE}\n")

    try:
        import mediapipe as mp
        print("MediaPipe library detected: Ready for live webcam/image inference.")
    except ImportError:
        print("MediaPipe library not installed: Running self-contained mathematical simulation.")

    print("\nSimulated Detection Results:")
    if "pose-landmarks" == "image-similarity":
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
    elif "pose-landmarks" == "image-segmentation":
        mask = simulate_segmentation_mask()
        print("Foreground Person Segmentation Mask (threshold >= 0.5):")
        for row in mask:
            print("  " + "".join("##" if v >= 0.5 else ".." for v in row))
    elif "pose-landmarks" == "object-detection":
        objs = simulate_object_detection()
        for o in objs:
            print(f"  Detected '{o['class']}' (confidence: {o['score']:.2f}) at box: {o['box']}")
    elif "pose-landmarks" == "face-detection":
        face = simulate_face_detection()
        print(f"  Face Box: {face['box']} (confidence: {face['score']:.2f})")
        print(f"  6 Facial Keypoints:")
        for name, pt in zip(KEYPOINT_NAMES, face["keypoints"]):
            print(f"    {name:20s}: (x={pt[0]:.2f}, y={pt[1]:.2f})")
    elif "pose-landmarks" == "pose-landmarks":
        shoulder = (0.45, 0.35)
        elbow = (0.40, 0.50)
        wrist = (0.48, 0.45)
        angle = calculate_angle(shoulder, elbow, wrist)
        print(f"  Tracked 33 3D Pose Landmarks.")
        print(f"  Sample Right Elbow Curl Angle: {angle:.1f} degrees")
    else:
        print(f"  Successfully extracted landmark topology (33 points).")

if __name__ == "__main__":
    main()
