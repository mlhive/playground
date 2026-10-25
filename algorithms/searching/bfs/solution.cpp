/**
 * Breadth-First Search (BFS) Implementation
 * Reference: https://mlhive.com/playground/algorithms/searching/bfs
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

std::vector<std::string> bfs(const std::unordered_map<std::string, std::vector<std::string>>& graph,
                            const std::string& start, const std::string& target, bool verbose = true) {
    std::vector<std::string> order;
    std::unordered_set<std::string> visited = {start};
    std::queue<std::string> q;
    q.push(start);
    int step = 1;

    while (!q.empty()) {
        std::string node = q.front();
        q.pop();
        order.push_back(node);
        if (verbose) std::cout << "Step " << step++ << ": Visit node '" << node << "'\n";

        if (!target.empty() && node == target) {
            if (verbose) std::cout << "Target '" << target << "' reached!\n";
            break;
        }

        auto it = graph.find(node);
        if (it != graph.end()) {
            for (const auto& neighbor : it->second) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                    if (verbose) std::cout << "  Discovered neighbor '" << neighbor << "' -> Enqueued\n";
                }
            }
        }
    }
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

    std::cout << "--- Breadth-First Search (BFS) (C++) ---\n";
    std::cout << "Start: " << START_NODE << ", Target: " << TARGET_NODE << "\n\n";

    std::vector<std::string> order = bfs(graph, START_NODE, TARGET_NODE, VERBOSE);
    std::cout << "\nTraversal Order: ";
    for (size_t i = 0; i < order.size(); ++i) {
        std::cout << order[i] << (i + 1 < order.size() ? " -> " : "");
    }
    std::cout << "\n";
    return 0;
}
