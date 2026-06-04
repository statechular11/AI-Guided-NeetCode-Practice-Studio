"""
21. Merge Two Sorted Lists - Recursive Reference

Merge two sorted linked lists recursively.

Variant role:
    Recursive learning variant. It mirrors the mathematical recurrence, but the
    iterative dummy-tail solution is usually the safer Python interview default
    because it avoids recursion stack depth.

Core idea:
    The smaller head becomes the merged head, and its next pointer is the merge
    of the remaining lists. This mirrors the sorted-list recurrence directly,
    though recursion uses stack space.

Recurrence:
    If either list is empty, the answer is the other list.

    Otherwise:

    - if `list1.val <= list2.val`, keep `list1` as the current head and set:

          list1.next = merge(list1.next, list2)

    - otherwise, keep `list2` as the current head and set:

          list2.next = merge(list1, list2.next)

Step-by-step:
    For:

        list1 = 1 -> 2 -> 4
        list2 = 1 -> 3 -> 4

    The first call compares the two heads. Since `list1.val <= list2.val`, the
    first `list1` node becomes the merged head. Its `.next` should be the merge
    of:

        2 -> 4
        1 -> 3 -> 4

    Each recursive call makes the same smaller-head decision until one list is
    empty. Then the remaining sorted suffix is returned as-is.

Why the links work:
    Each recursive frame returns the head of a fully merged suffix. Assigning
    that return value to the chosen node's `.next` connects the chosen node to
    the correct rest of the answer.

Complexity:
    Time:
        O(n + m)

    Space:
        O(n + m) recursion stack

When to choose this variant:
    Use it when the interviewer asks for recursion or when explaining the
    recurrence helps. For production-style Python, prefer the iterative
    dummy-tail variant to avoid O(n + m) stack space.
"""

from typing import Optional

from common.lc_types import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
