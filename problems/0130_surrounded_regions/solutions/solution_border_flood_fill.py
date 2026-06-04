"""
130. Surrounded Regions - Mark Border Connected Safe Regions Then Flip The Rest

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Invert the perspective: preserve border-connected O cells, then flip all other O cells.

    This specific variant uses: mark border-connected safe regions then flip the rest.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"board": [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]}` and the expected result is `{"args": [[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]]}`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    130. Surrounded Regions - border flood fill reference Core idea: Any O connected to the border cannot be captured. Mark all border-connected O cells as safe, flip remaining O to X, then restore safe marks to O. Complexity: O(m*n) time, O(m*n) worst-case stack/queue space.
"""

from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        q = deque()
        for r in range(rows):
            for c in (0, cols - 1):
                if board[r][c] == 'O': q.append((r,c))
        for c in range(cols):
            for r in (0, rows - 1):
                if board[r][c] == 'O': q.append((r,c))
        while q:
            r,c=q.popleft()
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] != 'O':
                continue
            board[r][c] = 'S'
            q.extend([(r+1,c),(r-1,c),(r,c+1),(r,c-1)])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O': board[r][c] = 'X'
                elif board[r][c] == 'S': board[r][c] = 'O'
