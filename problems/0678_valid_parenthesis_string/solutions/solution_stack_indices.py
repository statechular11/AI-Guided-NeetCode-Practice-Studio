"""
678. Valid Parenthesis String - stacks of open and star indices

Variant role:
    alternative greedy-stack reference

Core idea:
    Use stars as flexible parentheses, but respect order: a star can close an unmatched '(' only if it appears after it.

Key invariant:
    left stores unmatched '(' indices; star stores unused '*' indices.

Mechanics:
    Use '(' for opens, '*' as fallback for unmatched ')', then pair remaining '(' with later stars.

Common pitfalls:
    A star before '(' cannot close that later '(', so compare indices in the cleanup phase.

Complexity:
    Time: O(n); Space: O(n)

When to choose this variant:
    Use this when the min/max open-count range feels too abstract.
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        left: list[int] = []
        star: list[int] = []

        for i, ch in enumerate(s):
            if ch == "(":
                left.append(i)
            elif ch == "*":
                star.append(i)
            elif left:
                left.pop()
            elif star:
                star.pop()
            else:
                return False

        while left and star:
            if left.pop() > star.pop():
                return False
        return not left
