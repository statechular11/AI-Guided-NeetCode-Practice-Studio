# 51. N-Queens

Problem: https://leetcode.com/problems/n-queens/

## Study Lists

- NeetCode 150; order 76; section: Backtracking

## Problem Description

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

## Signature

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| n | integer |

Return type: `list<list<string>>`

## Examples

### Example 1

Input:

```text
n = 4
```

Output:

```text
[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

Explanation:

There exist two distinct solutions to the 4-queens puzzle as shown above

### Example 2

Input:

```text
n = 1
```

Output:

```text
[["Q"]]
```

## Constraints

- 1 <= n <= 9
