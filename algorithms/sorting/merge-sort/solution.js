/**
 * Merge Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/merge-sort
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

function mergeSort(arr, verbose = true) {
  let step = 1;
  function sort(list) {
    if (list.length <= 1) return list;
    const mid = Math.floor(list.length / 2);
    const left = sort(list.slice(0, mid));
    const right = sort(list.slice(mid));
    const merged = [];
    let i = 0, j = 0;
    while (i < left.length && j < right.length) {
      if (left[i] <= right[j]) merged.push(left[i++]);
      else merged.push(right[j++]);
    }
    const res = merged.concat(left.slice(i)).concat(right.slice(j));
    if (verbose) console.log(`Step ${String(step++).padStart(2, '0')}: Merge [${left}] and [${right}] -> [${res}]`);
    return res;
  }
  return sort(arr);
}

function main() {
  const arr = DATASETS[PRESET] || CUSTOM_INPUT;
  console.log(`--- Merge Sort Demonstration ---`);
  console.log(`Preset: ${PRESET}`);
  console.log(`Initial Array: [${arr.join(', ')}]\n`);

  const sorted = mergeSort(arr, VERBOSE);

  console.log(`\nFinal Sorted Array: [${sorted.join(', ')}]`);
}

main();
