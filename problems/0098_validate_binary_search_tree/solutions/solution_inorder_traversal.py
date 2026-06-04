"""
98. Validate Binary Search Tree - inorder sorted-order validation

Variant role:
    alternative BST invariant reference

Core idea:
    An inorder traversal of a valid BST must produce a strictly increasing sequence.

Key invariant:
    prev holds the value of the most recently visited inorder node, so every next node must be greater.

Mechanics:
    Traverse left subtree, compare current value to prev, then traverse right subtree.

Common pitfalls:
    BST validity is strict: duplicates on either side fail for this LeetCode problem.

Complexity:
    Time: O(n); Space: O(h)

When to choose this variant:
    Use this when the sorted-order property is easier to explain than passing lower/upper bounds.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def inorder(node: Optional[TreeNode]) -> bool:
            nonlocal prev
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev is not None and node.val <= prev:
                return False
            prev = node.val
            return inorder(node.right)

        return inorder(root)
