/**
 * Linear Search Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/linear-search
 */

// RUN CONFIGURATION
const TARGET = 50;
const PRESET = "sorted_standard"; // "sorted_standard", "target_absent", "custom"
const VERBOSE = true;

const DATASETS = {
  sorted_standard: [12, 18, 24, 32, 40, 50, 64, 78, 88, 96],
  target_absent: [10, 20, 30, 40, 60, 70, 80, 90, 100],
  custom: [15, 25, 35, 45, 50, 55, 65, 75],
};

function linearSearch(arr, target, verbose = true) {
  for (let i = 0; i < arr.length; i++) {
    if (verbose) console.log(`Step ${String(i + 1).padStart(2, '0')}: Checking index ${i} (value=${arr[i]})`);
    if (arr[i] === target) {
      if (verbose) console.log(`Match found at index ${i}!`);
      return i;
    }
  }
  return -1;
}

function main() {
  const arr = DATASETS[PRESET] || DATASETS.sorted_standard;
  console.log(`--- Linear Search Demonstration ---`);
  console.log(`Array:  [${arr.join(', ')}]`);
  console.log(`Target: ${TARGET}\n`);

  const result = linearSearch(arr, TARGET, VERBOSE);
  console.log(`\nResult: Index ${result} (Found: ${result !== -1})`);
}

main();
