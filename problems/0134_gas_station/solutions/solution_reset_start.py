"""
134. Gas Station - Reset Failed Segment Start

Variant role:
    primary greedy solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    A negative tank invalidates every start in the current segment, so reset after it.

    This specific variant uses: reset failed segment start.

Key invariant:
    The local choice preserves at least one optimal continuation, usually because choosing the best available option cannot reduce future feasibility.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"gas": [1, 2, 3, 4, 5], "cost": [3, 4, 5, 1, 2]}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the greedy choice and why earlier/later choices cannot improve it. Watch boundary cases where equality is allowed. For reachability problems, track the farthest possible boundary. For string balance problems, a range of possibilities can be more useful than one exact state.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary greedy solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    134. Gas Station - reset start reference Core idea: If total gas is less than total cost, no answer exists. Otherwise, when the running tank becomes negative at station i, no station in the current candidate segment can be the answer, so start from i + 1. Complexity: Time: O(n) Space: O(1)
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            if tank < 0:
                start = i + 1
                tank = 0
        return start
