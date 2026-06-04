# 98. Validate Binary Search Tree

Problem: https://leetcode.com/problems/validate-binary-search-tree/

## Study Lists

- LeetCode Top Interview 150; order 88; section: Binary Search Tree
- NeetCode 150; order 55; section: Trees

## Problem Description

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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
root = [2,1,3]
```

Output:

```text
true
```

### Example 2

Input:

```text
root = [5,1,4,null,null,3,6]
```

Output:

```text
false
```

Explanation:

The root node's value is 5 but its right child's value is 4.

## Constraints

- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
