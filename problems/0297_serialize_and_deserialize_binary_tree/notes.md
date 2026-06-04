# Notes - 297. Serialize and Deserialize Binary Tree

## Core Idea

Include null markers during serialization so shape can be reconstructed.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_level_order_codec.py` | primary codec solution | Time: O(n); Space: O(n) |
| `solution_preorder_codec.py` | alternative codec reference | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
