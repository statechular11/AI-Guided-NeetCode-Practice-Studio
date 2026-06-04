# 84. Largest Rectangle in Histogram

Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/

## Study Lists

- NeetCode 150; order 26; section: Stack

## Problem Description

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

## Signature

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| heights | integer[] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
heights = [2,1,5,6,2,3]
```

Output:

```text
10
```

Explanation:

```text
The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

### Example 2

Input:

```text
heights = [2,4]
```

Output:

```text
4
```

## Constraints

- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
