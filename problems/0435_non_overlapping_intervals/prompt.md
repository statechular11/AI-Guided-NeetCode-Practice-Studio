# 435. Non-overlapping Intervals

Problem: https://leetcode.com/problems/non-overlapping-intervals/

## Study Lists

- NeetCode 150; order 132; section: Intervals

## Problem Description

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

## Signature

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| intervals | integer[][] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

Output:

```text
1
```

Explanation:

[1,3] can be removed and the rest of the intervals are non-overlapping.

### Example 2

Input:

```text
intervals = [[1,2],[1,2],[1,2]]
```

Output:

```text
2
```

Explanation:

You need to remove two [1,2] to make the rest of the intervals non-overlapping.

### Example 3

Input:

```text
intervals = [[1,2],[2,3]]
```

Output:

```text
0
```

Explanation:

You don't need to remove any of the intervals since they're already non-overlapping.

## Constraints

- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4
