# Notes - 695. Max Area of Island

## Core Idea

Same flood-fill skeleton as islands, but return component size.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dfs_area.py` | primary solution | Time: O(m*n); Space: O(m*n) |
| `solution_bfs_area.py` | alternative graph traversal reference | Time: O(mn); Space: O(mn) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
