"""
973. K Closest Points to Origin - quickselect partitioning

Variant role:
    Optimized average-time selection. Instead of sorting all n points, partition
    the array until the first k positions contain the k closest points.

Core idea:
    Sorting answers more than the problem asks. We do not need the closest
    points in sorted order; we only need the set of k closest points.

    Quickselect uses the same partition idea as quicksort:

        values with distance <= pivot distance move left
        values with distance > pivot distance move right

    After a partition, the pivot lands at the exact index it would have in a
    fully sorted-by-distance array.

Mechanics:
    1. Work on a copy of `points`, because partitioning reorders the list.
    2. Partition around a pivot distance.
    3. If the pivot index is k, the first k positions are the answer.
    4. If the pivot index is less than k, continue on the right side.
    5. If the pivot index is greater than k, continue on the left side.

Small trace:
    distances = [10, 8, 5, 18], k = 2

    Suppose pivot distance 8 partitions to:

        [5, 8, 10, 18]
             ^
             pivot index 1

    The first two positions now contain two distances <= every distance to
    their right, so for k = 2 we can return the first two points.

Why it works:
    The invariant is:

        after partitioning around index p, every point left of p has distance
        <= the pivot distance, and every point right of p has distance greater
        than the pivot distance.

    Therefore, if p is exactly k, all positions before k are among the k closest.
    If p is too small or too large, only one side can still contain the boundary.

Common pitfalls:
    - Using `k - 1` and `k` inconsistently. This implementation searches for
      the boundary index `k`, meaning the answer is `work[:k]`.
    - Returning sorted output. Quickselect only guarantees the first k points
      are the closest set, not that they are ordered.
    - Forgetting that deterministic pivot choices can have O(n^2) worst case.

Complexity:
    Average time: O(n)
    Worst-case time: O(n^2)
    Space: O(n) here because we copy the input before partitioning.

When to choose this variant:
    Use it when the interviewer asks for better than sorting/heap asymptotics
    and accepts average-case analysis. Use the size-k heap when deterministic
    O(n log k) behavior or streaming input is more important.
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        work = [point[:] for point in points]

        def distance(index: int) -> int:
            x, y = work[index]
            return x * x + y * y

        def partition(left: int, right: int) -> int:
            pivot_index = (left + right) // 2
            pivot_distance = distance(pivot_index)
            work[pivot_index], work[right] = work[right], work[pivot_index]

            store = left
            for index in range(left, right):
                if distance(index) <= pivot_distance:
                    work[store], work[index] = work[index], work[store]
                    store += 1

            work[store], work[right] = work[right], work[store]
            return store

        left, right = 0, len(work) - 1
        while left <= right:
            pivot = partition(left, right)
            if pivot == k:
                break
            if pivot < k:
                left = pivot + 1
            else:
                right = pivot - 1

        return work[:k]
