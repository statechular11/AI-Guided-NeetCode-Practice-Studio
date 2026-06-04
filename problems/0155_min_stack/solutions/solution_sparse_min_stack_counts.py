"""
155. Min Stack - sparse min stack with counts reference

Variant role:
    This is a space-conscious auxiliary-stack design. It keeps a normal value
    stack, but the min stack stores only minima and how many times the current
    minimum has appeared.

Core idea:
    A value that is larger than the current minimum does not change `getMin()`,
    so it does not need a new min-stack entry. Only values that are less than or
    equal to the current minimum affect minimum history.

State:
    values:
        The actual stack values.

    mins:
        Pairs of `(minimum_value, count)`.
        The top pair says what the current minimum is and how many active values
        equal that minimum.

Step-by-step:
    push(2):
        values = [2]
        mins   = [(2, 1)]

    push(0):
        values = [2, 0]
        mins   = [(2, 1), (0, 1)]

    push(0):
        values = [2, 0, 0]
        mins   = [(2, 1), (0, 2)]

    pop():
        pop one 0 from values and decrement the top min count:
        mins = [(2, 1), (0, 1)]

    getMin() is still 0.

Why counts matter:
    If we stored each new minimum only once and ignored duplicate minima, popping
    one copy of the minimum would incorrectly restore an older larger minimum.
    Counts preserve duplicate minima one pop at a time.

When to choose this variant:
    The pair-stack or full parallel-min-stack versions are usually simpler.
    This version is useful when you want to make duplicate-min handling explicit
    or reduce auxiliary min-stack entries when many pushes do not change the
    minimum.

Complexity:
    Time: O(1) per operation
    Space: O(n) worst case, but the auxiliary `mins` stack can be smaller than
        the value stack when minima change infrequently.
"""


class MinStack:
    def __init__(self):
        self.values: list[int] = []
        self.mins: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        self.values.append(val)

        if not self.mins or val < self.mins[-1][0]:
            self.mins.append((val, 1))
        elif val == self.mins[-1][0]:
            min_value, count = self.mins[-1]
            self.mins[-1] = (min_value, count + 1)

    def pop(self) -> None:
        val = self.values.pop()

        if val == self.mins[-1][0]:
            min_value, count = self.mins[-1]
            if count == 1:
                self.mins.pop()
            else:
                self.mins[-1] = (min_value, count - 1)

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.mins[-1][0]
