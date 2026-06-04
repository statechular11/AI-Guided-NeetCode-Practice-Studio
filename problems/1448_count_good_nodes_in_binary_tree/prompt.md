# 1448. Count Good Nodes in Binary Tree

Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

## Study Lists

- NeetCode 150; order 54; section: Trees

## Problem Description

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

## Signature

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
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
root = [3,1,4,3,null,1,5]
```

Output:

```text
4
```

Explanation:

```text
Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

### Example 2

Input:

```text
root = [3,3,null,4,2]
```

Output:

```text
3
```

Explanation:

Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

### Example 3

Input:

```text
root = [1]
```

Output:

```text
1
```

Explanation:

Root is considered as good.

## Constraints

- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].
