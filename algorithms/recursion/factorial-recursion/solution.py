"""
Factorial Recursion Implementation
Reference: https://mlhive.com/playground/algorithms/recursion/factorial-recursion
"""

N = 5          # Target integer n to compute n!
VERBOSE = True # Log call stack push and pop operations

def factorial(n: int, depth: int = 0, verbose: bool = True) -> int:
    """Computes n! = n * (n-1)! recursively, tracing stack depth."""
    indent = "  " * depth
    if verbose:
        print(f"{indent}-> factorial({n}) called [Stack Depth: {depth}]")
    
    # Base case: 0! = 1, 1! = 1 (halts recursive calls to prevent stack overflow)
    if n <= 1:
        if verbose:
            print(f"{indent}* Base case reached: factorial({n}) = 1")
        return 1
        
    # Recursive step: push factorial(n - 1) onto call stack
    result = n * factorial(n - 1, depth + 1, verbose)
    # Unwinding: return accumulated product back up the call stack
    if verbose:
        print(f"{indent}<- Returning: {n} * factorial({n-1}) = {result}")
    return result

def main():
    print("--- Factorial Recursion Demonstration ---")
    print(f"Input N = {N}\n")
    result = factorial(N, depth=0, verbose=VERBOSE)
    print(f"\nFinal Result: {result}")

if __name__ == "__main__":
    main()
