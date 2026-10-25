"""
Insertion Sort Implementation
Reference: https://mlhive.com/playground/algorithms/sorting/insertion-sort
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

def insertion_sort(arr: list[int], verbose: bool = True) -> list[int]:
    arr = list(arr)
    step = 1
    # Build sorted prefix one element at a time
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if verbose:
            print(f"Step {step:02d}: Insert key={key} into sorted prefix {arr[:i]}")
        # Shift elements greater than key one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Place key into its sorted slot
        arr[j + 1] = key
        step += 1
    return arr

def main():
    arr = DATASETS.get(PRESET, CUSTOM_INPUT)
    print(f"--- Insertion Sort Demonstration ---")
    print(f"Preset: {PRESET}")
    print(f"Initial Array: {arr}\n")
    
    sorted_arr = insertion_sort(arr, verbose=VERBOSE)
    
    print(f"\nFinal Sorted Array: {sorted_arr}")
    print(f"Verified Sorted: {sorted_arr == sorted(arr)}")

if __name__ == "__main__":
    main()
