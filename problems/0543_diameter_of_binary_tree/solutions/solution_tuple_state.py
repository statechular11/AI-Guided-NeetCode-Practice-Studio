"""
543. Diameter of Binary Tree - postorder height and diameter tuple

Variant role:
    alternative state-return reference

Core idea:
    Each subtree can report both its height and its best diameter, avoiding a nonlocal variable.

Key invariant:
    dfs(node) returns (height, best_diameter_edges) for exactly node's subtree.

Mechanics:
    The best diameter through node is left_height + right_height; compare it with the best diameters from both children.

Common pitfalls:
    Diameter is counted in edges here, while height is counted in nodes.

Complexity:
    Time: O(n); Space: O(h)

When to choose this variant:
    Use this if explicit return contracts feel cleaner than updating outer state.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0
            left_height, left_best = dfs(node.left)
            right_height, right_best = dfs(node.right)
            height = 1 + max(left_height, right_height)
            diameter = max(left_best, right_best, left_height + right_height)
            return height, diameter

        return dfs(root)[1]
