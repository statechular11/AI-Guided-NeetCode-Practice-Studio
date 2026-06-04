"""
25. Reverse Nodes in k-Group - stack-assisted relinking

Variant role:
    Educational variant. It uses O(k) extra space to make the reversal order
    obvious. It does not satisfy the O(1)-extra-space follow-up, but it is a good
    stepping stone toward the in-place pointer solution.

Core idea:
    For each complete group, push the k nodes into a stack/list. Popping that
    stack yields the nodes in reverse order. Relink those popped nodes after
    `group_prev`, then attach the tail to `group_next`.

Mechanics:
    1. Starting at `group_prev.next`, try to collect k nodes.
    2. If fewer than k nodes remain, return; the suffix stays unchanged.
    3. Save `group_next`, the node after the k collected nodes.
    4. Pop nodes from the stack and append them to the output chain.
    5. Link the new tail to `group_next`.

Trace:
    [1, 2, 3, 4, 5], k = 2

    First group stack: [1, 2]
    Pop order: 2, 1
    Reconnect:
        dummy -> 2 -> 1 -> 3 -> 4 -> 5

    Second group stack: [3, 4]
    Pop order: 4, 3
    Reconnect:
        dummy -> 2 -> 1 -> 4 -> 3 -> 5

    Node 5 is left unchanged because it is not a full group.

Why this helps:
    The stack version isolates the "reverse k nodes" idea from the harder
    in-place reversal loop. Once the group boundary and reconnection are clear,
    the stack can be replaced with pointer rewiring.

Common pitfalls:
    - Forgetting to reconnect the reversed group tail to `group_next`.
    - Continuing when fewer than k nodes remain.
    - Accidentally creating a cycle by leaving the old tail link in place; the
      final `group_prev.next = group_next` breaks that old connection.

Complexity:
    Time: O(n).
    Space: O(k) for the stack.

When to choose this variant:
    Use it for learning or as a first draft. In interviews, mention it as a
    stepping stone, then move to the O(1)-space iterative solution.
"""

from typing import Optional

from common.lc_types import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            stack: list[ListNode] = []
            node = group_prev.next
            for _ in range(k):
                if not node:
                    return dummy.next
                stack.append(node)
                node = node.next

            group_next = node
            while stack:
                group_prev.next = stack.pop()
                group_prev = group_prev.next
            group_prev.next = group_next
