# 110. Balanced Binary Tree

Problem: https://leetcode.com/problems/balanced-binary-tree/

## Study Lists

- NeetCode 150; order 48; section: Trees

## Problem Description

Given a binary tree, determine if it is height-balanced.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| root | TreeNode |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
root = [3,9,20,null,null,15,7]
```

Output:

```text
true
```

### Example 2

Input:

```text
root = [1,2,2,3,3,null,null,4,4]
```

Output:

```text
false
```

### Example 3

Input:

```text
root = []
```

Output:

```text
true
```

## Constraints

- The number of nodes in the tree is in the range [0, 5000].
- -10^4 <= Node.val <= 10^4
