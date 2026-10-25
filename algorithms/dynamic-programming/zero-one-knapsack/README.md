# 0/1 Knapsack Problem Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack)

Interactive visualizer reference: [https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack](https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack)

![0/1 Knapsack Problem Preview](https://mlhive.com/playground/dynamic-programming.png)

---

## Overview

Finds the combination of items that maximizes total value within a weight limit W, using a 2D dynamic programming table where each item can either be taken or left.

### Complexity Analysis

| Metric | Complexity |
| :--- | :--- |
| **Time Complexity** | `O(n * W)` |
| **Space Complexity** | `O(n * W)` |

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/algorithms/dynamic-programming/zero-one-knapsack):

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
