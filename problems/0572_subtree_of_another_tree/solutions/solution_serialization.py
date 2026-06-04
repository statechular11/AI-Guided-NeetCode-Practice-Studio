"""
572. Subtree of Another Tree - tree serialization containment

Variant role:
    alternative tree-shape reference

Core idea:
    Serialize both trees with null markers and separators, then test whether subRoot's serialization appears inside root's serialization.

Key invariant:
    The serialization preserves both values and exact tree shape, including missing children.

Mechanics:
    Use preorder with explicit null tokens so different shapes cannot collapse into the same string.

Common pitfalls:
    A serialization without null markers can produce false positives for different tree shapes.

Complexity:
    Time: O(m + n); Space: O(m + n)

When to choose this variant:
    Use this to understand the shape-matching requirement; same-tree scanning is usually easier to explain in interviews.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return ",#"
            return f",{node.val}" + serialize(node.left) + serialize(node.right)

        return serialize(subRoot) in serialize(root)
