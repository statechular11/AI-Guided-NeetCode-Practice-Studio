# Notes - 133. Clone Graph

## Core Idea

The visited map is both cycle protection and identity preservation.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dfs_hash_map.py` | primary solution | Time: O(V+E); Space: O(V) |
| `solution_bfs_hash_map.py` | alternative graph traversal reference | Time: O(V + E); Space: O(V) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
