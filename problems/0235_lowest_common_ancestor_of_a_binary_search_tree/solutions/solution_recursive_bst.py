"""
235. Lowest Common Ancestor of a Binary Search Tree - recursive BST split point

Variant role:
    alternative BST traversal reference

Core idea:
    In a BST, if both targets are on the same side of root, the LCA must be on that side; otherwise root is the split point.

Key invariant:
    The current root is an ancestor of both targets. Recursing preserves that property for the side containing both targets.

Mechanics:
    Compare p.val and q.val to root.val. Recurse left if both are smaller, right if both are larger, else return root.

Common pitfalls:
    The first split point includes the case where root equals p or q.

Complexity:
    Time: O(h); Space: O(h)

When to choose this variant:
    Use this when recursive BST reasoning reads more naturally than the iterative loop.
"""

from common.lc_types import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
