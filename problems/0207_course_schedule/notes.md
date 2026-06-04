# Notes - 207. Course Schedule

## Core Idea

Cycle detection in a directed prerequisite graph is topological sorting.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_topological_sort.py` | primary solution | Time: O(V+E); Space: O(V+E) |
| `solution_dfs_cycle_detection.py` | alternative topological-sort reference | Time: O(V + E); Space: O(V + E) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
