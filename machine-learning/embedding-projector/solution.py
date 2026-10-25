"""
High-Dimensional Embedding Projector (PCA & Cosine Similarity)
Reference: https://mlhive.com/playground/machine-learning/embedding-projector
"""

import math

# RUN CONFIGURATION & PARAMETERS
METHOD = "PCA"
QUERY_WORD = "king"
TOP_K = 3
VERBOSE = True

# Sample 5-dimensional toy word embeddings
WORD_EMBEDDINGS = {
    "king":    [0.85,  0.45,  0.10, -0.20,  0.70],
    "queen":   [0.82,  0.48, -0.15, -0.18,  0.68],
    "man":     [0.40,  0.15,  0.75, -0.05,  0.30],
    "woman":   [0.38,  0.18,  0.60, -0.02,  0.28],
    "apple":   [-0.60, 0.70,  0.10,  0.80, -0.40],
    "banana":  [-0.55, 0.65,  0.15,  0.75, -0.38],
    "orange":  [-0.58, 0.68,  0.12,  0.78, -0.42],
}

def cosine_similarity(u: list[float], v: list[float]) -> float:
    dot = sum(ui * vi for ui, vi in zip(u, v))
    norm_u = math.sqrt(sum(ui ** 2 for ui in u))
    norm_v = math.sqrt(sum(vi ** 2 for vi in v))
    return dot / (norm_u * norm_v) if norm_u > 0 and norm_v > 0 else 0.0

def project_pca_2d(embeddings: dict[str, list[float]]):
    words = list(embeddings.keys())
    vectors = [embeddings[w] for w in words]
    n = len(words)
    d = len(vectors[0])

    # Center data
    means = [sum(vectors[i][j] for i in range(n)) / n for j in range(d)]
    centered = [[vectors[i][j] - means[j] for j in range(d)] for i in range(n)]

    # Compute top 2 components using power iteration
    def get_principal_component(data, prev_comp=None):
        comp = [1.0] * d
        for _ in range(50):
            # c = X^T * (X * c)
            xc = [sum(data[i][j] * comp[j] for j in range(d)) for i in range(n)]
            new_comp = [sum(data[i][j] * xc[i] for i in range(n)) for j in range(d)]
            if prev_comp:
                # Orthogonalize
                proj = sum(new_comp[j] * prev_comp[j] for j in range(d))
                new_comp = [new_comp[j] - proj * prev_comp[j] for j in range(d)]
            norm = math.sqrt(sum(x**2 for x in new_comp)) or 1.0
            comp = [x / norm for x in new_comp]
        return comp

    pc1 = get_principal_component(centered)
    pc2 = get_principal_component(centered, pc1)

    projected = {}
    for i, w in enumerate(words):
        x = sum(centered[i][j] * pc1[j] for j in range(d))
        y = sum(centered[i][j] * pc2[j] for j in range(d))
        projected[w] = (round(x, 4), round(y, 4))
    return projected

def main():
    print("--- Embedding Projector & Semantic Explorer ---")
    print(f"Total Words: {len(WORD_EMBEDDINGS)}")
    print(f"Query Word: '{QUERY_WORD}', Top-K: {TOP_K}\n")

    # Nearest Neighbors
    query_vec = WORD_EMBEDDINGS[QUERY_WORD]
    scores = []
    for word, vec in WORD_EMBEDDINGS.items():
        if word != QUERY_WORD:
            sim = cosine_similarity(query_vec, vec)
            scores.append((word, sim))
    scores.sort(key=lambda item: -item[1])

    print(f"Nearest Neighbors to '{QUERY_WORD}' (Cosine Similarity):")
    for rank, (word, sim) in enumerate(scores[:TOP_K], 1):
        print(f"  {rank}. {word:10s} (Similarity: {sim:.4f})")

    # 2D PCA Projection
    print("\n2D PCA Coordinates:")
    proj = project_pca_2d(WORD_EMBEDDINGS)
    for word, (x, y) in proj.items():
        print(f"  {word:10s} -> (x={x:+6.3f}, y={y:+6.3f})")

if __name__ == "__main__":
    main()
