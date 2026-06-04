"""
90. Subsets II - Sorted Backtracking With Same Depth Duplicate Skip

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Sort first, then skip duplicate values only at the same recursion depth.

    This specific variant uses: sorted backtracking with same-depth duplicate skip.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [1, 2, 2]}` and the expected result is `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(n*2^n); Space: O(n) excl. output

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    90. Subsets II - sort and skip duplicate branches reference Core idea: Sort nums so duplicates are adjacent. During backtracking, after choosing whether to start a branch at index i, skip nums[i] if it equals nums[i-1] and both are at the same recursion depth. Complexity: Time: O(n * 2^n) Space: O(n) recursion depth excluding output
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: list[list[int]] = []
        path: list[int] = []

        def dfs(start: int) -> None:
            result.append(path.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result
