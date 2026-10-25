public class Solution {
    static final int N = 10;
    static final boolean VERBOSE = true;

    public static long fibonacciDp(int n, boolean verbose) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        long[] dp = new long[n + 1];
        dp[0] = 0; dp[1] = 1;
        if (verbose) System.out.println("Step 01: Initialized dp[0]=0, dp[1]=1");
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
            if (verbose) System.out.printf("Step %02d: dp[%d] = %d + %d = %d%n", i, i, dp[i-1], dp[i-2], dp[i]);
        }
        return dp[n];
    }

    public static void main(String[] args) {
        System.out.println("--- Fibonacci Dynamic Programming (Java) ---");
        long result = fibonacciDp(N, VERBOSE);
        System.out.printf("%nResult: F(%d) = %d%n", N, result);
    }
}
