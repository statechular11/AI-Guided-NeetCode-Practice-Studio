"""
230. Kth Smallest Element in a BST - recursive inorder collection

Variant role:
    readable BST-order reference

Core idea:
    Inorder traversal of a BST visits values in ascending order, so the kth visited value is the answer.

Key invariant:
    values contains the inorder sequence of every fully visited subtree.

Mechanics:
    Traverse left, append node value, traverse right, then return values[k-1].

Common pitfalls:
    This stores all values. The iterative reference can stop once the kth value is reached.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this for maximum readability before optimizing space and early stopping.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values: list[int] = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return values[k - 1]
