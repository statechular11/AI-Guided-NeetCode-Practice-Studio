# 199. Binary Tree Right Side View

Problem: https://leetcode.com/problems/binary-tree-right-side-view/

## Study Lists

- LeetCode Top Interview 150; order 82; section: Binary Tree BFS
- NeetCode 150; order 53; section: Trees

## Problem Description

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| root | TreeNode |

Return type: `list<integer>`

## Examples

### Example 1

Input:

```text
root = [1,2,3,null,5,null,4]
```

Output:

```text
[1,3,4]
```

### Example 2

Input:

```text
root = [1,2,3,4,null,null,null,5]
```

Output:

```text
[1,3,4,5]
```

### Example 3

Input:

```text
root = [1,null,3]
```

Output:

```text
[1,3]
```

### Example 4

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
