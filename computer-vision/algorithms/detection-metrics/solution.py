"""
Object Detection Evaluation: IoU Matching, PR Curve & AP / mAP
Reference: https://mlhive.com/playground/computer-vision/algorithms/detection-metrics
"""

# RUN CONFIGURATION & PARAMETERS
IOU_THRESHOLD = 0.5
CONFIDENCE_THRESHOLD = 0.4
IMAGE_URL = "https://mlhive.com/playground/detection-metrics/street-scene.webp"

GROUND_TRUTH = [
    {"id": "gt1", "class": "car",    "x": 0.10, "y": 0.20, "w": 0.25, "h": 0.20},
    {"id": "gt2", "class": "car",    "x": 0.40, "y": 0.25, "w": 0.20, "h": 0.18},
    {"id": "gt3", "class": "person", "x": 0.70, "y": 0.30, "w": 0.10, "h": 0.40},
]

PREDICTIONS = [
    {"id": "p1", "class": "car",    "score": 0.92, "x": 0.11, "y": 0.21, "w": 0.24, "h": 0.19}, # TP
    {"id": "p2", "class": "car",    "score": 0.85, "x": 0.38, "y": 0.23, "w": 0.22, "h": 0.20}, # TP
    {"id": "p3", "class": "car",    "score": 0.65, "x": 0.12, "y": 0.20, "w": 0.25, "h": 0.20}, # Duplicate -> FP
    {"id": "p4", "class": "person", "score": 0.78, "x": 0.72, "y": 0.32, "w": 0.09, "h": 0.38}, # TP
    {"id": "p5", "class": "dog",    "score": 0.55, "x": 0.85, "y": 0.50, "w": 0.10, "h": 0.15}, # FP (no gt dog)
]

def compute_iou(b1, b2) -> float:
    x1 = max(b1["x"], b2["x"])
    y1 = max(b1["y"], b2["y"])
    x2 = min(b1["x"] + b1["w"], b2["x"] + b2["w"])
    y2 = min(b1["y"] + b1["h"], b2["y"] + b2["h"])
    inter = max(0.0, x2 - x1) * max(0.0, y2 - y1)
    union = b1["w"] * b1["h"] + b2["w"] * b2["h"] - inter
    return inter / union if union > 0 else 0.0

def evaluate_detections(gt_boxes, pred_boxes, iou_thr, conf_thr):
    # Filter by confidence
    preds = [p for p in pred_boxes if p["score"] >= conf_thr]
    preds.sort(key=lambda p: -p["score"])

    matched_gt = set()
    tp = fp = 0
    results = []

    for p in preds:
        best_iou = 0.0
        best_gt = None
        for gt in gt_boxes:
            if gt["class"] == p["class"] and gt["id"] not in matched_gt:
                overlap = compute_iou(p, gt)
                if overlap > best_iou:
                    best_iou = overlap
                    best_gt = gt

        if best_iou >= iou_thr and best_gt:
            matched_gt.add(best_gt["id"])
            tp += 1
            results.append((p["id"], "TP", best_gt["id"], best_iou))
        else:
            fp += 1
            results.append((p["id"], "FP", None, best_iou))

    fn = len(gt_boxes) - len(matched_gt)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / len(gt_boxes) if len(gt_boxes) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "tp": tp, "fp": fp, "fn": fn,
        "precision": precision, "recall": recall, "f1": f1,
        "results": results
    }

def main():
    print(f"--- Object Detection Metrics & mAP Explorer ---")
    print(f"IoU Threshold: {IOU_THRESHOLD}, Confidence Threshold: {CONFIDENCE_THRESHOLD}")
    print(f"Ground Truth Count: {len(GROUND_TRUTH)}, Predictions: {len(PREDICTIONS)}")
    print(f"Reference scene: {IMAGE_URL}\n")

    res = evaluate_detections(GROUND_TRUTH, PREDICTIONS, IOU_THRESHOLD, CONFIDENCE_THRESHOLD)

    print(f"{'Pred ID':8s} | {'Result':6s} | {'Matched GT':10s} | Max IoU")
    print("-" * 42)
    for p_id, outcome, gt_id, iou_val in res["results"]:
        gt_str = gt_id if gt_id else "None"
        print(f"{p_id:8s} | {outcome:6s} | {gt_str:10s} | {iou_val:.3f}")

    print(f"\nTrue Positives (TP):  {res['tp']}")
    print(f"False Positives (FP): {res['fp']}")
    print(f"False Negatives (FN): {res['fn']}")
    print(f"Precision:            {res['precision'] * 100:.1f}%")
    print(f"Recall:               {res['recall'] * 100:.1f}%")
    print(f"F1-Score:             {res['f1']:.4f}")

if __name__ == "__main__":
    main()
