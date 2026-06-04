"""
297. Serialize and Deserialize Binary Tree - preorder tokens with null markers

Variant role:
    alternative codec reference

Core idea:
    Preorder serialization with explicit null markers carries enough information to reconstruct the tree recursively.

Key invariant:
    deserialize consumes exactly the tokens belonging to the subtree currently being rebuilt.

Mechanics:
    Serialize node value, then left subtree, then right subtree. Deserialize by reading one token: '#' means None, otherwise rebuild left and right.

Common pitfalls:
    Without null markers, preorder alone cannot distinguish many tree shapes.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this when recursive tree shape encoding is clearer than level-order queues.
"""

from typing import Optional

from common.lc_types import TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens: list[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                tokens.append("#")
                return
            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))

        def build() -> Optional[TreeNode]:
            token = next(tokens)
            if token == "#":
                return None
            node = TreeNode(int(token))
            node.left = build()
            node.right = build()
            return node

        return build()
