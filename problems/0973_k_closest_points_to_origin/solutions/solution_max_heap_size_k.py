"""
973. K Closest Points to Origin - size-k max heap

Variant role:
    Streaming-friendly heap optimization. Keep only the best k points seen so
    far instead of storing or sorting every point.

Core idea:
    Python `heapq` is a min heap. To keep the k closest points while quickly
    finding the farthest kept point, store negative squared distances:

        item = (-distance, x, y)

    The heap root is the smallest tuple, so the most negative distance sits at
    the root. That root represents the farthest point among the k currently
    kept points.

Mechanics:
    1. Scan points from left to right.
    2. Until the heap has k points, push each candidate.
    3. Once the heap is full, compare the new candidate with the farthest kept
       point at `heap[0]`.
    4. If the new candidate is closer, replace the root.

Tiny trace:
    k = 2
    kept distances after seeing [5, 1, 10]:

        push 5  -> keep {5}
        push 1  -> keep {5, 1}
        see 10  -> farther than root 5, skip

    The heap keeps the two closest distances seen so far.

Why it works:
    The invariant is:

        after processing each point, the heap contains the k closest points
        among the processed prefix.

    If a new point is farther than the farthest kept point, it cannot belong in
    the top k. If it is closer, replacing the farthest kept point restores the
    invariant.

Common pitfalls:
    - Forgetting that the root stores the farthest kept point because distances
      are negated.
    - Keeping all n points when only k candidates are needed.
    - Using square root instead of squared distance.

Complexity:
    Time: O(n log k)
    Space: O(k)

When to choose this variant:
    Use it when k is much smaller than n, when points arrive as a stream, or
    when you want deterministic worst-case behavior without sorting all points.
"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: list[tuple[int, int, int]] = []
        for x, y in points:
            dist = x * x + y * y
            item = (-dist, x, y)
            if len(heap) < k:
                heapq.heappush(heap, item)
            elif item > heap[0]:
                heapq.heapreplace(heap, item)
        return [[x, y] for _neg_dist, x, y in heap]
