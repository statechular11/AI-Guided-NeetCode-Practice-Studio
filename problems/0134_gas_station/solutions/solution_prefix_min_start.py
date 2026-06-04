"""
134. Gas Station - prefix-sum minimum start

Variant role:
    alternative greedy proof reference

Core idea:
    If total gas is enough, start after the position where cumulative surplus reaches its minimum.

Key invariant:
    The chosen start never sees a negative relative prefix surplus while completing the circuit.

Mechanics:
    Track cumulative sum of gas-cost and the index after its lowest point. If total sum is negative, no start exists.

Common pitfalls:
    Return start modulo n because the minimum prefix can occur at the last station.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this when you want a prefix-sum proof of the same greedy reset idea.
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        min_prefix = float("inf")
        start = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            if total < min_prefix:
                min_prefix = total
                start = i + 1

        return start % len(gas) if total >= 0 else -1
