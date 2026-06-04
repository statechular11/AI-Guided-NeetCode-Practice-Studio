# 54. Spiral Matrix

Problem: https://leetcode.com/problems/spiral-matrix/

## Study Lists

- LeetCode Top Interview 150; order 35; section: Matrix
- NeetCode 150; order 137; section: Math & Geometry

## Problem Description

Given an m x n matrix, return all elements of the matrix in spiral order.

## Signature

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| matrix | integer[][] |

Return type: `list<integer>`

## Examples

### Example 1

Input:

```text
matrix = [[1,2,3],[4,5,6],[7,8,9]]
```

Output:

```text
[1,2,3,6,9,8,7,4,5]
```

### Example 2

Input:

```text
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
```

Output:

```text
[1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
