"""
875. Koko Eating Bananas - Binary Search Feasible Speed

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    This is binary search on the answer: feasible speeds form a suffix of the search range.

    This specific variant uses: binary search feasible speed.

Key invariant:
    The search interval always contains every still-possible answer. Each midpoint decision removes a side that cannot contain the target answer.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"piles": [3, 6, 7, 11], "h": 8}` and the expected result is `4`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define whether your binary search interval is closed or half-open. For answer-space search, prove the predicate is monotonic. For boundary problems, test empty arrays and values outside the range. For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

Complexity:
    Time: O(n log max(piles)); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    875. Koko Eating Bananas - binary search on answer reference Core idea: The eating speed is the answer. If Koko can finish at speed x, she can also finish at any larger speed. This monotonic predicate supports binary search. Predicate: hours(speed) = sum(ceil(pile / speed) for pile in piles) Complexity: Time: O(n log max(piles)) Space: O(1)
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return left
