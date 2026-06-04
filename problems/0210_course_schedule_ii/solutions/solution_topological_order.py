"""
210. Course Schedule II - Kahn Topological Sort Order

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The comparator validates any topological order, not one exact sequence.

    This specific variant uses: Kahn topological sort order.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"numCourses": 2, "prerequisites": [[1, 0]]}` and the expected result is `[0, 1]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(V+E); Space: O(V+E)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    210. Course Schedule II - topological order reference Core idea: Same indegree-zero BFS as Course Schedule, but record the removal order. If all courses are removed, the order is valid; otherwise a cycle blocks some courses and the answer is empty. Complexity: O(V+E) time and space.
"""

from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]; indeg=[0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course); indeg[course]+=1
        q=deque([i for i,d in enumerate(indeg) if d==0]); order=[]
        while q:
            cur=q.popleft(); order.append(cur)
            for nxt in graph[cur]:
                indeg[nxt]-=1
                if indeg[nxt]==0: q.append(nxt)
        return order if len(order)==numCourses else []
