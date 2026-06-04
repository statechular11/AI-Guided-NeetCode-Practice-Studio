"""
53. Maximum Subarray - Kadane Running Best Suffix

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Kadane's invariant: `current` is the best subarray sum ending at the current index.

    This specific variant uses: Kadane running best suffix.

Key invariant:
    The local choice preserves at least one optimal continuation, usually because choosing the best available option cannot reduce future feasibility.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}` and the expected result is `6`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the greedy choice and why earlier/later choices cannot improve it. Watch boundary cases where equality is allowed. For reachability problems, track the farthest possible boundary. For string balance problems, a range of possibilities can be more useful than one exact state.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    53. Maximum Subarray - Kadane reference Core idea: At each index, decide whether to extend the previous subarray or start fresh at the current value. Track the best sum seen anywhere. Complexity: Time: O(n) Space: O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = best = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)
        return best
