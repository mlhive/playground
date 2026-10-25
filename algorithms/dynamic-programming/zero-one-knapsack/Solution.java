/**
 * 0/1 Knapsack Problem Implementation
 * Reference: https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack
 */
public class Solution {
    // RUN CONFIGURATION & PARAMETERS
    static final int[] WEIGHTS = {2, 3, 4, 5}; // Item weights
    static final int[] VALUES = {3, 4, 5, 6};  // Item values
    static final int CAPACITY = 5;           // Knapsack capacity
    static final boolean VERBOSE = true;

    public static int knapsack(int[] weights, int[] values, int capacity, boolean verbose) {
        int n = weights.length;
        // dp[i][cap] represents max value using first i items with capacity cap
        int[][] dp = new int[n + 1][capacity + 1];
        int step = 1;

        for (int i = 1; i <= n; i++) {
            int w = weights[i - 1], v = values[i - 1];
            for (int cap = 0; cap <= capacity; cap++) {
                if (w <= cap) {
                    // Choice: Exclude item vs Include item
                    dp[i][cap] = Math.max(dp[i - 1][cap], dp[i - 1][cap - w] + v);
                } else {
                    // Item exceeds current capacity
                    dp[i][cap] = dp[i - 1][cap];
                }
            }
            if (verbose) System.out.printf("Step %02d: Item %d (wt=%d, val=%d)%n", step++, i, w, v);
        }
        return dp[n][capacity];
    }

    public static void main(String[] args) {
        System.out.println("--- 0/1 Knapsack (Java) ---");
        int maxVal = knapsack(WEIGHTS, VALUES, CAPACITY, VERBOSE);
        System.out.printf("%nMaximum Knapsack Value: %d%n", maxVal);
    }
}
