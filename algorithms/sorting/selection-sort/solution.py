"""
Selection Sort Implementation
Reference: https://mlhive.com/playground/algorithms/sorting/selection-sort
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

def selection_sort(arr: list[int], verbose: bool = True) -> list[int]:
    n = len(arr)
    arr = list(arr)
    step = 1
    for i in range(n - 1):
        # Find index of minimum element in unsorted subarray [i..n-1]
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap minimum element into its correct sorted position at index i
        if min_idx != i:
            if verbose:
                print(f"Step {step:02d}: Swap min arr[{min_idx}]={arr[min_idx]} with arr[{i}]={arr[i]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            if verbose:
                print(f"Step {step:02d}: Element arr[{i}]={arr[i]} is already in place")
        step += 1
    return arr

def main():
    arr = DATASETS.get(PRESET, CUSTOM_INPUT)
    print(f"--- Selection Sort Demonstration ---")
    print(f"Preset: {PRESET}")
    print(f"Initial Array: {arr}\n")
    
    sorted_arr = selection_sort(arr, verbose=VERBOSE)
    
    print(f"\nFinal Sorted Array: {sorted_arr}")
    print(f"Verified Sorted: {sorted_arr == sorted(arr)}")

if __name__ == "__main__":
    main()
