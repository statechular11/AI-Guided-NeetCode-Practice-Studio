"""
199. Binary Tree Right Side View - right-first DFS

Variant role:
    alternative tree traversal reference

Core idea:
    The first node visited at each depth during a right-first traversal is the visible right-side node.

Key invariant:
    When depth == len(view), no node has been recorded for that depth yet, so the current right-first node is visible.

Mechanics:
    Visit node, then right child, then left child. Append the value only when entering a depth for the first time.

Common pitfalls:
    If you visit left before right, first-seen per depth becomes the left-side view instead.

Complexity:
    Time: O(n); Space: O(h)

When to choose this variant:
    Use this as a DFS counterpart to BFS level-order last-value logic.
"""

from typing import List, Optional

from common.lc_types import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view: list[int] = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if depth == len(view):
                view.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return view
