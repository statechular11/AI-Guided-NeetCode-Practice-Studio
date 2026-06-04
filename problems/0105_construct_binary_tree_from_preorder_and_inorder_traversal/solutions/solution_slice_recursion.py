"""
105. Construct Binary Tree from Preorder and Inorder Traversal - readable slice recursion

Variant role:
    educational baseline

Core idea:
    Preorder reveals the root first; inorder splits the left and right subtrees around that root.

Key invariant:
    build(pre, ino) constructs exactly the tree whose preorder and inorder traversals are those slices.

Mechanics:
    Take pre[0] as the root, find it in inorder, then split both traversal slices into left and right portions.

Common pitfalls:
    This version copies lists and searches linearly. The index-map version keeps the same idea but avoids repeated slicing and index lookup.

Complexity:
    Time: O(n^2); Space: O(n^2) from slicing

When to choose this variant:
    Use this to understand the traversal relationship before moving to the optimized preorder-index solution.
"""

from typing import List, Optional

from common.lc_types import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_value = preorder[0]
        root = TreeNode(root_value)
        split = inorder.index(root_value)
        root.left = self.buildTree(preorder[1:1 + split], inorder[:split])
        root.right = self.buildTree(preorder[1 + split:], inorder[split + 1:])
        return root
