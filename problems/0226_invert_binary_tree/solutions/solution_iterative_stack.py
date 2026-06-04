"""
226. Invert Binary Tree - iterative DFS swapping

Variant role:
    alternative tree mutation reference

Core idea:
    Every node can swap its children independently; traversal order does not affect the final inverted tree.

Key invariant:
    Every node popped from the stack has not yet had its children swapped by this loop.

Mechanics:
    Pop a node, swap left and right, then push the non-empty children.

Common pitfalls:
    Return the original root pointer after mutating nodes in place.

Complexity:
    Time: O(n); Space: O(h) average, O(n) worst case

When to choose this variant:
    Use this when recursion is unnecessary or stack depth is a concern.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
