# 23. Merge k Sorted Lists

Problem: https://leetcode.com/problems/merge-k-sorted-lists/

## Study Lists

- LeetCode Top Interview 150; order 111; section: Divide & Conquer
- NeetCode 150; order 43; section: Linked List

## Problem Description

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Signature

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| lists | ListNode[] |

Return type: `ListNode`

## Examples

### Example 1

Input:

```text
lists = [[1,4,5],[1,3,4],[2,6]]
```

Output:

```text
[1,1,2,3,4,4,5,6]
```

Explanation:

```text
The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```

### Example 2

Input:

```text
lists = []
```

Output:

```text
[]
```

### Example 3

Input:

```text
lists = [[]]
```

Output:

```text
[]
```

## Constraints

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
