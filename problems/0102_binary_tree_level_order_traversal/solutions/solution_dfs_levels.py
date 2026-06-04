"""
102. Binary Tree Level Order Traversal - DFS carrying depth

Variant role:
    alternative tree traversal reference

Core idea:
    Level order can be produced without a queue by recording each node into the list for its depth.

Key invariant:
    result[d] contains exactly the node values seen so far at depth d.

Mechanics:
    DFS visits a node with its depth. If this is the first node at that depth, append a new level list, then recurse to children at depth + 1.

Common pitfalls:
    DFS traversal order still matters for left-to-right output: visit left child before right child.

Complexity:
    Time: O(n); Space: O(h) recursion plus output

When to choose this variant:
    Use this to connect recursive tree depth with level-indexed output; BFS queue remains the most direct level-order solution.
"""

from typing import List, Optional

from common.lc_types import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: list[list[int]] = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if depth == len(result):
                result.append([])
            result[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result
