# 62. Unique Paths

Problem: https://leetcode.com/problems/unique-paths/

## Study Lists

- NeetCode 150; order 111; section: 2-D Dynamic Programming

## Problem Description

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

## Signature

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| m | integer |
| n | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
m = 3, n = 7
```

Output:

```text
28
```

### Example 2

Input:

```text
m = 3, n = 2
```

Output:

```text
3
```

Explanation:

```text
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

## Constraints

- 1 <= m, n <= 100
