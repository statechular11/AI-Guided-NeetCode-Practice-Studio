"""
143. Reorder List - Stack Reference

Reorder the list using a stack of node objects.

Variant role:
    Baseline learning solution. It makes the target order easy to see:
    repeatedly take one node from the front and one node from the back. It is
    not the best interview target because it uses O(n) extra memory.

Core idea:
    A stack gives access to tail nodes in reverse order. Traverse the list once
    and push every node. Then walk from the head and pop one tail node at a
    time, inserting it after the current front node.

Step-by-step:
    For:

        1 -> 2 -> 3 -> 4 -> 5

    Build:

        stack = [1, 2, 3, 4, 5]

    Start at the front node 1:

        pop 5 and insert after 1:
        1 -> 5 -> 2 -> 3 -> 4

        move to the next front node 2,
        pop 4 and insert after 2:
        1 -> 5 -> 2 -> 4 -> 3

    Stop after `n // 2` insertions because each insertion consumes one node from
    the back and one position from the front.

Why the final `cur.next = None` matters:
    During rewiring, old links may temporarily point into the old list order.
    After the required front/back insertions, `cur` is the final tail of the
    reordered list. Clearing `cur.next` prevents stale links from creating a
    cycle or leaving extra nodes attached.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    Use it to understand the desired ordering or as a quick baseline if extra
    memory is allowed. Then upgrade to the split/reverse/weave solution for
    O(1) extra space.
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

        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        cur = head
        for _ in range(len(stack) // 2):
            tail = stack.pop()
            nxt = cur.next
            cur.next = tail
            tail.next = nxt
            cur = nxt

        cur.next = None
