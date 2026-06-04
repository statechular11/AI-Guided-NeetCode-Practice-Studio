"""
55. Jump Game - Farthest Reachable Index

Variant role:
    primary greedy solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The greedy state is the farthest reachable index. If the scan passes it, no future jump can help.

    This specific variant uses: farthest reachable index.

Key invariant:
    The local choice preserves at least one optimal continuation, usually because choosing the best available option cannot reduce future feasibility.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [2, 3, 1, 1, 4]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the greedy choice and why earlier/later choices cannot improve it. Watch boundary cases where equality is allowed. For reachability problems, track the farthest possible boundary. For string balance problems, a range of possibilities can be more useful than one exact state.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary greedy solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    55. Jump Game - farthest reach reference Core idea: Scan left to right and maintain the farthest index reachable so far. If the current index is ever beyond that reach, it is impossible to continue. Complexity: Time: O(n) Space: O(1)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
        return True
