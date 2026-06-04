"""
98. Validate Binary Search Tree - Dfs With Strict Value Bounds

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Use ancestor-derived bounds, not only parent-child comparisons.

    This specific variant uses: DFS with strict value bounds.

Key invariant:
    Each recursive or BFS step gives a precise meaning to the current node/subtree, so child results combine into the parent result without relying on parent-child checks alone.

Mechanics:
    1. Handle the empty subtree first.
    2. Process the current node with the exact information the helper owns.
    3. Recurse or enqueue children with updated context.
    4. Combine child results according to the helper's return contract.

Walkthrough:
    On the local case `example_1`, the input is `{"root": [2, 1, 3]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Be explicit about traversal order: preorder, inorder, postorder, or level order. For recursive tree code, define what each call returns before writing pointer changes. Distinguish node identity from node value for LCA-style problems. For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

Complexity:
    Time: O(n); Space: O(h)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.
"""

from typing import Optional

from common.lc_types import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Validate a BST by carrying strict lower/upper bounds.

        Each node constrains the whole subtree below it, not just its immediate
        children. The left subtree must stay below node.val and the right
        subtree must stay above node.val. Bounds are strict because duplicates
        are not allowed in this problem.

        Complexity: O(n) time, O(h) recursion stack.
        """
        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float('-inf'), float('inf'))
