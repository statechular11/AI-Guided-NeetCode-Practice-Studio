"""
739. Daily Temperatures - Brute Force Baseline

Return, for each day, how many days must pass until a warmer temperature.

Variant role:
    Simple educational baseline.

Core idea:
    For each day, scan every future day until the first warmer temperature is
    found. If no warmer future day exists, the answer stays 0.

Why this is useful:
    This is the easiest way to understand the required output, but it is not the
    interview target because the constraints allow up to 10^5 days.

Example:
    For:

        temperatures = [30, 40, 50, 60]

    - day 0 finds warmer day 1, so answer[0] = 1
    - day 1 finds warmer day 2, so answer[1] = 1
    - day 2 finds warmer day 3, so answer[2] = 1
    - day 3 has no future day, so answer[3] = 0

Tradeoff:
    The nested scan can revisit many future days. The monotonic-stack solution
    avoids that by keeping unresolved colder days and resolving them once.

Complexity:
    Time:
        O(n^2)

    Space:
        O(1) extra, excluding the output list

When to choose this variant:
    Use it only to establish the output contract. Move to the monotonic stack
    for the real interview solution.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temp:
                    answer[i] = j - i
                    break

        return answer
