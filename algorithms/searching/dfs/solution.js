/**
 * Depth-First Search (DFS) Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/dfs
 */

// RUN CONFIGURATION
const START_NODE = "A";
const TARGET_NODE = "F";
const GRAPH_PRESET = "standard_dag";
const VERBOSE = true;

const GRAPHS = {
  standard_dag: {
    A: ["B", "C"],
    B: ["D", "E"],
    C: ["F"],
    D: [],
    E: ["F"],
    F: [],
  },
  binary_tree: {
    A: ["B", "C"],
    B: ["D", "E"],
    C: ["F", "G"],
    D: [], E: [], F: [], G: []
  }
};

function dfs(graph, start, target = null, verbose = true) {
  const visited = new Set();
  const order = [];
  let step = 1;

  function traverse(node) {
    visited.add(node);
    order.push(node);
    if (verbose) console.log(`Step ${String(step++).padStart(2, '0')}: Visit node '${node}'`);

    if (target && node === target) return true;

    for (const neighbor of graph[node] || []) {
      if (!visited.has(neighbor)) {
        if (verbose) console.log(`  Diving deeper into '${neighbor}'`);
        if (traverse(neighbor)) return true;
      }
    }
    return false;
  }

  traverse(start);
  return order;
}

function main() {
  const graph = GRAPHS[GRAPH_PRESET] || GRAPHS.standard_dag;
  console.log(`--- Depth-First Search (DFS) Demonstration ---`);
  console.log(`Start: ${START_NODE}, Target: ${TARGET_NODE}\n`);

  const order = dfs(graph, START_NODE, TARGET_NODE, VERBOSE);
  console.log(`\nTraversal Order: ${order.join(' -> ')}`);
}

main();
