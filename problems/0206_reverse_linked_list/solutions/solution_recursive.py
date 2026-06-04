"""
206. Reverse Linked List - Recursive Reference

Reverse a singly linked list recursively.

Variant role:
    Recursive learning variant and follow-up solution.

Core idea:
    Reverse the suffix starting at `head.next`, then put `head` after that
    suffix by setting:

        head.next.next = head
        head.next = None

Recursive invariant:
    `reverseList(head.next)` returns the head of the reversed suffix. After that
    call, `head.next` is the tail of the reversed suffix, so appending `head`
    after it is exactly `head.next.next = head`.

Step-by-step:
    For:

        1 -> 2 -> 3 -> None

    The recursive call reverses the suffix:

        3 -> 2 -> None

    At the frame where `head` is 1:

        head.next is 2
        head.next.next = head turns 2.next into 1
        head.next = None makes 1 the new tail

    New head remains 3.

Base case:
    Empty list and single-node list are already reversed.

Complexity:
    Time:
        O(n)

    Space:
        O(n) recursion stack

When to choose this variant:
    Use this if the interviewer asks for recursion or if you want to practice
    recursive linked-list pointer reasoning. In Python, the iterative solution
    is usually safer for long lists because recursion uses call-stack space.
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
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
