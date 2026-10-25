"""
Linear Search Implementation
Reference: https://mlhive.com/playground/algorithms/searching/linear-search
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

def linear_search(arr: list[int], target: int, verbose: bool = True) -> int:
    # Sequentially check each element from left to right
    for index, value in enumerate(arr):
        if verbose:
            print(f"Step {index+1:02d}: Checking index {index} (value={value}) against target={target}")
        if value == target:
            if verbose:
                print(f"Match found at index {index}!")
            return index # Target found, return matching index
    # Traversed entire array without match
    if verbose:
        print(f"Target {target} not found in array.")
    return -1

def main():
    arr = DATASETS.get(PRESET, DATASETS["sorted_standard"])
    print(f"--- Linear Search Demonstration ---")
    print(f"Array:  {arr}")
    print(f"Target: {TARGET}\n")

    result = linear_search(arr, TARGET, verbose=VERBOSE)
    print(f"\nResult: Index {result} (Found: {result != -1})")

if __name__ == "__main__":
    main()
