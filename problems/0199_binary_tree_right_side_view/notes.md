# Notes - 199. Binary Tree Right Side View

## Core Idea

The visible value is the last node in each BFS level.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_bfs_last_value.py` | primary solution | Time: O(n); Space: O(width) |
| `solution_dfs_right_first.py` | alternative tree traversal reference | Time: O(n); Space: O(h) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
