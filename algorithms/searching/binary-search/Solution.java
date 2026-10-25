/**
 * Binary Search Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/binary-search
 */
import java.util.Arrays;

public class Solution {
    static final int TARGET = 50;
    static final boolean VERBOSE = true;

    public static int binarySearch(int[] arr, int target, boolean verbose) {
        int left = 0, right = arr.length - 1;
        int step = 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (verbose) System.out.printf("Step %02d: Range [%d..%d], mid %d (val=%d)%n", step++, left, right, mid, arr[mid]);
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {12, 18, 24, 32, 40, 50, 64, 78, 88, 96};
        System.out.println("--- Binary Search (Java) ---");
        System.out.println("Array:  " + Arrays.toString(arr));
        System.out.println("Target: " + TARGET + "\n");

        int result = binarySearch(arr, TARGET, VERBOSE);
        System.out.println("\nResult: Index " + result + " (Found: " + (result != -1) + ")");
    }
}
