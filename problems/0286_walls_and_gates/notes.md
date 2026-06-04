# Notes - 286. Walls and Gates

## Core Idea

Multi-source BFS is the natural shortest-distance tool when all gates are sources.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_multi_source_bfs.py` | primary solution | Time: O(m*n); Space: O(m*n) |
| `solution_dfs_relaxation.py` | educational baseline | Time: O(gmn) worst case; Space: O(mn) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
