"""
39. Combination Sum - Sorted Backtracking With Reusable Candidates

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Recurse with the same index to allow reuse; advance index to avoid permutation duplicates.

    This specific variant uses: sorted backtracking with reusable candidates.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"candidates": [2, 3, 6, 7], "target": 7}` and the expected result is `[[2, 2, 3], [7]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Exponential time; O(depth) space excl. output

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    39. Combination Sum - reuse same index reference Core idea: Sort candidates and backtrack over choices starting at a given index. After choosing candidates[i], recurse with the same i because the value can be reused unlimited times. Pruning: Once candidate > remaining target, later sorted candidates are also too big. Complexity: Time: exponential in target and candidate count Space: O(target / min(candidates)) recursion depth excluding output
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: list[list[int]] = []
        path: list[int] = []

        def dfs(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path.copy())
                return
            for i in range(start, len(candidates)):
                value = candidates[i]
                if value > remaining:
                    break
                path.append(value)
                dfs(i, remaining - value)
                path.pop()

        dfs(0, target)
        return result
