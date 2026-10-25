/**
 * Binary Search Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/binary-search
 */
#include <iostream>
#include <vector>

const int TARGET = 50;
const bool VERBOSE = true;

int binarySearch(const std::vector<int>& arr, int target, bool verbose = true) {
    int left = 0, right = arr.size() - 1;
    int step = 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (verbose) std::cout << "Step " << step++ << ": Range [" << left << ".." << right << "], mid " << mid << " (val=" << arr[mid] << ")\n";
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    std::vector<int> arr = {12, 18, 24, 32, 40, 50, 64, 78, 88, 96};
    std::cout << "--- Binary Search (C++) ---\nArray: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\nTarget: " << TARGET << "\n\n";

    int result = binarySearch(arr, TARGET, VERBOSE);
    std::cout << "\nResult: Index " << result << " (Found: " << (result != -1) << ")\n";
    return 0;
}
