"""
1046. Last Stone Weight - negative-value max heap

Variant role:
    Primary interview solution. This is the direct heap simulation: repeatedly
    remove the two heaviest stones, smash them, and insert the leftover when one
    remains.

Core idea:
    The operation we need over and over is:

        "give me the heaviest remaining stone"

    That is a priority-queue operation. Python's `heapq` is a min heap, so
    `heap[0]` is the smallest value. To simulate a max heap, store negative
    weights:

        original weights: [2, 7, 4, 1, 8, 1]
        heap values:      [-2, -7, -4, -1, -8, -1]

    The smallest heap value, -8, represents the largest stone, 8.

Heap mental model:
    `heap[0]` is the priority root/top, not a sorted-list index. With negated
    weights, the root is the most negative value, which corresponds to the
    heaviest stone.

Mechanics:
    1. Negate every stone and heapify once.
    2. While at least two stones remain:
       - pop the heaviest stone `y`,
       - pop the second heaviest stone `x`,
       - if `y != x`, push the leftover stone `y - x`.
    3. Return the remaining stone, or 0 if all stones were destroyed.

Trace:
    stones = [2, 7, 4, 1, 8, 1]

    Pop 8 and 7 -> leftover 1
    Remaining multiset: {4, 2, 1, 1, 1}

    Pop 4 and 2 -> leftover 2
    Remaining multiset: {2, 1, 1, 1}

    Pop 2 and 1 -> leftover 1
    Remaining multiset: {1, 1, 1}

    Pop 1 and 1 -> both destroyed
    Remaining multiset: {1}

    Return 1.

Why it works:
    The problem's rule always chooses the two heaviest stones. A max heap gives
    exactly those two stones in O(log n) pop operations. After a smash, the only
    possible new stone is smaller than the heaviest stone just popped, so pushing
    it back into the same heap preserves the simulation state.

Common pitfalls:
    - Forgetting to negate values when using Python `heapq`.
    - Computing the leftover with the wrong sign after popping negated values.
    - Assuming `heap[1]` is the second heaviest; heap order only guarantees the
      root. Use `heappop` twice.
    - Pushing a zero leftover when equal stones collide. Equal stones both
      disappear, so push nothing.

Complexity:
    Time: O(n log n). Heapify is O(n), then each smash uses heap pops/pushes.
    Space: O(n).

When to choose this variant:
    Use this as the default interview answer. It is concise, faithful to the
    problem statement, and reinforces Python's min-heap/negation pattern.
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0
