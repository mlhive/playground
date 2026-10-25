/**
 * 0/1 Knapsack Problem Implementation
 * Reference: https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack
 */

// RUN CONFIGURATION & PARAMETERS
const WEIGHTS = [2, 3, 4, 5]; // Weight of each available item
const VALUES = [3, 4, 5, 6];  // Value of each available item
const CAPACITY = 5;           // Maximum knapsack weight capacity
const VERBOSE = true;

function knapsack(weights, values, capacity, verbose = true) {
  const n = weights.length;
  // Initialize DP table: dp[i][cap] stores max value using first i items with capacity cap
  const dp = Array.from({ length: n + 1 }, () => new Array(capacity + 1).fill(0));

  let step = 1;
  for (let i = 1; i <= n; i++) {
    const w = weights[i - 1];
    const v = values[i - 1];
    for (let cap = 0; cap <= capacity; cap++) {
      if (w <= cap) {
        // Choice: Exclude item vs Include item and add its value
        dp[i][cap] = Math.max(dp[i - 1][cap], dp[i - 1][cap - w] + v);
      } else {
        // Item cannot fit into current sub-capacity
        dp[i][cap] = dp[i - 1][cap];
      }
    }
    if (verbose) {
      console.log(`Step ${String(step++).padStart(2, '0')}: Item ${i} (wt=${w}, val=${v}) -> Max: ${Math.max(...dp[i])}`);
    }
  }
  // Optimal value using all n items at full knapsack capacity
  return dp[n][capacity];
}

function main() {
  console.log("--- 0/1 Knapsack Problem Demonstration ---");
  console.log(`Weights:  [${WEIGHTS.join(', ')}]`);
  console.log(`Values:   [${VALUES.join(', ')}]`);
  console.log(`Capacity: ${CAPACITY}\n`);
  const maxVal = knapsack(WEIGHTS, VALUES, CAPACITY, VERBOSE);
  console.log(`\nMaximum Knapsack Value: ${maxVal}`);
}

main();
