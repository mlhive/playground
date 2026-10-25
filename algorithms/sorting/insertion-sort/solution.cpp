/**
 * Insertion Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/insertion-sort
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// RUN CONFIGURATION
const std::string PRESET = "random";
const bool VERBOSE = true;

std::vector<int> insertionSort(std::vector<int> arr, bool verbose = true) {
    int step = 1;
    for (size_t i = 1; i < arr.size(); ++i) {
        int key = arr[i];
        int j = i - 1;
        if (verbose) std::cout << "Step " << step++ << ": Insert key=" << key << "\n";
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
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

    std::cout << "--- Insertion Sort (C++) ---\nInitial Array: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n\n";

    std::vector<int> sorted = insertionSort(arr, VERBOSE);

    std::cout << "\nSorted Array: ";
    for (int x : sorted) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
