// 0/1 Knapsack Problem Implementation
// Reference: https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack
package main

import "fmt"

var (
	weights  = []int{2, 3, 4, 5} // Item weights
	values   = []int{3, 4, 5, 6} // Item values
	capacity = 5               // Knapsack capacity
	verbose  = true
)

func knapsack(weights []int, values []int, capacity int, verbose bool) int {
	n := len(weights)
	// dp[i][cap] represents max value using first i items with capacity cap
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, capacity+1)
	}
	step := 1
	for i := 1; i <= n; i++ {
		w, v := weights[i-1], values[i-1]
		for cap := 0; cap <= capacity; cap++ {
			if w <= cap {
				// Choice: Exclude item vs Include item
				valWith := dp[i-1][cap-w] + v
				if valWith > dp[i-1][cap] {
					dp[i][cap] = valWith
				} else {
					dp[i][cap] = dp[i-1][cap]
				}
			} else {
				dp[i][cap] = dp[i-1][cap]
			}
		}
		if verbose {
			fmt.Printf("Step %02d: Item %d (wt=%d, val=%d)\n", step, i, w, v)
			step++
		}
	}
	return dp[n][capacity]
}

func main() {
	fmt.Println("--- 0/1 Knapsack (Go) ---")
	maxVal := knapsack(weights, values, capacity, verbose)
	fmt.Printf("\nMaximum Knapsack Value: %d\n", maxVal)
}
