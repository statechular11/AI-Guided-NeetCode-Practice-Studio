"""
332. Reconstruct Itinerary - Lexicographic Eulerian Path With Reverse Sorted Adjacency

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    This is an Eulerian path problem; append airports after exhausting outgoing edges.

    This specific variant uses: lexicographic Eulerian path with reverse-sorted adjacency.

Key invariant:
    The frontier state includes every dimension that affects correctness, such as node, cost, time, effort, stops, or component membership.

Mechanics:
    1. Define a graph state that includes every constraint needed for correctness.
    2. Seed the frontier with the starting state.
    3. Process states in the order required by BFS, heap priority, or topological logic.
    4. Skip states that are already dominated by a better known state.

Walkthrough:
    On the local case `example_1`, the input is `{"tickets": [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]}` and the expected result is `["JFK", "MUC", "LHR", "SFO", "SJC"]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(E log E); Space: O(E)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    332. Reconstruct Itinerary - Hierholzer DFS reference Core idea: Use every directed ticket exactly once and choose lexical order. Sort each adjacency list in reverse so popping from the end gives the smallest next airport. Postorder DFS builds the Eulerian path in reverse. Complexity: O(E log E) time for sorting, O(E) space.
"""

from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        for a,b in sorted(tickets, reverse=True): graph[a].append(b)
        route=[]
        def visit(airport):
            while graph[airport]: visit(graph[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
