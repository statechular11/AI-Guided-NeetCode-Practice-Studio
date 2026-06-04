# 329. Longest Increasing Path in a Matrix

Problem: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

## Study Lists

- NeetCode 150; order 117; section: 2-D Dynamic Programming

## Problem Description

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

## Signature

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| matrix | integer[][] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
matrix = [[9,9,4],[6,6,8],[2,1,1]]
```

Output:

```text
4
```

Explanation:

The longest increasing path is [1, 2, 6, 9].

### Example 2

Input:

```text
matrix = [[3,4,5],[3,2,6],[2,2,1]]
```

Output:

```text
4
```

Explanation:

The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

### Example 3

Input:

```text
matrix = [[1]]
```

Output:

```text
1
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2^31 - 1
