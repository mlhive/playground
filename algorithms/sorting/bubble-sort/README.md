# Bubble Sort Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/algorithms/sorting/bubble-sort)

Interactive visualizer reference: [https://mlhive.com/playground/algorithms/sorting/bubble-sort](https://mlhive.com/playground/algorithms/sorting/bubble-sort)

![Bubble Sort Preview](https://mlhive.com/playground/sorting-algorithms.png)

---

## Overview

Bubble Sort repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. Passes through the list continue until no swaps are needed.

### Complexity Analysis

| Metric | Complexity |
| :--- | :--- |
| **Best Case Time** | `O(n)` |
| **Average Case Time** | `O(n²)` |
| **Worst Case Time** | `O(n²)` |
| **Space Complexity** | `O(1)` |
| **Stability** | `Stable` |

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/algorithms/sorting/bubble-sort):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `PRESET` | `string` | `"random"` | Array generation preset (`"random"`, `"nearly_sorted"`, `"reversed"`, `"few_unique"`, `"custom"`) |
| `CUSTOM_INPUT` | `list[int]` | `[64, 34, 25, 12, 22, 11, 90]` | Custom initial array when preset is `"custom"` |
| `SIZE` | `int` | `10` | Number of elements for generated presets |
| `VERBOSE` | `bool` | `True` | Prints each comparison, swap, and step |

---

## Multi-Language Implementations

This folder includes complete, runnable implementations in:
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
