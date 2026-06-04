"""
2013. Detect Squares - Coordinate-Bounded Grid Reference

Core idea:
    The constraints say every coordinate is between `0` and `1000`. That means
    a fixed `1001 x 1001` count grid can store all point multiplicities:

        grid[y][x] = count of point (x, y)

    With this representation, `add` is a direct array increment. For `count`,
    iterate every possible `x2` on the query row and use `(qx, qy)` to construct
    the two possible square rows.

Key invariant:
    Choosing a same-row point `(x2, qy)` fixes the side length:

        side = x2 - qx

    The two candidate opposite rows are `qy + side` and `qy - side`. For each
    row inside the coordinate bounds, the needed corners are `(qx, other_y)` and
    `(x2, other_y)`.

Why bounds matter:
    Unlike the sparse row-counter variant, this implementation can index the
    grid only for coordinates in `[0, 1000]`. Candidate rows outside that range
    are skipped.

Tradeoff:
    The grid gives predictable `count` time of `O(1001)` regardless of how many
    points have been added, but it spends `O(1001^2)` space. That is acceptable
    under these constraints, but the sparse `Counter` versions are usually more
    elegant and memory-friendly.

Common pitfalls:
    - Accidentally storing `grid[x][y]` in one method and reading `grid[y][x]`
      in another.
    - Forgetting to check `0 <= other_y <= 1000` before indexing.
    - Multiplying by the query point's count; the query point is external.
    - Using a grid and losing duplicate points by assigning `1` instead of
      incrementing.

Complexity:
    add:
        O(1).

    count:
        O(C), where `C = 1001` is the coordinate range size.

    Space:
        O(C^2).

When to choose this variant:
    Use this as a constraints-aware alternative. In interviews, mention it only
    after the sparse counter solution unless the interviewer asks how the
    bounded coordinate range can be used.
"""

from typing import List


class DetectSquares:
    LIMIT = 1000

    def __init__(self):
        size = self.LIMIT + 1
        self.grid = [[0] * size for _ in range(size)]

    def add(self, point: List[int]) -> None:
        x, y = point
        self.grid[y][x] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total = 0

        for x2, same_row_count in enumerate(self.grid[qy]):
            if x2 == qx or same_row_count == 0:
                continue

            side = x2 - qx
            for other_y in (qy + side, qy - side):
                if 0 <= other_y <= self.LIMIT:
                    total += (
                        same_row_count
                        * self.grid[other_y][qx]
                        * self.grid[other_y][x2]
                    )

        return total
