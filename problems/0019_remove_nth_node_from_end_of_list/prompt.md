# 19. Remove Nth Node From End of List

Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Study Lists

- LeetCode Top Interview 150; order 63; section: Linked List
- NeetCode 150; order 38; section: Linked List

## Problem Description

Given the head of a linked list, remove the n^th node from the end of the list and return its head.

## Signature

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| head | ListNode |
| n | integer |

Return type: `ListNode`

## Examples

### Example 1

Input:

```text
head = [1,2,3,4,5], n = 2
```

Output:

```text
[1,2,3,5]
```

### Example 2

Input:

```text
head = [1], n = 1
```

Output:

```text
[]
```

### Example 3

Input:

```text
head = [1,2], n = 1
```

Output:

```text
[1]
```

## Constraints

- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## Follow-up

Could you do this in one pass?
