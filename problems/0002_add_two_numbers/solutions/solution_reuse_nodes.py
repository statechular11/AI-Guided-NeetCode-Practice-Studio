"""
2. Add Two Numbers - Reuse-Input-Nodes Reference

Add two numbers represented by reverse-order linked lists while reusing input
nodes for the result.

Variant role:
    Allocation-minimizing mutation variant.

Core idea:
    Instead of creating a brand-new result node for every digit, reuse nodes from
    `l1` while it exists, then reuse leftover nodes from `l2`. Only allocate a
    new node when there is a final carry after both lists are exhausted.

Step-by-step:
    1. Use `l1` as the result head when possible.
    2. At each digit, choose the next reusable result node from `l1`, otherwise
       from `l2`.
    3. Add the matching `l2` digit when the result node came from `l1`.
    4. Write the result digit back into the reused node.
    5. Attach reused `l2` nodes or a final carry node to the result tail.

Example:
    [9] + [9,9]

    Reuse the first `l1` node as 8 with carry 1, attach and reuse the next `l2`
    node as 0 with carry 1, then allocate a final 1.

    Result:

        [8,0,1]

Mutation tradeoff:
    This version mutates input nodes. That can reduce allocation, but it is
    usually not the first interview answer unless mutation is explicitly allowed
    or desired.

Complexity:
    Time:
        O(max(n, m))

    Space:
        O(1) auxiliary space, excluding any unavoidable final carry node. This
        mutates and reuses input nodes.

When to choose this variant:
    Choose this only when mutation is allowed and the interviewer cares about
    allocation. The dummy-node version is clearer and preserves inputs
    conceptually.
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
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1
        node1 = l1
        node2 = l2
        tail = None
        carry = 0

        while node1 or node2 or carry:
            if node1:
                result_node = node1
                node1 = node1.next
                total = result_node.val
                if node2:
                    total += node2.val
                    node2 = node2.next
            elif node2:
                result_node = node2
                node2 = node2.next
                tail.next = result_node
                total = result_node.val
            else:
                result_node = ListNode()
                tail.next = result_node
                total = 0

            total += carry
            carry, result_node.val = divmod(total, 10)
            tail = result_node

        return head
