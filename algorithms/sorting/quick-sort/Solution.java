/**
 * Quick Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/quick-sort
 */
import java.util.Arrays;

public class Solution {
    // RUN CONFIGURATION
    static final String PRESET = "random"; // "random", "nearly_sorted", "reversed", "few_unique"
    static final boolean VERBOSE = true;

    public static int[] quickSort(int[] input, boolean verbose) {
        int[] arr = input.clone();
        sort(arr, 0, arr.length - 1, verbose, new int[]{1});
        return arr;
    }
    private static void sort(int[] arr, int low, int high, boolean verbose, int[] step) {
        if (low < high) {
            int pi = partition(arr, low, high, verbose, step);
            sort(arr, low, pi - 1, verbose, step);
            sort(arr, pi + 1, high, verbose, step);
        }
    }
    private static int partition(int[] arr, int low, int high, boolean verbose, int[] step) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
        if (verbose) System.out.printf("Step %02d: Pivot=%d placed at index %d%n", step[0]++, pivot, i + 1);
        return i + 1;
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

        System.out.println("--- Quick Sort (Java) ---");
        System.out.println("Initial Array: " + Arrays.toString(arr));
        int[] result = quickSort(arr, VERBOSE);
        System.out.println("Sorted Array:  " + Arrays.toString(result));
    }
}
