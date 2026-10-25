/**
 * Binary Search Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/binary-search
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

function binarySearch(arr, target, verbose = true) {
  let left = 0, right = arr.length - 1;
  let step = 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (verbose) console.log(`Step ${String(step++).padStart(2, '0')}: Range [${left}..${right}], mid index ${mid} (val=${arr[mid]})`);
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}

function main() {
  const arr = DATASETS[PRESET] || DATASETS.sorted_standard;
  console.log(`--- Binary Search Demonstration ---`);
  console.log(`Array:  [${arr.join(', ')}]`);
  console.log(`Target: ${TARGET}\n`);

  const result = binarySearch(arr, TARGET, VERBOSE);
  console.log(`\nResult: Index ${result} (Found: ${result !== -1})`);
}

main();
