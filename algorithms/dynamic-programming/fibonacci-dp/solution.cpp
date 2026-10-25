#include <iostream>
#include <vector>

const int N = 10;
const bool VERBOSE = true;

long long fibonacciDp(int n, bool verbose = true) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    std::vector<long long> dp(n + 1, 0);
    dp[0] = 0; dp[1] = 1;
    if (verbose) std::cout << "Step 01: Initialized dp[0]=0, dp[1]=1\n";
    for (int i = 2; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
        if (verbose) std::cout << "Step " << i << ": dp[" << i << "] = " << dp[i-1] << " + " << dp[i-2] << " = " << dp[i] << "\n";
    }
    return dp[n];
}

int main() {
    std::cout << "--- Fibonacci Dynamic Programming (C++) ---\n\n";
    auto result = fibonacciDp(N, VERBOSE);
    std::cout << "\nResult: F(" << N << ") = " << result << "\n";
    return 0;
}
