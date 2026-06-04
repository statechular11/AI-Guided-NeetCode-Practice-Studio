# 286. Walls and Gates

Problem: https://neetcode.io/problems/islands-and-treasure/question
LeetCode: https://leetcode.com/problems/walls-and-gates/

## Study Lists

- NeetCode 150; order 83; section: Graphs

## Problem Description

Statement source: NeetCode question page. The matching LeetCode page is Premium-only according to available metadata.

You are given a m x n 2D grid initialized with these three possible values:

- -1 - A water cell that can not be traversed.
- 0 - A treasure chest.
- INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

## Signature

```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        pass
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| rooms | integer[][] |

Return type: `void`

## Examples

### Example 1

Input:

```text
[
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
```

Output:

```text
[
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
```

### Example 2

Input:

```text
[
  [0,-1],
  [2147483647,2147483647]
]
```

Output:

```text
[
  [0,-1],
  [1,2]
]
```

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is one of {-1, 0, 2147483647}
