"""
K-Means Clustering Implementation
Reference: https://mlhive.com/playground/machine-learning/kmeans
"""

import math
import random

# RUN CONFIGURATION & PARAMETERS
K = 3
INIT = "kmeans++"  # "kmeans++" or "random"
MAX_ITERS = 50
TOLERANCE = 1e-4
PRESET = "three_blobs"
VERBOSE = True

DATASETS = {
    "three_blobs": [
        (1.0, 1.2), (1.5, 1.8), (1.2, 0.9), (2.0, 1.5), (0.8, 1.6),
        (5.0, 5.2), (5.5, 4.8), (4.8, 5.9), (5.2, 5.5), (6.0, 5.0),
        (1.2, 6.0), (1.8, 5.8), (1.5, 6.5), (0.9, 5.5), (1.4, 6.2)
    ]
}

def euclidean_dist(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def initialize_centroids(points: list[tuple[float, float]], k: int, method: str) -> list[tuple[float, float]]:
    random.seed(42)
    if method == "random":
        return [points[i] for i in random.sample(range(len(points)), k)]
    
    # K-Means++
    centroids = [random.choice(points)]
    while len(centroids) < k:
        dist_sq = [min(euclidean_dist(p, c)**2 for c in centroids) for p in points]
        total = sum(dist_sq)
        r = random.uniform(0, total)
        cum = 0.0
        for i, d2 in enumerate(dist_sq):
            cum += d2
            if cum >= r:
                centroids.append(points[i])
                break
    return centroids

def kmeans(points: list[tuple[float, float]], k: int, init_method: str, max_iters: int):
    centroids = initialize_centroids(points, k, init_method)
    
    for it in range(1, max_iters + 1):
        clusters = [[] for _ in range(k)]
        inertia = 0.0
        
        # Assignment
        for p in points:
            dists = [euclidean_dist(p, c) for c in centroids]
            best_c = dists.index(min(dists))
            clusters[best_c].append(p)
            inertia += min(dists)**2
            
        # Update
        new_centroids = []
        max_shift = 0.0
        for c_idx in range(k):
            if clusters[c_idx]:
                n = len(clusters[c_idx])
                mean_x = sum(p[0] for p in clusters[c_idx]) / n
                mean_y = sum(p[1] for p in clusters[c_idx]) / n
                new_c = (mean_x, mean_y)
            else:
                new_c = centroids[c_idx]
            max_shift = max(max_shift, euclidean_dist(centroids[c_idx], new_c))
            new_centroids.append(new_c)
            
        centroids = new_centroids
        if VERBOSE and (it % 2 == 0 or it == 1):
            print(f"Iteration {it:02d} | Inertia: {inertia:.4f} | Max Shift: {max_shift:.4f}")
            
        if max_shift < TOLERANCE:
            if VERBOSE:
                print(f"Converged at iteration {it}!")
            break
            
    return centroids, clusters

def main():
    points = DATASETS.get(PRESET, DATASETS["three_blobs"])
    print(f"--- K-Means Clustering (K = {K}) ---")
    print(f"Dataset Preset: {PRESET} ({len(points)} points)")
    print(f"Init: {INIT}\n")

    centroids, clusters = kmeans(points, K, INIT, MAX_ITERS)
    print("\nFinal Centroids:")
    for idx, c in enumerate(centroids, 1):
        print(f"  Cluster {idx} centroid: ({c[0]:.2f}, {c[1]:.2f}) - {len(clusters[idx-1])} points")

if __name__ == "__main__":
    main()
