"""
239. Sliding Window Maximum - brute-force baseline

Variant role:
    Educational baseline. This is intentionally not fast enough for the largest
    constraints, but it clarifies what every optimized solution must compute:
    for each window [left, left + k - 1], return the maximum value inside it.

Core idea:
    Enumerate every window start and scan the k elements in that window.

Why this is useful:
    The optimized monotonic deque solution can feel magical until the repeated
    work is visible. Adjacent windows overlap heavily:

        [1, 3, -1] -3  5
         1 [3, -1, -3] 5
         1  3 [-1, -3, 5]

    A brute-force scan recomputes information for the shared values again and
    again. The monotonic deque removes exactly that repeated work by keeping the
    surviving maximum candidates across window shifts.

Example:
    nums = [1, 3, -1, -3, 5], k = 3

    left=0 -> max([1, 3, -1]) = 3
    left=1 -> max([3, -1, -3]) = 3
    left=2 -> max([-1, -3, 5]) = 5

Common pitfalls:
    - There are n - k + 1 windows, not n windows.
    - Each window is inclusive from left to left + k - 1.
    - k can be 1, in which case every element is its own maximum.

Complexity:
    Time: O((n - k + 1) * k), which is O(nk) in the worst case.
    Space: O(1) auxiliary space, ignoring the output list.

When to choose this variant:
    Use it only to establish a baseline, test an oracle on small cases, or begin
    an interview explanation before deriving the optimized candidate structure.
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result: list[int] = []
        for left in range(len(nums) - k + 1):
            result.append(max(nums[left : left + k]))
        return result
