"""
25. Reverse Nodes in k-Group - iterative in-place group reversal

Variant role:
    Primary interview solution. It satisfies the follow-up requirement:
    reverse by changing node pointers in O(1) extra space.

Core idea:
    Treat each group as a half-open segment:

        group_prev -> [group_start ... kth] -> group_next

    Before touching pointers, first confirm that `kth` exists. If it does not,
    the remaining suffix has fewer than k nodes and must stay unchanged.

    Once a full group exists, reverse exactly the nodes in:

        [group_start, group_next)

    The helper `_reverse_range(group_start, group_next)` reverses the half-open
    range and returns the new head of that range, which is `kth`.

    Then reconnect:

        group_prev.next = reversed_head
        group_prev = group_start       # old head is now the tail

Reverse-range helper invariant:
    Set `prev = group_next` and `cur = group_start`.

    Inside `_reverse_range`, the loop:

        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    makes every processed node point backward toward the already-processed
    suffix. Starting `prev` at `group_next` is the trick: when the old group head
    becomes the group tail, it already points to the first node after the group.

Step-by-step trace:
    head = [1, 2, 3, 4, 5], k = 2

    Before first group:
        dummy -> 1 -> 2 -> 3 -> 4 -> 5
        group_prev = dummy
        kth = 2
        group_next = 3

    Call _reverse_range(1, 3) to reverse [1, 3):
        prev = 3, cur = 1
        1.next = 3
        prev = 1, cur = 2
        2.next = 1
        prev = 2, cur = 3 stop
        return 2

    Reconnect:
        group_prev.next = returned head = 2
        group_prev = group_start = 1

    List is now:
        dummy -> 2 -> 1 -> 3 -> 4 -> 5

    The next group starts after node 1 and reverses [3, 5) into 4 -> 3.

Why the incomplete suffix stays unchanged:
    `_get_kth(group_prev, k)` walks k nodes ahead from the node before the next
    group. If it cannot find k nodes, the algorithm breaks before rewiring
    anything. This is essential for cases like [1, 2, 3, 4, 5], k = 3, where
    [4, 5] must remain unchanged.

Common pitfalls:
    - Reversing before confirming a full group exists.
    - Losing `group_next` before the reversal loop.
    - Forgetting that the old group head becomes the tail after reversal.
    - Moving `group_prev` to `kth` instead of to the old group head.
    - Trying to swap values; the problem requires rewiring nodes.

Complexity:
    Time: O(n). Every node is visited a constant number of times.
    Space: O(1). Only pointer variables are used.

When to choose this variant:
    Use this as the main interview answer. It is iterative, in-place, and
    directly addresses the O(1) extra-space follow-up.
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
                break
            group_start = group_prev.next
            group_next = kth.next

            group_prev.next = self._reverse_range(group_start, group_next)
            group_prev = group_start

        return dummy.next

    def _get_kth(self, node: ListNode, k: int) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def _reverse_range(
        self, start: Optional[ListNode], stop: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = stop
        cur = start
        while cur is not stop:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
