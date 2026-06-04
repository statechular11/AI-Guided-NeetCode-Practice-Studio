# Notes - 543. Diameter of Binary Tree

## Core Idea

Diameter through a node is left height plus right height.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_height_and_best.py` | primary solution | Time: O(n); Space: O(h) |
| `solution_tuple_state.py` | alternative state-return reference | Time: O(n); Space: O(h) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
