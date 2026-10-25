// Factorial Recursion Implementation
// Reference: https://mlhive.com/playground/algorithms/recursion/factorial-recursion
package main

import (
	"fmt"
	"strings"
)

const (
	N       = 5
	Verbose = true
)

func factorial(n int, depth int, verbose bool) int64 {
	indent := strings.Repeat("  ", depth)
	if verbose {
		fmt.Printf("%s-> factorial(%d) called [Depth: %d]\n", indent, n, depth)
	}
	if n <= 1 {
		if verbose {
			fmt.Printf("%s* Base case reached: factorial(%d) = 1\n", indent, n)
		}
		return 1
	}
	result := int64(n) * factorial(n-1, depth+1, verbose)
	if verbose {
		fmt.Printf("%s<- Returning: %d * factorial(%d) = %d\n", indent, n, n-1, result)
	}
	return result
}

func main() {
	fmt.Printf("--- Factorial Recursion (Go) ---\nInput N = %d\n\n", N)
	result := factorial(N, 0, Verbose)
	fmt.Printf("\nFinal Result: %d\n", result)
}
