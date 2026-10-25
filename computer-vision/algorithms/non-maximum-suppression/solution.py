"""
Non-Maximum Suppression (NMS) Pure Python Implementation
Reference: https://mlhive.com/playground/computer-vision/algorithms/non-maximum-suppression
"""

# RUN CONFIGURATION & PARAMETERS
CONFIDENCE_THRESHOLD = 0.3
IOU_THRESHOLD = 0.5
CLASS_AWARE = True
PRESET = "duplicate_detections"
VERBOSE = True

# Coordinates: normalized (x, y, width, height)
CANDIDATE_BOXES = [
    {"id": "A", "classId": "person", "score": 0.95, "x": 0.14, "y": 0.13, "width": 0.30, "height": 0.68},
    {"id": "B", "classId": "person", "score": 0.87, "x": 0.16, "y": 0.15, "width": 0.30, "height": 0.68},
    {"id": "C", "classId": "person", "score": 0.58, "x": 0.12, "y": 0.11, "width": 0.31, "height": 0.70},
    {"id": "D", "classId": "dog",    "score": 0.92, "x": 0.55, "y": 0.40, "width": 0.28, "height": 0.45},
    {"id": "E", "classId": "dog",    "score": 0.64, "x": 0.58, "y": 0.42, "width": 0.25, "height": 0.42},
    {"id": "F", "classId": "car",    "score": 0.22, "x": 0.75, "y": 0.10, "width": 0.20, "height": 0.20}, # filtered
]

def iou(a: dict, b: dict) -> float:
    # Compute intersection rectangle
    x1 = max(a["x"], b["x"])
    y1 = max(a["y"], b["y"])
    x2 = min(a["x"] + a["width"], b["x"] + b["width"])
    y2 = min(a["y"] + a["height"], b["y"] + b["height"])

    inter_w = max(0.0, x2 - x1)
    inter_h = max(0.0, y2 - y1)
    intersection = inter_w * inter_h

    area_a = a["width"] * a["height"]
    area_b = b["width"] * b["height"]
    union = area_a + area_b - intersection

    return intersection / union if union > 0 else 0.0

def run_nms(boxes: list[dict], conf_thr: float, iou_thr: float, class_aware: bool):
    # 1. Confidence thresholding
    pending = [b for b in boxes if b["score"] >= conf_thr]
    filtered_out = [b for b in boxes if b["score"] < conf_thr]

    # 2. Sort descending by score
    pending.sort(key=lambda b: -b["score"])

    kept = []
    suppressed = []
    step = 1

    while pending:
        selected = pending.pop(0)
        kept.append(selected)
        if VERBOSE:
            print(f"Step {step:02d}: Select box '{selected['id']}' ({selected['classId']}, score={selected['score']:.2f})")
        step += 1

        next_pending = []
        for candidate in pending:
            same_class = (candidate["classId"] == selected["classId"])
            overlap = iou(selected, candidate)

            # Suppress if same class (or class-agnostic) and IoU > threshold
            if (not class_aware or same_class) and overlap > iou_thr:
                suppressed.append((candidate, selected["id"], overlap))
                if VERBOSE:
                    print(f"  Suppressed box '{candidate['id']}' (overlap={overlap:.3f} > {iou_thr}) by '{selected['id']}'")
            else:
                next_pending.append(candidate)
        pending = next_pending

    return kept, suppressed, filtered_out

def main():
    print(f"--- Non-Maximum Suppression (NMS) ---")
    print(f"Confidence Threshold: {CONFIDENCE_THRESHOLD}, IoU Threshold: {IOU_THRESHOLD}")
    print(f"Class Aware: {CLASS_AWARE}, Input Boxes: {len(CANDIDATE_BOXES)}\n")

    kept, suppressed, filtered = run_nms(CANDIDATE_BOXES, CONFIDENCE_THRESHOLD, IOU_THRESHOLD, CLASS_AWARE)

    print(f"\nKept Boxes Count: {len(kept)}")
    for b in kept:
        print(f"  [KEPT] Box '{b['id']}' | Class: {b['classId']:7s} | Score: {b['score']:.2f}")

    print(f"\nSuppressed Boxes Count: {len(suppressed)}")
    for b, by_id, score in suppressed:
        print(f"  [SUPPRESSED] Box '{b['id']}' by '{by_id}' (IoU: {score:.3f})")

if __name__ == "__main__":
    main()
