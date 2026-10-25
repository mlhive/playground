"""
0/1 Knapsack Problem Implementation
Reference: https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack
"""

# ==========================================
# RUN CONFIGURATION & PARAMETERS
# ==========================================
WEIGHTS = [2, 3, 4, 5]  # Weight of each available item
VALUES = [3, 4, 5, 6]   # Value / profit of each available item
CAPACITY = 5            # Maximum weight capacity of the knapsack
VERBOSE = True          # Log table progression per item

def knapsack(weights: list[int], values: list[int], capacity: int, verbose: bool = True) -> int:
    """
    Solves 0/1 Knapsack using 2D bottom-up tabulation.
    dp[i][cap] represents the maximum value achievable using a subset of the first i items
    with a knapsack capacity of cap.
    """
    n = len(weights)
    # Initialize DP table of dimensions (n + 1) x (capacity + 1) with zeros
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    step = 1
    # Iterate through each item (1-indexed for DP table rows)
    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for cap in range(capacity + 1):
            if w <= cap:
                # Two choices:
                # 1. Exclude item i: value is dp[i - 1][cap]
                # 2. Include item i: value is dp[i - 1][cap - w] + v
                dp[i][cap] = max(dp[i - 1][cap], dp[i - 1][cap - w] + v)
            else:
                # Item weight exceeds current sub-capacity, cannot be included
                dp[i][cap] = dp[i - 1][cap]

        if verbose:
            print(f"Step {step:02d}: Processed item {i} (weight={w}, val={v}) -> Row max: {max(dp[i])}")
            step += 1

    # Optimal value with all n items considered at full capacity W
    return dp[n][capacity]

def main():
    print("--- 0/1 Knapsack Problem Demonstration ---")
    print(f"Weights:  {WEIGHTS}")
    print(f"Values:   {VALUES}")
    print(f"Capacity: {CAPACITY}\n")
    max_val = knapsack(WEIGHTS, VALUES, CAPACITY, verbose=VERBOSE)
    print(f"\nMaximum Knapsack Value: {max_val}")

if __name__ == "__main__":
    main()
