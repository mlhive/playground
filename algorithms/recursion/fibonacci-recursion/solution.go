// Fibonacci Recursion Implementation
// Reference: https://mlhive.com/playground/algorithms/recursion/fibonacci-recursion
package main

import (
	"fmt"
	"strings"
)

const (
	N       = 5
	Verbose = true
)

func fibonacci(n int, depth int, verbose bool) int {
	indent := strings.Repeat("  ", depth)
	if verbose {
		fmt.Printf("%s-> fibonacci(%d) called\n", indent, n)
	}
	if n <= 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	left := fibonacci(n-1, depth+1, verbose)
	right := fibonacci(n-2, depth+1, verbose)
	res := left + right
	if verbose {
		fmt.Printf("%s<- fibonacci(%d) = %d\n", indent, n, res)
	}
	return res
}

func main() {
	fmt.Printf("--- Fibonacci Recursion (Go) ---\nInput N = %d\n\n", N)
	result := fibonacci(N, 0, Verbose)
	fmt.Printf("\nFinal Result: %d\n", result)
}
