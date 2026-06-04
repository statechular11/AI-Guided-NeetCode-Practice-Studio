"""
45. Jump Game II - Bfs Level Greedy Range

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Each jump expands a reachable range. Increment jumps only when finishing the current range.

    This specific variant uses: BFS-level greedy range.

Key invariant:
    The local choice preserves at least one optimal continuation, usually because choosing the best available option cannot reduce future feasibility.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [2, 3, 1, 1, 4]}` and the expected result is `2`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the greedy choice and why earlier/later choices cannot improve it. Watch boundary cases where equality is allowed. For reachability problems, track the farthest possible boundary. For string balance problems, a range of possibilities can be more useful than one exact state.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    45. Jump Game II - level greedy reference Core idea: Treat each jump count as a range of reachable indices, like BFS levels. Scan the current range while computing the farthest next range. When the scan reaches the current range end, take one jump. Complexity: Time: O(n) Space: O(1)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
