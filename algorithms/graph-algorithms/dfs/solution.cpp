/**
 * Depth-First Search (DFS) Implementation
 * Reference: https://mlhive.com/playground/algorithms/graph-algorithms/dfs
 */
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <queue>

const std::string START_NODE = "A";
const std::string TARGET_NODE = "F";
const bool VERBOSE = true;

bool dfsHelper(const std::unordered_map<std::string, std::vector<std::string>>& graph,
               const std::string& node, const std::string& target,
               std::unordered_set<std::string>& visited, std::vector<std::string>& order,
               bool verbose, int& step) {
    visited.insert(node);
    order.push_back(node);
    if (verbose) std::cout << "Step " << step++ << ": Visit node '" << node << "'\n";
    if (!target.empty() && node == target) return true;

    auto it = graph.find(node);
    if (it != graph.end()) {
        for (const auto& neighbor : it->second) {
            if (visited.find(neighbor) == visited.end()) {
                if (verbose) std::cout << "  Diving deeper into '" << neighbor << "'\n";
                if (dfsHelper(graph, neighbor, target, visited, order, verbose, step)) return true;
            }
        }
    }
    return false;
}
std::vector<std::string> dfs(const std::unordered_map<std::string, std::vector<std::string>>& graph,
                            const std::string& start, const std::string& target, bool verbose = true) {
    std::vector<std::string> order;
    std::unordered_set<std::string> visited;
    int step = 1;
    dfsHelper(graph, start, target, visited, order, verbose, step);
    return order;
}

int main() {
    std::unordered_map<std::string, std::vector<std::string>> graph = {
        {"A", {"B", "C"}},
        {"B", {"D", "E"}},
        {"C", {"F"}},
        {"D", {}},
        {"E", {"F"}},
        {"F", {}}
    };

    std::cout << "--- Depth-First Search (DFS) (C++) ---\n";
    std::cout << "Start: " << START_NODE << ", Target: " << TARGET_NODE << "\n\n";

    std::vector<std::string> order = dfs(graph, START_NODE, TARGET_NODE, VERBOSE);
    std::cout << "\nTraversal Order: ";
    for (size_t i = 0; i < order.size(); ++i) {
        std::cout << order[i] << (i + 1 < order.size() ? " -> " : "");
    }
    std::cout << "\n";
    return 0;
}
