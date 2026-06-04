# 105. Construct Binary Tree from Preorder and Inorder Traversal

Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Study Lists

- LeetCode Top Interview 150; order 72; section: Binary Tree General
- NeetCode 150; order 57; section: Trees

## Problem Description

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| preorder | integer[] |
| inorder | integer[] |

Return type: `TreeNode`

## Examples

### Example 1

Input:

```text
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
```

Output:

```text
[3,9,20,null,null,15,7]
```

### Example 2

Input:

```text
preorder = [-1], inorder = [-1]
```

Output:

```text
[-1]
```

## Constraints

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.
