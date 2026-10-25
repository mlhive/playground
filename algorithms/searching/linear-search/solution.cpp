/**
 * Linear Search Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/linear-search
 */
#include <iostream>
#include <vector>

const int TARGET = 50;
const bool VERBOSE = true;

int linearSearch(const std::vector<int>& arr, int target, bool verbose = true) {
    for (size_t i = 0; i < arr.size(); ++i) {
        if (verbose) std::cout << "Step " << i + 1 << ": Checking index " << i << " (value=" << arr[i] << ")\n";
        if (arr[i] == target) {
            if (verbose) std::cout << "Match found at index " << i << "!\n";
            return i;
        }
    }
    return -1;
}

int main() {
    std::vector<int> arr = {12, 18, 24, 32, 40, 50, 64, 78, 88, 96};
    std::cout << "--- Linear Search (C++) ---\nArray: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\nTarget: " << TARGET << "\n\n";

    int result = linearSearch(arr, TARGET, VERBOSE);
    std::cout << "\nResult: Index " << result << " (Found: " << (result != -1) << ")\n";
    return 0;
}
