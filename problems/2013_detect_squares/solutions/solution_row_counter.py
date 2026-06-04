"""
2013. Detect Squares - Row-Grouped Counter Reference

Core idea:
    Group point counts by horizontal row:

        rows[y][x] = how many times point (x, y) was added

    For a query `(qx, qy)`, choose another x-coordinate `x2` on the same query
    row. The segment from `(qx, qy)` to `(x2, qy)` is one side of the square.
    Its length is:

        side = x2 - qx

    Then there are two possible rows for the opposite side:

        qy + side
        qy - side

Key invariant:
    Once we choose `(x2, qy)` as the horizontal neighbor of the query, the two
    remaining corners for row `other_y` are forced:

        (qx, other_y)
        (x2, other_y)

    The contribution is the product of the three stored corner counts:

        count(x2, qy) * count(qx, other_y) * count(x2, other_y)

    The query point itself does not need to have been added.

Why iterate the query row:
    A square containing `(qx, qy)` must have one stored corner on the same row as
    the query. Grouping by row lets `count` examine only distinct x-values on
    that row instead of every stored point.

Implementation detail:
    Use `.get(...)` inside `count` instead of indexing the `defaultdict`.
    Counting should be a read-only operation; it should not create empty rows
    for missing y-coordinates.

Mini trace:
    Added:

        (3, 10), (11, 2), (3, 2)

    Query `(11, 10)`. On row `10`, `x2 = 3`, so `side = -8`. The possible
    opposite rows are `2` and `18`. Row `2` contains both `(11, 2)` and
    `(3, 2)`, contributing `1`.

Common pitfalls:
    - Forgetting that `side` can be negative. Checking both `qy + side` and
      `qy - side` naturally covers above and below.
    - Using only one opposite row and missing squares on the other side.
    - Multiplying by the query point count; the query point is not selected from
      the data structure.
    - Losing duplicate counts by storing a `set` instead of a counter.

Complexity:
    add:
        O(1).

    count:
        O(R), where `R` is the number of distinct x-coordinates on the query
        row.

    Space:
        O(P), where `P` is the number of distinct stored points.

When to choose this variant:
    Use this when you want a slightly more optimized and query-focused
    explanation. It is also a good mental model for deriving the square from a
    side instead of from the diagonal.
"""

from collections import Counter, defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.rows = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.rows[y][x] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total = 0
        query_row = self.rows.get(qy, {})

        for x2, same_row_count in query_row.items():
            if x2 == qx:
                continue

            side = x2 - qx
            for other_y in (qy + side, qy - side):
                other_row = self.rows.get(other_y)
                if other_row is None:
                    continue
                total += (
                    same_row_count
                    * other_row[qx]
                    * other_row[x2]
                )

        return total
