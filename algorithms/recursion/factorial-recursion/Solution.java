/**
 * Factorial Recursion Implementation
 * Reference: https://mlhive.com/playground/algorithms/recursion/factorial-recursion
 */
public class Solution {
    static final int N = 5;
    static final boolean VERBOSE = true;

    public static long factorial(int n, int depth, boolean verbose) {
        String indent = "  ".repeat(depth);
        if (verbose) System.out.printf("%s-> factorial(%d) called [Depth: %d]%n", indent, n, depth);
        if (n <= 1) {
            if (verbose) System.out.printf("%s* Base case reached: factorial(%d) = 1%n", indent, n);
            return 1;
        }
        long result = n * factorial(n - 1, depth + 1, verbose);
        if (verbose) System.out.printf("%s<- Returning: %d * factorial(%d) = %d%n", indent, n, n - 1, result);
        return result;
    }

    public static void main(String[] args) {
        System.out.println("--- Factorial Recursion (Java) ---");
        System.out.printf("Input N = %d%n%n", N);
        long result = factorial(N, 0, VERBOSE);
        System.out.printf("%nFinal Result: %d%n", result);
    }
}
