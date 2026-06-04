"""
238. Product of Array Except Self - optimized prefix/suffix reference

Variant role:
    Primary interview-ready solution. It satisfies the required O(n) time,
    avoids division, and also satisfies the follow-up O(1) extra space target
    when the output array is not counted.

Problem restatement:
    For every index i, return the product of all values except nums[i].

Core idea:
    Reuse the output array to store one half of the answer.

    First pass:
        answer[i] stores the product of all values strictly to the left of i.

    Second pass:
        A running suffix stores the product of all values strictly to the right
        of i. Multiplying answer[i] by that suffix completes the answer.

Key invariant:
    Before processing index i in the forward pass:

        prefix == product(nums[0:i])

    Before processing index i in the backward pass:

        suffix == product(nums[i + 1:])

    Because nums[i] is multiplied into the running product only after answer[i]
    is updated, nums[i] is never included in its own answer.

Step-by-step walkthrough:
    1. Initialize answer with 1s.
    2. Scan left to right.
       Store the current prefix in answer[i], then multiply prefix by nums[i].
    3. Scan right to left.
       Multiply answer[i] by the current suffix, then multiply suffix by nums[i].
    4. Return answer.

Example:
    nums = [1, 2, 3, 4]

    After the forward pass:
        answer = [1, 1, 2, 6]

    Backward suffixes used at each index:
        index 3: suffix = 1
        index 2: suffix = 4
        index 1: suffix = 12
        index 0: suffix = 24

    Final answer:
        [24, 12, 8, 6]

Why zeros work naturally:
    Since the algorithm never divides by nums[i], zero values simply become part
    of any prefix or suffix product that crosses them. One zero leaves only that
    zero's position with a nonzero product; two or more zeros make every output
    zero.

Complexity:
    Time: O(n)
    Space: O(1) extra, excluding the returned answer array.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            answer[i] = prefix
            prefix *= num

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
