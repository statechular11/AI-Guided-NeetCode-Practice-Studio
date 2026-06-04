"""
2013. Detect Squares - Sparse Point Counter Reference

Core idea:
    Store how many times each exact point has been added. A query point
    `(qx, qy)` forms an axis-aligned square once we choose the opposite diagonal
    corner `(x, y)`.

Key invariant:
    `(x, y)` is a valid diagonal corner only when:

        x != qx
        y != qy
        abs(x - qx) == abs(y - qy)

    The first two checks enforce positive area. The distance equality enforces
    equal side lengths.

Why the other corners are forced:
    After choosing the diagonal `(x, y)`, the remaining corners must be:

        (qx, y)  # same x as query, same y as diagonal
        (x, qy)  # same x as diagonal, same y as query

    There is no extra search needed. If both corners exist, they form exactly
    one square shape with the query and diagonal corner.

Duplicate handling:
    Duplicates are distinct points in this problem. If `(x, y)` was added `a`
    times, `(qx, y)` was added `b` times, and `(x, qy)` was added `c` times,
    then this diagonal contributes:

        a * b * c

    choices. This multiplication is the most important counting detail.

Mini trace:
    Added points:

        (3, 10), (11, 2), (3, 2)

    Query `(11, 10)`. The point `(3, 2)` is a valid diagonal because the
    horizontal and vertical distances are both `8`. The other corners are
    `(11, 2)` and `(3, 10)`, so it contributes `1 * 1 * 1 = 1`.

Common pitfalls:
    - Counting rectangles by accepting any different `x` and `y`; the side
      lengths must match.
    - Forgetting `x != qx` and `y != qy`; otherwise zero-area "squares" sneak
      in.
    - Treating duplicate points as one point instead of multiplying counts.
    - Iterating over raw added points and overcounting duplicate diagonals
      separately; a `Counter` lets one distinct diagonal contribute its full
      multiplicity once.

Complexity:
    add:
        O(1).

    count:
        O(P), where `P` is the number of distinct stored points.

    Space:
        O(P).

When to choose this variant:
    This is the most direct interview solution: small state, clear diagonal
    reasoning, and no dependency on the coordinate upper bound.
"""

from collections import Counter
from typing import List


class DetectSquares:
    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total = 0
        for (x, y), diagonal_count in self.points.items():
            if x == qx or y == qy:
                continue
            if abs(x - qx) != abs(y - qy):
                continue
            total += diagonal_count * self.points[(qx, y)] * self.points[(x, qy)]
        return total
