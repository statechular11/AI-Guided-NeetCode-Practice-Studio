"""
40. Combination Sum II - frequency-count backtracking

Variant role:
    alternative duplicate-handling reference

Core idea:
    Compress duplicates into (value, count), then choose how many copies of each value to use.

Key invariant:
    Each unique value is considered once, so duplicate candidates cannot create duplicate output rows.

Mechanics:
    For every value, try taking 0..count copies while the running sum stays within target, then recurse to the next unique value.

Common pitfalls:
    If you recurse over raw sorted candidates, you still need skip-duplicate logic. Counts move that logic into the state representation.

Complexity:
    Time: O(product(count_i + 1)); Space: O(u + target/min(candidates)) excl. output

When to choose this variant:
    Use this when duplicate skipping feels subtle; counts make the choice space explicit.
"""

from collections import Counter
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counts = sorted(Counter(candidates).items())
        result: list[list[int]] = []
        path: list[int] = []

        def dfs(index: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            if index == len(counts) or remaining < 0:
                return

            value, count = counts[index]
            dfs(index + 1, remaining)

            used = 0
            while used < count and remaining >= value * (used + 1):
                used += 1
                path.append(value)
                dfs(index + 1, remaining - value * used)
            for _ in range(used):
                path.pop()

        dfs(0, target)
        return result
