"""
79. Word Search - DFS with explicit visited set

Variant role:
    alternative backtracking reference

Core idea:
    Try every cell as the word start and use a path-local visited set instead of mutating board cells.

Key invariant:
    visited contains exactly the cells already used in the current partial word path.

Mechanics:
    At each step, verify bounds, character match, and unused cell, then recurse into four neighbors with the next character index.

Common pitfalls:
    The same board cell cannot be reused within one path, but it must become available again for other paths after backtracking.

Complexity:
    Time: O(mn * 4^L); Space: O(L)

When to choose this variant:
    Use this when in-place marking feels risky; the in-place variant is slightly leaner.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited: set[tuple[int, int]] = set()

        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if r < 0 or r == rows or c < 0 or c == cols:
                return False
            if (r, c) in visited or board[r][c] != word[index]:
                return False

            visited.add((r, c))
            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )
            visited.remove((r, c))
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
