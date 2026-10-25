/**
 * Factorial Recursion Implementation
 * Reference: https://mlhive.com/playground/algorithms/recursion/factorial-recursion
 */

// RUN CONFIGURATION
const N = 5;
const VERBOSE = true;

function factorial(n, depth = 0, verbose = true) {
  const indent = "  ".repeat(depth);
  if (verbose) console.log(`${indent}-> factorial(${n}) called [Depth: ${depth}]`);
  if (n <= 1) {
    if (verbose) console.log(`${indent}* Base case reached: factorial(${n}) = 1`);
    return 1;
  }
  const result = n * factorial(n - 1, depth + 1, verbose);
  if (verbose) console.log(`${indent}<- Returning: ${n} * factorial(${n - 1}) = ${result}`);
  return result;
}

function main() {
  console.log(`--- Factorial Recursion Demonstration ---`);
  console.log(`Input N = ${N}\n`);
  const result = factorial(N, 0, VERBOSE);
  console.log(`\nFinal Result: ${result}`);
}

main();
