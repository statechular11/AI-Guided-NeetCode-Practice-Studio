# Notes - 230. Kth Smallest Element in a BST

## Core Idea

Inorder traversal of a BST yields sorted values.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_iterative_inorder.py` | primary solution | Time: O(h+k); Space: O(h) |
| `solution_recursive_inorder.py` | readable BST-order reference | Time: O(n); Space: O(n) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
