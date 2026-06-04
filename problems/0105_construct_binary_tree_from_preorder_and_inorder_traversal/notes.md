# Notes - 105. Construct Binary Tree from Preorder and Inorder Traversal

## Core Idea

Preorder identifies roots; inorder splits left and right subtree ranges.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_preorder_index.py` | primary solution | Time: O(n); Space: O(n) |
| `solution_slice_recursion.py` | educational baseline | Time: O(n^2); Space: O(n^2) from slicing |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
