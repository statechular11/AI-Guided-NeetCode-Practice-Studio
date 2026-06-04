"""
131. Palindrome Partitioning - Choose Palindrome Prefixes By Direct Check

Variant role:
    primary clear solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Backtracking chooses the next palindrome prefix; DP precompute removes repeated palindrome checks.

    This specific variant uses: choose palindrome prefixes by direct check.

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
    Time: O(n*2^n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary clear solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    131. Palindrome Partitioning - backtracking reference Core idea: A partition is built by choosing the next palindrome substring starting at the current index. Once the index reaches the end, the current path is one complete partition. Example: s = "aab" choices from index 0: "a", "aa" partitions: ["a","a","b"] and ["aa","b"]. Complexity: Time: O(n * 2^n) worst case Space: O(n) recursion depth excluding output
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result: list[list[str]] = []
        path: list[str] = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start: int) -> None:
            if start == len(s):
                result.append(path.copy())
                return
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return result
