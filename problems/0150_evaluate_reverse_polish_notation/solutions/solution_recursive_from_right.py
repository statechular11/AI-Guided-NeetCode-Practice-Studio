"""
150. Evaluate Reverse Polish Notation - recursive right-to-left reference

Variant role:
    This is an educational parser-style variant. It is not the usual interview
    implementation, but it reveals that RPN is a postfix encoding of an
    expression tree.

Core idea:
    In Reverse Polish Notation, every operator appears after its operands.
    Therefore, the final token is the root of the whole expression.

    If we consume tokens from right to left:

    - a number is already a complete expression,
    - an operator means we must recursively evaluate its right operand first,
      then its left operand.

Why right operand first:
    Consider:

        ["2", "1", "+", "3", "*"]

    The final "*" is the root. The token immediately before it belongs to the
    right operand, which is "3". The remaining prefix is the left operand,
    which is ["2", "1", "+"].

    So from the right side:

        operator "*"
        right = 3
        left = 2 + 1
        result = left * right

Operand order still matters:
    For subtraction and division, after recursively evaluating:

        right = eval_from_right()
        left = eval_from_right()

    compute:

        left - right
        left / right

Division rule:
    Division truncates toward zero. The helper below performs that with integer
    arithmetic so it does not rely on float conversion:

        sign * (abs(left) // abs(right))

When to choose this variant:
    Use the iterative stack solution in interviews. Use this variant when you
    want to understand RPN as a compact tree traversal: postfix means
    left-subtree, right-subtree, root.

Complexity:
    Time: O(n)
    Space: O(n), for recursion depth in a deeply nested expression.
"""

from typing import List


def trunc_div(left: int, right: int) -> int:
    sign = -1 if (left < 0) ^ (right < 0) else 1
    return sign * (abs(left) // abs(right))


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        index = len(tokens) - 1
        operators = {"+", "-", "*", "/"}

        def eval_from_right() -> int:
            nonlocal index

            token = tokens[index]
            index -= 1

            if token not in operators:
                return int(token)

            right = eval_from_right()
            left = eval_from_right()

            if token == "+":
                return left + right
            if token == "-":
                return left - right
            if token == "*":
                return left * right
            return trunc_div(left, right)

        return eval_from_right()
