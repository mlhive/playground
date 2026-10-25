// Merge Sort Implementation
// Reference: https://mlhive.com/playground/algorithms/sorting/merge-sort
package main

import (
	"fmt"
)

// RUN CONFIGURATION
const (
	Preset  = "random"
	Verbose = true
)

func mergeSort(arr []int, verbose bool) []int {
	step := 1
	var sort func([]int) []int
	sort = func(list []int) []int {
		if len(list) <= 1 {
			return list
		}
		mid := len(list) / 2
		left := sort(list[:mid])
		right := sort(list[mid:])
		merged := make([]int, 0, len(left)+len(right))
		i, j := 0, 0
		for i < len(left) && j < len(right) {
			if left[i] <= right[j] {
				merged = append(merged, left[i])
				i++
			} else {
				merged = append(merged, right[j])
				j++
			}
		}
		merged = append(merged, left[i:]...)
		merged = append(merged, right[j:]...)
		if verbose {
			fmt.Printf("Step %02d: Merged %v and %v -> %v\n", step, left, right, merged)
			step++
		}
		return merged
	}
	return sort(arr)
}

func main() {
	arr := []int{45, 12, 89, 34, 70, 23, 56, 91, 18, 62}
	if Preset == "reversed" {
		arr = []int{95, 80, 72, 61, 53, 44, 32, 21, 15, 8}
	} else if Preset == "nearly_sorted" {
		arr = []int{10, 20, 25, 40, 35, 50, 60, 75, 70, 90}
	}

	fmt.Println("--- Merge Sort (Go) ---")
	fmt.Printf("Initial Array: %v\n\n", arr)

	sorted := mergeSort(arr, Verbose)

	fmt.Printf("\nSorted Array: %v\n", sorted)
}
