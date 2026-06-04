"""
621. Task Scheduler - cooldown cycle heap simulation

Variant role:
    Process-oriented heap variant. It builds the answer one cooldown cycle at a
    time, which is often easier to derive before the formula.

Core idea:
    In any window of length n + 1, the same task label can appear at most once.
    Therefore, each cycle can schedule up to n + 1 distinct labels.

    To minimize future idles, greedily run the task labels with the largest
    remaining counts first. Python `heapq` is a min heap, so store negative
    counts to pop the largest remaining count.

Mechanics:
    1. Count task frequencies and heapify negative counts.
    2. Start a cycle with n + 1 slots.
    3. Pop up to n + 1 distinct tasks from the heap.
    4. Decrement each chosen count and save unfinished tasks.
    5. Push unfinished tasks back after the cycle.
    6. If more work remains, unused slots in the cycle are idle time.

Trace:
    tasks = A A A B B B, n = 2

    cycle size = 3

    cycle 1: run A, B, idle -> time 3
    cycle 2: run A, B, idle -> time 6
    cycle 3: run A, B       -> time 8

Why it works:
    The heap chooses the labels most likely to create future bottlenecks. Holding
    used labels out of the heap until the cycle ends enforces the cooldown
    constraint because no label can be selected twice in the same n + 1 block.

Common pitfalls:
    - Pushing a task back into the heap immediately; that would allow the same
      label to run again before the cooldown is satisfied.
    - Adding idle slots after the final cycle. If the heap is empty after a
      partial cycle, the schedule is done and no trailing idle time is needed.
    - Forgetting that heap values are negative counts.

Complexity:
    Time: O(answer * log A), where A is distinct task labels and answer is the
    final interval count.
    Space: O(A).

When to choose this variant:
    Use it to explain the scheduling process or to debug the formula. Prefer
    the formula when only the minimum length is required.
"""

from collections import Counter
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        time = 0

        while heap:
            used: list[int] = []
            slots = n + 1
            while slots and heap:
                count = heapq.heappop(heap) + 1
                if count:
                    used.append(count)
                time += 1
                slots -= 1
            for count in used:
                heapq.heappush(heap, count)
            if heap:
                time += slots

        return time
