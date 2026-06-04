# Notes - 124. Binary Tree Maximum Path Sum

## Core Idea

Returned gain is one-sided; global best can use both children through the current node.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_gain_dfs.py` | primary solution | Time: O(n); Space: O(h) |
| `solution_tuple_state.py` | alternative state-shape reference | Time: O(n); Space: O(h) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
