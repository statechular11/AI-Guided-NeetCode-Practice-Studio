"""
206. Reverse Linked List - Explicit Stack Reference

Reverse a singly linked list using an explicit stack of nodes.

Variant role:
    Learning bridge between the iterative and recursive solutions.

Core idea:
    A stack reverses order naturally. Push every node while traversing the list
    from left to right, then pop nodes to reconnect them from right to left.

Step-by-step:
    For:

        1 -> 2 -> 3 -> None

    Push nodes:

        stack = [1, 2, 3]

    Pop and reconnect:

        new_head = 3
        3.next = 2
        2.next = 1
        1.next = None

Pitfall:
    The final `tail.next = None` is important because node 1 originally pointed
    to node 2. Without clearing it, the reversed list can form a cycle.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    This is not the best interview solution because it uses O(n) extra space.
    It is useful when learning because it makes the reversal order explicit and
    mirrors what recursion does implicitly.
"""

from typing import Optional

from common.lc_types import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        new_head = stack.pop()
        tail = new_head

        while stack:
            tail.next = stack.pop()
            tail = tail.next

        tail.next = None
        return new_head
