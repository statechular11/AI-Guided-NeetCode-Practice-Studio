"""
22. Generate Parentheses - explicit stack of backtracking states

Variant role:
    iterative backtracking reference

Core idea:
    The recursive state can be stored explicitly as (prefix, opens_used, closes_used), then expanded while respecting validity constraints.

Key invariant:
    Every stack state is a prefix that can still be extended to a valid parentheses string.

Mechanics:
    Push '(' when opens_used < n. Push ')' when closes_used < opens_used. Record a prefix only when it reaches length 2n.

Common pitfalls:
    The close count cannot exceed the open count at any prefix, even if the final counts would balance later.

Complexity:
    Time: O(C_n * n); Space: O(C_n * n)

When to choose this variant:
    Use this to make backtracking state concrete or to practice translating recursion into an explicit stack.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: list[str] = []
        stack = [("", 0, 0)]

        while stack:
            prefix, opened, closed = stack.pop()
            if len(prefix) == 2 * n:
                result.append(prefix)
                continue
            if opened < n:
                stack.append((prefix + "(", opened + 1, closed))
            if closed < opened:
                stack.append((prefix + ")", opened, closed + 1))

        return result
