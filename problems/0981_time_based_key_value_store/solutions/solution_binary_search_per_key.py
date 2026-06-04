"""
981. Time Based Key-Value Store - Per Key Timestamp List

Variant role:
    primary design solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Per key, timestamps are sorted by construction. Use binary search to find the rightmost timestamp not greater than the query.

    This specific variant uses: per-key timestamp list.

Key invariant:
    The search interval always contains every still-possible answer. Each midpoint decision removes a side that cannot contain the target answer.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{}` and the expected result is `[null, null, "bar", "bar", null, "bar2", "bar2"]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Define whether your binary search interval is closed or half-open. For answer-space search, prove the predicate is monotonic. For boundary problems, test empty arrays and values outside the range. For non-unique valid outputs, the comparator should validate the requirement, not one fixed answer.

Complexity:
    set O(1), get O(log n); Space O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary design solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    981. Time Based Key-Value Store - per-key binary search reference Core idea: Store a sorted list of `(timestamp, value)` pairs for each key. LeetCode's calls use increasing timestamps for each key, so append preserves order. For get(key, timestamp), binary-search the rightmost timestamp <= query. Complexity: set: O(1) get: O(log n) for that key space: O(total set calls)
"""

from collections import defaultdict
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store.get(key, [])
        index = bisect_right(entries, (timestamp, chr(255))) - 1
        return "" if index < 0 else entries[index][1]
