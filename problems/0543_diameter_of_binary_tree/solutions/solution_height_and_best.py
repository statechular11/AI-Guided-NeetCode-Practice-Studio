"""
543. Diameter of Binary Tree - Postorder Height And Path Through Node Best

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Diameter through a node is left height plus right height.

    This specific variant uses: postorder height and path-through-node best.

Key invariant:
    Each recursive or BFS step gives a precise meaning to the current node/subtree, so child results combine into the parent result without relying on parent-child checks alone.

Mechanics:
    1. Handle the empty subtree first.
    2. Process the current node with the exact information the helper owns.
    3. Recurse or enqueue children with updated context.
    4. Combine child results according to the helper's return contract.

Walkthrough:
    On the local case `example_1`, the input is `{"root": [1, 2, 3, 4, 5]}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Compute diameter while returning subtree heights.

        The longest path through a node uses left_height + right_height edges.
        A postorder traversal updates the global best at each node.

        Complexity: O(n) time, O(h) stack.
        """
        best = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            best = max(best, left + right)
            return 1 + max(left, right)

        height(root)
        return best
