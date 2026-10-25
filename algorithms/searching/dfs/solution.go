// Depth-First Search (DFS) Implementation
// Reference: https://mlhive.com/playground/algorithms/searching/dfs
package main

import (
	"fmt"
	"strings"
)

const (
	StartNode  = "A"
	TargetNode = "F"
	Verbose    = true
)

func dfs(graph map[string][]string, start string, target string, verbose bool) []string {
	order := []string{}
	visited := map[string]bool{}
	step := 1

	var traverse func(node string) bool
	traverse = func(node string) bool {
		visited[node] = true
		order = append(order, node)
		if verbose {
			fmt.Printf("Step %02d: Visit node '%s'\n", step, node)
			step++
		}
		if target != "" && node == target {
			return true
		}
		for _, neighbor := range graph[node] {
			if !visited[neighbor] {
				if verbose {
					fmt.Printf("  Diving deeper into '%s'\n", neighbor)
				}
				if traverse(neighbor) {
					return true
				}
			}
		}
		return false
	}
	traverse(start)
	return order
}

func main() {
	graph := map[string][]string{
		"A": {"B", "C"},
		"B": {"D", "E"},
		"C": {"F"},
		"D": {},
		"E": {"F"},
		"F": {},
	}

	fmt.Println("--- Depth-First Search (DFS) (Go) ---")
	fmt.Printf("Start: %s, Target: %s\n\n", StartNode, TargetNode)

	order := dfs(graph, StartNode, TargetNode, Verbose)
	fmt.Printf("\nTraversal Order: %s\n", strings.Join(order, " -> "))
}
