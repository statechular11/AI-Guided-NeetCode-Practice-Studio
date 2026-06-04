# 56. Merge Intervals

Problem: https://leetcode.com/problems/merge-intervals/

## Study Lists

- LeetCode Top Interview 150; order 49; section: Intervals
- NeetCode 150; order 131; section: Intervals

## Problem Description

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Signature

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| intervals | integer[][] |

Return type: `integer[][]`

## Examples

### Example 1

Input:

```text
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

Output:

```text
[[1,6],[8,10],[15,18]]
```

Explanation:

Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

### Example 2

Input:

```text
intervals = [[1,4],[4,5]]
```

Output:

```text
[[1,5]]
```

Explanation:

Intervals [1,4] and [4,5] are considered overlapping.

### Example 3

Input:

```text
intervals = [[4,7],[1,4]]
```

Output:

```text
[[1,7]]
```

Explanation:

Intervals [1,4] and [4,7] are considered overlapping.

## Constraints

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4
