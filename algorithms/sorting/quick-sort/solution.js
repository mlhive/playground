/**
 * Quick Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/quick-sort
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

function quickSort(arr, verbose = true) {
  const result = [...arr];
  let step = 1;
  function partition(low, high) {
    const pivot = result[high];
    let i = low - 1;
    for (let j = low; j < high; j++) {
      if (result[j] <= pivot) {
        i++;
        [result[i], result[j]] = [result[j], result[i]];
      }
    }
    [result[i + 1], result[high]] = [result[high], result[i + 1]];
    if (verbose) console.log(`Step ${String(step++).padStart(2, '0')}: Pivot=${pivot} at index ${i+1}`);
    return i + 1;
  }
  function sort(low, high) {
    if (low < high) {
      const pi = partition(low, high);
      sort(low, pi - 1);
      sort(pi + 1, high);
    }
  }
  sort(0, result.length - 1);
  return result;
}

function main() {
  const arr = DATASETS[PRESET] || CUSTOM_INPUT;
  console.log(`--- Quick Sort Demonstration ---`);
  console.log(`Preset: ${PRESET}`);
  console.log(`Initial Array: [${arr.join(', ')}]\n`);

  const sorted = quickSort(arr, VERBOSE);

  console.log(`\nFinal Sorted Array: [${sorted.join(', ')}]`);
}

main();
