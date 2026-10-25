/**
 * Breadth-First Search (BFS) Implementation
 * Reference: https://mlhive.com/playground/algorithms/graph-algorithms/bfs
 */
import java.util.*;

public class Solution {
    static final String START_NODE = "A";
    static final String TARGET_NODE = "F";
    static final boolean VERBOSE = true;

    public static List<String> bfs(Map<String, List<String>> graph, String start, String target, boolean verbose) {
        List<String> order = new ArrayList<>();
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new ArrayDeque<>();

        visited.add(start);
        queue.add(start);
        int step = 1;

        while (!queue.isEmpty()) {
            String node = queue.poll();
            order.add(node);
            if (verbose) System.out.printf("Step %02d: Visit node '%s'%n", step++, node);

            if (target != null && node.equals(target)) {
                if (verbose) System.out.println("Target '" + target + "' reached!");
                break;
            }

            for (String neighbor : graph.getOrDefault(node, Collections.emptyList())) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                    if (verbose) System.out.println("  Discovered neighbor '" + neighbor + "' -> Enqueued");
                }
            }
        }
        return order;
    }

    public static void main(String[] args) {
        Map<String, List<String>> graph = new HashMap<>();
        graph.put("A", Arrays.asList("B", "C"));
        graph.put("B", Arrays.asList("D", "E"));
        graph.put("C", Arrays.asList("F"));
        graph.put("D", Collections.emptyList());
        graph.put("E", Arrays.asList("F"));
        graph.put("F", Collections.emptyList());

        System.out.println("--- Breadth-First Search (BFS) (Java) ---");
        System.out.printf("Start: %s, Target: %s%n%n", START_NODE, TARGET_NODE);

        List<String> order = bfs(graph, START_NODE, TARGET_NODE, VERBOSE);
        System.out.println("\nTraversal Order: " + String.join(" -> ", order));
    }
}
