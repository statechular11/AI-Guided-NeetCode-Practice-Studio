"""
846. Hand of Straights - Consume Runs From Smallest Card

Variant role:
    primary greedy solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    The smallest remaining card has no predecessor available, so it must start a group.

    This specific variant uses: consume runs from smallest card.

Key invariant:
    The local choice preserves at least one optimal continuation, usually because choosing the best available option cannot reduce future feasibility.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"hand": [1, 2, 3, 6, 2, 3, 4, 7, 8], "groupSize": 3}` and the expected result is `true`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    State the greedy choice and why earlier/later choices cannot improve it. Watch boundary cases where equality is allowed. For reachability problems, track the farthest possible boundary. For string balance problems, a range of possibilities can be more useful than one exact state.

Complexity:
    Time: O(n log n + n*g); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary greedy solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    846. Hand of Straights - counter start runs reference Core idea: Always start groups from the smallest remaining card. If card x remains, it must be the start of some group, so consume x, x+1, ..., x+groupSize-1. Complexity: Time: O(n log n + n * groupSize) in the direct implementation. Space: O(n)
"""

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        counts = Counter(hand)
        for card in sorted(counts):
            amount = counts[card]
            if amount == 0:
                continue
            for next_card in range(card, card + groupSize):
                if counts[next_card] < amount:
                    return False
                counts[next_card] -= amount
        return True
