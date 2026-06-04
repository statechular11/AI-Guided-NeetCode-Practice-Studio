# Notes - 127. Word Ladder

## Core Idea

Because every edit has equal cost, BFS gives the shortest ladder.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_bfs_patterns.py` | primary solution | Time: O(n*L^2); Space: O(n*L) |
| `solution_bidirectional_bfs.py` | optimized graph-search reference | Time: O(n * L^2); Space: O(n * L) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
