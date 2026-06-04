"""
138. Copy List with Random Pointer - Interweaving Reference

Deep-copy a linked list where each node has both `next` and `random` pointers.

Variant role:
    Optimized O(1)-extra-space linked-list solution.

Core idea:
    Insert each clone immediately after its original node:

        A -> B -> C
        A -> A' -> B -> B' -> C -> C'

    Now every original node's clone is `original.next`, and every original
    random target's clone is `original.random.next`. After assigning random
    pointers, split the interwoven list back into the original chain and the
    cloned chain.

Three passes:
    1. Weave each clone after its original.
    2. Assign clone random pointers using `cur.random.next`.
    3. Restore original `.next` pointers and extract the clone list.

Walkthrough:
    If original B.random points to A, then after weaving:

        B.next is B'
        B.random is A
        B.random.next is A'

    So B'.random should be A'.

Pointer-restoration invariant:
    The returned copy must be detached, and the input list should be restored to
    its original `next` chain.

Split-pass mechanics:
    During extraction, keep `cur` on the current original node:

        clone = cur.next
        cur.next = clone.next
        copy_tail.next = clone
        copy_tail = clone
        cur = cur.next

    `cur.next = clone.next` restores the original chain. `copy_tail.next =
    clone` appends the clone to the detached copied chain.

Complexity:
    Time:
        O(n)

    Space:
        O(1) extra excluding cloned nodes

When to choose this variant:
    Choose this after the hash-map version when asked to reduce extra space. It
    is more pointer-heavy, so narrate the three passes clearly.
"""

from typing import Optional

from common.lc_types import RandomPointerNode as Node


# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        cur = head
        while cur:
            clone = Node(cur.val)
            clone.next = cur.next
            cur.next = clone
            cur = clone.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        dummy = Node(0)
        copy_tail = dummy
        cur = head
        while cur:
            clone = cur.next
            cur.next = clone.next
            copy_tail.next = clone
            copy_tail = clone
            cur = cur.next

        return dummy.next
