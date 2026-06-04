"""
73. Set Matrix Zeroes - First Row/Column Marker Reference

Core idea:
    The difficult part is not deciding which rows and columns need zeroing; it
    is preserving the original zero information while mutating in place.

    Use the matrix itself as marker storage:

        matrix[r][0] == 0 means row r must become all zero
        matrix[0][c] == 0 means column c must become all zero

    The first row and first column are real data too, so record whether they
    originally contained a zero before using them as marker arrays.

Key invariant:
    After the marking pass over the inner matrix, the first cell of each
    non-first row and each non-first column correctly records whether that row
    or column should be zeroed. The inner cells can then be rewritten based only
    on those markers.

Why this works:
    We never zero an entire row or column during the discovery pass. Instead,
    each original zero only writes marker cells. This avoids the classic
    cascading bug where a zero created by the algorithm is mistaken for an
    original zero.

Step-by-step mechanics:
    1. Check whether the original first row has a zero.
    2. Check whether the original first column has a zero.
    3. Scan cells excluding the first row and first column. For every zero at
       `(r, c)`, mark `matrix[r][0]` and `matrix[0][c]`.
    4. Rewrite the inner matrix using those markers.
    5. Zero the first row and/or first column if their saved flags say so.

Example:
    For:

        1 1 1
        1 0 1
        1 1 1

    The zero at `(1, 1)` marks `matrix[1][0]` and `matrix[0][1]`. During the
    rewrite pass, every cell in row 1 or column 1 becomes zero.

Common pitfalls:
    - Zeroing rows/columns immediately during the first scan, causing cascading
      zeros.
    - Forgetting that `matrix[0][0]` belongs to both the first row and first
      column, so first-row/first-column state needs special handling.
    - Applying first-row or first-column zeroing before rewriting the inner
      matrix, which destroys marker information too early.
    - Returning a new matrix instead of mutating the input in place.

Complexity:
    Time:
        O(m * n), with a constant number of matrix passes.

    Space:
        O(1), excluding the input matrix.

When to choose this variant:
    This is the primary interview solution when the follow-up asks for constant
    extra space. The two explicit booleans make the first row/column edge cases
    easier to explain.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
