"""
124. Binary Tree Maximum Path Sum - postorder returns gain and best path

Variant role:
    alternative state-shape reference

Core idea:
    Each subtree has two useful facts: the best one-sided gain extendable to its parent, and the best complete path anywhere inside it.

Key invariant:
    dfs(node) returns (extendable_gain, best_path_sum) for exactly node's subtree.

Mechanics:
    Clamp child gains at zero when extending through the current node, but compare full left-through-node-right paths for the local best.

Common pitfalls:
    Only one branch can be extended upward to a parent; a split path using both children is complete at the current node.

Complexity:
    Time: O(n); Space: O(h)

When to choose this variant:
    Use this when a tuple return feels clearer than a nonlocal/global best variable.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, float("-inf")

            left_gain, left_best = dfs(node.left)
            right_gain, right_best = dfs(node.right)
            left_gain = max(left_gain, 0)
            right_gain = max(right_gain, 0)

            extendable = node.val + max(left_gain, right_gain)
            through_node = node.val + left_gain + right_gain
            best = max(left_best, right_best, through_node)
            return extendable, best

        return dfs(root)[1]
