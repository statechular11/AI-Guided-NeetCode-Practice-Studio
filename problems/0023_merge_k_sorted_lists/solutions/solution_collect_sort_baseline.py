"""
23. Merge k Sorted Lists - Collect And Sort Baseline

Core idea:
    Ignore the linked-list merge structure at first: collect every value into a
    Python list, sort the values, and build a new linked list from the sorted
    array.

Key invariant:
    After collection, `values` contains exactly the values from all input
    nodes. Sorting that array gives the final linked-list order.

Why this works:
    The output only needs to contain the same values in sorted order. If we
    collect all values and sort them, we produce a globally sorted sequence
    regardless of which input list each value came from.

Step-by-step mechanics:
    1. Traverse every input linked list and append each value to `values`.
    2. Sort `values`.
    3. Build a new linked list by appending one new node for each sorted value.

Example:
    Input values across all lists:

        [1, 4, 5], [1, 3, 4], [2, 6]

    Collection gives:

        [1, 4, 5, 1, 3, 4, 2, 6]

    Sorting gives:

        [1, 1, 2, 3, 4, 4, 5, 6]

Common pitfalls:
    - Forgetting that this builds new nodes instead of reusing existing nodes.
    - Calling this optimal; it does not exploit the fact that each list is
      already sorted.
    - Accidentally appending `ListNode` objects to the array and then relying on
      unsupported node comparisons.

Complexity:
    Time:
        O(N log N), where N is the total number of nodes.

    Space:
        O(N), for the collected values and newly built linked list.

When to choose this variant:
    Use it as a correctness baseline or a quick first idea. It is not the
    interview target for this Hard problem, but it clarifies the output contract
    before optimizing with a heap or divide and conquer.
"""

from typing import List, Optional

from common.lc_types import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        values.sort()

        dummy = ListNode()
        tail = dummy
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next
        return dummy.next
