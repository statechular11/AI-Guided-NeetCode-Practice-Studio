"""
78. Subsets - Binary Include/Exclude Recursion

Variant role:
    backtracking pattern. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Subsets are a binary decision tree: include or exclude each value.

    This specific variant uses: binary include/exclude recursion.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [1, 2, 3]}` and the expected result is `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(n*2^n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: backtracking pattern. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    78. Subsets - include/exclude recursion reference Core idea: For each index, branch into excluding nums[index] and including nums[index]. This makes the binary decision tree explicit. Complexity: Time: O(n * 2^n) Space: O(n) recursion depth excluding output
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        path: list[int] = []

        def dfs(index: int) -> None:
            if index == len(nums):
                result.append(path.copy())
                return
            dfs(index + 1)
            path.append(nums[index])
            dfs(index + 1)
            path.pop()

        dfs(0)
        return result
