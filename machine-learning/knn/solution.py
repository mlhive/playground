"""
K-Nearest Neighbors (KNN) Classification
Reference: https://mlhive.com/playground/machine-learning/knn
"""

import math
from collections import Counter

# RUN CONFIGURATION & PARAMETERS
K = 3
DISTANCE_METRIC = "euclidean"  # "euclidean" or "manhattan"
QUERY_POINT = (3.2, 2.8)
PRESET = "two_clusters"
VERBOSE = True

DATASETS = {
    "two_clusters": [
        # (x, y, label)
        (1.0, 1.2, "Red"), (1.5, 1.8, "Red"), (2.0, 1.0, "Red"), (2.2, 2.5, "Red"),
        (4.0, 3.8, "Blue"), (4.5, 4.2, "Blue"), (5.0, 3.5, "Blue"), (3.8, 4.5, "Blue"),
    ],
    "three_classes": [
        (1.0, 1.0, "Class A"), (1.2, 1.5, "Class A"), (1.8, 1.1, "Class A"),
        (4.0, 1.2, "Class B"), (4.2, 1.8, "Class B"), (4.8, 1.0, "Class B"),
        (2.5, 4.0, "Class C"), (2.8, 4.5, "Class C"), (3.2, 3.8, "Class C"),
    ]
}

def distance(p1: tuple[float, float], p2: tuple[float, float], metric: str) -> float:
    if metric == "manhattan":
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def knn_classify(training_data: list[tuple[float, float, str]], query: tuple[float, float], k: int, metric: str):
    distances = []
    for x, y, label in training_data:
        d = distance(query, (x, y), metric)
        distances.append((d, (x, y), label))
    
    # Sort by ascending distance
    distances.sort(key=lambda item: item[0])
    k_nearest = distances[:k]
    
    votes = Counter(item[2] for item in k_nearest)
    predicted_class, top_votes = votes.most_common(1)[0]
    
    return predicted_class, k_nearest, votes

def main():
    data = DATASETS.get(PRESET, DATASETS["two_clusters"])
    print(f"--- K-Nearest Neighbors (KNN) ---")
    print(f"K = {K}, Metric: {DISTANCE_METRIC}")
    print(f"Query Point: {QUERY_POINT}\n")

    predicted, nearest, votes = knn_classify(data, QUERY_POINT, K, DISTANCE_METRIC)

    print(f"Nearest {K} Neighbors:")
    for idx, (dist, coord, label) in enumerate(nearest, 1):
        print(f"  {idx}. Coord: {coord} | Label: {label} | Distance: {dist:.4f}")

    print(f"\nClass Votes: {dict(votes)}")
    print(f"Predicted Class: {predicted}")

if __name__ == "__main__":
    main()
