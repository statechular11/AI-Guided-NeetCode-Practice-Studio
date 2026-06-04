"""
110. Balanced Binary Tree - top-down height recomputation

Variant role:
    educational baseline

Core idea:
    A tree is balanced if each node's left and right heights differ by at most one and both subtrees are balanced.

Key invariant:
    height(node) returns the true height of that subtree; isBalanced checks the definition directly at every node.

Mechanics:
    Compute left/right heights for the current node, compare them, then recursively validate both children.

Common pitfalls:
    This repeats height work many times on skewed trees. The optimized variant combines height and validity in one postorder pass.

Complexity:
    Time: O(n^2) worst case; Space: O(h)

When to choose this variant:
    Use this as the literal definition before learning the O(n) height-or-minus-one trick.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True
        if abs(height(root.left) - height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
