# 21. Merge Two Sorted Lists

Problem: https://leetcode.com/problems/merge-two-sorted-lists/

## Study Lists

- LeetCode Top Interview 150; order 59; section: Linked List
- NeetCode 150; order 35; section: Linked List

## Problem Description

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Signature

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| list1 | ListNode |
| list2 | ListNode |

Return type: `ListNode`

## Examples

### Example 1

Input:

```text
list1 = [1,2,4], list2 = [1,3,4]
```

Output:

```text
[1,1,2,3,4,4]
```

### Example 2

Input:

```text
list1 = [], list2 = []
```

Output:

```text
[]
```

### Example 3

Input:

```text
list1 = [], list2 = [0]
```

Output:

```text
[0]
```

## Constraints

- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
