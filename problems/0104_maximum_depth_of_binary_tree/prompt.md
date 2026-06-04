# 104. Maximum Depth of Binary Tree

Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Study Lists

- LeetCode Top Interview 150; order 68; section: Binary Tree General
- NeetCode 150; order 46; section: Trees

## Problem Description

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| root | TreeNode |

Return type: `integer`

## Examples

### Example 1

Input:

```text
root = [3,9,20,null,null,15,7]
```

Output:

```text
3
```

### Example 2

Input:

```text
root = [1,null,2]
```

Output:

```text
2
```

## Constraints

- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
