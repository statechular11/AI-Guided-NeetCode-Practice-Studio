# 25. Reverse Nodes in k-Group

Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/

## Study Lists

- LeetCode Top Interview 150; order 62; section: Linked List
- NeetCode 150; order 44; section: Linked List

## Problem Description

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Signature

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| head | ListNode |
| k | integer |

Return type: `ListNode`

## Examples

### Example 1

Input:

```text
head = [1,2,3,4,5], k = 2
```

Output:

```text
[2,1,4,3,5]
```

### Example 2

Input:

```text
head = [1,2,3,4,5], k = 3
```

Output:

```text
[3,2,1,4,5]
```

## Constraints

- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

## Follow-up

Can you solve the problem in O(1) extra memory space?
