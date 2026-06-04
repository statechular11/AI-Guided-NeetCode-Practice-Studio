"""
138. Copy List with Random Pointer - Hash Map Reference

Deep-copy a linked list where each node has both `next` and `random` pointers.

Variant role:
    Primary clear solution.

Core idea:
    Use a dictionary keyed by original node identity:

        original node -> cloned node

    First create a clone node for every original node. Then make a second pass
    to wire each clone's `next` and `random` pointers by looking up the cloned
    version of the original pointer target.

Why two passes:
    A random pointer may point forward to a node that has not been wired yet.
    Creating all clones first makes every possible target available.

Walkthrough:
    For:

        [[7, null], [13, 0]]

    Pass 1 creates:

        clone(7)
        clone(13)

    Pass 2 wires:

        clone(7).next = clone(13)
        clone(13).random = clone(7)

    because original node 13's random pointer targets original node 7.

Deep-copy invariant:
    Every pointer in the copied list must point to a cloned node or `None`. It
    should never point back into the original list.

Identity pitfall:
    Key the map by original node object, not by node value. Duplicate values are
    allowed, but each original node still needs its own distinct clone.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    Choose this when you want the safest implementation. It is usually the best
    first answer before discussing the O(1)-extra-space interweaving
    optimization.
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

        clones: dict[Node, Node] = {}
        cur = head
        while cur:
            clones[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            clones[cur].next = clones.get(cur.next)
            clones[cur].random = clones.get(cur.random)
            cur = cur.next

        return clones[head]
