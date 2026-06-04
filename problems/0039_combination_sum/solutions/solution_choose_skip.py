"""
39. Combination Sum - choose-or-skip recursion

Variant role:
    alternative backtracking reference

Core idea:
    At each candidate index, decide whether to use the current value again or skip to the next distinct value.

Key invariant:
    The recursion only forms nondecreasing combinations, so the same multiset is never emitted in multiple orders.

Mechanics:
    The choose branch keeps the same index because values may be reused. The skip branch advances the index.

Common pitfalls:
    Advancing the index after choosing would incorrectly forbid reuse. Keeping the index after skipping would loop forever.

Complexity:
    Time: exponential in target/min(candidates); Space: O(target/min(candidates)) excl. output

When to choose this variant:
    Use this to understand the include/exclude decision tree behind the compact for-loop backtracking solution.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: list[list[int]] = []
        path: list[int] = []

        def dfs(index: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            if index == len(candidates) or remaining < 0:
                return

            value = candidates[index]
            path.append(value)
            dfs(index, remaining - value)
            path.pop()

            dfs(index + 1, remaining)

        dfs(0, target)
        return result
