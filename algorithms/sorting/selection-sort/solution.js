/**
 * Selection Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/selection-sort
 */

// ==========================================
// RUN CONFIGURATION & PARAMETERS
// ==========================================
const PRESET = "random"; // Options: "random", "nearly_sorted", "reversed", "few_unique", "custom"
const CUSTOM_INPUT = [64, 34, 25, 12, 22, 11, 90];
const VERBOSE = true;

const DATASETS = {
  random: [45, 12, 89, 34, 70, 23, 56, 91, 18, 62],
  nearly_sorted: [10, 20, 25, 40, 35, 50, 60, 75, 70, 90],
  reversed: [95, 80, 72, 61, 53, 44, 32, 21, 15, 8],
  few_unique: [5, 2, 8, 2, 5, 8, 2, 8, 5, 2],
  custom: CUSTOM_INPUT,
};

function selectionSort(arr, verbose = true) {
  const result = [...arr];
  let step = 1;
  for (let i = 0; i < result.length - 1; i++) {
    let minIdx = i;
    for (let j = i + 1; j < result.length; j++) {
      if (result[j] < result[minIdx]) minIdx = j;
    }
    if (minIdx !== i) {
      if (verbose) console.log(`Step ${String(step++).padStart(2, '0')}: Swap min ${result[minIdx]} with ${result[i]}`);
      [result[i], result[minIdx]] = [result[minIdx], result[i]];
    } else {
      if (verbose) console.log(`Step ${String(step++).padStart(2, '0')}: ${result[i]} is already in place`);
    }
  }
  return result;
}

function main() {
  const arr = DATASETS[PRESET] || CUSTOM_INPUT;
  console.log(`--- Selection Sort Demonstration ---`);
  console.log(`Preset: ${PRESET}`);
  console.log(`Initial Array: [${arr.join(', ')}]\n`);

  const sorted = selectionSort(arr, VERBOSE);

  console.log(`\nFinal Sorted Array: [${sorted.join(', ')}]`);
}

main();
