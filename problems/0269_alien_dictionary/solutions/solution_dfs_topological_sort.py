"""
269. Alien Dictionary - DFS topological sort

Variant role:
    alternative advanced-graph reference

Core idea:
    Infer ordering edges from the first differing character of adjacent words, then topologically sort the character graph.

Key invariant:
    A visiting character on the recursion path means a cycle, so no valid alien order exists.

Mechanics:
    Initialize every seen letter, add one edge per adjacent word pair, reject invalid prefix order, then reverse DFS postorder.

Common pitfalls:
    Only the first differing character between adjacent words creates an ordering constraint.

Complexity:
    Time: O(total characters + edges); Space: O(unique characters + edges)

When to choose this variant:
    Use this as the DFS counterpart to BFS indegree topological sorting.
"""

from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {ch: set() for word in words for ch in word}

        for first, second in zip(words, words[1:]):
            limit = min(len(first), len(second))
            if len(first) > len(second) and first[:limit] == second[:limit]:
                return ""
            for i in range(limit):
                if first[i] != second[i]:
                    graph[first[i]].add(second[i])
                    break

        state: dict[str, int] = {}
        order: list[str] = []

        def dfs(ch: str) -> bool:
            if state.get(ch, 0) == 1:
                return False
            if state.get(ch, 0) == 2:
                return True
            state[ch] = 1
            for nei in graph[ch]:
                if not dfs(nei):
                    return False
            state[ch] = 2
            order.append(ch)
            return True

        for ch in graph:
            if not dfs(ch):
                return ""

        return "".join(reversed(order))
