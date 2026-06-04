"""
143. Reorder List - Split, Reverse, and Weave Reference

Reorder:

    L0 -> L1 -> ... -> Ln

into:

    L0 -> Ln -> L1 -> Ln-1 -> ...

Variant role:
    Primary interview solution. It modifies links in place and uses O(1) extra
    memory.

Core idea:
    The target order alternates between the front of the list and the back of
    the list:

        first front node, last node, second front node, second last...

    A singly linked list cannot move backward, so make the back half easy to
    consume by reversing it.

Step 1: split around the middle:
    Use slow/fast pointers. When `fast` cannot move two steps further, `slow`
    is at the end of the first half.

    For odd length:

        1 -> 2 -> 3 -> 4 -> 5

    split into:

        first:  1 -> 2 -> 3
        second: 4 -> 5

    For even length:

        1 -> 2 -> 3 -> 4

    split into:

        first:  1 -> 2
        second: 3 -> 4

    The assignment `slow.next = None` is important because it separates the two
    halves before weaving. Without it, old links can create a cycle or leave
    extra tail nodes attached.

Step 2: reverse the second half:
    Reverse:

        4 -> 5

    into:

        5 -> 4

    Now the nodes that should be interleaved after each first-half node are
    available from left to right.

Step 3: weave the two halves:
    Repeatedly save both next pointers, then attach one node from the reversed
    second half after one node from the first half:

        first.next = second
        second.next = first_next

    The saved `first_next` and `second_next` pointers preserve access to the
    remaining nodes before links are overwritten.

Example:
    [1,2,3,4,5] -> split [1,2,3] and [4,5], reverse second to [5,4], then weave
    -> [1,5,2,4,3].

Complexity:
    Time:
        O(n)

    Space:
        O(1)

When to choose this variant:
    Use this in interviews. It satisfies the in-place requirement and is the
    standard composition of three linked-list skills: middle-finding, reversal,
    and alternating merge.
"""

from typing import Optional

from common.lc_types import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev

        first = head
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
