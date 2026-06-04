"""
215. Kth Largest Element in an Array - quickselect order statistic

Variant role:
    Optimized average-time solution. It finds the needed order statistic without
    sorting the entire array.

Core idea:
    The kth largest value is the same as the value at this index in ascending
    sorted order:

        target = len(nums) - k

    Example:
        nums sorted ascending = [1, 2, 3, 4, 5, 6]
        k = 2
        target = 6 - 2 = 4
        nums[target] = 5

    Quickselect partitions like quicksort but only recurses/iterates into the
    side that can still contain `target`.

Mechanics:
    1. Copy nums because partitioning reorders values.
    2. Pick a pivot and partition so values <= pivot move left and values >
       pivot move right.
    3. The pivot lands at its final sorted index.
    4. If that index is target, return it.
    5. Otherwise, continue only on the side containing target.

Why it works:
    After partitioning, every value left of the pivot is <= it and every value
    right of the pivot is > it. Therefore the pivot's position is final with
    respect to sorted order, even though the two sides are not fully sorted.

Duplicate handling:
    Duplicates are values in separate positions. Quickselect naturally counts
    them because it partitions the array positions, not a set of distinct
    values.

Common pitfalls:
    - Searching for index `k - 1`; that is the descending index. In this
      ascending-partition implementation, search for `len(nums) - k`.
    - Assuming quickselect returns a sorted array. It only guarantees the target
      value lands at the correct order-statistic index.
    - Forgetting worst-case O(n^2) when pivot choices are consistently bad.

Complexity:
    Average time: O(n)
    Worst-case time: O(n^2)
    Space: O(n) here because we copy the input before partitioning.

When to choose this variant:
    Use it when the interviewer asks for a non-sorting optimized solution and
    accepts average-case analysis. Use the size-k min heap for deterministic
    O(n log k) behavior or streaming input.
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        work = list(nums)
        target = len(work) - k

        def partition(left: int, right: int) -> int:
            pivot_index = (left + right) // 2
            pivot_value = work[pivot_index]
            work[pivot_index], work[right] = work[right], work[pivot_index]

            store = left
            for index in range(left, right):
                if work[index] <= pivot_value:
                    work[store], work[index] = work[index], work[store]
                    store += 1

            work[store], work[right] = work[right], work[store]
            return store

        left, right = 0, len(work) - 1
        while left <= right:
            pivot = partition(left, right)
            if pivot == target:
                return work[pivot]
            if pivot < target:
                left = pivot + 1
            else:
                right = pivot - 1

        return work[target]
