# Notes - 102. Binary Tree Level Order Traversal

## Core Idea

Use the queue size at the start of each round to isolate one level.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_bfs_queue.py` | primary solution | Time: O(n); Space: O(width) |
| `solution_dfs_levels.py` | alternative tree traversal reference | Time: O(n); Space: O(h) recursion plus output |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
