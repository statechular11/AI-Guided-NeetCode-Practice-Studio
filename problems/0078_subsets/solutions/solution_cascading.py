"""
78. Subsets - Iteratively Extend Existing Subsets

Variant role:
    primary concise solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Subsets are a binary decision tree: include or exclude each value.

    This specific variant uses: iteratively extend existing subsets.

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
    Time: O(n*2^n); Space: O(n*2^n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary concise solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    78. Subsets - cascading reference Core idea: Start with the empty subset. For each number, every existing subset can produce a new subset that includes that number. Example: nums = [1,2] start [[]] add 1 -> [[], [1]] add 2 -> [[], [1], [2], [1,2]] Complexity: Time: O(n * 2^n) Space: O(n * 2^n) for output
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: list[list[int]] = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result
