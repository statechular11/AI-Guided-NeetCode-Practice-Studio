"""
46. Permutations - Fix Positions By Swapping In Place

Variant role:
    alternative backtracking pattern. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Either track used indices or swap values into fixed positions; both are core permutation patterns.

    This specific variant uses: fix positions by swapping in-place.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [1, 2, 3]}` and the expected result is `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(n!*n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: alternative backtracking pattern. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    46. Permutations - in-place swaps reference Core idea: Fix one position at a time by swapping each possible remaining value into that position. After recursion, swap back to restore the array for the next branch. This avoids a separate used array, but the restoration step is easy to forget. Complexity: Time: O(n! * n) Space: O(n) recursion depth excluding output
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []

        def dfs(index: int) -> None:
            if index == len(nums):
                result.append(nums.copy())
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index + 1)
                nums[index], nums[i] = nums[i], nums[index]

        dfs(0)
        return result
