/**
 * 0/1 Knapsack Problem Implementation
 * Reference: https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack
 */
#include <iostream>
#include <vector>
#include <algorithm>

// RUN CONFIGURATION & PARAMETERS
const std::vector<int> WEIGHTS = {2, 3, 4, 5}; // Item weights
const std::vector<int> VALUES = {3, 4, 5, 6};  // Item values
const int CAPACITY = 5;                        // Knapsack capacity
const bool VERBOSE = true;

int knapsack(const std::vector<int>& weights, const std::vector<int>& values, int capacity, bool verbose = true) {
    int n = weights.size();
    // dp[i][cap] represents max value using first i items with capacity cap
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(capacity + 1, 0));
    int step = 1;

    for (int i = 1; i <= n; ++i) {
        int w = weights[i - 1], v = values[i - 1];
        for (int cap = 0; cap <= capacity; ++cap) {
            if (w <= cap) {
                // Choice: Exclude item vs Include item
                dp[i][cap] = std::max(dp[i - 1][cap], dp[i - 1][cap - w] + v);
            } else {
                // Item exceeds capacity
                dp[i][cap] = dp[i - 1][cap];
            }
        }
        if (verbose) std::cout << "Step " << step++ << ": Item " << i << " (wt=" << w << ", val=" << v << ")\n";
    }
    return dp[n][capacity];
}

int main() {
    std::cout << "--- 0/1 Knapsack (C++) ---\n\n";
    int maxVal = knapsack(WEIGHTS, VALUES, CAPACITY, VERBOSE);
    std::cout << "\nMaximum Knapsack Value: " << maxVal << "\n";
    return 0;
}
