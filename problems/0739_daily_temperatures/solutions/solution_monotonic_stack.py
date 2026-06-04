"""
739. Daily Temperatures - monotonic stack reference.

Return, for each day, how many days pass before a warmer temperature appears.

Core idea:
    A day only needs to wait until the first warmer day to its right. While
    scanning left to right, keep a stack of indices whose answers are still
    unknown. When today's temperature is warmer than the temperature at the
    stack top, today is exactly the first warmer day for that older index.

Stack invariant:
    The stack stores unresolved indices. Their temperatures are monotonically
    non-increasing from bottom to top. If a warmer temperature appears, it can
    resolve one or more indices at the top before the current day is pushed.

Walkthrough:
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    - day 0, 73: stack = [0]
    - day 1, 74: 74 > 73, so answer[0] = 1 - 0 = 1; push 1
    - day 2, 75: 75 > 74, so answer[1] = 1; push 2
    - days 3 and 4 are cooler, so they wait on the stack
    - day 5, 72 resolves day 4 and day 3, but not day 2
    - day 6, 76 resolves every colder unresolved day before it

Why each index is processed once:
    Every day is pushed once and popped at most once. That is why the nested
    while loop is still linear overall.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack: list[int] = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)

        return answer
