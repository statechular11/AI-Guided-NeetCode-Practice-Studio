"""
36. Valid Sudoku - bitmask reference

Variant role:
    Compressed-state reference. This version encodes each row, column, and box
    as a 9-bit integer instead of storing tuple markers in a set.

Core idea:
    Digits 1 through 9 can be represented by bits 0 through 8:

        digit "1" -> 1 << 0
        digit "2" -> 1 << 1
        ...
        digit "9" -> 1 << 8

    For each filled cell, compute the bit for its digit. If that bit is already
    present in the corresponding row, column, or box mask, then the digit has
    appeared before in that scope and the board is invalid.

Box indexing:
    A cell `(r, c)` belongs to one of 9 boxes:

        box = (r // 3) * 3 + (c // 3)

    This maps the top-left box to 0, top-middle to 1, ..., bottom-right to 8.

Step-by-step walkthrough:
    1. Keep three arrays of 9 integers:
       `rows`, `cols`, and `boxes`.
    2. For each non-empty cell, convert the digit into one bit.
    3. Check whether that bit is already set in the row, column, or box mask.
    4. If not, set the bit in all three masks and continue.

Example:
    If digit "8" appears in row 0, bit `1 << 7` is set in `rows[0]`.
    Seeing another "8" in row 0 later would find that bit already set, so the
    function returns False.

Why this is useful:
    The marker-set solution is often easiest to write. The bitmask version is a
    nice compressed-state pattern: it replaces many hashable markers with fixed
    integer masks and makes the duplicate check a few bit operations.

Complexity:
    Time: O(1), because the board is always 9x9.
    Space: O(1), using three fixed arrays of 9 integers.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue

                bit = 1 << (ord(digit) - ord("1"))
                box = (r // 3) * 3 + (c // 3)

                if rows[r] & bit or cols[c] & bit or boxes[box] & bit:
                    return False

                rows[r] |= bit
                cols[c] |= bit
                boxes[box] |= bit

        return True
