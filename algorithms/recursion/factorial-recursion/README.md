# Factorial Recursion Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/algorithms/recursion/factorial-recursion)

Interactive visualizer reference: [https://mlhive.com/playground/algorithms/recursion/factorial-recursion](https://mlhive.com/playground/algorithms/recursion/factorial-recursion)

![Factorial Recursion Preview](https://mlhive.com/playground/recursion-algorithms.png)

---

## Overview

Calculates n! by multiplying n by the factorial of (n - 1), illustrating the call stack, stack frames, and the base case n <= 1.

### Complexity Analysis

| Metric | Complexity |
| :--- | :--- |
| **Time Complexity** | `O(n)` |
| **Space Complexity** | `O(n) call stack` |

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/algorithms/recursion/factorial-recursion):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `N` | `int` | `5` | Input integer value to compute |
| `VERBOSE` | `bool` | `True` | Logs call stack push and pop operations |

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
