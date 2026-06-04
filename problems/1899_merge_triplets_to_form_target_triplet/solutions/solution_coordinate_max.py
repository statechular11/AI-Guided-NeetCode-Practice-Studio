"""
1899. Merge Triplets to Form Target Triplet - coordinate-wise maximum simulation

Variant role:
    alternative greedy reference

Core idea:
    After discarding triplets that would overshoot target, simulate merging by taking coordinate-wise maximums.

Key invariant:
    best is the coordinate-wise maximum of all valid triplets considered so far.

Mechanics:
    Skip any triplet with a coordinate greater than target. Merge valid triplets into best and compare best to target.

Common pitfalls:
    A triplet that overshoots one coordinate can never be used, even if it matches another coordinate.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this when simulating the merge operation feels clearer than tracking three covered booleans.
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        best = [0, 0, 0]
        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    best[i] = max(best[i], triplet[i])
        return best == target
