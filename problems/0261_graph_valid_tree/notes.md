# Notes - 261. Graph Valid Tree

## Core Idea

A tree has n-1 edges and no cycle.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_union_find.py` | primary solution | Time: O(E alpha n); Space: O(n) |
| `solution_dfs.py` | alternative graph reference | Time: O(V + E); Space: O(V + E) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
