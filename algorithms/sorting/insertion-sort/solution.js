/**
 * Insertion Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/insertion-sort
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

function insertionSort(arr, verbose = true) {
  const result = [...arr];
  let step = 1;
  for (let i = 1; i < result.length; i++) {
    const key = result[i];
    let j = i - 1;
    if (verbose) console.log(`Step ${String(step++).padStart(2, '0')}: Insert key=${key}`);
    while (j >= 0 && result[j] > key) {
      result[j + 1] = result[j];
      j--;
    }
    result[j + 1] = key;
  }
  return result;
}

function main() {
  const arr = DATASETS[PRESET] || CUSTOM_INPUT;
  console.log(`--- Insertion Sort Demonstration ---`);
  console.log(`Preset: ${PRESET}`);
  console.log(`Initial Array: [${arr.join(', ')}]\n`);

  const sorted = insertionSort(arr, VERBOSE);

  console.log(`\nFinal Sorted Array: [${sorted.join(', ')}]`);
}

main();
