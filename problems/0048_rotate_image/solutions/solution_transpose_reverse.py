"""
48. Rotate Image - Transpose Then Reverse Rows Reference

Core idea:
    A 90-degree clockwise rotation maps every cell:

        old (r, c) -> new (c, n - 1 - r)

    We can decompose that mapping into two simpler in-place transforms:

        1. Transpose across the main diagonal:
              old (r, c) -> (c, r)

        2. Reverse every row horizontally:
              (c, r) -> (c, n - 1 - r)

    Combined, those two steps give exactly the clockwise rotation target:

        old (r, c) -> (c, n - 1 - r)

Key invariant:
    During transpose, swap only the upper triangle with the lower triangle:

        for r in range(n):
            for c in range(r + 1, n):

    Starting `c` at `r + 1` avoids swapping the diagonal with itself and avoids
    undoing a swap by later visiting `(c, r)`.

Step-by-step example:
    Start:

        1 2 3
        4 5 6
        7 8 9

    After transpose:

        1 4 7
        2 5 8
        3 6 9

    After reversing each row:

        7 4 1
        8 5 2
        9 6 3

Common pitfalls:
    - Returning a new matrix; the prompt requires mutating `matrix` in place.
    - Transposing every `(r, c)` pair, which swaps elements twice and restores
      the original matrix.
    - Reversing columns instead of rows after transpose; that would produce a
      counterclockwise rotation.
    - Forgetting that `matrix.reverse()` reverses row order, while
      `row.reverse()` reverses values inside one row.

Complexity:
    Time:
        O(n^2), because each cell participates in constant work.

    Space:
        O(1), ignoring loop variables.

When to choose this variant:
    This is usually the cleanest interview solution. It gives a memorable
    identity and less boundary bookkeeping than the layer-by-layer swap.
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in matrix:
            row.reverse()
