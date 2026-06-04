# Notes - 684. Redundant Connection

## Core Idea

Union-find detects the first edge connecting two already-connected nodes.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_union_find.py` | primary solution | Time: O(E alpha n); Space: O(n) |
| `solution_dfs_incremental.py` | alternative graph baseline | Time: O(n^2); Space: O(n) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
