# 143. Reorder List

Problem: https://leetcode.com/problems/reorder-list/

## Study Lists

- NeetCode 150; order 37; section: Linked List

## Problem Description

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Signature

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| head | ListNode |

Return type: `void`

## Examples

### Example 1

Input:

```text
head = [1,2,3,4]
```

Output:

```text
[1,4,2,3]
```

### Example 2

Input:

```text
head = [1,2,3,4,5]
```

Output:

```text
[1,5,2,4,3]
```

## Constraints

- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000
