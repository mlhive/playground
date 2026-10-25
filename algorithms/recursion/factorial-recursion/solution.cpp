/**
 * Factorial Recursion Implementation
 * Reference: https://mlhive.com/playground/algorithms/recursion/factorial-recursion
 */
#include <iostream>
#include <string>

const int N = 5;
const bool VERBOSE = true;

long long factorial(int n, int depth = 0, bool verbose = true) {
    std::string indent(depth * 2, ' ');
    if (verbose) std::cout << indent << "-> factorial(" << n << ") called [Depth: " << depth << "]\n";
    if (n <= 1) {
        if (verbose) std::cout << indent << "* Base case reached: factorial(" << n << ") = 1\n";
        return 1;
    }
    long long result = n * factorial(n - 1, depth + 1, verbose);
    if (verbose) std::cout << indent << "<- Returning: " << n << " * factorial(" << n - 1 << ") = " << result << "\n";
    return result;
}

int main() {
    std::cout << "--- Factorial Recursion (C++) ---\nInput N = " << N << "\n\n";
    auto result = factorial(N, 0, VERBOSE);
    std::cout << "\nFinal Result: " << result << "\n";
    return 0;
}
