"""
21. Merge Two Sorted Lists - Iterative Dummy-Tail Reference

Merge two sorted linked lists by rewiring existing nodes.

Variant role:
    Primary interview solution.

Core idea:
    Keep a tail pointer for the merged list. At each step, attach the smaller
    current node and advance that input list. The dummy node avoids
    special-casing the first attached node.

Pointer invariant:
    Before each loop iteration:

    - `dummy.next` is the head of the merged prefix.
    - `tail` is the last node in that merged prefix.
    - `list1` and `list2` point to the first unmerged nodes in their original
      lists.

Why this pointer movement is safe:
    Suppose `list1` points to:

        A -> B -> C

    When we do:

        tail.next = list1
        list1 = list1.next

    `tail.next` stores a reference to node A. Reassigning the local variable
    `list1` to B does not change `tail.next`; it only records that B is now the
    next unmerged node from the first list.

    Later, after `tail = tail.next`, `tail` also points to A. If the next chosen
    node comes from `list2`, assigning `tail.next = list2` may overwrite A.next.
    That is still safe because `list1` already preserved B before the overwrite.

Step-by-step:
    For:

        list1 = 1 -> 2 -> 4
        list2 = 1 -> 3 -> 4

    A dummy node starts before the answer:

        dummy -> None
        tail = dummy

    Choose the smaller current node each time:

        dummy -> 1(list1)
        dummy -> 1(list1) -> 1(list2)
        dummy -> 1 -> 1 -> 2
        dummy -> 1 -> 1 -> 2 -> 3

    When one list is empty, the other remaining suffix is already sorted, so one
    final assignment attaches it:

        tail.next = list1 or list2

Complexity:
    Time:
        O(n + m)

    Space:
        O(1) extra; output reuses existing nodes.

When to choose this variant:
    Use this in interviews. It is iterative, stable for Python, avoids head
    special cases with the dummy node, and uses O(1) extra space.
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
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next
