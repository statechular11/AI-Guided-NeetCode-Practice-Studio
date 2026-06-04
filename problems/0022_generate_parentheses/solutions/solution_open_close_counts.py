"""
22. Generate Parentheses - Backtrack Only Valid Prefixes

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Only add a close parenthesis when it can match a previously opened one.

    This specific variant uses: backtrack only valid prefixes.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 3}` and the expected result is `["((()))", "(()())", "(())()", "()(())", "()()()"]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(C_n*n); Space: O(n) excl. output

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    22. Generate Parentheses - open/close count reference Core idea: Build a valid string incrementally. Add '(' if fewer than n opens have been used. Add ')' only if there are more opens than closes already in the path. Invariant: The path is always a prefix of some valid parentheses string, so no invalid partial strings are explored. Complexity: Time: O(C_n * n), where C_n is the nth Catalan number Space: O(n) recursion depth excluding output
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: list[str] = []
        path: list[str] = []

        def dfs(open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                dfs(open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(")")
                dfs(open_count, close_count + 1)
                path.pop()

        dfs(0, 0)
        return result
