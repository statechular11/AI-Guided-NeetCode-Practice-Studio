"""
23. Merge k Sorted Lists - Divide And Conquer Reference

Core idea:
    Merge lists in balanced rounds, like the merge step of merge sort. Instead
    of repeatedly merging one list into a growing result, pair lists together:

        round 1: merge pairs of size 1
        round 2: merge pairs of size 2
        round 3: merge pairs of size 4
        ...

    After O(log k) rounds, one merged list remains.

Key invariant:
    At the start of a round with `interval`, each list at an index that is a
    multiple of `interval` represents the sorted merge of a block of up to
    `interval` original lists. Merging `lists[i]` with `lists[i + interval]`
    forms a block twice as large.

Why this works:
    Merging two sorted lists preserves sorted order and includes all nodes from
    both inputs. Balanced pairwise merging ensures each node participates in at
    most one merge per round, and there are O(log k) rounds.

Step-by-step mechanics:
    1. If `lists` is empty, return None.
    2. Set `interval = 1`.
    3. Merge index pairs `(0, 1)`, `(2, 3)`, `(4, 5)`, ...
    4. Double `interval`.
    5. Merge `(0, 2)`, `(4, 6)`, ...
    6. Continue until `interval >= len(lists)`.

Example:
    For 5 lists:

        round interval=1: [0+1], [2+3], [4]
        round interval=2: [0..3], [4]
        round interval=4: [0..4]

Common pitfalls:
    - Sequentially merging every list into one accumulated list and calling it
      divide and conquer. That can be O(N * k), not O(N log k).
    - Getting the loop bound wrong: `i + interval` must be a valid index.
    - Forgetting `lists = []`.
    - Losing the tail remainder when merging two lists.
    - Allocating new nodes unnecessarily when re-linking existing nodes is
      enough.

Complexity:
    Time:
        O(N log k), where N is total nodes and k is number of lists.

    Space:
        O(1) extra for the iterative version, excluding the input list array and
        output nodes. The implementation reuses original nodes.

When to choose this variant:
    Choose this when you want to avoid heap tie-breaker details or when the
    interviewer wants to see divide-and-conquer thinking. It is also a natural
    follow-up after mastering Merge Two Sorted Lists.
"""

from typing import Optional

from common.lc_types import ListNode

from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = self._merge_two(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

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
