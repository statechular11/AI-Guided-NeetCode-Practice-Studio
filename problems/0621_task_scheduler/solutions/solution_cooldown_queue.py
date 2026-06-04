"""
621. Task Scheduler - one-interval heap plus cooldown queue simulation

Variant role:
    Fine-grained simulation. It advances time one interval at a time and keeps
    tasks that are cooling down in a queue until they are eligible again.

Core idea:
    At each interval, run the currently available task with the largest
    remaining count. Once a task runs, it cannot be chosen again until:

        current_time + n + 1

    The `+1` matters because if n = 2 and A runs at time 1, then times 2 and 3
    must separate the next A, so A is available again at time 4.

State meaning:
    - `heap` stores available task counts as negative numbers, so the largest
      remaining count is popped first.
    - `cooldown` stores `(ready_time, remaining_negative_count)` for tasks that
      have been run but still have remaining copies.

Mechanics:
    1. At the start of each interval, release every task whose ready time has
       arrived.
    2. If an available task exists, run the one with largest remaining count.
    3. If that task still has copies left, place it into cooldown.
    4. If no task is available, the interval is idle.
    5. Continue until both heap and cooldown are empty.

Trace:
    tasks = A A A B B B, n = 2

        time 1: run A, A ready again at 4
        time 2: run B, B ready again at 5
        time 3: idle
        time 4: release/run A
        time 5: release/run B
        time 6: idle
        time 7: run A
        time 8: run B

    answer = 8

Why it works:
    The heap greedily reduces the largest remaining bottleneck among currently
    legal tasks. The cooldown queue prevents illegal repeats by making a task
    unavailable until exactly the first time it can be scheduled again.

Common pitfalls:
    - Using `current_time + n` instead of `current_time + n + 1`.
    - Releasing cooled tasks after scheduling the current interval; tasks ready
      at this time should be eligible before deciding whether to idle.
    - Forgetting that negative heap counts move toward zero after each run.

Complexity:
    Time: O(answer * log A), where A is distinct task labels.
    Space: O(A).

When to choose this variant:
    Use it when you need to understand the cooldown mechanics step by step. It
    is more verbose than the cycle simulation and formula, but excellent for
    debugging off-by-one timing mistakes.
"""

from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        cooldown: deque[tuple[int, int]] = deque()

        time = 0
        while heap or cooldown:
            time += 1

            while cooldown and cooldown[0][0] <= time:
                _ready_time, count = cooldown.popleft()
                heapq.heappush(heap, count)

            if not heap:
                continue

            count = heapq.heappop(heap) + 1
            if count:
                cooldown.append((time + n + 1, count))

        return time
