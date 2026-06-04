"""
269. Alien Dictionary - Derive Char Constraints From Adjacent Words Then Topo Sort

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Only the first differing character between adjacent words creates an ordering edge.

    This specific variant uses: derive char constraints from adjacent words then topo sort.

Key invariant:
    The frontier state includes every dimension that affects correctness, such as node, cost, time, effort, stops, or component membership.

Mechanics:
    1. Define a graph state that includes every constraint needed for correctness.
    2. Seed the frontier with the starting state.
    3. Process states in the order required by BFS, heap priority, or topological logic.
    4. Skip states that are already dominated by a better known state.

Walkthrough:
    On the local case `example_1`, the input is `{"words": ["wrt", "wrf", "er", "ett", "rftt"]}` and the expected result is `"wertf"`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Choose the graph representation that matches the query: adjacency list, trie, union-find, heap, or grid mutation. For shortest paths in unweighted graphs, use BFS; for weighted non-negative graphs, use Dijkstra or a problem-specific variant. Mark visited at the right time to avoid duplicate work or infinite cycles. For topological sort, handle invalid prefix/cycle cases explicitly.

Complexity:
    Time: O(C+E); Space: O(C+E)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    269. Alien Dictionary - topological sort reference Core idea: Adjacent sorted words reveal the first differing character order. Build a graph of those constraints and topologically sort it. A longer word before its exact prefix is invalid. Complexity: O(total characters + edges) time and space.
"""

from collections import deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph={ch:set() for word in words for ch in word}; indeg={ch:0 for ch in graph}
        for a,b in zip(words, words[1:]):
            if len(a)>len(b) and a.startswith(b): return ''
            for x,y in zip(a,b):
                if x!=y:
                    if y not in graph[x]: graph[x].add(y); indeg[y]+=1
                    break
        q=deque([ch for ch,d in indeg.items() if d==0]); order=[]
        while q:
            ch=q.popleft(); order.append(ch)
            for nxt in graph[ch]:
                indeg[nxt]-=1
                if indeg[nxt]==0: q.append(nxt)
        return ''.join(order) if len(order)==len(graph) else ''
