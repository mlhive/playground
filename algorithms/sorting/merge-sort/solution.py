"""
Merge Sort Implementation
Reference: https://mlhive.com/playground/algorithms/sorting/merge-sort
"""

# ==========================================
# RUN CONFIGURATION & PARAMETERS
# ==========================================
PRESET = "random"  # Options: "random", "nearly_sorted", "reversed", "few_unique", "custom"
CUSTOM_INPUT = [64, 34, 25, 12, 22, 11, 90]
SIZE = 10
VERBOSE = True

DATASETS = {
    "random": [45, 12, 89, 34, 70, 23, 56, 91, 18, 62],
    "nearly_sorted": [10, 20, 25, 40, 35, 50, 60, 75, 70, 90],
    "reversed": [95, 80, 72, 61, 53, 44, 32, 21, 15, 8],
    "few_unique": [5, 2, 8, 2, 5, 8, 2, 8, 5, 2],
    "custom": CUSTOM_INPUT,
}

def merge_sort(arr: list[int], verbose: bool = True) -> list[int]:
    step = [1]
    def _sort(lst: list[int]) -> list[int]:
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = _sort(lst[:mid])
        right = _sort(lst[mid:])
        
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        if verbose:
            print(f"Step {step[0]:02d}: Merged {left} and {right} -> {merged}")
            step[0] += 1
        return merged
    return _sort(arr)

def main():
    arr = DATASETS.get(PRESET, CUSTOM_INPUT)
    print(f"--- Merge Sort Demonstration ---")
    print(f"Preset: {PRESET}")
    print(f"Initial Array: {arr}\n")
    
    sorted_arr = merge_sort(arr, verbose=VERBOSE)
    
    print(f"\nFinal Sorted Array: {sorted_arr}")
    print(f"Verified Sorted: {sorted_arr == sorted(arr)}")

if __name__ == "__main__":
    main()
