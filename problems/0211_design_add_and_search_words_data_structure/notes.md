# Notes - 211. Design Add and Search Words Data Structure

## Core Idea

The dot wildcard turns trie search into DFS over all child branches.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_trie_dfs_wildcard.py` | primary design solution | add O(L); search wildcard-dependent |
| `solution_length_buckets.py` | educational non-trie baseline | addWord: O(1) amortized; search: O(kL) for same-length words; Space: O(total characters) |

## Pitfalls To Watch

- Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation.
- For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant.
- Mark visited at the right time to avoid duplicate work or infinite cycles.
- For topological sort, handle invalid prefix/cycle cases explicitly.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
