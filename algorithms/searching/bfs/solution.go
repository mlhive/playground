// Breadth-First Search (BFS) Implementation
// Reference: https://mlhive.com/playground/algorithms/searching/bfs
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

func bfs(graph map[string][]string, start string, target string, verbose bool) []string {
	order := []string{}
	visited := map[string]bool{start: true}
	queue := []string{start}
	step := 1

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		order = append(order, node)
		if verbose {
			fmt.Printf("Step %02d: Visit node '%s'\n", step, node)
			step++
		}
		if target != "" && node == target {
			if verbose {
				fmt.Printf("Target '%s' reached!\n", target)
			}
			break
		}
		for _, neighbor := range graph[node] {
			if !visited[neighbor] {
				visited[neighbor] = true
				queue = append(queue, neighbor)
				if verbose {
					fmt.Printf("  Discovered neighbor '%s' -> Enqueued\n", neighbor)
				}
			}
		}
	}
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

	fmt.Println("--- Breadth-First Search (BFS) (Go) ---")
	fmt.Printf("Start: %s, Target: %s\n\n", StartNode, TargetNode)

	order := bfs(graph, StartNode, TargetNode, Verbose)
	fmt.Printf("\nTraversal Order: %s\n", strings.Join(order, " -> "))
}
