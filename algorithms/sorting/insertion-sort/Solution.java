/**
 * Insertion Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/insertion-sort
 */
import java.util.Arrays;

public class Solution {
    // RUN CONFIGURATION
    static final String PRESET = "random"; // "random", "nearly_sorted", "reversed", "few_unique"
    static final boolean VERBOSE = true;

    public static int[] insertionSort(int[] input, boolean verbose) {
        int[] arr = input.clone();
        int step = 1;
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            if (verbose) System.out.printf("Step %02d: Insert key=%d%n", step++, key);
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
        return arr;
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

        System.out.println("--- Insertion Sort (Java) ---");
        System.out.println("Initial Array: " + Arrays.toString(arr));
        int[] result = insertionSort(arr, VERBOSE);
        System.out.println("Sorted Array:  " + Arrays.toString(result));
    }
}
