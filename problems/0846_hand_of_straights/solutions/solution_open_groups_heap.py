"""
846. Hand of Straights - min-heap of open groups

Variant role:
    alternative greedy grouping reference

Core idea:
    Process cards in sorted order and always extend the group that needs the smallest next card.

Key invariant:
    The heap stores open groups as (next_needed_card, remaining_cards_to_complete).

Mechanics:
    If the earliest group needs a card smaller than the current card, the group can never be completed. If it needs current card, extend it; otherwise start a new group.

Common pitfalls:
    Open groups must be extended before starting new groups at the same card value.

Complexity:
    Time: O(n log n); Space: O(n)

When to choose this variant:
    Use this to understand the scheduling-like view of forming consecutive groups; counter-start-runs is usually simpler.
"""

import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        if groupSize == 1:
            return True

        heap: list[tuple[int, int]] = []
        for card in sorted(hand):
            if heap and heap[0][0] < card:
                return False
            if heap and heap[0][0] == card:
                _, remaining = heapq.heappop(heap)
                if remaining > 1:
                    heapq.heappush(heap, (card + 1, remaining - 1))
            else:
                heapq.heappush(heap, (card + 1, groupSize - 1))
        return not heap
