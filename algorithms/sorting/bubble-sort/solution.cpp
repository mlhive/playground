/**
 * Bubble Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/bubble-sort
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// RUN CONFIGURATION
const std::string PRESET = "random";
const bool VERBOSE = true;

std::vector<int> bubbleSort(std::vector<int> arr, bool verbose = true) {
    int step = 1;
    for (int end = arr.size() - 1; end > 0; --end) {
        bool swapped = false;
        for (int i = 0; i < end; ++i) {
            if (arr[i] > arr[i + 1]) {
                if (verbose) std::cout << "Step " << step++ << ": Swap " << arr[i] << " and " << arr[i+1] << "\n";
                std::swap(arr[i], arr[i + 1]);
                swapped = true;
            } else {
                if (verbose) std::cout << "Step " << step++ << ": Compare " << arr[i] << " <= " << arr[i+1] << "\n";
            }
        }
        if (!swapped) break;
    }
    return arr;
}

int main() {
    std::vector<int> arr = {45, 12, 89, 34, 70, 23, 56, 91, 18, 62};
    if (PRESET == "reversed") {
        arr = {95, 80, 72, 61, 53, 44, 32, 21, 15, 8};
    } else if (PRESET == "nearly_sorted") {
        arr = {10, 20, 25, 40, 35, 50, 60, 75, 70, 90};
    }

    std::cout << "--- Bubble Sort (C++) ---\nInitial Array: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n\n";

    std::vector<int> sorted = bubbleSort(arr, VERBOSE);

    std::cout << "\nSorted Array: ";
    for (int x : sorted) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
