"""
Bubble Sort Implementation
Reference: https://mlhive.com/playground/algorithms/sorting/bubble-sort
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

def bubble_sort(arr: list[int], verbose: bool = True) -> list[int]:
    n = len(arr)
    arr = list(arr)
    step = 1
    # end tracks the boundary of the unsorted subarray; largest element bubbles to the right
    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            # Compare adjacent pair: swap if left > right
            if arr[i] > arr[i + 1]:
                if verbose:
                    print(f"Step {step:02d}: Swap arr[{i}]={arr[i]} with arr[{i+1}]={arr[i+1]} -> {arr}")
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                step += 1
            else:
                if verbose:
                    print(f"Step {step:02d}: Compare arr[{i}]={arr[i]} <= arr[{i+1}]={arr[i+1]} (ok)")
                step += 1
        # Early stopping optimization: if no swaps occurred, array is already sorted
        if not swapped:
            if verbose:
                print("Early stopping: Array is already sorted!")
            break
    return arr

def main():
    arr = DATASETS.get(PRESET, CUSTOM_INPUT)
    print(f"--- Bubble Sort Demonstration ---")
    print(f"Preset: {PRESET}")
    print(f"Initial Array: {arr}\n")
    
    sorted_arr = bubble_sort(arr, verbose=VERBOSE)
    
    print(f"\nFinal Sorted Array: {sorted_arr}")
    print(f"Verified Sorted: {sorted_arr == sorted(arr)}")

if __name__ == "__main__":
    main()
