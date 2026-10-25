/**
 * Merge Sort Implementation
 * Reference: https://mlhive.com/playground/algorithms/sorting/merge-sort
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// RUN CONFIGURATION
const std::string PRESET = "random";
const bool VERBOSE = true;

void merge(std::vector<int>& arr, int l, int m, int r, bool verbose, int& step) {
    std::vector<int> L(arr.begin() + l, arr.begin() + m + 1);
    std::vector<int> R(arr.begin() + m + 1, arr.begin() + r + 1);
    size_t i = 0, j = 0, k = l;
    while (i < L.size() && j < R.size()) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < L.size()) arr[k++] = L[i++];
    while (j < R.size()) arr[k++] = R[j++];
    if (verbose) std::cout << "Step " << step++ << ": Merged range [" << l << ".." << r << "]\n";
}
void mergeSortHelper(std::vector<int>& arr, int l, int r, bool verbose, int& step) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSortHelper(arr, l, m, verbose, step);
        mergeSortHelper(arr, m + 1, r, verbose, step);
        merge(arr, l, m, r, verbose, step);
    }
}
std::vector<int> mergeSort(std::vector<int> arr, bool verbose = true) {
    int step = 1;
    mergeSortHelper(arr, 0, arr.size() - 1, verbose, step);
    return arr;
}

int main() {
    std::vector<int> arr = {45, 12, 89, 34, 70, 23, 56, 91, 18, 62};
    if (PRESET == "reversed") {
        arr = {95, 80, 72, 61, 53, 44, 32, 21, 15, 8};
    } else if (PRESET == "nearly_sorted") {
        arr = {10, 20, 25, 40, 35, 50, 60, 75, 70, 90};
    }

    std::cout << "--- Merge Sort (C++) ---\nInitial Array: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\n\n";

    std::vector<int> sorted = mergeSort(arr, VERBOSE);

    std::cout << "\nSorted Array: ";
    for (int x : sorted) std::cout << x << " ";
    std::cout << "\n";
    return 0;
}
