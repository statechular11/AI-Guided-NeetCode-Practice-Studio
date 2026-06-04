"""
141. Linked List Cycle - Visited-Set Reference

Detect whether a singly linked list contains a cycle by remembering node
objects that have already been visited.

Variant role:
    Baseline clarity solution. It is usually the easiest version to reason
    about, but it does not satisfy the O(1)-memory follow-up.

Core idea:
    Walk through the list. If we ever see the same node object twice, following
    `.next` pointers has looped back into a cycle. If traversal reaches `None`,
    the list terminates and has no cycle.

Why this uses node identity:
    The set stores node objects, not node values. Two different nodes can have
    the same value, and that should not count as a cycle.

    In Python:

        cur in seen

    checks whether this exact object has appeared before. That matches the
    problem definition: a cycle means a node can be reached again by repeatedly
    following `.next`.

Step-by-step:
    For:

        3 -> 2 -> 0 -> -4
             ^         |
             |_________|

    traversal sees:

        3, 2, 0, -4, 2

    The second time it sees the same node object `2`, it returns True.

    For:

        1 -> 2 -> None

    traversal sees:

        1, 2, None

    It reaches `None`, so it returns False.

Pitfall:
    Do not store only `node.val`. Repeated values are allowed in a linked list,
    and repeated values do not imply a cycle.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    Use it as a first-pass solution if you want maximum clarity. Then upgrade to
    Floyd's slow/fast pointers to satisfy the constant-space follow-up.
"""

from typing import Optional

from common.lc_types import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head

        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next

        return False
