# Fibonacci Dynamic Programming Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/algorithms/dynamic-programming/fibonacci-dp)

Interactive visualizer reference: [https://mlhive.com/playground/algorithms/dynamic-programming/fibonacci-dp](https://mlhive.com/playground/algorithms/dynamic-programming/fibonacci-dp)

![Fibonacci Dynamic Programming Preview](https://mlhive.com/playground/dynamic-programming.png)

---

## Overview

Computes Fibonacci numbers in linear time using bottom-up tabulation, storing intermediate subproblem solutions in a DP table.

### Complexity Analysis

| Metric | Complexity |
| :--- | :--- |
| **Time Complexity** | `O(n)` |
| **Space Complexity** | `O(n) or O(1) optimized` |

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/algorithms/dynamic-programming/fibonacci-dp):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `INPUT` | `int / list` | Configurable | Subproblem bounds or items and capacity |
| `VERBOSE` | `bool` | `True` | Prints each table update and state transition |

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
