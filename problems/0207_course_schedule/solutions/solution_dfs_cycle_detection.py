"""
207. Course Schedule - DFS cycle detection

Variant role:
    alternative topological-sort reference

Core idea:
    Courses can be completed exactly when the prerequisite graph has no directed cycle.

Key invariant:
    A node in the visiting state is on the current recursion path; seeing it again proves a cycle.

Mechanics:
    Use states 0=unvisited, 1=visiting, 2=done. DFS every course and fail on a back edge to a visiting node.

Common pitfalls:
    Do not mark a node done until all descendants have been proven acyclic.

Complexity:
    Time: O(V + E); Space: O(V + E)

When to choose this variant:
    Use this as the DFS counterpart to Kahn's BFS topological sort.
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            state[course] = 2
            return True

        return all(dfs(course) for course in range(numCourses))
