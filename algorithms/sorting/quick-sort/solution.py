"""
Quick Sort Implementation
Reference: https://mlhive.com/playground/algorithms/sorting/quick-sort
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

def quick_sort(arr: list[int], verbose: bool = True) -> list[int]:
    arr = list(arr)
    step = [1]
    def _partition(low: int, high: int) -> int:
        # Choose last element as pivot
        pivot = arr[high]
        i = low - 1
        # Rearrange elements: smaller than pivot to left, larger to right
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # Place pivot at its final sorted boundary index
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        if verbose:
            print(f"Step {step[0]:02d}: Partitioned around pivot={pivot} at index {i+1} -> {arr}")
            step[0] += 1
        return i + 1

    def _quick(low: int, high: int):
        if low < high:
            pi = _partition(low, high)
            # Recursively sort sub-arrays before and after pivot
            _quick(low, pi - 1)
            _quick(pi + 1, high)

    _quick(0, len(arr) - 1)
    return arr

def main():
    arr = DATASETS.get(PRESET, CUSTOM_INPUT)
    print(f"--- Quick Sort Demonstration ---")
    print(f"Preset: {PRESET}")
    print(f"Initial Array: {arr}\n")
    
    sorted_arr = quick_sort(arr, verbose=VERBOSE)
    
    print(f"\nFinal Sorted Array: {sorted_arr}")
    print(f"Verified Sorted: {sorted_arr == sorted(arr)}")

if __name__ == "__main__":
    main()
