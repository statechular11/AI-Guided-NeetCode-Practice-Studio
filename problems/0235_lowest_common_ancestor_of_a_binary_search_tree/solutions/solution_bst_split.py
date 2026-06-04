"""
235. Lowest Common Ancestor of a Binary Search Tree - Walk Toward The Bst Split Point

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The LCA is the first node whose value lies between p and q, inclusive.

    This specific variant uses: walk toward the BST split point.

Key invariant:
    Each recursive or BFS step gives a precise meaning to the current node/subtree, so child results combine into the parent result without relying on parent-child checks alone.

Mechanics:
    1. Handle the empty subtree first.
    2. Process the current node with the exact information the helper owns.
    3. Recurse or enqueue children with updated context.
    4. Combine child results according to the helper's return contract.

Walkthrough:
    On the local case `example_1`, the input is `{"root": [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], "p": 2, "q": 8}` and the expected result is `{"return": [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]}`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Be explicit about traversal order: preorder, inorder, postorder, or level order. For recursive tree code, define what each call returns before writing pointer changes. Distinguish node identity from node value for LCA-style problems. For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

Complexity:
    Time: O(h); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.
"""

from common.lc_types import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Use BST ordering to find the split point.

        If both targets are smaller than the current node, move left. If both
        are larger, move right. Otherwise the current node is where the target
        paths split, so it is the LCA.

        Complexity: O(h) time, O(1) space.
        """
        low, high = sorted((p.val, q.val))
        node = root
        while node:
            if high < node.val:
                node = node.left
            elif low > node.val:
                node = node.right
            else:
                return node
