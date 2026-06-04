"""
36. Valid Sudoku - Row/Column/Box Markers

Variant role:
    primary concise solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    For each non-empty cell, validate the digit in three independent scopes: row, column, and 3x3 box.

    This specific variant uses: row/column/box markers.

Key invariant:
    The lookup/counting state contains exactly the facts needed from the portion of the input already processed, so later checks never rescan unnecessary earlier work.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"board": [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "...` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Ignore `"."` cells. Compute the box as `(row // 3, col // 3)`. This validates the current board only; it does not solve Sudoku. Complexity is O(1) because the board size is fixed at 9x9, though you can also describe it as scanning 81 cells.

Complexity:
    Time: O(1); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary concise solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    36. Valid Sudoku - seen sets reference Variant role: Primary concise interview solution. Core idea: Every filled digit must be unique in three scopes: - its row - its column - its 3x3 box Store markers for those scopes in one set. If any marker is seen twice, the board is invalid. Box indexing: A cell `(r, c)` belongs to box: (r // 3, c // 3) Example: Seeing digit "8" at both `(0, 0)` and `(3, 0)` repeats the column marker `("col", 0, "8")`, so return False. Complexity: Time: O(1), because the board is always 9x9. Space: O(1), for the same reason.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen: set[tuple] = set()

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue

                markers = (
                    ("row", r, digit),
                    ("col", c, digit),
                    ("box", r // 3, c // 3, digit),
                )
                if any(marker in seen for marker in markers):
                    return False
                seen.update(markers)

        return True
