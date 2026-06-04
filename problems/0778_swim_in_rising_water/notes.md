# Notes - 778. Swim in Rising Water

## Core Idea

This is shortest path under a minimax path cost.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_dijkstra_minimax.py` | primary solution | Time: O(n^2 log n); Space: O(n^2) |
| `solution_binary_search_bfs.py` | alternative answer-search reference | Time: O(n^2 log n); Space: O(n^2) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
