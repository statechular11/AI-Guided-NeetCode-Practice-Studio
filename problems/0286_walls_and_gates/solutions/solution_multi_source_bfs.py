"""
286. Walls and Gates - Bfs From Every Gate Simultaneously

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Multi-source BFS is the natural shortest-distance tool when all gates are sources.

    This specific variant uses: BFS from every gate simultaneously.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"rooms": [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]}` and the expected result is `{"args": [[[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]]}`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    286. Walls and Gates - multi-source BFS reference Core idea: Start BFS from all gates at once. The first time an empty room is reached, it is reached by the nearest gate because BFS expands by distance layers. Complexity: O(m*n) time and space.
"""

from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms: return
        INF=2147483647; rows,cols=len(rooms),len(rooms[0]); q=deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c]==0: q.append((r,c))
        while q:
            r,c=q.popleft()
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc]==INF:
                    rooms[nr][nc]=rooms[r][c]+1; q.append((nr,nc))
