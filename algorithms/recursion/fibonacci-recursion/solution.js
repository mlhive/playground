/**
 * Fibonacci Recursion Implementation
 * Reference: https://mlhive.com/playground/algorithms/recursion/fibonacci-recursion
 */

// RUN CONFIGURATION
const N = 5;
const VERBOSE = true;

function fibonacci(n, depth = 0, verbose = true) {
  const indent = "  ".repeat(depth);
  if (verbose) console.log(`${indent}-> fibonacci(${n}) called`);
  if (n <= 0) return 0;
  if (n === 1) return 1;
  const left = fibonacci(n - 1, depth + 1, verbose);
  const right = fibonacci(n - 2, depth + 1, verbose);
  const result = left + right;
  if (verbose) console.log(`${indent}<- fibonacci(${n}) = ${result}`);
  return result;
}

function main() {
  console.log(`--- Fibonacci Recursion Demonstration ---`);
  console.log(`Input N = ${N}\n`);
  const result = fibonacci(N, 0, VERBOSE);
  console.log(`\nFinal Result: ${result}`);
}

main();
