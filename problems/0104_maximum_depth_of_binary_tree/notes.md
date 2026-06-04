# Notes - 104. Maximum Depth of Binary Tree

## Core Idea

Empty depth is zero; each non-empty node contributes one.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_recursive_depth.py` | primary solution | Time: O(n); Space: O(h) |
| `solution_bfs_queue.py` | iterative traversal reference | Time: O(n); Space: O(w) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
