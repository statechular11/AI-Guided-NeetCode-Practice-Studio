"""
40. Combination Sum II - Sort And Skip Duplicate Branches Per Depth

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Sort first; skip duplicate values only within the same recursion depth.

    This specific variant uses: sort and skip duplicate branches per depth.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"candidates": [10, 1, 2, 7, 6, 1, 5], "target": 8}` and the expected result is `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(2^n*n); Space: O(n) excl. output

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    40. Combination Sum II - sorted skip-duplicates reference Core idea: Each candidate can be used once, so after choosing index i recurse from i + 1. Sort first so duplicate values are adjacent; at the same recursion depth, skip a value if it equals the previous value already considered. Why skip only at the same depth: We still need to allow combinations such as [1,1,6] when there are two 1s. The duplicate skip prevents starting two identical branches from equal values at the same choice position. Complexity: Time: O(2^n * n) worst case Space: O(n) recursion depth excluding output
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: list[list[int]] = []
        path: list[int] = []

        def dfs(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path.copy())
                return
            prev = None
            for i in range(start, len(candidates)):
                value = candidates[i]
                if value == prev:
                    continue
                if value > remaining:
                    break
                path.append(value)
                dfs(i + 1, remaining - value)
                path.pop()
                prev = value

        dfs(0, target)
        return result
