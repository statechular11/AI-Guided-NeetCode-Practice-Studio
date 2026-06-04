"""
100. Same Tree - Recursive Structure/Value Comparison

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Structure and node values must both match at every position.

    This specific variant uses: recursive structure/value comparison.

Key invariant:
    Each recursive or BFS step gives a precise meaning to the current node/subtree, so child results combine into the parent result without relying on parent-child checks alone.

Mechanics:
    1. Handle the empty subtree first.
    2. Process the current node with the exact information the helper owns.
    3. Recurse or enqueue children with updated context.
    4. Combine child results according to the helper's return contract.

Walkthrough:
    On the local case `example_1`, the input is `{"p": [1, 2, 3], "q": [1, 2, 3]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Be explicit about traversal order: preorder, inorder, postorder, or level order. For recursive tree code, define what each call returns before writing pointer changes. Distinguish node identity from node value for LCA-style problems. For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

Complexity:
    Time: O(n); Space: O(h)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.
"""

from typing import Optional

from common.lc_types import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Compare two trees recursively by structure and value.

        Two empty nodes match. One empty and one non-empty node fails. Otherwise
        the values must match and both left and right subtrees must match.

        Complexity: O(n) time, O(h) recursion stack.
        """
        if not p or not q:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
