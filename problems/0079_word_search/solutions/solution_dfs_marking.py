"""
79. Word Search - Grid Dfs With Temporary Visited Marks

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Mark visited cells temporarily and restore them when backtracking.

    This specific variant uses: grid DFS with temporary visited marks.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"board": [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "word": "ABCCED"}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(m*n*4^L); Space: O(L)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    79. Word Search - DFS with in-place marking reference Core idea: Try every board cell as the start. From a matching cell, DFS to neighboring cells for the next character. Mark the current cell as visited during the recursive call, then restore it afterward. Why restore matters: The same board cell cannot be reused within one path, but it must be available for other paths starting elsewhere. Complexity: Time: O(m*n*4^L), where L = len(word) Space: O(L) recursion depth
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != word[index]:
                return False

            saved = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, index + 1)
                or dfs(r - 1, c, index + 1)
                or dfs(r, c + 1, index + 1)
                or dfs(r, c - 1, index + 1)
            )
            board[r][c] = saved
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
