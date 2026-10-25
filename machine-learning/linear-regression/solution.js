/**
 * Linear Regression Implementation (JavaScript / Node.js)
 * Reference: https://mlhive.com/playground/machine-learning/linear-regression
 */

const LEARNING_RATE = 0.01;
const EPOCHS = 100;
const PRESET = "linear_trend";

const DATASETS = {
  linear_trend: [
    [1, 2.5], [2, 3.8], [3, 5.2], [4, 6.9], [5, 8.1],
    [6, 9.8], [7, 11.2], [8, 12.9], [9, 14.5], [10, 16.2]
  ]
};

function train(points, lr, epochs) {
  let w = 0, b = 0;
  const n = points.length;

  for (let epoch = 1; epoch <= epochs; epoch++) {
    let dw = 0, db = 0, mse = 0;
    for (const [x, y] of points) {
      const pred = w * x + b;
      const err = pred - y;
      dw += (2 / n) * err * x;
      db += (2 / n) * err;
      mse += (err * err) / n;
    }
    w -= lr * dw;
    b -= lr * db;

    if (epoch % 20 === 0 || epoch === epochs) {
      console.log(`Epoch ${String(epoch).padStart(3, '0')} | Loss: ${mse.toFixed(4)} | w: ${w.toFixed(4)}, b: ${b.toFixed(4)}`);
    }
  }
  return { w, b };
}

const points = DATASETS[PRESET];
console.log("--- Linear Regression (JavaScript) ---");
const { w, b } = train(points, LEARNING_RATE, EPOCHS);
console.log(`\nFitted Line: y = ${w.toFixed(4)}x + ${b.toFixed(4)}`);
