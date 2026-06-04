"""
20. Valid Parentheses - repeated reduction baseline

Variant role:
    This is a learning baseline, not the recommended interview solution. It
    repeatedly removes adjacent matched pairs until no more pairs can be removed.

Core idea:
    In any valid parentheses string, the innermost valid pair must appear as one
    of:

        ()
        []
        {}

    If we repeatedly delete these adjacent pairs, a valid string eventually
    reduces to the empty string.

Example:
    s = "([])"

    First pass removes "[]":

        "([])" -> "()"

    Next pass removes "()":

        "()" -> ""

    The final string is empty, so the original string was valid.

Counterexample:
    s = "([)]"

    There is no adjacent valid pair to remove, so the string gets stuck and is
    not valid.

Why this is not ideal:
    Each replacement pass scans the string and may remove only a small amount of
    content. Deeply nested input such as "((((...))))" can therefore take many
    passes.

When to choose this variant:
    Use it only to build intuition: valid nested structures can be reduced from
    the inside out. For interviews and real constraints, use a stack.

Complexity:
    Time: O(n^2) in the worst case.
    Space: O(n), because strings are recreated during replacement.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        previous = None
        while previous != s:
            previous = s
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return not s
