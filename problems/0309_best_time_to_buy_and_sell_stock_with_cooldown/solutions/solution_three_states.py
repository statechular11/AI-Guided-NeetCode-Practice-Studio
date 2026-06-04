"""
309. Best Time to Buy and Sell Stock with Cooldown - Hold/Sold/Rest Cooldown State Machine

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Cooldown is captured by separating just-sold from resting/not-holding state.

    This specific variant uses: hold/sold/rest cooldown state machine.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"prices": [1, 2, 3, 0, 2]}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    309. Stock With Cooldown - three states reference Core idea: Track hold (own stock), sold (just sold today), and rest (not holding and not just sold). Buying can only come from rest; resting can come from previous rest or previous sold after cooldown. Complexity: O(n) time, O(1) space.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        sold = 0
        rest = 0
        for price in prices:
            prev_hold, prev_sold, prev_rest = hold, sold, rest
            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)
        return max(sold, rest)
