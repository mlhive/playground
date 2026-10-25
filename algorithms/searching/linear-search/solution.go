// Linear Search Implementation
// Reference: https://mlhive.com/playground/algorithms/searching/linear-search
package main

import "fmt"

const (
	Target  = 50
	Verbose = true
)

func linearSearch(arr []int, target int, verbose bool) int {
	for i, val := range arr {
		if verbose {
			fmt.Printf("Step %02d: Checking index %d (val=%d)\n", i+1, i, val)
		}
		if val == target {
			if verbose {
				fmt.Printf("Match found at index %d!\n", i)
			}
			return i
		}
	}
	return -1
}

func main() {
	arr := []int{12, 18, 24, 32, 40, 50, 64, 78, 88, 96}
	fmt.Println("--- Linear Search (Go) ---")
	fmt.Printf("Array:  %v\nTarget: %d\n\n", arr, Target)

	result := linearSearch(arr, Target, Verbose)
	fmt.Printf("\nResult: Index %d (Found: %t)\n", result, result != -1)
}
