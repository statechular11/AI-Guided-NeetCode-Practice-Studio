"""
133. Clone Graph - DFS + Hash Map Reference

Variant role:
    Primary interview solution.

Core idea:
    A graph node may be reachable through many paths, and cycles are allowed.
    Therefore, cloning cannot be a simple tree-style recursion. We need a map
    from each original node to its cloned node:

        original node -> cloned node

    When DFS first sees a node, create its clone immediately and store it in
    the map before cloning neighbors. That early insertion is what breaks
    cycles safely.

Step-by-step walkthrough:
    1. If the input node is None, return None.
    2. If a node is already in `clones`, return the existing clone.
    3. Otherwise create a new `Node(cur.val)`.
    4. Store it in `clones` before visiting neighbors.
    5. Recursively clone every neighbor and attach the cloned neighbor list.

Example:
    For an edge 1 -- 2, DFS clones node 1, then clones node 2, then when node 2
    points back to node 1, the map returns the existing clone of 1 instead of
    recursing forever.

Complexity:
    Time: O(V + E), visiting each node and edge relation once.
    Space: O(V), for the clone map and recursion stack.
"""

from typing import Optional

from common.lc_types import GraphNode as Node


# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        clones = {}

        def clone(cur: Optional[Node]) -> Optional[Node]:
            if cur is None:
                return None
            if cur in clones:
                return clones[cur]
            copied = Node(cur.val)
            clones[cur] = copied
            copied.neighbors = [clone(nei) for nei in cur.neighbors]
            return copied
        return clone(node)
