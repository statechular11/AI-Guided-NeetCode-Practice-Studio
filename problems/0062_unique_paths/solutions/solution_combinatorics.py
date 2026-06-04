"""
62. Unique Paths - combinatorial path count

Variant role:
    math optimized reference

Core idea:
    Every valid path is a permutation of exactly m-1 down moves and n-1 right moves.

Key invariant:
    Choosing where one move type appears completely determines the path.

Mechanics:
    Compute C((m-1)+(n-1), m-1), using Python's exact integer combination helper.

Common pitfalls:
    The grid dimensions count cells, so the number of moves is one less in each direction.

Complexity:
    Time: O(min(m, n)); Space: O(1)

When to choose this variant:
    Use this when the interviewer is open to the closed form; DP is better when obstacles or changing costs are introduced.
"""

from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)
