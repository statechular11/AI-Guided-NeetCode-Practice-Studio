"""
239. Sliding Window Maximum - block decomposition

Variant role:
    Alternative O(n) formulation. This is less common than the monotonic deque in
    interviews, but it gives a powerful first-principles view: precompute enough
    local maxima so every length-k window can be answered with two table lookups.

Core idea:
    Split nums into blocks of size k:

        block 0: indices 0..k-1
        block 1: indices k..2k-1
        block 2: indices 2k..3k-1

    Build two arrays:

        left_max[i]  = max from the start of i's block through i
        right_max[i] = max from i through the end of i's block

    For a window [left, right] of length k, the maximum is:

        max(right_max[left], left_max[right])

Why the formula works:
    Any length-k window overlaps at most two size-k blocks.

    The part of the window in the left block is a suffix of that block, and
    right_max[left] is exactly the maximum of that suffix.

    The part of the window in the right block is a prefix of that block, and
    left_max[right] is exactly the maximum of that prefix.

    Taking the max of those two values covers the entire window. If the window is
    exactly aligned within one block, the same formula still works because both
    table values are computed inside that block.

Concrete trace:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

    Blocks:
        [1, 3, -1] | [-3, 5, 3] | [6, 7]

    left_max:
        [1, 3, 3] | [-3, 5, 5] | [6, 7]

    right_max:
        [3, 3, -1] | [5, 5, 3] | [7, 7]

    Window [1..3] = [3, -1, -3]:
        suffix from index 1 in block 0 -> right_max[1] = 3
        prefix through index 3 in block 1 -> left_max[3] = -3
        answer = max(3, -3) = 3

    Window [2..4] = [-1, -3, 5]:
        suffix from index 2 in block 0 -> right_max[2] = -1
        prefix through index 4 in block 1 -> left_max[4] = 5
        answer = max(-1, 5) = 5

Common pitfalls:
    - Reset left_max at the start of each block: i % k == 0.
    - Reset right_max at the end of each block: (i + 1) % k == 0, and also at
      the final array index because the last block may be shorter than k.
    - Use right_max[left] and left_max[left + k - 1], not the other way around.

Complexity:
    Time: O(n), with two preprocessing passes and one answer pass.
    Space: O(n), because it stores left_max and right_max.

When to choose this variant:
    Prefer the monotonic deque for a typical interview. Use this variant when the
    interviewer asks for another O(n) method, when offline preprocessing is
    acceptable, or when explaining how fixed-size windows can be answered from
    prefix/suffix summaries.
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left_max = [0] * n
        right_max = [0] * n

        for i, num in enumerate(nums):
            if i % k == 0:
                left_max[i] = num
            else:
                left_max[i] = max(left_max[i - 1], num)

        for i in range(n - 1, -1, -1):
            if i == n - 1 or (i + 1) % k == 0:
                right_max[i] = nums[i]
            else:
                right_max[i] = max(right_max[i + 1], nums[i])

        result: list[int] = []
        for left in range(n - k + 1):
            right = left + k - 1
            result.append(max(right_max[left], left_max[right]))
        return result
