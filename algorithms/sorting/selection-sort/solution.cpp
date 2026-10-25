/**
 * Selection Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/selection-sort
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// RUN CONFIGURATION
const std::string PRESET = "random";
const bool VERBOSE = true;

std::vector<int> selectionSort(std::vector<int> arr, bool verbose = true) {
    int step = 1;
    for (size_t i = 0; i < arr.size() - 1; ++i) {
        size_t minIdx = i;
        for (size_t j = i + 1; j < arr.size(); ++j) {
            if (arr[j] < arr[minIdx]) minIdx = j;
        }
        if (minIdx != i) {
            if (verbose) std::cout << "Step " << step++ << ": Swap min " << arr[minIdx] << " with " << arr[i] << "\n";
            std::swap(arr[i], arr[minIdx]);
        } else {
            if (verbose) std::cout << "Step " << step++ << ": " << arr[i] << " is already in place\n";
        }
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

    std::cout << "--- Selection Sort (C++) ---\nInitial Array: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n\n";

    std::vector<int> sorted = selectionSort(arr, VERBOSE);

    std::cout << "\nSorted Array: ";
    for (int x : sorted) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
