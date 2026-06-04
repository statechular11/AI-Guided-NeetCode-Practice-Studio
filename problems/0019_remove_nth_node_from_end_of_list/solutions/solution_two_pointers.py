"""
19. Remove Nth Node From End of List - One-Pass Fast/Slow Reference

Remove the nth node from the end of a singly linked list and return the new
head.

Variant role:
    Primary interview-ready one-pass solution.

Core idea:
    Put a dummy node before `head`, then keep `fast` exactly `n + 1` links ahead
    of `slow`. That extra one-link offset means that when `fast` falls off the
    list, `slow` is the predecessor of the node to remove. Deleting is then the
    usual predecessor rewrite:

        slow.next = slow.next.next

Why the gap is `n + 1`:
    Both pointers start at `dummy`. If `fast` advances `n + 1` links first, then
    `slow` is positioned one node before the target when `fast` reaches `None`.
    Linked-list deletion needs that predecessor, not the target itself.

Walkthrough:
    For:

        head = [1, 2, 3, 4, 5]
        n = 2

    Start:

        dummy -> 1 -> 2 -> 3 -> 4 -> 5
        slow = dummy
        fast = dummy

    Move `fast` three links from dummy:

        fast = 3

    Move `fast` and `slow` together until `fast` becomes `None`. `slow` ends on
    node 3, so `slow.next` is node 4, the target.

Why dummy:
    If `n` equals the list length, the target is the original head. Keeping
    `slow` on dummy makes that case use the same rewrite as deleting any middle
    or tail node.

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Choose this when the follow-up asks for one pass. The main thing to explain
    out loud is the invariant: `slow` stops immediately before the node being
    removed.
"""

from typing import Optional

from common.lc_types import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
