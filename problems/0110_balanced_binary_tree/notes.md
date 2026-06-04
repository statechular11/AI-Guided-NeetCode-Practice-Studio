# Notes - 110. Balanced Binary Tree

## Core Idea

Compute balance and height together to avoid repeated subtree height scans.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_height_or_minus_one.py` | primary solution | Time: O(n); Space: O(h) |
| `solution_top_down_height_check.py` | educational baseline | Time: O(n^2) worst case; Space: O(h) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
