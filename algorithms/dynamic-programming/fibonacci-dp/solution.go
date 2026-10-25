package main

import "fmt"

const (
	N       = 10
	Verbose = true
)

func fibonacciDp(n int, verbose bool) int64 {
	if n <= 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	dp := make([]int64, n+1)
	dp[0], dp[1] = 0, 1
	if verbose {
		fmt.Println("Step 01: Initialized dp[0]=0, dp[1]=1")
	}
	for i := 2; i <= n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
		if verbose {
			fmt.Printf("Step %02d: dp[%d] = %d + %d = %d\n", i, i, dp[i-1], dp[i-2], dp[i])
		}
	}
	return dp[n]
}

func main() {
	fmt.Printf("--- Fibonacci Dynamic Programming (Go) ---\n\n")
	result := fibonacciDp(N, Verbose)
	fmt.Printf("\nResult: F(%d) = %d\n", N, result)
}
