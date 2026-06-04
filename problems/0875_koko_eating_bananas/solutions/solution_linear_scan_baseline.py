"""
875. Koko Eating Bananas - linear scan over speeds

Variant role:
    educational answer-search baseline

Core idea:
    Try speeds from slowest to fastest and return the first one that finishes within h hours.

Key invariant:
    The first feasible speed is minimal because speeds are tested in increasing order.

Mechanics:
    For each candidate speed, sum ceil(pile / speed) over all piles.

Common pitfalls:
    This is too slow for large values; binary search is justified because feasibility is monotonic in speed.

Complexity:
    Time: O(max(piles) * n); Space: O(1)

When to choose this variant:
    Use this to make the monotonic predicate obvious before applying binary search on answer.
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for speed in range(1, max(piles) + 1):
            hours = sum((pile + speed - 1) // speed for pile in piles)
            if hours <= h:
                return speed
        return max(piles)
