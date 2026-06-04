"""
100. Same Tree - iterative paired-node stack

Variant role:
    alternative traversal reference

Core idea:
    Compare the two trees by popping corresponding node pairs from a stack.

Key invariant:
    Every pair on the stack represents positions that must match structurally and by value.

Mechanics:
    If both nodes are empty, continue. If only one is empty or values differ, fail. Otherwise push matching child pairs.

Common pitfalls:
    Checking values without checking structure lets missing children slip through.

Complexity:
    Time: O(n); Space: O(h) average, O(n) worst case

When to choose this variant:
    Use this when recursion depth is a concern or when practicing iterative tree traversals.
"""

from typing import Optional

from common.lc_types import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append((left.left, right.left))
            stack.append((left.right, right.right))
        return True
