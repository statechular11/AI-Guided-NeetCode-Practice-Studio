# Notes - 743. Network Delay Time

## Core Idea

The delay is the longest shortest-path distance from the source.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dijkstra.py` | primary solution | Time: O((V+E)logV); Space: O(V+E) |
| `solution_bellman_ford.py` | alternative shortest-path baseline | Time: O(VE); Space: O(V) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
