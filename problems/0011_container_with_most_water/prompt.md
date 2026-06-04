# 11. Container With Most Water

Problem: https://leetcode.com/problems/container-with-most-water/

## Study Lists

- LeetCode Top Interview 150; order 28; section: Two Pointers
- NeetCode 150; order 13; section: Two Pointers

## Problem Description

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i^th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

## Signature

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
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
height = [1,8,6,2,5,4,8,3,7]
```

Output:

```text
49
```

Explanation:

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

### Example 2

Input:

```text
height = [1,1]
```

Output:

```text
1
```

## Constraints

- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
