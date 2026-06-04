# Notes - 787. Cheapest Flights Within K Stops

## Core Idea

Copy distances each round to enforce the edge-count limit.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_bellman_ford_limited.py` | primary solution | Time: O(kE); Space: O(V) |
| `solution_state_dijkstra.py` | alternative constrained-shortest-path reference | Time: O(EK log(VK)); Space: O(VK) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
