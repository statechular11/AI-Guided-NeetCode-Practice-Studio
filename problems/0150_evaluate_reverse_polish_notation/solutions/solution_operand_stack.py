"""
150. Evaluate Reverse Polish Notation - operand stack reference

Variant role:
    This is the primary interview solution. It evaluates the postfix expression
    in one left-to-right pass using a stack of computed operand values.

Core idea:
    Numbers are pushed onto a stack. An operator pops the two most recent
    operands, applies the operation, and pushes the result.

Order matters:
    The first pop is the right operand, and the second pop is the left operand:

        b = stack.pop()
        a = stack.pop()

    For subtraction and division, compute:

        a - b
        a / b

    not:

        b - a
        b / a

Division rule:
    LeetCode expects truncation toward zero, not Python's floor division.

    Examples:

        7 / 3   ->  2
        7 / -3  -> -2
       -7 / 3   -> -2

    Python `//` floors, so `-7 // 3 == -3`, which is wrong here. Use
    `int(a / b)` for LeetCode's constraints, or use an integer helper if you
    want to avoid float conversion.

Walkthrough:
    tokens = ["2", "1", "+", "3", "*"]

    "2" -> push 2                    stack = [2]
    "1" -> push 1                    stack = [2, 1]
    "+" -> pop 1 and 2, push 3       stack = [3]
    "3" -> push 3                    stack = [3, 3]
    "*" -> pop 3 and 3, push 9       stack = [9]

    Final answer is stack[-1] = 9.

When to choose this variant:
    Use this as the default interview answer. It is direct, iterative, and makes
    the operand-order invariant explicit.

Complexity:
    Time: O(n)
    Space: O(n)
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))

        return stack[-1]
