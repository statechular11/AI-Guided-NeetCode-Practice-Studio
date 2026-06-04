"""
17. Letter Combinations of a Phone Number - Choose One Mapped Letter Per Digit

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    This is direct choice-tree backtracking: one digit position, one letter choice.

    This specific variant uses: choose one mapped letter per digit.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"digits": "23"}` and the expected result is `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(4^n*n); Space: O(n) excl. output

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    17. Letter Combinations of a Phone Number - backtracking reference Core idea: Each digit contributes a small set of choices. Build the output one position at a time; when the path length equals the number of digits, emit one full combination. Example: digits = "23" choices: 2 -> abc, 3 -> def output includes ad, ae, af, bd, be, bf, cd, ce, cf. Complexity: Time: O(4^n * n), because each emitted string has length n Space: O(n) recursion depth excluding output
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        result: list[str] = []
        path: list[str] = []

        def dfs(index: int) -> None:
            if index == len(digits):
                result.append("".join(path))
                return
            for ch in mapping[digits[index]]:
                path.append(ch)
                dfs(index + 1)
                path.pop()

        dfs(0)
        return result
