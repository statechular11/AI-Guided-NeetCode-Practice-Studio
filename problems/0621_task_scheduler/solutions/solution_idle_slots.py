"""
621. Task Scheduler - fill idle slots from the dominant task

Variant role:
    Alternative formula derivation. It starts by counting the idle slots forced
    by the most frequent task, then subtracts slots filled by other tasks.

Core idea:
    Place the most frequent task first. If it appears `max_freq` times, there
    are `max_freq - 1` gaps between its copies:

        A _ _ | A _ _ | A

    Each gap needs n cooldown positions, so the initial number of forced idle
    slots is:

        idle_slots = (max_freq - 1) * n

    Other tasks can fill those slots. A task with count c can fill at most
    `max_freq - 1` of these gaps, because there are only that many gaps.

Example:
    tasks = A A A B B B, n = 2

        A _ _ | A _ _ | A
        idle_slots = 2 * 2 = 4

    Place B in at most two gaps:

        A B _ | A B _ | A B

    idle_slots becomes 2, so answer is:

        len(tasks) + idle_slots = 6 + 2 = 8

Handling ties:
    Sorting counts descending and skipping the first max-frequency task makes
    tied max-frequency tasks behave like fillers. Each tied task fills
    `max_freq - 1` slots and then occupies the final tail position naturally as
    part of `len(tasks)`.

Why max with zero:
    If there are more than enough filler tasks, idle_slots can go negative.
    Negative idle time does not exist; it simply means all gaps were filled and
    the answer is just len(tasks).

Common pitfalls:
    - Subtracting the full count for a filler task. It can fill at most one
      position per gap, so subtract `min(max_freq - 1, count)`.
    - Forgetting that tied max-frequency tasks still contribute tail positions.
    - Confusing this with constructing the actual schedule; this only counts
      the minimum length.

Complexity:
    Time: O(T + A log A), where T is task count and A is distinct labels.
    Space: O(A), which is O(1) for uppercase English letters.

When to choose this variant:
    Use it when the frame formula feels too magical. It gives the same optimized
    result through a more concrete "how many idles remain?" lens.
"""

from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = sorted(Counter(tasks).values(), reverse=True)
        max_freq = counts[0]
        idle_slots = (max_freq - 1) * n

        for count in counts[1:]:
            idle_slots -= min(max_freq - 1, count)

        return len(tasks) + max(0, idle_slots)
