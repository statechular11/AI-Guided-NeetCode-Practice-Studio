from __future__ import annotations

from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


_UNSET = object()


class GraphNode:
    def __init__(self, val: int = 0, neighbors: Optional[list["GraphNode"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class RandomPointerNode:
    def __init__(
        self,
        x=_UNSET,
        next: Optional["RandomPointerNode"] = None,
        random: Optional["RandomPointerNode"] = None,
        *,
        val=_UNSET,
    ):
        if x is _UNSET:
            x = 0 if val is _UNSET else val
        self.val = int(x)
        self.next = next
        self.random = random


class NextTreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["NextTreeNode"] = None,
        right: Optional["NextTreeNode"] = None,
        next: Optional["NextTreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class QuadTreeNode:
    def __init__(
        self,
        val: bool = False,
        isLeaf: bool = False,
        topLeft: Optional["QuadTreeNode"] = None,
        topRight: Optional["QuadTreeNode"] = None,
        bottomLeft: Optional["QuadTreeNode"] = None,
        bottomRight: Optional["QuadTreeNode"] = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Node:
    """Backward-compatible catch-all Node.

    New generated problem files should import a problem-specific node class as
    `Node`. This compatibility class remains for older local solutions and
    scratch work that still import `Node` directly.
    """

    def __init__(
        self,
        val=_UNSET,
        neighbors: Optional[list["Node"]] = None,
        next: Optional["Node"] = None,
        random: Optional["Node"] = None,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        isLeaf: bool = False,
        topLeft: Optional["Node"] = None,
        topRight: Optional["Node"] = None,
        bottomLeft: Optional["Node"] = None,
        bottomRight: Optional["Node"] = None,
        x=_UNSET,
    ):
        if val is _UNSET:
            val = 0 if x is _UNSET else x
        if isinstance(neighbors, bool):
            isLeaf = neighbors
            topLeft, topRight, bottomLeft, bottomRight = next, random, left, right
            neighbors = None
            next = random = left = right = None
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        self.next = next
        self.random = random
        self.left = left
        self.right = right
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next


def build_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def list_to_values(head):
    values = []
    seen = set()
    while head is not None:
        ident = id(head)
        if ident in seen:
            raise ValueError("cycle detected while serializing ListNode")
        seen.add(ident)
        values.append(head.val)
        head = head.next
    return values


def build_tree(values):
    if not values:
        return None
    nodes = [None if value is None else TreeNode(value) for value in values]
    kids = deque(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        if kids:
            node.left = kids.popleft()
        if kids:
            node.right = kids.popleft()
    return nodes[0]


def tree_to_values(root):
    if root is None:
        return []
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(getattr(node, "left", None))
        queue.append(getattr(node, "right", None))
    while values and values[-1] is None:
        values.pop()
    return values


def find_tree_node(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    return find_tree_node(root.left, target) or find_tree_node(root.right, target)


def build_graph(adjacency):
    if not adjacency:
        return None
    nodes = [GraphNode(i + 1) for i in range(len(adjacency))]
    for i, neighbors in enumerate(adjacency):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def graph_to_adjacency(node):
    if node is None:
        return []
    seen = {}
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        if cur.val in seen:
            continue
        seen[cur.val] = cur
        for nxt in getattr(cur, "neighbors", []):
            if nxt.val not in seen:
                queue.append(nxt)
    return [[neighbor.val for neighbor in seen[i].neighbors] for i in sorted(seen)]


def build_random_list(values):
    if not values:
        return None
    nodes = [RandomPointerNode(pair[0]) for pair in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for node, pair in zip(nodes, values):
        random_idx = pair[1]
        node.random = None if random_idx is None else nodes[random_idx]
    return nodes[0]


def random_list_to_values(head):
    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    index = {id(node): i for i, node in enumerate(nodes)}
    out = []
    for node in nodes:
        random = getattr(node, "random", None)
        out.append([node.val, None if random is None else index.get(id(random))])
    return out


def build_next_tree(values):
    if not values:
        return None
    nodes = [None if value is None else NextTreeNode(value) for value in values]
    kids = deque(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        if kids:
            node.left = kids.popleft()
        if kids:
            node.right = kids.popleft()
    return nodes[0]


def next_tree_to_levels(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if getattr(node, "left", None):
                queue.append(node.left)
            if getattr(node, "right", None):
                queue.append(node.right)
        result.extend(level)
        result.append("#")
    return result


def quad_tree_to_values(node):
    if node is None:
        return None
    return [
        bool(getattr(node, "isLeaf", False)),
        bool(getattr(node, "val", False)),
        quad_tree_to_values(getattr(node, "topLeft", None)),
        quad_tree_to_values(getattr(node, "topRight", None)),
        quad_tree_to_values(getattr(node, "bottomLeft", None)),
        quad_tree_to_values(getattr(node, "bottomRight", None)),
    ]
