# Notes - 130. Surrounded Regions

## Core Idea

Invert the perspective: preserve border-connected O cells, then flip all other O cells.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_border_flood_fill.py` | primary solution | Time: O(m*n); Space: O(m*n) |
| `solution_union_find.py` | alternative graph connectivity reference | Time: O(mn alpha(mn)); Space: O(mn) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
