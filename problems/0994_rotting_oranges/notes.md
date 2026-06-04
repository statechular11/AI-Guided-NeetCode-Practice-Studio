# Notes - 994. Rotting Oranges

## Core Idea

Minute count is BFS layer distance from the nearest initially rotten orange.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_multi_source_bfs.py` | primary solution | Time: O(m*n); Space: O(m*n) |
| `solution_minute_layers.py` | alternative multi-source BFS reference | Time: O(mn); Space: O(mn) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
