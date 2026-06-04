"""
131. Palindrome Partitioning - Precompute Palindrome Table Before Backtracking

Variant role:
    optimized substring-check variant. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Backtracking chooses the next palindrome prefix; DP precompute removes repeated palindrome checks.

    This specific variant uses: precompute palindrome table before backtracking.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"s": "aab"}` and the expected result is `[["a", "a", "b"], ["aa", "b"]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(n^2 + output*n); Space: O(n^2)

When to choose this variant:
    Use this variant when its role matches the interview goal: optimized substring-check variant. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    131. Palindrome Partitioning - DP precompute reference Core idea: Precompute palindrome[start][end] so backtracking can test substrings in O(1). This is useful when many overlapping substring checks would otherwise repeat work. Complexity: Time: O(n^2 + n * number_of_partitions) Space: O(n^2)
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                palindrome[start][end] = s[start] == s[end] and (end - start <= 2 or palindrome[start + 1][end - 1])

        result: list[list[str]] = []
        path: list[str] = []

        def dfs(start: int) -> None:
            if start == n:
                result.append(path.copy())
                return
            for end in range(start, n):
                if palindrome[start][end]:
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return result
