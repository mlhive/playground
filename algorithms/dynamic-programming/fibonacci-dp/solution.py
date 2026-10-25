"""
Fibonacci Dynamic Programming (Bottom-Up Tabulation)
Reference: https://mlhive.com/playground/algorithms/dynamic-programming/fibonacci-dp
"""

# RUN CONFIGURATION & PARAMETERS
N = 10         # Target Fibonacci index F(N)
VERBOSE = True # Print intermediate tabulation updates

def fibonacci_dp(n: int, verbose: bool = True) -> int:
    """Computes F(n) in O(n) time and O(n) space using bottom-up tabulation."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # dp[i] stores the i-th Fibonacci number computed so far
    dp = [0] * (n + 1)
    # Base cases: F(0) = 0, F(1) = 1
    dp[0] = 0
    dp[1] = 1

    if verbose:
        print("Step 01: Initialized base cases dp[0]=0, dp[1]=1")

    # Tabulation: compute each subproblem using previously stored results
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        if verbose:
            print(f"Step {i:02d}: Compute dp[{i}] = dp[{i-1}] ({dp[i-1]}) + dp[{i-2}] ({dp[i-2]}) = {dp[i]}")

    return dp[n]

def main():
    print("--- Fibonacci Dynamic Programming ---")
    print(f"Input N = {N}\n")
    result = fibonacci_dp(N, verbose=VERBOSE)
    print(f"\nResult: F({N}) = {result}")

if __name__ == "__main__":
    main()
