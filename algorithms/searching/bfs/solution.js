/**
 * Breadth-First Search (BFS) Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/bfs
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

function bfs(graph, start, target = null, verbose = true) {
  const visited = new Set([start]);
  const queue = [start];
  const order = [];
  let step = 1;

  while (queue.length > 0) {
    const node = queue.shift();
    order.push(node);
    if (verbose) console.log(`Step ${String(step++).padStart(2, '0')}: Visit node '${node}', Queue: [${queue.join(', ')}]`);

    if (target && node === target) {
      if (verbose) console.log(`Target '${target}' reached!`);
      break;
    }

    for (const neighbor of graph[node] || []) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
        if (verbose) console.log(`  Discovered neighbor '${neighbor}' -> Enqueued`);
      }
    }
  }
  return order;
}

function main() {
  const graph = GRAPHS[GRAPH_PRESET] || GRAPHS.standard_dag;
  console.log(`--- Breadth-First Search (BFS) Demonstration ---`);
  console.log(`Start: ${START_NODE}, Target: ${TARGET_NODE}\n`);

  const order = bfs(graph, START_NODE, TARGET_NODE, VERBOSE);
  console.log(`\nTraversal Order: ${order.join(' -> ')}`);
}

main();
