"""
138. Copy List with Random Pointer - Graph Traversal Reference

Deep-copy a linked list where each node has both `next` and `random` pointers.

Variant role:
    Educational graph-clone framing.

Core idea:
    Treat each node as a graph vertex and treat `next` and `random` as outgoing
    edges. Use a dictionary from original node to clone node, then traverse the
    reachable graph with a stack. Whenever an edge points to a node we have not
    cloned yet, create that clone and push the original target onto the stack.

Walkthrough:
    For:

        A.next = B
        B.random = A

    Start by creating A' and pushing A.

    Pop A:

        discover B through `next`
        create B'
        set A'.next = B'

    Pop B:

        discover A through `random`
        reuse existing A'
        set B'.random = A'

Why this works:
    The memo dictionary is the source of truth. It prevents duplicate clone
    nodes and safely handles random-pointer cycles.

Relationship to Clone Graph:
    This problem is a linked-list-shaped graph with up to two outgoing edges per
    node. The same memoized clone pattern applies to arbitrary graph cloning.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    This is not as simple as the two-pass hash-map solution for a linked list,
    but it is useful when explaining the relationship to Clone Graph and other
    deep-copy problems with arbitrary pointers.
"""

from typing import Optional

from common.lc_types import RandomPointerNode as Node


# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        clones: dict[Node, Node] = {head: Node(head.val)}
        stack = [head]

        while stack:
            node = stack.pop()
            clone = clones[node]

            for attr in ("next", "random"):
                neighbor = getattr(node, attr)
                if not neighbor:
                    continue
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                setattr(clone, attr, clones[neighbor])

        return clones[head]
