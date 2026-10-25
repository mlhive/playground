"""
Breadth-First Search (BFS) Implementation
Reference: https://mlhive.com/playground/algorithms/graph-algorithms/bfs
"""

# ==========================================
# RUN CONFIGURATION & PARAMETERS
# ==========================================
START_NODE = "A"
TARGET_NODE = "F"
GRAPH_PRESET = "standard_dag"  # "standard_dag", "binary_tree", "cycle_graph"
VERBOSE = True

GRAPHS = {
    "standard_dag": {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    },
    "binary_tree": {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": [], "E": [], "F": [], "G": []
    },
    "cycle_graph": {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["A", "E"],
        "E": ["F"],
        "F": []
    }
}

from collections import deque

def bfs(graph: dict[str, list[str]], start: str, target: str = None, verbose: bool = True) -> list[str]:
    # Queue (FIFO) maintains nodes for breadth-first level-by-level traversal
    queue = deque([start])
    # Visited set prevents infinite loops in cyclic graphs
    visited = set([start])
    order = []
    step = 1

    while queue:
        node = queue.popleft()
        order.append(node)
        if verbose:
            print(f"Step {step:02d}: Visit node '{node}', Queue: {list(queue)}")
        step += 1

        # Check early exit if target node is reached
        if target and node == target:
            if verbose:
                print(f"Target '{target}' reached!")
            break

        # Discover all unvisited neighbors and enqueue
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if verbose:
                    print(f"  Discovered neighbor '{neighbor}' -> Enqueued")

    return order

def main():
    graph = GRAPHS.get(GRAPH_PRESET, GRAPHS["standard_dag"])
    print(f"--- Breadth-First Search (BFS) Demonstration ---")
    print(f"Preset: {GRAPH_PRESET}")
    print(f"Start Node: {START_NODE}, Target: {TARGET_NODE}\n")

    traversal = bfs(graph, START_NODE, TARGET_NODE, verbose=VERBOSE)
    print(f"\nTraversal Order: {' -> '.join(traversal)}")

if __name__ == "__main__":
    main()
