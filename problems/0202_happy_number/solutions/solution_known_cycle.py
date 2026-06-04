"""
202. Happy Number - Known Unhappy Cycle Shortcut

Core idea:
    In base 10, every unhappy number eventually enters the same cycle:

        4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

    Therefore a number is happy if the process reaches `1`, and unhappy if the
    process reaches `4`.

Why this is valid:
    The digit-square-sum process quickly falls into a small bounded state
    space. In decimal, the only non-happy cycle reachable from positive
    integers is the cycle containing `4`. Once `4` appears, the sequence is
    forced through the cycle above and can never reach `1`.

Step-by-step mechanics:
    1. While `n` is neither `1` nor `4`, replace it with the digit-square sum.
    2. Return `True` only if the terminal value is `1`.

Example:
    `2` is not happy:

        2 -> 4

    Seeing `4` is enough to stop; the full cycle will follow.

Common pitfalls:
    - Treating this as the best first explanation. The seen-set and Floyd
      variants explain the general cycle-detection idea better.
    - Forgetting that this shortcut depends on base 10. It is a useful math
      fact for this problem, not a general cycle-detection pattern.
    - Using this without being able to justify why `4` is special.

Complexity:
    Time:
        Bounded for base 10 after the first O(log n) digit-square step.

    Space:
        O(1).

When to choose this variant:
    Use this as a compact math shortcut after you already understand the cycle
    argument. In an interview, lead with seen set or Floyd unless the shortcut
    is explicitly welcomed.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        while n not in {1, 4}:
            total = 0
            while n:
                n, digit = divmod(n, 10)
                total += digit * digit
            n = total
        return n == 1
