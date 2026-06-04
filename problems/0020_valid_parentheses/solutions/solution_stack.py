"""
20. Valid Parentheses - stack reference

Variant role:
    This is the primary interview solution. It stores unmatched opening brackets
    and checks each closing bracket against the most recent unmatched opening.

Core idea:
    Opening brackets create obligations. The next closing bracket must satisfy
    the most recent unmatched opening bracket, so a stack is the natural state.

Walkthrough:
    s = "([])"
    Push "(", push "[", see "]" and pop "[", see ")" and pop "(". The stack is
    empty at the end, so the string is valid.

Why a stack:
    Parentheses must close in reverse order:

        ( [ ] )

    The "[" opens after "(", so it must close before "(". That is exactly
    last-in, first-out behavior.

Failure examples:
    s = "(]"
        The closing "]" expects "[", but the stack top is "(", so return False.

    s = "([)]"
        The ")" appears while "[" is still the most recent unmatched opening, so
        the nesting order is invalid.

    s = "((("
        The scan ends with unmatched openings left in the stack, so return False.

When to choose this variant:
    Use this as the default interview answer. It is direct, short, and makes the
    stack invariant easy to state:

        stack contains the unmatched opening brackets in the order they must be
        closed.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []

        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)

        return not stack
