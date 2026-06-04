"""
200. Number of Islands - Count Land Components By Sinking Visited Land

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Mutating visited land to water is the simplest visited set.

    This specific variant uses: count land components by sinking visited land.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"grid": [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]}` and the expected result is `1`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(m*n); Space: O(m*n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    200. Number of Islands - DFS sink reference Core idea: Each time an unvisited land cell is found, it starts one island. Flood-fill that island by changing connected land to water so it is not counted again. Complexity: O(m*n) time, O(m*n) worst-case recursion stack.
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != '1': return
            grid[r][c] = '0'
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1; dfs(r,c)
        return count
