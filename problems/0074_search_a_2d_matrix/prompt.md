# 74. Search a 2D Matrix

Problem: https://leetcode.com/problems/search-a-2d-matrix/

## Study Lists

- LeetCode Top Interview 150; order 115; section: Binary Search
- NeetCode 150; order 28; section: Binary Search

## Problem Description

You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

## Signature

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| matrix | integer[][] |
| target | integer |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
```

Output:

```text
true
```

### Example 2

Input:

```text
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
```

Output:

```text
false
```

## Constraints

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4
