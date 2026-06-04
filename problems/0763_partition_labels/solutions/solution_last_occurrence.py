"""
763. Partition Labels - Farthest Last Occurrence

Variant role:
    primary greedy solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The current partition must extend to the farthest last occurrence of every character seen so far.

    This specific variant uses: farthest last occurrence.

Key invariant:
    The local choice preserves at least one optimal continuation, usually because choosing the best available option cannot reduce future feasibility.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"s": "ababcbacadefegdehijhklij"}` and the expected result is `[9, 7, 8]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the greedy choice and why earlier/later choices cannot improve it. Watch boundary cases where equality is allowed. For reachability problems, track the farthest possible boundary. For string balance problems, a range of possibilities can be more useful than one exact state.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary greedy solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    763. Partition Labels - last occurrence reference Core idea: A partition cannot end before the last occurrence of any character it contains. Scan while maintaining the farthest last occurrence required by the current partition. When the index reaches that boundary, cut. Complexity: Time: O(n) Space: O(1) for lowercase English letters.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        start = end = 0
        result: list[int] = []

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result
