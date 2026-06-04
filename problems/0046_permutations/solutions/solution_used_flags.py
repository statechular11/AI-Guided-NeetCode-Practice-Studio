"""
46. Permutations - Choose Unused Value For Each Position

Variant role:
    primary clear solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Either track used indices or swap values into fixed positions; both are core permutation patterns.

    This specific variant uses: choose unused value for each position.

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
    Use this variant when its role matches the interview goal: primary clear solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    46. Permutations - used flags reference Core idea: A permutation chooses one unused number for each position. Track which indices are already used and append a copy of the path when it reaches n. Complexity: Time: O(n! * n), because each permutation copy costs O(n) Space: O(n) recursion depth plus used flags excluding output
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = []
        path: list[int] = []
        used = [False] * len(nums)

        def dfs() -> None:
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(num)
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return result
