/**
 * Confusion Matrix in JavaScript
 * Reference: https://mlhive.com/playground/machine-learning/confusion-matrix
 */

const THRESHOLD = 0.5;
const SAMPLES = [
  [1, 0.95], [1, 0.88], [1, 0.76], [1, 0.65], [1, 0.45],
  [1, 0.82], [1, 0.55], [1, 0.35], [0, 0.58], [0, 0.42],
  [0, 0.31], [0, 0.22], [0, 0.15], [0, 0.08], [0, 0.62]
];

let tp = 0, fp = 0, tn = 0, fn = 0;
for (const [y, score] of SAMPLES) {
  const pred = score >= THRESHOLD ? 1 : 0;
  if (y === 1 && pred === 1) tp++;
  else if (y === 0 && pred === 1) fp++;
  else if (y === 0 && pred === 0) tn++;
  else fn++;
}

console.log("--- Confusion Matrix (JavaScript) ---");
console.log(`TP: ${tp}, FP: ${fp}, FN: ${fn}, TN: ${tn}`);
console.log(`Accuracy:  ${((tp + tn) / SAMPLES.length * 100).toFixed(1)}%`);
console.log(`Precision: ${(tp / (tp + fp) * 100).toFixed(1)}%`);
console.log(`Recall:    ${(tp / (tp + fn) * 100).toFixed(1)}%`);
