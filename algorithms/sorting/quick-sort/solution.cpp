/**
 * Quick Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/quick-sort
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// RUN CONFIGURATION
const std::string PRESET = "random";
const bool VERBOSE = true;

int partition(std::vector<int>& arr, int low, int high, bool verbose, int& step) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; ++j) {
        if (arr[j] <= pivot) {
            ++i;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    if (verbose) std::cout << "Step " << step++ << ": Pivot=" << pivot << " placed at index " << i + 1 << "\n";
    return i + 1;
}
void quickSortHelper(std::vector<int>& arr, int low, int high, bool verbose, int& step) {
    if (low < high) {
        int pi = partition(arr, low, high, verbose, step);
        quickSortHelper(arr, low, pi - 1, verbose, step);
        quickSortHelper(arr, pi + 1, high, verbose, step);
    }
}
std::vector<int> quickSort(std::vector<int> arr, bool verbose = true) {
    int step = 1;
    quickSortHelper(arr, 0, arr.size() - 1, verbose, step);
    return arr;
}

int main() {
    std::vector<int> arr = {45, 12, 89, 34, 70, 23, 56, 91, 18, 62};
    if (PRESET == "reversed") {
        arr = {95, 80, 72, 61, 53, 44, 32, 21, 15, 8};
    } else if (PRESET == "nearly_sorted") {
        arr = {10, 20, 25, 40, 35, 50, 60, 75, 70, 90};
    }

    std::cout << "--- Quick Sort (C++) ---\nInitial Array: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n\n";

    std::vector<int> sorted = quickSort(arr, VERBOSE);

    std::cout << "\nSorted Array: ";
    for (int x : sorted) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
