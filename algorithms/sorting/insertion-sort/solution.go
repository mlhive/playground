// Insertion Sort Implementation
// Reference: https://mlhive.com/playground/algorithms/sorting/insertion-sort
package main

import (
	"fmt"
)

// RUN CONFIGURATION
const (
	Preset  = "random"
	Verbose = true
)

func insertionSort(arr []int, verbose bool) []int {
	result := make([]int, len(arr))
	copy(result, arr)
	step := 1
	for i := 1; i < len(result); i++ {
		key := result[i]
		j := i - 1
		if verbose {
			fmt.Printf("Step %02d: Insert key=%d\n", step, key)
			step++
		}
		for j >= 0 && result[j] > key {
			result[j+1] = result[j]
			j--
		}
		result[j+1] = key
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

	fmt.Println("--- Insertion Sort (Go) ---")
	fmt.Printf("Initial Array: %v\n\n", arr)

	sorted := insertionSort(arr, Verbose)

	fmt.Printf("\nSorted Array: %v\n", sorted)
}
