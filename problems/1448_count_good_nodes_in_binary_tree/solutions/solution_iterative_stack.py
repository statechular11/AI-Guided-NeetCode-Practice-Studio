"""
1448. Count Good Nodes in Binary Tree - iterative DFS with path maximum

Variant role:
    alternative tree traversal reference

Core idea:
    A node is good when its value is at least the maximum value seen on the path from root to parent.

Key invariant:
    Each stack item carries the correct path maximum before visiting that node.

Mechanics:
    Pop node and path max, count it if node.val >= path max, then push children with updated max.

Common pitfalls:
    The path maximum is branch-specific; do not keep one global maximum for the whole traversal.

Complexity:
    Time: O(n); Space: O(h) average, O(n) worst case

When to choose this variant:
    Use this when avoiding recursion or practicing state carried through tree traversal.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        stack = [(root, float("-inf"))] if root else []
        while stack:
            node, path_max = stack.pop()
            if node.val >= path_max:
                count += 1
            next_max = max(path_max, node.val)
            if node.left:
                stack.append((node.left, next_max))
            if node.right:
                stack.append((node.right, next_max))
        return count
