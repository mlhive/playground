/**
 * Fibonacci Recursion Implementation
 * Reference: https://mlhive.com/playground/algorithms/recursion/fibonacci-recursion
 */
public class Solution {
    static final int N = 5;
    static final boolean VERBOSE = true;

    public static int fibonacci(int n, int depth, boolean verbose) {
        String indent = "  ".repeat(depth);
        if (verbose) System.out.printf("%s-> fibonacci(%d) called%n", indent, n);
        if (n <= 0) return 0;
        if (n == 1) return 1;
        int left = fibonacci(n - 1, depth + 1, verbose);
        int right = fibonacci(n - 2, depth + 1, verbose);
        int res = left + right;
        if (verbose) System.out.printf("%s<- fibonacci(%d) = %d%n", indent, n, res);
        return res;
    }

    public static void main(String[] args) {
        System.out.println("--- Fibonacci Recursion (Java) ---");
        System.out.printf("Input N = %d%n%n", N);
        long result = fibonacci(N, 0, VERBOSE);
        System.out.printf("%nFinal Result: %d%n", result);
    }
}
