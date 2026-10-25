// Binary Search Implementation
// Reference: https://mlhive.com/playground/algorithms/searching/binary-search
package main

import "fmt"

const (
	Target  = 50
	Verbose = true
)

func binarySearch(arr []int, target int, verbose bool) int {
	left, right := 0, len(arr)-1
	step := 1
	for left <= right {
		mid := left + (right-left)/2
		if verbose {
			fmt.Printf("Step %02d: Range [%d..%d], mid %d (val=%d)\n", step, left, right, mid, arr[mid])
			step++
		}
		if arr[mid] == target {
			return mid
		}
		if arr[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}

func main() {
	arr := []int{12, 18, 24, 32, 40, 50, 64, 78, 88, 96}
	fmt.Println("--- Binary Search (Go) ---")
	fmt.Printf("Array:  %v\nTarget: %d\n\n", arr, Target)

	result := binarySearch(arr, Target, Verbose)
	fmt.Printf("\nResult: Index %d (Found: %t)\n", result, result != -1)
}
