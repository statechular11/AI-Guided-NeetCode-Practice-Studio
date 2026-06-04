"""
19. Remove Nth Node From End of List - Two-Pass Length Reference

Remove the nth node from the end of a singly linked list and return the new
head.

Variant role:
    Clarity-first baseline solution.

Core idea:
    Count the list length first. The nth node from the end is at zero-based
    index:

        length - n

    from the front. Walk to the predecessor of that index, then remove its next
    node.

Walkthrough:
    For:

        head = [1, 2, 3, 4, 5]
        n = 2

    First pass:

        length = 5

    Convert from-end position to front index:

        target index = 5 - 2 = 3

    The predecessor index is 2, which is node 3. Rewriting node 3's next pointer
    skips node 4:

        prev.next = prev.next.next

Why dummy:
    When the target index is 0, the original head must be removed. Starting the
    predecessor walk from dummy keeps head deletion and middle deletion
    identical.

Relationship to the one-pass solution:
    The one-pass fast/slow version avoids the explicit length pass by preserving
    a fixed gap between two pointers. This two-pass version is easier to derive
    because it names the target index directly.

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Choose this first if you want the simplest reasoning path. Then mention
    that the one-pass fast/slow version compresses the length pass into a
    fixed-gap traversal.
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

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        steps_to_prev = length - n
        prev = dummy
        for _ in range(steps_to_prev):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next
