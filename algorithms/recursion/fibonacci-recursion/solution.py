"""
Fibonacci Recursion Implementation
Reference: https://mlhive.com/playground/algorithms/recursion/fibonacci-recursion
"""

N = 5          # Target index n
VERBOSE = True # Log branching call tree

def fibonacci(n: int, depth: int = 0, verbose: bool = True) -> int:
    """Computes F(n) using naive recursive branching."""
    indent = "  " * depth
    if verbose:
        print(f"{indent}-> fibonacci({n}) called")
    # Base cases: F(0) = 0, F(1) = 1
    if n <= 0:
        return 0
    if n == 1:
        if verbose:
            print(f"{indent}* Base case: fibonacci(1) = 1")
        return 1
    # Branching recursive step: divide problem into two subproblems
    left = fibonacci(n - 1, depth + 1, verbose)
    right = fibonacci(n - 2, depth + 1, verbose)
    result = left + right
    if verbose:
        print(f"{indent}<- fibonacci({n}) = {left} + {right} = {result}")
    return result

def main():
    print("--- Fibonacci Recursion Demonstration ---")
    print(f"Input N = {N}\n")
    result = fibonacci(N, depth=0, verbose=VERBOSE)
    print(f"\nFinal Result: {result}")

if __name__ == "__main__":
    main()
