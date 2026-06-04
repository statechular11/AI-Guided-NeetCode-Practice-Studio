"""
155. Min Stack - value/current-min pair reference

Variant role:
    Very readable design solution. Each stack entry stores both the pushed value
    and the minimum value at the time of that push.

Core idea:
    A normal stack remembers value history, but `getMin()` also needs minimum
    history. Store both pieces of state together:

        (value, minimum_so_far_after_this_push)

    Then the top pair always knows the current top value and current minimum.

Step-by-step:
    push(-2):
        stack = [(-2, -2)]

    push(0):
        current min is min(0, -2) = -2
        stack = [(-2, -2), (0, -2)]

    push(-3):
        current min is min(-3, -2) = -3
        stack = [(-2, -2), (0, -2), (-3, -3)]

    getMin() reads stack[-1][1] = -3.
    pop() removes (-3, -3), so getMin() becomes stack[-1][1] = -2.

Why duplicates are safe:
    Every pushed value gets its own snapshot of the current minimum. If the same
    minimum appears multiple times, each occurrence is represented in stack
    history and disappears one pop at a time.

When to choose this variant:
    This is often the easiest version to implement correctly in an interview.
    It uses one stack and keeps the invariant local to each entry.

Complexity:
    Time: O(1) per operation
    Space: O(n)
"""


class MinStack:
    def __init__(self):
        self.stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
