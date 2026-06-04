# 200. Number of Islands

Problem: https://leetcode.com/problems/number-of-islands/

## Study Lists

- LeetCode Top Interview 150; order 89; section: Graph General
- NeetCode 150; order 80; section: Graphs

## Problem Description

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Signature

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| grid | character[][] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```

Output:

```text
1
```

### Example 2

Input:

```text
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

Output:

```text
3
```

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
