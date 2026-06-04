# 102. Binary Tree Level Order Traversal

Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

## Study Lists

- LeetCode Top Interview 150; order 84; section: Binary Tree BFS
- NeetCode 150; order 52; section: Trees

## Problem Description

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| root | TreeNode |

Return type: `list<list<integer>>`

## Examples

### Example 1

Input:

```text
root = [3,9,20,null,null,15,7]
```

Output:

```text
[[3],[9,20],[15,7]]
```

### Example 2

Input:

```text
root = [1]
```

Output:

```text
[[1]]
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

- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
