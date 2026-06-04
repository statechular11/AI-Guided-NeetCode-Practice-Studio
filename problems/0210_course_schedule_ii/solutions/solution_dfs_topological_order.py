"""
210. Course Schedule II - DFS postorder topological sort

Variant role:
    alternative topological-order reference

Core idea:
    A directed acyclic graph can be topologically ordered by reversing DFS postorder.

Key invariant:
    A node is appended only after every course reachable from it has been appended.

Mechanics:
    Build prereq -> course edges, use visiting/done states for cycle detection, append each node after DFS children, then reverse the result.

Common pitfalls:
    If a cycle is found, return [] immediately. Reversing postorder is required for prereq-before-course ordering.

Complexity:
    Time: O(V + E); Space: O(V + E)

When to choose this variant:
    Use this as the DFS counterpart to BFS indegree/Kahn order.
"""

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        state = [0] * numCourses
        order: list[int] = []

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            state[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order[::-1]
