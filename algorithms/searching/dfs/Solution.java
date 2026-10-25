/**
 * Depth-First Search (DFS) Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/dfs
 */
import java.util.*;

public class Solution {
    static final String START_NODE = "A";
    static final String TARGET_NODE = "F";
    static final boolean VERBOSE = true;

    public static List<String> dfs(Map<String, List<String>> graph, String start, String target, boolean verbose) {
        List<String> order = new ArrayList<>();
        Set<String> visited = new HashSet<>();
        int[] step = {1};
        traverse(graph, start, target, visited, order, verbose, step);
        return order;
    }
    private static boolean traverse(Map<String, List<String>> graph, String node, String target,
                                   Set<String> visited, List<String> order, boolean verbose, int[] step) {
        visited.add(node);
        order.add(node);
        if (verbose) System.out.printf("Step %02d: Visit node '%s'%n", step[0]++, node);
        if (target != null && node.equals(target)) return true;

        for (String neighbor : graph.getOrDefault(node, Collections.emptyList())) {
            if (!visited.contains(neighbor)) {
                if (verbose) System.out.println("  Diving deeper into '" + neighbor + "'");
                if (traverse(graph, neighbor, target, visited, order, verbose, step)) return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Map<String, List<String>> graph = new HashMap<>();
        graph.put("A", Arrays.asList("B", "C"));
        graph.put("B", Arrays.asList("D", "E"));
        graph.put("C", Arrays.asList("F"));
        graph.put("D", Collections.emptyList());
        graph.put("E", Arrays.asList("F"));
        graph.put("F", Collections.emptyList());

        System.out.println("--- Depth-First Search (DFS) (Java) ---");
        System.out.printf("Start: %s, Target: %s%n%n", START_NODE, TARGET_NODE);

        List<String> order = dfs(graph, START_NODE, TARGET_NODE, VERBOSE);
        System.out.println("\nTraversal Order: " + String.join(" -> ", order));
    }
}
