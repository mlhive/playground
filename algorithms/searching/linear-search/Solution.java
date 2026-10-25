/**
 * Linear Search Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/linear-search
 */
import java.util.Arrays;

public class Solution {
    static final int TARGET = 50;
    static final boolean VERBOSE = true;

    public static int linearSearch(int[] arr, int target, boolean verbose) {
        for (int i = 0; i < arr.length; i++) {
            if (verbose) System.out.printf("Step %02d: Checking index %d (value=%d)%n", i + 1, i, arr[i]);
            if (arr[i] == target) {
                if (verbose) System.out.println("Match found at index " + i + "!");
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {12, 18, 24, 32, 40, 50, 64, 78, 88, 96};
        System.out.println("--- Linear Search (Java) ---");
        System.out.println("Array:  " + Arrays.toString(arr));
        System.out.println("Target: " + TARGET + "\n");

        int result = linearSearch(arr, TARGET, VERBOSE);
        System.out.println("\nResult: Index " + result + " (Found: " + (result != -1) + ")");
    }
}
