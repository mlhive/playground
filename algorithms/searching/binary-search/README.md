# Binary Search Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/algorithms/searching/binary-search)

Interactive visualizer reference: [https://mlhive.com/playground/algorithms/searching/binary-search](https://mlhive.com/playground/algorithms/searching/binary-search)

![Binary Search Preview](https://mlhive.com/playground/searching-algorithms.png)

---

## Overview

Binary Search repeatedly divides the search interval in half on a sorted array, comparing the target value to the middle element.

### Complexity Analysis

| Metric | Complexity |
| :--- | :--- |
| **Best Case Time** | `O(1)` |
| **Average Case Time** | `O(log n)` |
| **Worst Case Time** | `O(log n)` |
| **Space Complexity** | `O(1)` |

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/algorithms/searching/binary-search):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `TARGET` | `int` | `50` | Target value to search for |
| `PRESET` | `string` | `"sorted_standard"` | Dataset preset (`"sorted_standard"`, `"target_absent"`, `"custom"`) |
| `CUSTOM_ARRAY` | `list[int]` | `[10, 20, 30, 40, 50, 60, 70, 80, 90]` | Custom search array |
| `VERBOSE` | `bool` | `True` | Prints each comparison step and index |

---

## Multi-Language Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)
- **Java**: [`Solution.java`](./Solution.java)
- **C++**: [`solution.cpp`](./solution.cpp)
- **Go**: [`solution.go`](./solution.go)

### How to Run

```bash
# Python
python solution.py

# Node.js
node solution.js

# Java
javac Solution.java
java Solution

# C++
g++ -O2 solution.cpp -o solution
./solution

# Go
go run solution.go
```
