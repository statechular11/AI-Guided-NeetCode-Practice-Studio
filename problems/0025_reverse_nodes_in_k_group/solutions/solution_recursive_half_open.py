"""
25. Reverse Nodes in k-Group - recursive half-open reversal

Variant role:
    Elegant recursive formulation. It is not O(1) extra space because recursion
    uses call stack frames, but it cleanly separates "is there a full group?"
    from "reverse this half-open segment".

Core idea:
    For the current head, walk k nodes ahead.

    - If fewer than k nodes remain, return head unchanged.
    - Otherwise, let `group_next` be the node after the group.
    - Reverse the half-open segment [head, group_next).
    - Recursively solve the suffix starting at `group_next`.
    - Connect the old head, now the group tail, to the recursively processed
      suffix.

Half-open reverse helper:
    `_reverse_range(start, stop)` reverses nodes starting at `start` and stops
    before `stop`.

    Initializing `prev = stop` means the old head will point to the untouched
    suffix after reversal, which is exactly the connection we need.

Trace:
    reverseKGroup([1, 2, 3, 4, 5], k = 2)

    First call confirms [1, 2] is complete and `group_next = 3`.
    Reverse [1, 3):
        2 -> 1 -> 3
    Then recurse on [3, 4, 5].

    Second call confirms [3, 4] is complete and `group_next = 5`.
    Reverse [3, 5):
        4 -> 3 -> 5
    Then recurse on [5].

    Third call sees fewer than 2 nodes, so it returns [5] unchanged.

    Reconnection produces:
        2 -> 1 -> 4 -> 3 -> 5

Common pitfalls:
    - Recursing before reversing the current group can make reconnection harder
      to reason about.
    - Forgetting to return the original head unchanged when fewer than k nodes
      remain.
    - Treating `stop` as part of the reversed segment; it is the first node
      after the group.
    - Calling this O(1) space; recursion adds O(number of groups) stack space.

Complexity:
    Time: O(n).
    Space: O(n / k) recursion depth, O(n) in the worst case when k = 1.

When to choose this variant:
    Use it to understand the recursive structure or if recursion is acceptable.
    For the follow-up, prefer the iterative O(1)-space reference.
"""

from typing import Optional

from common.lc_types import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group_next = head
        for _ in range(k):
            if not group_next:
                return head
            group_next = group_next.next

        new_head = self._reverse_range(head, group_next)
        head.next = self.reverseKGroup(group_next, k)
        return new_head

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
