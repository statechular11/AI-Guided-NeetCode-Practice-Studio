# Notes - 332. Reconstruct Itinerary

## Core Idea

This is an Eulerian path problem; append airports after exhausting outgoing edges.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_hierholzer.py` | primary solution | Time: O(E log E); Space: O(E) |
| `solution_backtracking_baseline.py` | educational baseline | Time: O(E! * E) worst case; Space: O(E) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
