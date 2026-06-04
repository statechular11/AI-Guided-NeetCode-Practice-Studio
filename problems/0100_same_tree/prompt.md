# 100. Same Tree

Problem: https://leetcode.com/problems/same-tree/

## Study Lists

- LeetCode Top Interview 150; order 69; section: Binary Tree General
- NeetCode 150; order 49; section: Trees

## Problem Description

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| p | TreeNode |
| q | TreeNode |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
p = [1,2,3], q = [1,2,3]
```

Output:

```text
true
```

### Example 2

Input:

```text
p = [1,2], q = [1,null,2]
```

Output:

```text
false
```

### Example 3

Input:

```text
p = [1,2,1], q = [1,1,2]
```

Output:

```text
false
```

## Constraints

- The number of nodes in both trees is in the range [0, 100].
- -10^4 <= Node.val <= 10^4
