"""
133. Clone Graph - BFS clone map

Variant role:
    alternative graph traversal reference

Core idea:
    Clone nodes breadth-first while a map preserves the one-to-one relationship between original nodes and cloned nodes.

Key invariant:
    Whenever an original node is in clones, clones[original] is the unique clone object that all copied edges should point to.

Mechanics:
    Create the start clone, BFS through original nodes, create missing neighbor clones, and append cloned neighbors to the copied adjacency list.

Common pitfalls:
    Do not create a fresh clone every time a neighbor is seen; cycles and shared neighbors require reuse from the map.

Complexity:
    Time: O(V + E); Space: O(V)

When to choose this variant:
    Use this when iterative BFS feels safer than recursive DFS for graph cloning.
"""

from collections import deque
from typing import Optional

from common.lc_types import GraphNode as Node


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        clones = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clones[cur].neighbors.append(clones[neighbor])
        return clones[node]
