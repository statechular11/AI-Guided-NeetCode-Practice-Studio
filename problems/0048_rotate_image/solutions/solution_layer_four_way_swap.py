"""
48. Rotate Image - Layer Four-Way Swap Reference

Core idea:
    Rotate the matrix one square "ring" at a time. For each layer, move four
    corresponding cells in a cycle:

        top    <- left
        left   <- bottom
        bottom <- right
        right  <- top

    This directly implements the coordinate mapping without using the
    transpose identity.

Index mechanics:
    For a layer bounded by:

        top = layer
        left = layer
        bottom = n - 1 - layer
        right = n - 1 - layer

    walk `offset` from `0` to `right - left - 1`. The four cells are:

        top-left edge:     (top, left + offset)
        left-bottom edge:  (bottom - offset, left)
        bottom-right edge: (bottom, right - offset)
        right-top edge:    (top + offset, right)

    For clockwise rotation:

        matrix[top][left + offset]
            <- matrix[bottom - offset][left]
            <- matrix[bottom][right - offset]
            <- matrix[top + offset][right]
            <- saved top

Why the loop excludes the last index:
    In a layer of width `w`, there are only `w - 1` four-cycles. Including the
    last corner would rotate the same corner group twice.

Mini trace for a 3x3:
    The outer layer has one offset group around the corners:

        (0,0), (2,0), (2,2), (0,2)

    and one offset group around the edge middles:

        (0,1), (1,0), (2,1), (1,2)

    The center `(1,1)` stays fixed.

Common pitfalls:
    - Off-by-one errors in the offset range.
    - Overwriting a value before saving it in `top_left`.
    - Mixing up clockwise and counterclockwise assignment order.
    - Forgetting that odd-sized matrices have a center cell that should not
      move.

Complexity:
    Time:
        O(n^2), because every cell moves once.

    Space:
        O(1), only one temporary value per cycle.

When to choose this variant:
    Use this when asked to rotate by explicitly moving layers, or when you want
    to practice matrix boundary/index control. The transpose+reverse approach is
    usually shorter and easier to explain.
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for layer in range(n // 2):
            top = layer
            left = layer
            bottom = n - 1 - layer
            right = n - 1 - layer

            for offset in range(right - left):
                top_left = matrix[top][left + offset]

                matrix[top][left + offset] = matrix[bottom - offset][left]
                matrix[bottom - offset][left] = matrix[bottom][right - offset]
                matrix[bottom][right - offset] = matrix[top + offset][right]
                matrix[top + offset][right] = top_left
