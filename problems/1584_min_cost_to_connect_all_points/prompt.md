# 1584. Min Cost to Connect All Points

Problem: https://leetcode.com/problems/min-cost-to-connect-all-points/

## Study Lists

- NeetCode 150; order 95; section: Advanced Graphs

## Problem Description

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

## Signature

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| points | integer[][] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
```

Output:

```text
20
```

Explanation:

```text
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

### Example 2

Input:

```text
points = [[3,12],[-2,5],[-4,1]]
```

Output:

```text
18
```

## Constraints

- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct.
