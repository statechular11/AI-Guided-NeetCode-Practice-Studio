"""
141. Linked List Cycle - Floyd Slow/Fast Reference

Detect whether a singly linked list contains a cycle.

Variant role:
    Primary interview solution and the answer to the O(1)-memory follow-up.

Core idea:
    Move `slow` by one step and `fast` by two steps. If a cycle exists, `fast`
    eventually laps `slow` inside the cycle. If `fast` reaches `None`, the list
    terminates and has no cycle.

Why meeting proves a cycle:
    In an acyclic list, both pointers only move forward toward `None`; there is
    no path that lets a pointer revisit an earlier node.

    In a cyclic list, once both pointers enter the cycle, each loop iteration
    changes their circular distance by one because `fast` moves two nodes while
    `slow` moves one. Modulo the cycle length, that distance must eventually
    become zero, so both variables reference the same node object.

Mental trace:
    For:

        3 -> 2 -> 0 -> -4
             ^         |
             |_________|

    `slow` moves one node per round:

        3, 2, 0, -4, 2, ...

    `fast` moves two nodes per round:

        3, 0, 2, -4, 0, ...

    Inside the cycle, `fast` keeps gaining one node on `slow`; they must
    eventually point to the same node.

Identity, not value:
    Use `slow is fast`, not `slow.val == fast.val`. A cycle is about visiting
    the same node object again, not seeing the same value.

Loop guard:
    Check:

        while fast and fast.next:

    before advancing `fast.next.next`; otherwise a short acyclic list can raise
    an attribute error.

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Use this in interviews once you are comfortable with the invariant. It is
    optimal: linear time and constant extra memory.
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
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
