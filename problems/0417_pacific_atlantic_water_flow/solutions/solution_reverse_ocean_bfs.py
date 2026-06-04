"""
417. Pacific Atlantic Water Flow - Reverse Bfs From Both Ocean Borders Then Intersect

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Reverse the flow and climb from oceans; intersection gives both-ocean cells.

    This specific variant uses: reverse BFS from both ocean borders then intersect.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"heights": [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]}` and the expected result is `[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    417. Pacific Atlantic Water Flow - reverse ocean BFS reference Core idea: Instead of flowing from every cell down to oceans, start from each ocean's border and move uphill/reverse-flow to cells that can reach that ocean. The answer is the intersection of Pacific-reachable and Atlantic-reachable cells. Complexity: O(m*n) time and space.
"""

from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        def bfs(starts):
            seen=set(starts); q=deque(starts)
            while q:
                r,c=q.popleft()
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in seen and heights[nr][nc]>=heights[r][c]:
                        seen.add((nr,nc)); q.append((nr,nc))
            return seen
        pac=[(0,c) for c in range(cols)]+[(r,0) for r in range(rows)]
        atl=[(rows-1,c) for c in range(cols)]+[(r,cols-1) for r in range(rows)]
        return [[r,c] for r,c in bfs(pac) & bfs(atl)]
