"""
1899. Merge Triplets to Form Target Triplet - Discard Oversized Triplets Then Cover Coordinates

Variant role:
    primary greedy solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Discard any triplet that exceeds target in any coordinate; valid triplets only need to cover each target coordinate.

    This specific variant uses: discard oversized triplets then cover coordinates.

Key invariant:
    The local choice preserves at least one optimal continuation, usually because choosing the best available option cannot reduce future feasibility.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"triplets": [[2, 5, 3], [1, 8, 4], [1, 7, 5]], "target": [2, 7, 5]}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the greedy choice and why earlier/later choices cannot improve it. Watch boundary cases where equality is allowed. For reachability problems, track the farthest possible boundary. For string balance problems, a range of possibilities can be more useful than one exact state.

Complexity:
    Time: O(n); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary greedy solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    1899. Merge Triplets to Form Target Triplet - filter and cover reference Core idea: A triplet with any coordinate greater than target can never be used, because merging takes coordinate-wise maximums. Among valid triplets, check whether each target coordinate can be matched by at least one triplet. Complexity: Time: O(n) Space: O(1)
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        covered = [False, False, False]

        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(3)):
                continue
            for i in range(3):
                if triplet[i] == target[i]:
                    covered[i] = True

        return all(covered)
