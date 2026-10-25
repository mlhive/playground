/**
 * K-Means Clustering in JavaScript
 * Reference: https://mlhive.com/playground/machine-learning/kmeans
 */

const K = 3;
const POINTS = [
  [1.0, 1.2], [1.5, 1.8], [1.2, 0.9], [2.0, 1.5], [0.8, 1.6],
  [5.0, 5.2], [5.5, 4.8], [4.8, 5.9], [5.2, 5.5], [6.0, 5.0],
  [1.2, 6.0], [1.8, 5.8], [1.5, 6.5], [0.9, 5.5], [1.4, 6.2]
];

function dist(p1, p2) {
  return Math.hypot(p1[0] - p2[0], p1[1] - p2[1]);
}

let centroids = [POINTS[0], POINTS[5], POINTS[10]];

for (let iter = 1; iter <= 20; iter++) {
  const clusters = Array.from({ length: K }, () => []);
  for (const p of POINTS) {
    let best = 0, bestD = Infinity;
    centroids.forEach((c, idx) => {
      const d = dist(p, c);
      if (d < bestD) { bestD = d; best = idx; }
    });
    clusters[best].push(p);
  }

  centroids = clusters.map((group, idx) => {
    if (group.length === 0) return centroids[idx];
    const meanX = group.reduce((sum, p) => sum + p[0], 0) / group.length;
    const meanY = group.reduce((sum, p) => sum + p[1], 0) / group.length;
    return [meanX, meanY];
  });
}

console.log("--- K-Means (JavaScript) ---");
centroids.forEach((c, i) => console.log(`Cluster ${i+1} Centroid: (${c[0].toFixed(2)}, ${c[1].toFixed(2)})`));
