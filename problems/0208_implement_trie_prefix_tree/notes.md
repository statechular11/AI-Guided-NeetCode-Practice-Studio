# Notes - 208. Implement Trie (Prefix Tree)

## Core Idea

Exact search needs terminal marker; prefix search only needs the path to exist.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_nested_nodes.py` | primary design solution | O(L) operations; Space: O(total chars) |
| `solution_dict_sentinel.py` | compact design reference | O(L) per operation; Space: O(total characters) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
