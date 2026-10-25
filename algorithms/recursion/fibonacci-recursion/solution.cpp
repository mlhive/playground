/**
 * Fibonacci Recursion Implementation
 * Reference: https://mlhive.com/playground/algorithms/recursion/fibonacci-recursion
 */
#include <iostream>
#include <string>

const int N = 5;
const bool VERBOSE = true;

int fibonacci(int n, int depth = 0, bool verbose = true) {
    std::string indent(depth * 2, ' ');
    if (verbose) std::cout << indent << "-> fibonacci(" << n << ") called\n";
    if (n <= 0) return 0;
    if (n == 1) return 1;
    int left = fibonacci(n - 1, depth + 1, verbose);
    int right = fibonacci(n - 2, depth + 1, verbose);
    int res = left + right;
    if (verbose) std::cout << indent << "<- fibonacci(" << n << ") = " << res << "\n";
    return res;
}

int main() {
    std::cout << "--- Fibonacci Recursion (C++) ---\nInput N = " << N << "\n\n";
    auto result = fibonacci(N, 0, VERBOSE);
    std::cout << "\nFinal Result: " << result << "\n";
    return 0;
}
