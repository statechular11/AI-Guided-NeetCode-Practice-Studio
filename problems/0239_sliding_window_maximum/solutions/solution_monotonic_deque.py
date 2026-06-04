"""
239. Sliding Window Maximum - monotonic deque

Variant role:
    Primary interview solution. This is the pattern worth being able to derive
    and explain from memory because it gives the optimal O(n) time bound while
    staying online: it can emit each answer as soon as that window is complete.

Core idea:
    A window maximum is the largest value among the indices currently inside the
    fixed-size window. Instead of rescanning all k values for every window, keep
    only the indices that could still become the maximum of the current or a
    future window.

Deque invariant:
    The deque stores indices in increasing index order, and their values are in
    strictly decreasing order:

        nums[dq[0]] > nums[dq[1]] > nums[dq[2]] > ...

    Because indices increase from front to back, the front is the oldest
    candidate. Because values decrease from front to back, the front is also the
    largest candidate. Once a window is complete, nums[dq[0]] is the answer.

Why smaller/equal values are removed from the back:
    Suppose a previous index j is behind the current index i and
    nums[j] <= nums[i]. Index i is newer, so i will stay inside every future
    window at least as long as j. Since i is also at least as large, j can never
    be the maximum while i remains available. That makes j permanently
    dominated, so we pop it.

Why indices, not only values:
    The algorithm must know when the maximum candidate leaves the window. Storing
    indices lets us expire dq[0] when dq[0] <= right - k. It also handles
    duplicate values naturally; when equal values arrive, this implementation
    keeps the newer one by popping the older equal value.

Walkthrough:
    nums = [1, 3, -1, -3, 5], k = 3

    right=0, value=1:
        dq indices [0], values [1]
    right=1, value=3:
        1 is dominated by 3, pop 0.
        dq [1], values [3]
    right=2, value=-1:
        dq [1, 2], values [3, -1]
        first complete window [1, 3, -1] has max nums[1] = 3
    right=3, value=-3:
        dq [1, 2, 3], values [3, -1, -3]
        window [3, -1, -3] still has max nums[1] = 3
    right=4, value=5:
        index 1 is expired because it is outside [2..4].
        -3 and -1 are dominated by 5, so pop them.
        dq [4], values [5]
        window [-1, -3, 5] has max 5

Order of operations:
    1. Remove expired indices from the front.
    2. Remove dominated indices from the back.
    3. Append the current index.
    4. Once right >= k - 1, append the front value to the result.

Common pitfalls:
    - Forgetting to expire old front indices.
    - Storing values only, then losing track of whether a value is still inside
      the current window.
    - Popping from the front when a smaller value leaves; only the index at the
      front can expire.
    - Using a regular queue instead of maintaining decreasing values.
    - Outputting before the first full window exists.

Complexity:
    Time: O(n). Each index is appended once, popped from the back at most once,
    and popped from the front at most once.
    Space: O(k). The deque contains only candidates from the current window.

When to choose this variant:
    Use this in interviews when asked for the optimized solution. It is the
    canonical monotonic-queue pattern and generalizes to other "best value over a
    sliding window" problems.
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window: deque[int] = deque()
        result: list[int] = []

        for i, num in enumerate(nums):
            while window and window[0] <= i - k:
                window.popleft()
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result
