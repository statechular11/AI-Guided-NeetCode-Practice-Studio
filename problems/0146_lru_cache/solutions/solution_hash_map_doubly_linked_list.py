"""
146. LRU Cache - Hash Map Plus Doubly Linked List Reference

Core idea:
    LRU Cache needs two abilities at the same time:

        1. find a key in O(1),
        2. move a key to "most recently used" and evict "least recently used"
           in O(1).

    A dictionary gives O(1) key lookup. A doubly linked list gives O(1)
    removal/insertion when we already have the node. The dictionary maps each
    key to its linked-list node, so both structures work together.

List invariant:
    The list stores real cache nodes between two sentinels:

        head <-> most recent ... least recent <-> tail

    `head.next` is the most recently used real node.
    `tail.prev` is the least recently used real node.
    Every key in `self.nodes` points to exactly one node currently in the list.

Why this works:
    Recency changes on both successful `get` and every `put` of an existing or
    new key. Moving a node to the front records that it was just used. When the
    cache exceeds capacity, the only possible eviction target is `tail.prev`,
    because that node has gone longest without being moved to the front.

Step-by-step mechanics:
    get(key):
        - if missing, return -1
        - remove the existing node from its current position
        - insert it after `head`
        - return its value

    put(key, value):
        - if the key exists, update its node and move it after `head`
        - otherwise create a node, add it after `head`, and store it in the map
        - if size is now too large, remove `tail.prev` and delete its map entry

Example trace:
    Capacity 2:

        put(1, 1) -> [1]
        put(2, 2) -> [2, 1]    # 2 most recent
        get(1)    -> [1, 2]    # 1 moved to front
        put(3, 3) -> [3, 1]    # 2 was least recent and is evicted

Why sentinels help:
    Dummy `head` and `tail` turn every add/remove into the same pointer
    operation. There are no special cases for empty list, one-node list,
    removing the first real node, or removing the last real node.

Common pitfalls:
    - Updating a value without refreshing its recency.
    - Forgetting that `get` also counts as use.
    - Evicting from the wrong side of the list.
    - Removing a node from the list but forgetting to delete it from the map.
    - Inserting an existing node at the front without first unlinking it.
    - Letting the dictionary and linked list disagree about which keys exist.

Complexity:
    get:
        O(1) average time.

    put:
        O(1) average time.

    Space:
        O(capacity), one node and one map entry per cached key.

When to choose this variant:
    This is the primary interview solution. It is language-independent and
    directly demonstrates the design invariant behind an LRU cache.
"""


class _Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes: dict[int, _Node] = {}
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._remove(node)
        self._add_after_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._remove(node)
            self._add_after_head(node)
            return

        node = _Node(key, value)
        self.nodes[key] = node
        self._add_after_head(node)
        if len(self.nodes) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.nodes[lru.key]

    def _remove(self, node: _Node) -> None:
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before

    def _add_after_head(self, node: _Node) -> None:
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node
