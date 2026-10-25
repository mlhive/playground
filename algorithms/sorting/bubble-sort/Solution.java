/**
 * Bubble Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/bubble-sort
 */
import java.util.Arrays;

public class Solution {
    // RUN CONFIGURATION
    static final String PRESET = "random"; // "random", "nearly_sorted", "reversed", "few_unique"
    static final boolean VERBOSE = true;

    public static int[] bubbleSort(int[] input, boolean verbose) {
        int[] arr = input.clone();
        int step = 1;
        for (int end = arr.length - 1; end > 0; end--) {
            boolean swapped = false;
            for (int i = 0; i < end; i++) {
                if (arr[i] > arr[i + 1]) {
                    if (verbose) System.out.printf("Step %02d: Swap %d and %d%n", step++, arr[i], arr[i + 1]);
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    swapped = true;
                } else {
                    if (verbose) System.out.printf("Step %02d: Compare %d <= %d%n", step++, arr[i], arr[i + 1]);
                }
            }
            if (!swapped) break;
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

        System.out.println("--- Bubble Sort (Java) ---");
        System.out.println("Initial Array: " + Arrays.toString(arr));
        int[] result = bubbleSort(arr, VERBOSE);
        System.out.println("Sorted Array:  " + Arrays.toString(result));
    }
}
