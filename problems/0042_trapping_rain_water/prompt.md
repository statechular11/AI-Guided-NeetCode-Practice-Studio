# 42. Trapping Rain Water

Problem: https://leetcode.com/problems/trapping-rain-water/

## Study Lists

- LeetCode Top Interview 150; order 16; section: Array / String
- NeetCode 150; order 14; section: Two Pointers

## Problem Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Signature

```python
class Solution:
    def trap(self, height: List[int]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| height | integer[] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Output:

```text
6
```

Explanation:

The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

### Example 2

Input:

```text
height = [4,2,0,3,2,5]
```

Output:

```text
9
```

## Constraints

- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
