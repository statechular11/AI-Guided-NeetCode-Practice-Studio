"""
54. Spiral Matrix - Boundary Shrink Reference

Core idea:
    Think of the matrix as nested rectangles. For the current rectangle, walk
    its outer ring in clockwise order:

        top row -> right column -> bottom row -> left column

    After finishing that ring, shrink the four boundaries inward and repeat.

Boundary meaning:
    `top` and `bottom` are the first and last unvisited row indexes.
    `left` and `right` are the first and last unvisited column indexes.

    The loop invariant is:

        every cell outside [top..bottom] x [left..right] has already been output
        every cell inside that rectangle is still unvisited

Why guards are needed:
    The top row and right column are always valid at the start of a loop because
    `top <= bottom` and `left <= right`.

    But after walking the top row, `top` moves down. If the matrix has only one
    remaining row, `top` can pass `bottom`; walking the bottom row would repeat
    the same row. Similarly, after walking the right column, `right` moves left;
    in a one-column remaining rectangle, walking the left column would repeat
    the same column.

    That is why the bottom and left traversals are guarded with:

        if top <= bottom:
        if left <= right:

Step-by-step example:
    For:

        1  2  3  4
        5  6  7  8
        9 10 11 12

    Ring 1 outputs:

        1, 2, 3, 4, 8, 12, 11, 10, 9, 5

    Then the remaining rectangle is:

        6 7

    Ring 2 outputs:

        6, 7

Common pitfalls:
    - Forgetting the bottom-row guard and duplicating a single remaining row.
    - Forgetting the left-column guard and duplicating a single remaining column.
    - Updating boundaries before finishing the side that still needs them.
    - Using `while len(result) < m * n` but still allowing out-of-bound side
      traversals.

Complexity:
    Time:
        O(m * n), every cell is appended exactly once.

    Space:
        O(1) excluding the output list.

When to choose this variant:
    This is the primary interview answer: no visited matrix, clear O(1) extra
    space, and good practice with inclusive boundaries.
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
