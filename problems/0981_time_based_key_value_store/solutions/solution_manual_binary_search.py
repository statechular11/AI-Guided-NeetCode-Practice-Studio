"""
981. Time Based Key-Value Store - manual rightmost-timestamp binary search

Variant role:
    alternative design reference

Core idea:
    Per key, timestamps arrive in increasing order, so get can binary-search the rightmost timestamp <= query.

Key invariant:
    answer is the best value seen so far whose timestamp is <= the query timestamp.

Mechanics:
    Move right when entries[mid].timestamp is valid, saving its value; otherwise move left.

Common pitfalls:
    Do not search across different keys. Each key owns an independent sorted timeline.

Complexity:
    set: O(1); get: O(log n); Space: O(total set calls)

When to choose this variant:
    Use this if tuple sentinels or bisect feel too implicit; the boundary logic is visible.
"""

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store.get(key, [])
        left, right = 0, len(entries) - 1
        answer = ""
        while left <= right:
            mid = (left + right) // 2
            time, value = entries[mid]
            if time <= timestamp:
                answer = value
                left = mid + 1
            else:
                right = mid - 1
        return answer
