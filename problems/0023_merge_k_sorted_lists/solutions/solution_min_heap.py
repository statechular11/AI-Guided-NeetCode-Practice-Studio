"""
23. Merge k Sorted Lists - Min-Heap Reference

Core idea:
    At any moment, the next output node must be the smallest current head among
    all non-empty lists. A min-heap is exactly a data structure for repeatedly
    asking "which current candidate is smallest?"

    Put one node from each non-empty list into the heap. Every time a node is
    popped, append it to the answer and push that node's `next` pointer, because
    that successor is now the current head of the same original list.

Key invariant:
    The heap contains at most one candidate from each input list: the first
    unmerged node of that list. Therefore, the minimum heap entry is the next
    globally smallest node.

Why this works:
    Each input list is already sorted. If the smallest current head is `x`, no
    hidden later node in any list can be smaller than its current head. So `x`
    is safe to append. After appending `x`, only `x.next` can newly become a
    candidate from that list.

Tie breaker:
    Python cannot compare `ListNode` objects when two values tie. Heap entries
    use:

        (node.val, counter, node)

    `counter` is unique and increasing, so equal values still have a stable
    comparable tuple.

Step-by-step mechanics:
    1. Push every non-null list head into the heap.
    2. Pop the smallest node.
    3. Attach it to the result tail.
    4. If it has a successor, push that successor into the heap.
    5. Repeat until the heap is empty.

Example:
    Lists:

        1 -> 4 -> 5
        1 -> 3 -> 4
        2 -> 6

    Initial heap has heads `1, 1, 2`. Pop a `1`, then push its successor `4`.
    The heap again exposes the smallest current head. The output grows in sorted
    order without scanning every list on every step.

Common pitfalls:
    - Pushing `(node.val, node)` and crashing when values tie.
    - Pushing all nodes instead of only current heads, which increases heap
      space to O(N).
    - Forgetting to push `node.next` after popping a node.
    - Forgetting to terminate `tail.next = None` when reusing original nodes;
      this prevents accidentally carrying stale links.
    - Not handling `lists = []` or lists containing `None`.

Complexity:
    Time:
        O(N log k), where N is the total number of nodes and k is the number of
        lists. Each node is pushed and popped once, and the heap size is at most
        k.

    Space:
        O(k) for the heap, excluding the output list. The implementation reuses
        original list nodes.

When to choose this variant:
    This is the most direct optimized answer when the interviewer expects a
    priority queue. It is also the natural pattern for "merge many sorted
    streams" problems.
"""

from typing import Optional

from common.lc_types import ListNode

import heapq
from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode()
        tail = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        tail.next = None
        return dummy.next
