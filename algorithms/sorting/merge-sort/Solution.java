/**
 * Merge Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/merge-sort
 */
import java.util.Arrays;

public class Solution {
    // RUN CONFIGURATION
    static final String PRESET = "random"; // "random", "nearly_sorted", "reversed", "few_unique"
    static final boolean VERBOSE = true;

    public static int[] mergeSort(int[] input, boolean verbose) {
        int[] arr = input.clone();
        sort(arr, 0, arr.length - 1, verbose, new int[]{1});
        return arr;
    }
    private static void sort(int[] arr, int l, int r, boolean verbose, int[] step) {
        if (l < r) {
            int m = l + (r - l) / 2;
            sort(arr, l, m, verbose, step);
            sort(arr, m + 1, r, verbose, step);
            merge(arr, l, m, r, verbose, step);
        }
    }
    private static void merge(int[] arr, int l, int m, int r, boolean verbose, int[] step) {
        int n1 = m - l + 1, n2 = r - m;
        int[] L = new int[n1], R = new int[n2];
        System.arraycopy(arr, l, L, 0, n1);
        System.arraycopy(arr, m + 1, R, 0, n2);
        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
        if (verbose) System.out.printf("Step %02d: Merged range [%d..%d]%n", step[0]++, l, r);
    }

    public static void main(String[] args) {
        int[] arr;
        switch (PRESET) {
            case "nearly_sorted":
                arr = new int[]{10, 20, 25, 40, 35, 50, 60, 75, 70, 90};
                break;
            case "reversed":
                arr = new int[]{95, 80, 72, 61, 53, 44, 32, 21, 15, 8};
                break;
            case "few_unique":
                arr = new int[]{5, 2, 8, 2, 5, 8, 2, 8, 5, 2};
                break;
            default:
                arr = new int[]{45, 12, 89, 34, 70, 23, 56, 91, 18, 62};
                break;
        }

        System.out.println("--- Merge Sort (Java) ---");
        System.out.println("Initial Array: " + Arrays.toString(arr));
        int[] result = mergeSort(arr, VERBOSE);
        System.out.println("Sorted Array:  " + Arrays.toString(result));
    }
}
