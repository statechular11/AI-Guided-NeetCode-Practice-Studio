"""
104. Maximum Depth of Binary Tree - level-order depth count

Variant role:
    iterative traversal reference

Core idea:
    Count how many breadth-first layers are present in the tree.

Key invariant:
    At the start of each outer loop iteration, the queue holds exactly one depth level.

Mechanics:
    Process the current queue length, enqueue children for the next level, then increment depth.

Common pitfalls:
    Increment depth once per level, not once per node.

Complexity:
    Time: O(n); Space: O(w)

When to choose this variant:
    Use this when recursion depth may be a concern or when practicing level-order traversal.
"""

from collections import deque
from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
