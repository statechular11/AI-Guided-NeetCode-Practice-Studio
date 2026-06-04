"""
739. Daily Temperatures - reverse scan with a next-temperature table.

This approach uses a detail from the constraints:

    30 <= temperatures[i] <= 100

There are only 71 possible temperature values. While scanning from right to
left, store the nearest future index where each exact temperature appears.

Core idea:
    For day i with temperature t, any warmer future day must have temperature
    in:

        t + 1, t + 2, ..., 100

    If we know the nearest future index for each of those temperatures, the
    answer for day i is the smallest such index minus i.

Walkthrough:
    temperatures = [30, 40, 50, 60]

    Scan from right to left:

    - day 3, temp 60: no warmer stored yet -> 0; record temp 60 at index 3
    - day 2, temp 50: nearest warmer among 51..100 is index 3 -> answer 1
    - day 1, temp 40: nearest warmer among 41..100 is index 2 -> answer 1
    - day 0, temp 30: nearest warmer among 31..100 is index 1 -> answer 1

When to use:
    The monotonic stack is usually the clean interview solution. This table
    solution is useful when you notice a small bounded value range and want to
    trade a tiny constant factor for a different state representation.

Complexity:
    Time: O(71 * n), which is O(n) because the temperature range is fixed
    Space: O(101), which is O(1)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        next_index_for_temperature = [n] * 101

        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            nearest_warmer_index = n

            for warmer_temp in range(temp + 1, 101):
                nearest_warmer_index = min(
                    nearest_warmer_index,
                    next_index_for_temperature[warmer_temp],
                )

            if nearest_warmer_index < n:
                answer[i] = nearest_warmer_index - i

            next_index_for_temperature[temp] = i

        return answer
