# Notes - 100. Same Tree

## Core Idea

Structure and node values must both match at every position.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_recursive.py` | primary solution | Time: O(n); Space: O(h) |
| `solution_iterative_stack.py` | alternative traversal reference | Time: O(n); Space: O(h) average, O(n) worst case |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
