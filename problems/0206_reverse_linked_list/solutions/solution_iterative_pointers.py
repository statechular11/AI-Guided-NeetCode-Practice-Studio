"""
206. Reverse Linked List - Iterative Pointers Reference

Reverse a singly linked list iteratively with two moving pointers.

Variant role:
    Primary interview solution.

Core idea:
    Walk through the list and redirect each node's next pointer to the previous
    node. Save the original next pointer before overwriting it.

Pointer invariant:
    Before each loop iteration:

    - `prev` is the head of the already reversed prefix.
    - `cur` is the first node in the unreversed suffix.

Step-by-step:
    For a list:

        1 -> 2 -> 3 -> None

    Start:

        prev = None
        cur = 1

    At node 1:

        nxt = 2
        1.next = None
        prev = 1
        cur = 2

    At node 2:

        nxt = 3
        2.next = 1
        prev = 2
        cur = 3

    At node 3:

        nxt = None
        3.next = 2
        prev = 3
        cur = None

    `prev` now points to:

        3 -> 2 -> 1 -> None

Pitfall:
    Save `nxt = cur.next` before assigning `cur.next = prev`. If you overwrite
    `cur.next` first, you lose access to the rest of the original list.

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Use this in interviews. It is short, iterative, and uses O(1) extra space.
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
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
