"""
105. Construct Binary Tree from Preorder and Inorder Traversal - Preorder Root Pointer Plus Inorder Index Map

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Preorder identifies roots; inorder splits left and right subtree ranges.

    This specific variant uses: preorder root pointer plus inorder index map.

Key invariant:
    Each recursive or BFS step gives a precise meaning to the current node/subtree, so child results combine into the parent result without relying on parent-child checks alone.

Mechanics:
    1. Handle the empty subtree first.
    2. Process the current node with the exact information the helper owns.
    3. Recurse or enqueue children with updated context.
    4. Combine child results according to the helper's return contract.

Walkthrough:
    On the local case `example_1`, the input is `{"preorder": [3, 9, 20, 15, 7], "inorder": [9, 3, 15, 20, 7]}` and the expected result is `{"return": [3, 9, 20, null, null, 15, 7]}`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Be explicit about traversal order: preorder, inorder, postorder, or level order. For recursive tree code, define what each call returns before writing pointer changes. Distinguish node identity from node value for LCA-style problems. For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.
"""

from typing import Optional, List

from common.lc_types import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Build a tree from preorder and inorder traversals.

        Preorder gives the next root. Inorder tells how many nodes belong to
        the left and right subtrees. A value-to-index map makes each split O(1).

        Complexity: O(n) time, O(n) space.
        """
        index = {value: i for i, value in enumerate(inorder)}
        pre_i = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal pre_i
            if left > right:
                return None
            value = preorder[pre_i]
            pre_i += 1
            root = TreeNode(value)
            mid = index[value]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
