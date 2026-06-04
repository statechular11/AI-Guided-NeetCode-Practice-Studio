# Notes - 269. Alien Dictionary

## Core Idea

Only the first differing character between adjacent words creates an ordering edge.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_topological_sort.py` | primary solution | Time: O(C+E); Space: O(C+E) |
| `solution_dfs_topological_sort.py` | alternative advanced-graph reference | Time: O(total characters + edges); Space: O(unique characters + edges) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
