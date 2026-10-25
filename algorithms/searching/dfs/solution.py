"""
Depth-First Search (DFS) Implementation
Reference: https://mlhive.com/playground/algorithms/searching/dfs
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

def dfs(graph: dict[str, list[str]], start: str, target: str = None, verbose: bool = True) -> list[str]:
    # Set to record visited nodes avoiding cycles
    visited = set()
    order = []
    step = [1]

    def _traverse(node: str):
        visited.add(node)
        order.append(node)
        if verbose:
            print(f"Step {step[0]:02d}: Visit node '{node}'")
        step[0] += 1

        if target and node == target:
            return True

        # Recursively explore depth of each unvisited branch before backtracking
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if verbose:
                    print(f"  Diving deeper into '{neighbor}'")
                found = _traverse(neighbor)
                if found:
                    return True
        return False

    _traverse(start)
    return order

def main():
    graph = GRAPHS.get(GRAPH_PRESET, GRAPHS["standard_dag"])
    print(f"--- Depth-First Search (DFS) Demonstration ---")
    print(f"Preset: {GRAPH_PRESET}")
    print(f"Start Node: {START_NODE}, Target: {TARGET_NODE}\n")

    traversal = dfs(graph, START_NODE, TARGET_NODE, verbose=VERBOSE)
    print(f"\nTraversal Order: {' -> '.join(traversal)}")

if __name__ == "__main__":
    main()
