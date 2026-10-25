// Quick Sort Implementation
// Reference: https://mlhive.com/playground/algorithms/sorting/quick-sort
package main

import (
	"fmt"
)

// RUN CONFIGURATION
const (
	Preset  = "random"
	Verbose = true
)

func quickSort(arr []int, verbose bool) []int {
	result := make([]int, len(arr))
	copy(result, arr)
	step := 1
	var partition func(int, int) int
	partition = func(low, high int) int {
		pivot := result[high]
		i := low - 1
		for j := low; j < high; j++ {
			if result[j] <= pivot {
				i++
				result[i], result[j] = result[j], result[i]
			}
		}
		result[i+1], result[high] = result[high], result[i+1]
		if verbose {
			fmt.Printf("Step %02d: Pivot=%d at index %d\n", step, pivot, i+1)
			step++
		}
		return i + 1
	}
	var sort func(int, int)
	sort = func(low, high int) {
		if low < high {
			pi := partition(low, high)
			sort(low, pi-1)
			sort(pi+1, high)
		}
	}
	sort(0, len(result)-1)
	return result
}

func main() {
	arr := []int{45, 12, 89, 34, 70, 23, 56, 91, 18, 62}
	if Preset == "reversed" {
		arr = []int{95, 80, 72, 61, 53, 44, 32, 21, 15, 8}
	} else if Preset == "nearly_sorted" {
		arr = []int{10, 20, 25, 40, 35, 50, 60, 75, 70, 90}
	}

	fmt.Println("--- Quick Sort (Go) ---")
	fmt.Printf("Initial Array: %v\n\n", arr)

	sorted := quickSort(arr, Verbose)

	fmt.Printf("\nSorted Array: %v\n", sorted)
}
