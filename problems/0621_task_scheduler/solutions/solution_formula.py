"""
621. Task Scheduler - max-frequency frame formula

Variant role:
    Primary optimized solution. It computes the minimum interval count directly
    from task frequencies instead of simulating the schedule.

Core idea:
    The most frequent task is the bottleneck. If task A appears f times and the
    cooldown is n, the first f - 1 copies of A force f - 1 blocks:

        A _ _ | A _ _ | A

    Each non-final A starts a block of length n + 1: the A itself plus n
    intervals before A can appear again.

Key formula:
    Let:

        max_freq = the highest frequency of any task
        max_count = how many task labels have that frequency

    Then the bottleneck frame length is:

        (max_freq - 1) * (n + 1) + max_count

    The final `max_count` handles ties at the highest frequency. For example,
    with A, B, and C each appearing 3 times and n = 3, the tail is not just one
    task:

        A B C _ | A B C _ | A B C

Why max with len(tasks):
    If enough other tasks exist, they fill all idle slots and may even extend
    the schedule beyond the bottleneck frame. The answer is therefore:

        max(total_tasks, bottleneck_frame)

Example:
    tasks = A A A B B B, n = 2

        max_freq = 3
        max_count = 2   # A and B
        frame = (3 - 1) * (2 + 1) + 2 = 8
        answer = max(6, 8) = 8

    One optimal schedule:

        A B idle A B idle A B

Common pitfalls:
    - Forgetting `max_count`; this breaks cases with multiple most-frequent
      task labels.
    - Returning only the frame length. When there are enough filler tasks, the
      total task count can be larger.
    - Treating this as a heap problem only; the optimized answer is a counting
      / greedy formula.

Formula:
    max(len(tasks), (max_freq - 1) * (n + 1) + number_of_max_freq_tasks)

Complexity:
    Time: O(T + A), where T is number of tasks and A is distinct labels.
    Space: O(A), which is O(1) for uppercase English letters.

When to choose this variant:
    Use this as the interview target when asked for the minimum interval count,
    not an actual schedule. It is compact, optimal, and avoids simulation.
"""

from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_count = sum(1 for count in counts.values() if count == max_freq)
        frame = (max_freq - 1) * (n + 1) + max_count
        return max(len(tasks), frame)
