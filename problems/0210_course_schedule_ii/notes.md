# Notes - 210. Course Schedule II

## Core Idea

The comparator validates any topological order, not one exact sequence.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_topological_order.py` | primary solution | Time: O(V+E); Space: O(V+E) |
| `solution_dfs_topological_order.py` | alternative topological-order reference | Time: O(V + E); Space: O(V + E) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
