"""
202. Happy Number - Seen Set Cycle Reference

Core idea:
    Treat the digit-square-sum process as a deterministic sequence:

        n -> next(n) -> next(next(n)) -> ...

    where `next(n)` is the sum of the squares of the decimal digits of `n`.
    Because each number maps to exactly one next number, the sequence has only
    two possible outcomes:

        1. it reaches `1`, then stays at `1`;
        2. it repeats a previous value, forming a cycle that does not include
           `1`.

    A set of seen states makes that cycle detection explicit.

Key invariant:
    Before each transformation, every value in `seen` has already appeared in
    this sequence. If the current `n` is in `seen`, continuing would repeat the
    same transitions forever, so `n` is not happy.

Why the sequence is bounded:
    The input can be large, but one digit-square step quickly shrinks it. For a
    10-digit integer, the largest possible next value is:

        10 * 9^2 = 810

    After the first step, the sequence lives in a small finite state space.
    That is why cycle detection is enough; the process cannot grow forever.

Step-by-step example:
    For `n = 19`:

        19  -> 1^2 + 9^2 = 82
        82  -> 8^2 + 2^2 = 68
        68  -> 6^2 + 8^2 = 100
        100 -> 1^2 + 0^2 + 0^2 = 1

    The sequence reaches `1`, so `19` is happy.

    For `n = 2`, the sequence eventually repeats:

        2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

    Seeing `4` again proves the sequence is trapped in a cycle.

Digit-square helper mechanics:
    Use `divmod(n, 10)` to pop the last decimal digit:

        n, digit = divmod(n, 10)
        total += digit * digit

    This is more direct than converting to a string and keeps the solution in
    the math/digit-manipulation style.

Common pitfalls:
    - Checking for repeated values only after transforming can still work, but
      the loop condition becomes easier to get wrong. This reference checks the
      current state before transforming.
    - Forgetting that `1` is terminal: once the sequence reaches `1`, it is
      happy and should return `True`.
    - Trying to reason by monotonic decrease. The sequence is bounded, but it
      is not always decreasing.
    - Overstating the time as O(log n) total. Each transformation costs digits,
      and the number of states after the first step is bounded for base 10.

Complexity:
    Time:
        O(log n) for the first digit-square transformation, then bounded work
        over a small finite state space.

    Space:
        O(k), where `k` is the number of distinct states seen before reaching
        `1` or detecting a cycle. In base 10 this is bounded, but the set is the
        main extra storage.

When to choose this variant:
    This is the clearest primary solution. It makes the "reaches 1 or cycles"
    definition literal and is easy to explain before optimizing space.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while n:
                n, digit = divmod(n, 10)
                total += digit * digit
            n = total
        return n == 1
