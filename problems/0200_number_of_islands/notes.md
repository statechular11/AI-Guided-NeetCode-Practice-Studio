# Notes - 200. Number of Islands

## Core Idea

Mutating visited land to water is the simplest visited set.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dfs_sink.py` | primary solution | Time: O(m*n); Space: O(m*n) |
| `solution_bfs_queue.py` | alternative graph traversal reference | Time: O(mn); Space: O(mn) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
