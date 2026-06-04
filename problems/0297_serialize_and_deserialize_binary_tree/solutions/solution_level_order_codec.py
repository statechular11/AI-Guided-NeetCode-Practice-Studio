"""
297. Serialize and Deserialize Binary Tree - Level Order Tokens With Null Markers

Variant role:
    primary codec solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Include null markers during serialization so shape can be reconstructed.

    This specific variant uses: level-order tokens with null markers.

Key invariant:
    Each recursive or BFS step gives a precise meaning to the current node/subtree, so child results combine into the parent result without relying on parent-child checks alone.

Mechanics:
    1. Handle the empty subtree first.
    2. Process the current node with the exact information the helper owns.
    3. Recurse or enqueue children with updated context.
    4. Combine child results according to the helper's return contract.

Walkthrough:
    On the local case `example_1`, the input is `{"root": [1, 2, 3, null, null, 4, 5]}` and the expected result is `{"return": [1, 2, 3, null, null, 4, 5]}`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Be explicit about traversal order: preorder, inorder, postorder, or level order. For recursive tree code, define what each call returns before writing pointer changes. Distinguish node identity from node value for LCA-style problems. For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary codec solution. Be ready
    to explain both the state invariant and why the update step preserves it.
"""

from typing import Optional

from common.lc_types import TreeNode

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    """Level-order serializer/deserializer for binary trees.

    Serialization emits comma-separated values with # for missing children.
    Deserialization rebuilds the tree by reading child pairs from the token list.

    Complexity: O(n) time and O(n) space for both operations.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        tokens = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                tokens.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                tokens.append('#')
        while tokens and tokens[-1] == '#':
            tokens.pop()
        return ','.join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tokens = data.split(',')
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(tokens):
            node = queue.popleft()
            if i < len(tokens) and tokens[i] != '#':
                node.left = TreeNode(int(tokens[i]))
                queue.append(node.left)
            i += 1
            if i < len(tokens) and tokens[i] != '#':
                node.right = TreeNode(int(tokens[i]))
                queue.append(node.right)
            i += 1
        return root
