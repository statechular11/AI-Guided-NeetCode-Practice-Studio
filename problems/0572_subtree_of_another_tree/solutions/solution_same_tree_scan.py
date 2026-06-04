"""
572. Subtree of Another Tree - Dfs Scan With Same Tree Comparison

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Subtree means same structure and values from some node downward.

    This specific variant uses: DFS scan with same-tree comparison.

Key invariant:
    Each recursive or BFS step gives a precise meaning to the current node/subtree, so child results combine into the parent result without relying on parent-child checks alone.

Mechanics:
    1. Handle the empty subtree first.
    2. Process the current node with the exact information the helper owns.
    3. Recurse or enqueue children with updated context.
    4. Combine child results according to the helper's return contract.

Walkthrough:
    On the local case `example_1`, the input is `{"root": [3, 4, 5, 1, 2], "subRoot": [4, 1, 2]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Be explicit about traversal order: preorder, inorder, postorder, or level order. For recursive tree code, define what each call returns before writing pointer changes. Distinguish node identity from node value for LCA-style problems. For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

Complexity:
    Time: O(n*m); Space: O(h)

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Scan root and compare same-tree at candidate matches.

        At each node in root, check whether the subtree is identical to subRoot.
        If not, recurse into root's children.

        Complexity: O(n*m) worst case, O(h) stack.
        """
        def same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a or not b:
                return a is b
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        if not root:
            return subRoot is None
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
