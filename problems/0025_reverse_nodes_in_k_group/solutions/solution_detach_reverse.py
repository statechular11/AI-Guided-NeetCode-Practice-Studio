"""
25. Reverse Nodes in k-Group - detach, reverse, reconnect

Variant role:
    Alternative O(1)-space formulation. It makes the group boundary especially
    explicit by temporarily cutting the group from the rest of the list.

Core idea:
    For each complete group:

        group_prev -> group_start -> ... -> kth -> group_next

    Temporarily set `kth.next = None`, reverse the isolated list
    `group_start -> ... -> kth`, and reconnect the reversed group back into the
    original chain.

Mechanics:
    1. Find `kth`, the kth node after `group_prev`.
    2. If `kth` is missing, return; the suffix is shorter than k.
    3. Save `group_start = group_prev.next` and `group_next = kth.next`.
    4. Cut the group with `kth.next = None`.
    5. Reverse the isolated group using ordinary linked-list reversal.
    6. Connect `group_prev.next` to the reversed head.
    7. Connect the old group head, now the tail, to `group_next`.
    8. Move `group_prev` to that tail.

Trace:
    [1, 2, 3, 4, 5], k = 3

    group_start = 1, kth = 3, group_next = 4

    Cut:
        1 -> 2 -> 3 -> None      4 -> 5

    Reverse isolated group:
        3 -> 2 -> 1 -> None      4 -> 5

    Reconnect:
        dummy -> 3 -> 2 -> 1 -> 4 -> 5

    The remaining [4, 5] has fewer than k nodes, so it is left as-is.

Why this is correct:
    Cutting the group converts the hard problem into two simpler operations:
    reverse a normal complete list segment, then reconnect two saved boundaries.
    The saved `group_next` ensures the rest of the list is not lost.

Common pitfalls:
    - Forgetting to save `group_next` before `kth.next = None`.
    - Forgetting that `group_start` becomes the tail after reversal.
    - Returning the reversed group head directly instead of `dummy.next`.
    - Cutting an incomplete suffix; always confirm `kth` first.

Complexity:
    Time: O(n).
    Space: O(1).

When to choose this variant:
    Use it when pointer boundaries feel easier to reason about with an explicit
    cut. The primary half-open version avoids temporarily breaking the list, but
    this variant is often easier to debug aloud.
"""

from typing import Optional

from common.lc_types import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self._get_kth(group_prev, k)
            if not kth:
                return dummy.next

            group_start = group_prev.next
            group_next = kth.next

            kth.next = None
            group_prev.next = self._reverse(group_start)
            group_start.next = group_next
            group_prev = group_start

    def _get_kth(self, node: ListNode, k: int) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
