/**
 * Logistic Regression in JavaScript
 * Reference: https://mlhive.com/playground/machine-learning/logistic-regression
 */

const LR = 0.1;
const EPOCHS = 200;
const DATA = [
  [0.5, 0], [1.0, 0], [1.5, 0], [2.0, 0], [2.5, 0],
  [3.0, 0], [3.5, 1], [4.0, 1], [4.5, 1], [5.0, 1]
];

function sigmoid(z) { return 1 / (1 + Math.exp(-z)); }

let w = 0, b = 0;
const n = DATA.length;

for (let ep = 1; ep <= EPOCHS; ep++) {
  let dw = 0, db = 0;
  for (const [x, y] of DATA) {
    const pred = sigmoid(w * x + b);
    dw += (1 / n) * (pred - y) * x;
    db += (1 / n) * (pred - y);
  }
  w -= LR * dw;
  b -= LR * db;
}

console.log("--- Logistic Regression (JavaScript) ---");
console.log(`Model: P(y=1) = sigmoid(${w.toFixed(4)}x + ${b.toFixed(4)})`);
console.log(`Decision Boundary: x = ${(-b / w).toFixed(2)}`);
