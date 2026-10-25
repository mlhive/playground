# Depth-First Search (DFS) Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/algorithms/searching/dfs)

Interactive visualizer reference: [https://mlhive.com/playground/algorithms/searching/dfs](https://mlhive.com/playground/algorithms/searching/dfs)

![Depth-First Search (DFS) Preview](https://mlhive.com/playground/graph-algorithms.png)

---

## Overview

Depth-First Search explores as far as possible along each branch before backtracking, utilizing a stack (call stack or explicit).

### Complexity Analysis

| Metric | Complexity |
| :--- | :--- |
| **Time Complexity** | `O(V + E)` |
| **Space Complexity** | `O(V)` |

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/algorithms/searching/dfs):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `START_NODE` | `string` | `"A"` | Source starting node for traversal |
| `TARGET_NODE` | `string` | `"F"` | Optional target node to find and stop |
| `GRAPH_PRESET` | `string` | `"standard_dag"` | Graph topology preset (`"standard_dag"`, `"binary_tree"`, `"cycle_graph"`) |
| `VERBOSE` | `bool` | `True` | Prints traversal state and queue/stack steps |

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
