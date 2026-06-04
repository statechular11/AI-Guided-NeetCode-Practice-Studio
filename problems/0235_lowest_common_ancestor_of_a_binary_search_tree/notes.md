# Notes - 235. Lowest Common Ancestor of a Binary Search Tree

## Core Idea

The LCA is the first node whose value lies between p and q, inclusive.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_bst_split.py` | primary solution | Time: O(h); Space: O(1) |
| `solution_recursive_bst.py` | alternative BST traversal reference | Time: O(h); Space: O(h) |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
