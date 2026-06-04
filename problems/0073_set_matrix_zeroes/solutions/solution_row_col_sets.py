"""
73. Set Matrix Zeroes - Row/Column Sets Reference

Core idea:
    Split the work into two phases:

        1. discover which rows and columns originally contain a zero,
        2. rewrite cells whose row or column was marked.

    Store the discovered row indexes in `zero_rows` and column indexes in
    `zero_cols`.

Key invariant:
    During the second pass, `zero_rows` and `zero_cols` represent only original
    zeros from the input matrix. They are unaffected by zeros written during the
    rewrite pass.

Why this works:
    The bug to avoid is cascading: if we set a row to zero while still scanning,
    those new zeros could incorrectly cause more columns to become zero. By
    recording all original zero locations first, every rewrite decision is based
    on stable state.

Step-by-step mechanics:
    For each cell `(r, c)`:

        if matrix[r][c] == 0:
            zero_rows.add(r)
            zero_cols.add(c)

    Then scan again:

        if r in zero_rows or c in zero_cols:
            matrix[r][c] = 0

Example:
    For:

        1 2 3
        4 0 6
        7 8 9

    `zero_rows = {1}` and `zero_cols = {1}`, so the final matrix zeroes row 1
    and column 1.

Common pitfalls:
    - Mutating rows/columns during the discovery pass.
    - Recording coordinates but then forgetting to deduplicate rows/columns.
    - Returning a new matrix instead of modifying `matrix` in place.

Complexity:
    Time:
        O(m * n), two full matrix scans.

    Space:
        O(m + n), for the row and column marker sets.

When to choose this variant:
    Use this as the clean baseline before optimizing to O(1) space. It is often
    the easiest version to code correctly under interview pressure.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
