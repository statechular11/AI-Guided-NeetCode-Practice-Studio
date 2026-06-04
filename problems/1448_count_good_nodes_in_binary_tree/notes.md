# Notes - 1448. Count Good Nodes in Binary Tree

## Core Idea

Carry the path maximum; a node is good when it meets or exceeds it.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_path_max.py` | primary solution | Time: O(n); Space: O(h) |
| `solution_iterative_stack.py` | alternative tree traversal reference | Time: O(n); Space: O(h) average, O(n) worst case |

## Pitfalls To Watch

- Be explicit about traversal order: preorder, inorder, postorder, or level order.
- For recursive tree code, define what each call returns before writing pointer changes.
- Distinguish node identity from node value for LCA-style problems.
- For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
