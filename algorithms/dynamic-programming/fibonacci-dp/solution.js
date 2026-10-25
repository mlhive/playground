/**
 * Fibonacci Dynamic Programming Implementation
 * Reference: https://mlhive.com/playground/algorithms/dynamic-programming/fibonacci-dp
 */

const N = 10;
const VERBOSE = true;

function fibonacciDp(n, verbose = true) {
  if (n <= 0) return 0;
  if (n === 1) return 1;
  const dp = new Array(n + 1).fill(0);
  dp[0] = 0;
  dp[1] = 1;

  if (verbose) console.log("Step 01: Initialized DP table dp[0]=0, dp[1]=1");

  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
    if (verbose) console.log(`Step ${String(i).padStart(2, '0')}: dp[${i}] = dp[${i-1}] (${dp[i-1]}) + dp[${i-2}] (${dp[i-2]}) = ${dp[i]}`);
  }
  return dp[n];
}

function main() {
  console.log(`--- Fibonacci Dynamic Programming Demonstration ---`);
  console.log(`Input N = ${N}\n`);
  const result = fibonacciDp(N, VERBOSE);
  console.log(`\nResult: F(${N}) = ${result}`);
}

main();
