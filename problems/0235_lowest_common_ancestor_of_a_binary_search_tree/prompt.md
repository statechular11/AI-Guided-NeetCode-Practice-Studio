# 235. Lowest Common Ancestor of a Binary Search Tree

Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

## Study Lists

- NeetCode 150; order 51; section: Trees

## Problem Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| root | TreeNode |
| p | integer |
| q | integer |

Return type: `TreeNode`

## Examples

### Example 1

Input:

```text
root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
```

Output:

```text
6
```

Explanation:

The LCA of nodes 2 and 8 is 6.

### Example 2

Input:

```text
root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
```

Output:

```text
2
```

Explanation:

The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

### Example 3

Input:

```text
root = [2,1], p = 2, q = 1
```

Output:

```text
2
```

## Constraints

- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.
