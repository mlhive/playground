// Selection Sort Implementation
// Reference: https://mlhive.com/playground/algorithms/sorting/selection-sort
package main

import (
	"fmt"
)

// RUN CONFIGURATION
const (
	Preset  = "random"
	Verbose = true
)

func selectionSort(arr []int, verbose bool) []int {
	result := make([]int, len(arr))
	copy(result, arr)
	step := 1
	for i := 0; i < len(result)-1; i++ {
		minIdx := i
		for j := i + 1; j < len(result); j++ {
			if result[j] < result[minIdx] {
				minIdx = j
			}
		}
		if minIdx != i {
			if verbose {
				fmt.Printf("Step %02d: Swap min %d with %d\n", step, result[minIdx], result[i])
				step++
			}
			result[i], result[minIdx] = result[minIdx], result[i]
		} else {
			if verbose {
				fmt.Printf("Step %02d: %d is already in place\n", step, result[i])
				step++
			}
		}
	}
	return result
}

func main() {
	arr := []int{45, 12, 89, 34, 70, 23, 56, 91, 18, 62}
	if Preset == "reversed" {
		arr = []int{95, 80, 72, 61, 53, 44, 32, 21, 15, 8}
	} else if Preset == "nearly_sorted" {
		arr = []int{10, 20, 25, 40, 35, 50, 60, 75, 70, 90}
	}

	fmt.Println("--- Selection Sort (Go) ---")
	fmt.Printf("Initial Array: %v\n\n", arr)

	sorted := selectionSort(arr, Verbose)

	fmt.Printf("\nSorted Array: %v\n", sorted)
}
