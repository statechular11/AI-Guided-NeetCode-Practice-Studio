"""
23. Merge k Sorted Lists - Sequential Pairwise Merge Baseline

Core idea:
    Reuse the familiar "merge two sorted lists" helper. Start with an empty
    merged list, then merge each input list into it one at a time.

Key invariant:
    After processing the first `i` lists, `merged` is the sorted merge of exactly
    those `i` lists. Merging `merged` with the next sorted list preserves sorted
    order.

Why this works:
    The two-list merge primitive is correct for sorted linked lists. Applying it
    repeatedly eventually includes every list. The drawback is balance: early
    nodes can be reprocessed many times as the accumulated `merged` list grows.

Step-by-step mechanics:
    1. Set `merged = None`.
    2. For each list head, replace `merged` with `merge_two(merged, head)`.
    3. Return the final merged list.

Example:
    For 4 lists, sequential merging does:

        (((list0 + list1) + list2) + list3)

    Divide and conquer instead does:

        ((list0 + list1) + (list2 + list3))

    The balanced version avoids repeatedly merging a large accumulated list with
    one small list.

Common pitfalls:
    - Thinking repeated pairwise merge is automatically O(N log k); it is only
      O(N log k) when the merges are balanced.
    - Forgetting to use a dummy node in `merge_two`, leading to messy head
      special cases.
    - Losing the remainder of a list after one side is exhausted.

Complexity:
    Time:
        O(N * k) in the worst case when many lists have similar length. More
        precisely, nodes in early lists may be merged again and again.

    Space:
        O(1) extra, excluding recursion and output. The implementation reuses
        original nodes.

When to choose this variant:
    Use it as the stepping stone from "merge two lists" to the optimized
    divide-and-conquer solution. It is simple but usually not the final answer.
"""

from typing import List, Optional

from common.lc_types import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None
        for node in lists:
            merged = self._merge_two(merged, node)
        return merged

    def _merge_two(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a or b
        return dummy.next
