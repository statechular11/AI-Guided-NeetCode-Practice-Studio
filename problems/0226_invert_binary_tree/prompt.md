# 226. Invert Binary Tree

Problem: https://leetcode.com/problems/invert-binary-tree/

## Study Lists

- LeetCode Top Interview 150; order 70; section: Binary Tree General
- NeetCode 150; order 45; section: Trees

## Problem Description

Given the root of a binary tree, invert the tree, and return its root.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| root | TreeNode |

Return type: `TreeNode`

## Examples

### Example 1

Input:

```text
root = [4,2,7,1,3,6,9]
```

Output:

```text
[4,7,2,9,6,3,1]
```

### Example 2

Input:

```text
root = [2,1,3]
```

Output:

```text
[2,3,1]
```

### Example 3

Input:

```text
root = []
```

Output:

```text
[]
```

## Constraints

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
