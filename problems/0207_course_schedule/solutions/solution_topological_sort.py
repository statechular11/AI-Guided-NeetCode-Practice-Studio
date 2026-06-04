"""
207. Course Schedule - Kahn Bfs Over Indegree Zero Courses

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Cycle detection in a directed prerequisite graph is topological sorting.

    This specific variant uses: Kahn BFS over indegree-zero courses.

Key invariant:
    The visited, distance, or component state records exactly which graph states have already been accounted for, so traversal does not double-count or loop.

Mechanics:
    1. Build or read the adjacency/state representation.
    2. Seed the traversal frontier with the initial state.
    3. Mark or relax states at the moment required by the invariant.
    4. Expand neighbors while avoiding duplicate or stale work.

Walkthrough:
    On the local case `example_1`, the input is `{"numCourses": 2, "prerequisites": [[1, 0]]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(V+E); Space: O(V+E)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    207. Course Schedule - topological sort reference Core idea: Courses can be finished iff the prerequisite graph has no cycle. Kahn's algorithm repeatedly takes courses with indegree 0 and removes their edges. Complexity: O(V+E) time and space.
"""

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]; indeg=[0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course); indeg[course]+=1
        q=deque([i for i,d in enumerate(indeg) if d==0]); taken=0
        while q:
            cur=q.popleft(); taken+=1
            for nxt in graph[cur]:
                indeg[nxt]-=1
                if indeg[nxt]==0: q.append(nxt)
        return taken==numCourses
