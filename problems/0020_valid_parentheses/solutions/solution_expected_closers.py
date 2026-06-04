"""
20. Valid Parentheses - expected closers stack reference

Variant role:
    This is the same stack idea with a different state representation. Instead
    of storing opening brackets, the stack stores the exact closing brackets we
    expect to see later.

Core idea:
    When we see an opening bracket, push its matching closing bracket:

        "(" -> push ")"
        "[" -> push "]"
        "{" -> push "}"

    When we see a closing bracket, it must equal the top expected closer.

Step-by-step:
    s = "([])"

    1. See "(": push ")".
    2. See "[": push "]".
    3. See "]": it matches the top expected closer, so pop.
    4. See ")": it matches the top expected closer, so pop.
    5. Stack is empty, so the string is valid.

Why this can be easier:
    The stack directly answers the question:

        "What closing bracket am I waiting for next?"

    That avoids a closing-to-opening lookup at the moment we process a closer.

Failure examples:
    s = "(]"
        After "(", the stack expects ")". Seeing "]" fails immediately.

    s = "([)]"
        After "(", "[", the stack expects "]". Seeing ")" fails immediately.

When to choose this variant:
    Use this if "push the future obligation" feels more natural than "push the
    opening bracket." It has the same complexity and the same interview quality
    as the opening-stack version.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        expected: list[str] = []
        closing_for = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for ch in s:
            if ch in closing_for:
                expected.append(closing_for[ch])
            elif not expected or expected.pop() != ch:
                return False

        return not expected
