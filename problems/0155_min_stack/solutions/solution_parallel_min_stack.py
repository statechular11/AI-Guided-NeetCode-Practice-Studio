"""
155. Min Stack - parallel min stack reference

Variant role:
    This is the primary two-stack design. One stack stores values; the second
    stack stores the minimum value after each corresponding push.

Core idea:
    Keep one normal value stack and one stack of minimums. When pushing a value,
    also push the minimum of that value and the previous minimum.

Why duplicates matter:
    Push a minimum for every value, not only when the value is smaller. That
    keeps both stacks the same length and makes pop O(1) without special cases.

Step-by-step:
    push(-2):
        values   = [-2]
        minimums = [-2]

    push(0):
        values   = [-2, 0]
        minimums = [-2, -2]

    push(-3):
        values   = [-2, 0, -3]
        minimums = [-2, -2, -3]

    pop():
        pop from both stacks, restoring the previous minimum automatically.

Invariant:
    `values` and `minimums` have the same length.

    For every index i:

        minimums[i] = min(values[0:i + 1])

    Therefore `minimums[-1]` is always the current minimum.

When to choose this variant:
    Use this when you want the stack states separated and easy to inspect. It is
    also a good stepping stone to the sparse min-stack variant.

Complexity:
    Time: O(1) per operation
    Space: O(n)
"""


class MinStack:
    def __init__(self):
        self.values: list[int] = []
        self.minimums: list[int] = []

    def push(self, val: int) -> None:
        self.values.append(val)
        self.minimums.append(val if not self.minimums else min(val, self.minimums[-1]))

    def pop(self) -> None:
        self.values.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
