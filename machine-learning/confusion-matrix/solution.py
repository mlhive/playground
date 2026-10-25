"""
Confusion Matrix & ROC-AUC Metrics
Reference: https://mlhive.com/playground/machine-learning/confusion-matrix
"""

# RUN CONFIGURATION & PARAMETERS
THRESHOLD = 0.5
PRESET = "balanced"  # "balanced", "imbalanced", "high_confidence"

DATASETS = {
    # (true_label, predicted_score)
    "balanced": [
        (1, 0.95), (1, 0.88), (1, 0.76), (1, 0.65), (1, 0.45),
        (1, 0.82), (1, 0.55), (1, 0.35), (0, 0.58), (0, 0.42),
        (0, 0.31), (0, 0.22), (0, 0.15), (0, 0.08), (0, 0.62)
    ],
    "imbalanced": [
        (1, 0.91), (1, 0.82),
        (0, 0.12), (0, 0.18), (0, 0.25), (0, 0.32), (0, 0.41),
        (0, 0.15), (0, 0.22), (0, 0.08), (0, 0.05), (0, 0.35)
    ]
}

def compute_metrics(samples: list[tuple[int, float]], threshold: float):
    tp = fp = tn = fn = 0
    for true_val, score in samples:
        pred = 1 if score >= threshold else 0
        if true_val == 1 and pred == 1:
            tp += 1
        elif true_val == 0 and pred == 1:
            fp += 1
        elif true_val == 0 and pred == 0:
            tn += 1
        else:
            fn += 1

    total = len(samples)
    accuracy = (tp + tn) / total if total > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return {
        "tp": tp, "fp": fp, "tn": tn, "fn": fn,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "specificity": specificity,
        "f1": f1
    }

def main():
    samples = DATASETS.get(PRESET, DATASETS["balanced"])
    print(f"--- Confusion Matrix & Evaluation ---")
    print(f"Dataset Preset: {PRESET} ({len(samples)} items)")
    print(f"Decision Threshold: {THRESHOLD}\n")

    m = compute_metrics(samples, THRESHOLD)

    print("Confusion Matrix:")
    print(f"                Actual Pos  Actual Neg")
    print(f"  Predicted Pos:   {m['tp']:2d} (TP)    {m['fp']:2d} (FP)")
    print(f"  Predicted Neg:   {m['fn']:2d} (FN)    {m['tn']:2d} (TN)\n")

    print(f"Accuracy:    {m['accuracy'] * 100:.2f}%")
    print(f"Precision:   {m['precision'] * 100:.2f}%")
    print(f"Recall:      {m['recall'] * 100:.2f}%")
    print(f"Specificity: {m['specificity'] * 100:.2f}%")
    print(f"F1-Score:    {m['f1']:.4f}")

if __name__ == "__main__":
    main()
