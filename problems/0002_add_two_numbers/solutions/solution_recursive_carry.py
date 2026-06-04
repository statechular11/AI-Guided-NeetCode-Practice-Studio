"""
2. Add Two Numbers - Recursive Carry Reference

Add two numbers represented by reverse-order linked lists.

Variant role:
    Recursive carry-propagation variant.

Core idea:
    The lists are already in least-significant-digit-first order, so a recursive
    call can represent "add the rest of the digits." Each frame consumes one
    node from each list if present, creates the current result digit, and passes
    the carry to the next frame.

Step-by-step:
    1. Stop only when both lists are exhausted and carry is 0.
    2. Sum the current `l1` digit, current `l2` digit, and carry.
    3. Create a node for `total % 10`.
    4. Recursively compute the next node with `total // 10`.

Example:
    [2,4,3] + [5,6,4]

    The frames write:

        7
        0 with carry 1
        8

    returning:

        [7,0,8]

Base case:
    The recursion ends only when there is no node left in either list and no
    carry left to emit. If carry is still 1, one more node is needed.

Complexity:
    Time:
        O(max(n, m))

    Space:
        O(max(n, m)) recursion stack, plus the returned list

When to choose this variant:
    Useful when the interviewer asks about the recursion tag or when you want to
    show the carry invariant compactly. The iterative dummy-node version is
    usually safer in Python for very long lists.
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
        def add_nodes(
            node1: Optional[ListNode],
            node2: Optional[ListNode],
            carry: int,
        ) -> Optional[ListNode]:
            if not node1 and not node2 and carry == 0:
                return None

            total = carry
            next1 = None
            next2 = None
            if node1:
                total += node1.val
                next1 = node1.next
            if node2:
                total += node2.val
                next2 = node2.next

            carry, digit = divmod(total, 10)
            return ListNode(digit, add_nodes(next1, next2, carry))

        return add_nodes(l1, l2, 0)
