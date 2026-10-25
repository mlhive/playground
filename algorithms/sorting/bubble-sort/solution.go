// Bubble Sort Implementation
// Reference: https://mlhive.com/playground/algorithms/sorting/bubble-sort
package main

import (
	"fmt"
)

// RUN CONFIGURATION
const (
	Preset  = "random"
	Verbose = true
)

func bubbleSort(arr []int, verbose bool) []int {
	result := make([]int, len(arr))
	copy(result, arr)
	step := 1
	for end := len(result) - 1; end > 0; end-- {
		swapped := false
		for i := 0; i < end; i++ {
			if result[i] > result[i+1] {
				if verbose {
					fmt.Printf("Step %02d: Swap %d and %d\n", step, result[i], result[i+1])
					step++
				}
				result[i], result[i+1] = result[i+1], result[i]
				swapped = true
			} else {
				if verbose {
					fmt.Printf("Step %02d: Compare %d <= %d\n", step, result[i], result[i+1])
					step++
				}
			}
		}
		if !swapped {
			break
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

	fmt.Println("--- Bubble Sort (Go) ---")
	fmt.Printf("Initial Array: %v\n\n", arr)

	sorted := bubbleSort(arr, Verbose)

	fmt.Printf("\nSorted Array: %v\n", sorted)
}
