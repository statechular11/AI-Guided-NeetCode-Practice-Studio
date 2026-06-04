# 130. Surrounded Regions

Problem: https://leetcode.com/problems/surrounded-regions/

## Study Lists

- LeetCode Top Interview 150; order 90; section: Graph General
- NeetCode 150; order 86; section: Graphs

## Problem Description

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

- Connect: A cell is connected to adjacent cells horizontally or vertically.
- Region: To form a region connect every 'O' cell.
- Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

## Signature

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| board | character[][] |

Return type: `void`

## Examples

### Example 1

Input:

```text
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
```

Output:

```text
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
```

Explanation:

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

### Example 2

Input:

```text
board = [["X"]]
```

Output:

```text
[["X"]]
```

## Constraints

- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.
