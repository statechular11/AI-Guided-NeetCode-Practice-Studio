# Notes - 212. Word Search II

## Core Idea

Trie prefixes stop impossible DFS paths early; clear found words to avoid duplicates.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_trie_backtracking.py` | primary solution | Time: pruned DFS; Space: O(total word chars) |
| `solution_word_by_word_backtracking.py` | educational baseline | Time: O(W * mn * 4^L); Space: O(L) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
