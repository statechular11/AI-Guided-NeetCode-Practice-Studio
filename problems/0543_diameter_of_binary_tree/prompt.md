# 543. Diameter of Binary Tree

Problem: https://leetcode.com/problems/diameter-of-binary-tree/

## Study Lists

- NeetCode 150; order 47; section: Trees

## Problem Description

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
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
root = [1,2,3,4,5]
```

Output:

```text
3
```

Explanation:

3 is the length of the path [4,2,1,3] or [5,2,1,3].

### Example 2

Input:

```text
root = [1,2]
```

Output:

```text
1
```

## Constraints

- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100
