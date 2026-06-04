"""
146. LRU Cache - OrderedDict Reference

Core idea:
    Python's `collections.OrderedDict` already combines dictionary lookup with
    a linked ordering of keys. It can move a key to either end in O(1), and it
    can pop the oldest key in O(1).

    Treat the left side as least recently used and the right side as most
    recently used:

        least recent ... most recent

Key invariant:
    `self.cache` contains exactly the cached keys. Its iteration order is LRU
    order from oldest to newest. After every successful `get` or `put`, the
    touched key is moved to the right end.

Why this works:
    LRU eviction only needs the oldest key. If every access moves the key to the
    newest end, then the leftmost key is always the least recently used key.
    `popitem(last=False)` removes that leftmost key.

Step-by-step mechanics:
    get(key):
        - missing: return -1
        - present: move key to the right end and return its value

    put(key, value):
        - if key exists, update it and move it to the right end
        - if key is new, insert it at the right end
        - if capacity is exceeded, pop the leftmost key

Example:
    Capacity 2:

        put(1, 1) -> OrderedDict([(1, 1)])
        put(2, 2) -> OrderedDict([(1, 1), (2, 2)])
        get(1)    -> OrderedDict([(2, 2), (1, 1)])
        put(3, 3) -> evict 2, keep [(1, 1), (3, 3)]

Common pitfalls:
    - Forgetting that assigning to an existing key does not automatically make
      it most recent in all mapping types; call `move_to_end`.
    - Popping the rightmost item instead of the leftmost item.
    - Using a plain `dict` and assuming the needed move/pop operations are all
      available with the right semantics.
    - Depending on this in an interview without being ready to explain the
      underlying hash-map-plus-linked-list design.

Complexity:
    get:
        O(1) average time.

    put:
        O(1) average time.

    Space:
        O(capacity).

When to choose this variant:
    This is excellent Python production code and a good way to verify the
    abstract behavior. In interviews, use it only if built-ins are allowed or
    after explaining the custom doubly linked list solution.
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
