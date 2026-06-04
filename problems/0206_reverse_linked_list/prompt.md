# 206. Reverse Linked List

Problem: https://leetcode.com/problems/reverse-linked-list/

## Study Lists

- NeetCode 150; order 34; section: Linked List

## Problem Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Signature

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| head | ListNode |

Return type: `ListNode`

## Examples

### Example 1

Input:

```text
head = [1,2,3,4,5]
```

Output:

```text
[5,4,3,2,1]
```

### Example 2

Input:

```text
head = [1,2]
```

Output:

```text
[2,1]
```

### Example 3

Input:

```text
head = []
```

Output:

```text
[]
```

## Constraints

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

## Follow-up

A linked list can be reversed either iteratively or recursively. Could you implement both?
