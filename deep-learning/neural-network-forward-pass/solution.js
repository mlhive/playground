/**
 * Neural Network Forward Pass in JavaScript
 * Reference: https://mlhive.com/playground/deep-learning/neural-network-forward-pass
 */

const LAYER_SIZES = [3, 4, 2, 1];
const INPUTS = [0.75, -0.3, 0.5];

function relu(z) { return Math.max(0, z); }
function sigmoid(z) { return 1 / (1 + Math.exp(-z)); }

let a = [...INPUTS];
console.log("--- NN Forward Pass (JavaScript) ---");
console.log(`Input: [${a.join(', ')}]`);

for (let l = 0; l < LAYER_SIZES.length - 1; l++) {
  const fanIn = LAYER_SIZES[l];
  const fanOut = LAYER_SIZES[l + 1];
  const isOut = l === LAYER_SIZES.length - 2;
  const nextA = [];

  for (let j = 0; j < fanOut; j++) {
    let z = 0.05; // bias
    for (let i = 0; i < fanIn; i++) {
      const w = Math.sin((j + 1) * 1.5 + (i + 1) * 2.3) * 0.5;
      z += w * a[i];
    }
    nextA.push(isOut ? sigmoid(z) : relu(z));
  }
  a = nextA;
  console.log(`Layer ${l + 1} (${isOut ? 'Output' : 'Hidden'}): [${a.map(v => v.toFixed(4)).join(', ')}]`);
}

console.log(`\nPrediction: ${a[0].toFixed(4)}`);
