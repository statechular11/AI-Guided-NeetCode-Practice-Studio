"""
51. N-Queens - Row By Row Queens With Column And Diagonal Sets

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The reusable encoding is columns plus row-col and row+col diagonals.

    This specific variant uses: row-by-row queens with column and diagonal sets.

Key invariant:
    The current path contains exactly the choices made so far. Every recursive choice is undone before trying the next sibling choice.

Mechanics:
    1. Choose one legal next value or position.
    2. Record it in the current path/state.
    3. Recurse to finish the remaining choices.
    4. Undo the choice before exploring the next option.

Walkthrough:
    On the local case `example_1`, the input is `{"n": 4}` and the expected result is `[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the recursion state clearly: index, start position, path, and remaining target. Copy the current path before adding it to results. Restore every mutation during backtracking, including used flags, board cells, swaps, and sets. For duplicate inputs, sort first and skip duplicate branches at the same recursion depth.

Complexity:
    Time: O(n!); Space: O(n) excl. output

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    51. N-Queens - set-based backtracking reference Core idea: Place one queen per row. A square (row, col) is invalid if its column, main diagonal row-col, or anti-diagonal row+col is already occupied. Board construction: During search keep queen columns by row. When all rows are filled, render each row as dots with one Q at the chosen column. Complexity: Time: O(n!) search scale Space: O(n) recursion/state excluding output
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result: list[list[str]] = []
        cols: set[int] = set()
        diag: set[int] = set()
        anti: set[int] = set()
        queens: list[int] = []

        def render() -> list[str]:
            board = []
            for col in queens:
                board.append("." * col + "Q" + "." * (n - col - 1))
            return board

        def dfs(row: int) -> None:
            if row == n:
                result.append(render())
                return
            for col in range(n):
                if col in cols or row - col in diag or row + col in anti:
                    continue
                cols.add(col)
                diag.add(row - col)
                anti.add(row + col)
                queens.append(col)
                dfs(row + 1)
                queens.pop()
                anti.remove(row + col)
                diag.remove(row - col)
                cols.remove(col)

        dfs(0)
        return result
