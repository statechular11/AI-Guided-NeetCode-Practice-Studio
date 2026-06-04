"""
73. Set Matrix Zeroes - Single-Flag First Row/Column Markers

Core idea:
    This is the compact constant-space marker pattern. It still reuses the
    first row and first column as marker arrays, but it needs only one extra
    boolean:

        row_zero == True means the first row must become zero

    The first column is represented by `matrix[0][0]`.

Key invariant:
    After the marking pass:

        matrix[0][c] == 0 marks column c
        matrix[r][0] == 0 marks row r for r > 0
        row_zero marks the original first row
        matrix[0][0] marks the original first column

    The overlap at `matrix[0][0]` is safe because the first row has its own
    separate boolean.

Why this works:
    A zero in the first row cannot be stored in `matrix[0][0]` without
    confusing first-column state, so `row_zero` saves that information. A zero
    in the first column naturally makes `matrix[0][0] == 0`, so that cell can
    act as the first-column marker.

Step-by-step mechanics:
    1. Scan every cell.
       - Mark the column with `matrix[0][c] = 0`.
       - If `r > 0`, mark the row with `matrix[r][0] = 0`.
       - If `r == 0`, set `row_zero = True`.
    2. Rewrite the inner matrix from the markers.
    3. If `matrix[0][0] == 0`, zero the first column.
    4. If `row_zero`, zero the first row.

Example:
    If a zero appears at `(0, 2)`, `row_zero` becomes true and column 2 is
    marked with `matrix[0][2] = 0`. This does not force column 0 to zero unless
    `matrix[0][0]` is also zero.

Common pitfalls:
    - Treating `matrix[0][0]` as both first-row and first-column state without
      an extra flag.
    - Zeroing the first row before using its column markers.
    - Forgetting to mark `row_zero` when the original zero is in row 0.
    - Forgetting that the method must mutate in place and return `None`.

Complexity:
    Time:
        O(m * n), with a constant number of matrix passes.

    Space:
        O(1), excluding the input matrix.

When to choose this variant:
    Use this when you want the canonical constant-space implementation. It is
    slightly denser than the two-flag version, but it is a common interview
    follow-up pattern.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        row_zero = True
                    else:
                        matrix[r][0] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
