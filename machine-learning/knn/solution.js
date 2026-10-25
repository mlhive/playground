/**
 * K-Nearest Neighbors (KNN) in JavaScript
 * Reference: https://mlhive.com/playground/machine-learning/knn
 */

const K = 3;
const QUERY = [3.2, 2.8];
const DATASET = [
  [1.0, 1.2, "Red"], [1.5, 1.8, "Red"], [2.0, 1.0, "Red"], [2.2, 2.5, "Red"],
  [4.0, 3.8, "Blue"], [4.5, 4.2, "Blue"], [5.0, 3.5, "Blue"], [3.8, 4.5, "Blue"]
];

function dist(a, b) {
  return Math.hypot(a[0] - b[0], a[1] - b[1]);
}

const scored = DATASET.map(([x, y, label]) => ({
  x, y, label,
  distance: dist(QUERY, [x, y])
})).sort((a, b) => a.distance - b.distance);

const neighbors = scored.slice(0, K);
const counts = {};
neighbors.forEach(n => counts[n.label] = (counts[n.label] || 0) + 1);

const best = Object.keys(counts).reduce((a, b) => counts[a] > counts[b] ? a : b);

console.log("--- KNN (JavaScript) ---");
console.log(`Query: [${QUERY.join(', ')}]`);
console.log(`Predicted Class: ${best} (${counts[best]}/${K} votes)`);
