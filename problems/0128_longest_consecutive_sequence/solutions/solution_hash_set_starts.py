"""
128. Longest Consecutive Sequence - Sequence Starts Reference

Return the length of the longest run of consecutive integer values.

Variant role:
    Primary optimized interview solution.

Core idea:
    First put every number in a set:

        values = set(nums)

    This is a full preprocessing step. After it finishes, `values` already
    contains every number from the input. The later counting phase is not
    limited by input order, and it is not limited by which values have been
    visited in the outer loop so far.

    Then only start counting from numbers that are the beginning of a sequence,
    meaning:

        num - 1 not in values

    If `num - 1` exists, then `num` is part of a sequence that will be counted
    from an earlier value.

Key invariant:
    A sequence is counted exactly once, from its smallest value.

    For any consecutive run:

        a, a + 1, a + 2, ..., b

    only `a` is allowed to start counting, because `a - 1` is absent. Every
    other value in the run is skipped as a start because its predecessor exists:

        a + 1 is skipped because a exists
        a + 2 is skipped because a + 1 exists
        ...

    When we start from `a`, we do not need to "wait" to see `a + 1`, `a + 2`,
    or later values in input order. They are already in `values`, so we can walk
    forward with O(1) membership checks.

Example:
    For:

        nums = [100, 4, 200, 1, 3, 2]

    Step 1: Build the full set.

        values = {1, 2, 3, 4, 100, 200}

    Step 2: Inspect each unique value as a possible sequence start.

        num = 1
            0 is not in values, so 1 is a start.
            Count forward:
                1 exists -> length at least 1
                2 exists -> length becomes 2
                3 exists -> length becomes 3
                4 exists -> length becomes 4
                5 does not exist -> stop
            best = 4

        num = 2
            1 is in values, so 2 is not a start. Skip it.

        num = 3
            2 is in values, so 3 is not a start. Skip it.

        num = 4
            3 is in values, so 4 is not a start. Skip it.

        num = 100
            99 is not in values, so 100 is a start.
            101 does not exist -> length 1.

        num = 200
            199 is not in values, so 200 is a start.
            201 does not exist -> length 1.

    The answer is 4.

Clarifying the ordering question:
    Suppose the input order is:

        [1, 100, 4, 3, 2]

    The start value `1` appears before `2`, `3`, and `4` in the input. That is
    still fine because the algorithm does not count while reading the input.
    It first builds:

        values = {1, 2, 3, 4, 100}

    Then, when it later processes `1`, it can immediately check whether `2`,
    `3`, and `4` exist in the set. The sequence length is computed from the
    complete set, not from the portion of the input seen so far.

Why this is O(n):
    Although the code has a nested `while` loop, it does not expand from every
    number. It expands only from sequence starts. Each consecutive run is walked
    once from its smallest value, so the total forward-walk work across all
    starts is O(number of unique values), which is O(n).

Pitfall:
    Do not expand from every number. Expanding from non-starts causes repeated
    work and can degrade toward O(n^2).

    Also, iterate over `values` rather than `nums`. Duplicates in `nums` should
    not repeat the same start check or inflate a streak.

Complexity:
    Time:
        O(n)

    Space:
        O(n)

When to choose this variant:
    Use this in interviews. The whole proof lives in the sequence-start
    invariant: count only when the predecessor is absent.
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The set is complete before counting starts, so input order no longer
        # matters during the sequence-length phase.
        values = set(nums)
        best = 0

        for num in values:
            if num - 1 in values:
                # Not a start; the true start of this run will count it.
                continue

            length = 1
            while num + length in values:
                length += 1
            best = max(best, length)

        return best
