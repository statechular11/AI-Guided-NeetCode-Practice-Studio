"""
199. Binary Tree Right Side View - Bfs And Keep Last Node Per Level

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The visible value is the last node in each BFS level.

    This specific variant uses: BFS and keep last node per level.

Key invariant:
    Each recursive or BFS step gives a precise meaning to the current node/subtree, so child results combine into the parent result without relying on parent-child checks alone.

Mechanics:
    1. Handle the empty subtree first.
    2. Process the current node with the exact information the helper owns.
    3. Recurse or enqueue children with updated context.
    4. Combine child results according to the helper's return contract.

Walkthrough:
    On the local case `example_1`, the input is `{"root": [1, 2, 3, null, 5, null, 4]}` and the expected result is `[1, 3, 4]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Be explicit about traversal order: preorder, inorder, postorder, or level order. For recursive tree code, define what each call returns before writing pointer changes. Distinguish node identity from node value for LCA-style problems. For serialized tree outputs, remember that empty trees normalize to `None` in the local runner.

Complexity:
    Time: O(n); Space: O(width)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.
"""

from typing import Optional, List

from common.lc_types import TreeNode

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Return the last visible node at each level.

        BFS processes one level at a time. The final node popped in that level is
        the rightmost value visible from the right side.

        Complexity: O(n) time, O(width) space.
        """
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == level_size - 1:
                    result.append(node.val)
        return result
