"""
146. LRU Cache - Linear Ordered-Keys Baseline

Core idea:
    Keep the cache values in a dictionary and keep recency order in a Python
    list. The list stores keys from least recently used to most recently used.

        self.order[0]  -> least recent
        self.order[-1] -> most recent

Key invariant:
    `self.values` and `self.order` contain the same keys. The order list is the
    source of truth for recency, while the dictionary is the source of truth for
    values.

Why this works:
    The logic matches the LRU rule directly: whenever a key is used, remove it
    from its old position and append it to the end. When capacity is exceeded,
    remove the first key from the order list.

Step-by-step mechanics:
    get(key):
        - if missing, return -1
        - move key to the end of `self.order`
        - return its dictionary value

    put(key, value):
        - if existing, update value and move key to the end
        - if new and full, pop the first key and delete its value
        - append the new key as most recent

Why this is only a baseline:
    Removing a key from a Python list is O(capacity) because the list has to
    search for the key and shift elements. That violates the problem's required
    O(1) average time for `get` and `put`.

Common pitfalls:
    - Thinking dictionary lookup alone solves the order-maintenance part.
    - Forgetting to remove the evicted key from both the list and dictionary.
    - Updating an existing key without making it most recent.
    - Passing local examples but timing out under many operations.

Complexity:
    get:
        O(capacity), because `list.remove` is linear.

    put:
        O(capacity), because updating an existing key uses `list.remove`, and
        evicting from the front shifts list elements.

    Space:
        O(capacity).

When to choose this variant:
    Use it only as a teaching baseline. It is compact and correct, but not
    acceptable for the LeetCode follow-up because it is not O(1).
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values: dict[int, int] = {}
        self.order: list[int] = []

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self._touch(key)
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key] = value
            self._touch(key)
            return

        if len(self.values) == self.capacity:
            oldest = self.order.pop(0)
            del self.values[oldest]

        self.values[key] = value
        self.order.append(key)

    def _touch(self, key: int) -> None:
        self.order.remove(key)
        self.order.append(key)
