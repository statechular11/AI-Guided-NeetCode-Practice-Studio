# Notes - 98. Validate Binary Search Tree

## Core Idea

Use ancestor-derived bounds, not only parent-child comparisons.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_bounds_dfs.py` | primary solution | Time: O(n); Space: O(h) |
| `solution_inorder_traversal.py` | alternative BST invariant reference | Time: O(n); Space: O(h) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
