"""
994. Rotting Oranges - Bfs Infection Layers From All Rotten Oranges

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Minute count is BFS layer distance from the nearest initially rotten orange.

    This specific variant uses: BFS infection layers from all rotten oranges.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}` and the expected result is `4`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    994. Rotting Oranges - multi-source BFS reference Core idea: All initially rotten oranges start BFS at minute 0. Each BFS layer rots adjacent fresh oranges one minute later. If fresh oranges remain, return -1. Complexity: O(m*n) time and space.
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0]); q=deque(); fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2: q.append((r,c,0))
                elif grid[r][c]==1: fresh+=1
        minutes=0
        while q:
            r,c,minutes=q.popleft()
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2; fresh-=1; q.append((nr,nc,minutes+1))
        return minutes if fresh==0 else -1
