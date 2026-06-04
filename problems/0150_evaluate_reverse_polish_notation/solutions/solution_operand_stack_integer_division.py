"""
150. Evaluate Reverse Polish Notation - operand stack with integer division helper

Variant role:
    This is the same primary stack approach, but it spells out truncation toward
    zero with integer arithmetic. It is useful when you want to avoid Python's
    `//` floor-division pitfall and avoid float conversion from `int(a / b)`.

Core idea:
    Use the standard operand stack:

    - push numbers,
    - pop right operand first,
    - pop left operand second,
    - apply the operator,
    - push the result.

Division helper:
    LeetCode wants truncation toward zero:

        7 / -3 -> -2

    Python floor division gives:

        7 // -3 -> -3

    To truncate toward zero using integers:

        sign = -1 if exactly one operand is negative else 1
        result = sign * (abs(left) // abs(right))

Example:
    tokens = ["7", "-3", "/"]

        right = -3
        left = 7
        sign = -1
        abs(left) // abs(right) = 7 // 3 = 2
        result = -2

When to choose this variant:
    Use this if you want the division rule to be visibly correct in Python.
    Otherwise, the shorter `int(left / right)` form is accepted under LeetCode's
    32-bit intermediate-value constraint.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from typing import Callable, List


def trunc_div(left: int, right: int) -> int:
    sign = -1 if (left < 0) ^ (right < 0) else 1
    return sign * (abs(left) // abs(right))


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []

        operations: dict[str, Callable[[int, int], int]] = {
            "+": lambda left, right: left + right,
            "-": lambda left, right: left - right,
            "*": lambda left, right: left * right,
            "/": trunc_div,
        }

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()
            stack.append(operations[token](left, right))

        return stack[-1]
