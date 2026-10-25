"""
Binary Search Implementation
Reference: https://mlhive.com/playground/algorithms/searching/binary-search
"""

# ==========================================
# RUN CONFIGURATION & PARAMETERS
# ==========================================
TARGET = 50
PRESET = "sorted_standard"  # "sorted_standard", "target_absent", "custom"
VERBOSE = True

DATASETS = {
    "sorted_standard": [12, 18, 24, 32, 40, 50, 64, 78, 88, 96],
    "target_absent": [10, 20, 30, 40, 60, 70, 80, 90, 100],
    "custom": [15, 25, 35, 45, 50, 55, 65, 75],
}

def binary_search(arr: list[int], target: int, verbose: bool = True) -> int:
    left, right = 0, len(arr) - 1
    step = 1
    while left <= right:
        # Calculate midpoint avoiding overflow
        mid = (left + right) // 2
        mid_val = arr[mid]
        if verbose:
            print(f"Step {step:02d}: Range [{left}..{right}], mid index {mid} (value={mid_val})")
        step += 1
        if mid_val == target:
            if verbose:
                print(f"Match found at index {mid}!")
            return mid # Target found at midpoint
        elif mid_val < target:
            # Target is larger: discard left half and search right half
            if verbose:
                print(f"  {mid_val} < {target} -> Search right half")
            left = mid + 1
        else:
            # Target is smaller: discard right half and search left half
            if verbose:
                print(f"  {mid_val} > {target} -> Search left half")
            right = mid - 1
    # Search space exhausted without match
    if verbose:
        print(f"Target {target} not found in array.")
    return -1

def main():
    arr = DATASETS.get(PRESET, DATASETS["sorted_standard"])
    print(f"--- Binary Search Demonstration ---")
    print(f"Array:  {arr}")
    print(f"Target: {TARGET}\n")

    result = binary_search(arr, TARGET, verbose=VERBOSE)
    print(f"\nResult: Index {result} (Found: {result != -1})")

if __name__ == "__main__":
    main()
