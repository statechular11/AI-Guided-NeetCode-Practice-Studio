# 261. Graph Valid Tree

Problem: https://neetcode.io/problems/valid-tree/question
LeetCode: https://leetcode.com/problems/graph-valid-tree/

## Study Lists

- NeetCode 150; order 89; section: Graphs

## Problem Description

Statement source: NeetCode question page. The matching LeetCode page is Premium-only according to available metadata.

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

## Signature

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| n | integer |
| edges | integer[][] |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
```

Output:

```text
true
```

### Example 2

Input:

```text
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
```

Output:

```text
false
```

## Constraints

- 1 <= n <= 100
- 0 <= edges.length <= n * (n - 1) / 2
