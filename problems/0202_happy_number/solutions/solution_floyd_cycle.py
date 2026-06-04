"""
202. Happy Number - Floyd Cycle Detection Reference

Core idea:
    The happy-number process defines a linked-list-like functional graph:

        n -> next(n)

    Every value has exactly one outgoing edge. If the sequence does not reach
    `1`, it must eventually enter a cycle. Instead of storing all seen values,
    use Floyd's slow/fast pointers:

        slow moves one step:  slow = next(slow)
        fast moves two steps: fast = next(next(fast))

    If the process reaches `1`, the number is happy. If `slow == fast` before
    that, the sequence has a cycle that does not include `1`.

Key invariant:
    `slow` and `fast` are always values from the same deterministic sequence,
    with `fast` moving twice as quickly. In a finite cycle, the faster pointer
    must eventually lap the slower pointer.

Why this works:
    This is the same idea as Linked List Cycle, except the "next pointer" is
    computed by summing squared digits. The sequence is bounded after a small
    number of steps, so if `1` is never reached, both pointers eventually live
    inside the same cycle. Once inside, their distance modulo the cycle length
    changes by one each round, so they must meet.

Step-by-step mechanics:
    1. Define `next_value(num)` as the sum of squared digits.
    2. Initialize `slow = n` and `fast = next_value(n)`.
    3. While `fast != 1` and `slow != fast`:
       - advance `slow` once,
       - advance `fast` twice.
    4. Return whether `fast == 1`.

Example:
    For `n = 19`, the sequence is:

        19 -> 82 -> 68 -> 100 -> 1

    The fast pointer reaches `1`, so return `True`.

    For `n = 2`, the sequence enters:

        4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

    Slow and fast eventually meet inside this cycle, so return `False`.

Common pitfalls:
    - Advancing `fast` only once, which becomes the same as `slow` and detects
      nothing useful.
    - Returning `slow == 1` only. The fast pointer may be the one that reaches
      `1` first.
    - Forgetting that this is an optimization of the seen-set idea, not a
      different mathematical condition.

Complexity:
    Time:
        Bounded for base 10 after the first O(log n) digit-square step.

    Space:
        O(1), because no seen set is stored.

When to choose this variant:
    Use this when the interviewer asks for O(1) extra space or when you want to
    connect Happy Number to cycle detection / two pointers.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def next_value(num: int) -> int:
            total = 0
            while num:
                num, digit = divmod(num, 10)
                total += digit * digit
            return total

        slow = n
        fast = next_value(n)

        while fast != 1 and slow != fast:
            slow = next_value(slow)
            fast = next_value(next_value(fast))

        return fast == 1
