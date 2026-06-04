# 2. Add Two Numbers

Problem: https://leetcode.com/problems/add-two-numbers/

## Study Lists

- LeetCode Top Interview 150; order 58; section: Linked List
- NeetCode 150; order 40; section: Linked List

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

## Signature

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| l1 | ListNode |
| l2 | ListNode |

Return type: `ListNode`

## Examples

### Example 1

Input:

```text
l1 = [2,4,3], l2 = [5,6,4]
```

Output:

```text
[7,0,8]
```

Explanation:

342 + 465 = 807.

### Example 2

Input:

```text
l1 = [0], l2 = [0]
```

Output:

```text
[0]
```

### Example 3

Input:

```text
l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
```

Output:

```text
[8,9,9,9,0,0,0,1]
```

## Constraints

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
