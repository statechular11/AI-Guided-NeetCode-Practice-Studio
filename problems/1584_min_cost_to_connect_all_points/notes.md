# Notes - 1584. Min Cost to Connect All Points

## Core Idea

This is an MST on a complete graph; compute distances lazily in Prim.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_prim.py` | primary solution | Time: O(n^2); Space: O(n) |
| `solution_kruskal.py` | alternative MST reference | Time: O(n^2 log n); Space: O(n^2) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
