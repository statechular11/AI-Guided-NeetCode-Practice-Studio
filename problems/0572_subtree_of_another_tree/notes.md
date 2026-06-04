# Notes - 572. Subtree of Another Tree

## Core Idea

Subtree means same structure and values from some node downward.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_same_tree_scan.py` | primary solution | Time: O(n*m); Space: O(h) |
| `solution_serialization.py` | alternative tree-shape reference | Time: O(m + n); Space: O(m + n) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
