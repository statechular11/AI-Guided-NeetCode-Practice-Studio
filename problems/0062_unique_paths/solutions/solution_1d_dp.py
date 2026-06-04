"""
62. Unique Paths - Rolling Row Path Counts

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The transition is paths from above plus paths from left.

    This specific variant uses: rolling row path counts.

Key invariant:
    Each DP cell represents a pair of subproblem positions or constraints, and the transition covers all valid ways to reach that cell.

Mechanics:
    1. Define what each row/column coordinate means.
    2. Initialize empty-prefix or boundary states.
    3. Fill each cell from the smaller neighboring subproblems required by the recurrence.
    4. Return the cell or compressed state for the full input.

Walkthrough:
    On the local case `example_1`, the input is `{"m": 3, "n": 7}` and the expected result is `28`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Write down whether the state represents a prefix, grid cell, interval, transaction state, or memoized subproblem. Initialize empty-prefix and first-row/first-column cases deliberately. For 1D compressed DP, choose forward vs backward iteration based on whether reuse is allowed. For interval DP, consider choosing the last action rather than the first action.

Complexity:
    Time: O(m*n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    62. Unique Paths - 1D grid DP reference Core idea: ways[c] stores the number of paths to the current row and column c. Moving left-to-right, ways[c] already contains paths from above and ways[c-1] contains paths from the left. Complexity: O(m*n) time, O(n) space.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                ways[c] += ways[c - 1]
        return ways[-1]
