"""
2. Add Two Numbers - Iterative Digit-Carry Reference

Add two numbers represented by reverse-order linked lists.

Variant role:
    Primary linked-list solution.

Core idea:
    The linked lists already store least-significant digits first, so we can add
    exactly like elementary school addition: current digit from `l1`, current
    digit from `l2`, plus carry.

    For each position:

        total = carry + l1_digit + l2_digit
        digit = total % 10
        carry = total // 10

    `divmod(total, 10)` gives both values at once:

        carry, digit = divmod(total, 10)

Why the loop includes `carry`:
    The final addition can create one extra digit. For example:

        [9,9] + [1]

    writes 0, then 0, then still has carry 1, so the result needs a final node:

        [0,0,1]

Example:
    [2,4,3] + [5,6,4] represents:

        342 + 465

    Digit work:

        2 + 5 = 7
        4 + 6 = 10 -> write 0, carry 1
        3 + 4 + 1 = 8

    Result:

        [7,0,8]

Dummy-tail construction:
    `dummy` avoids special-casing the first result node. `cur` always points to
    the tail of the result built so far.

Complexity:
    Time:
        O(max(n, m))

    Space:
        O(max(n, m)) for the returned list

When to choose this variant:
    Use this in interviews. It is clear, handles uneven lengths naturally, and
    does not mutate the input lists.
"""

from typing import Optional

from common.lc_types import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry, digit = divmod(total, 10)
            cur.next = ListNode(digit)
            cur = cur.next

        return dummy.next
