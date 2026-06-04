# 239. Sliding Window Maximum

Problem: https://leetcode.com/problems/sliding-window-maximum/

## Study Lists

- NeetCode 150; order 20; section: Sliding Window

## Problem Description

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

## Signature

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |
| k | integer |

Return type: `integer[]`

## Examples

### Example 1

Input:

```text
nums = [1,3,-1,-3,5,3,6,7], k = 3
```

Output:

```text
[3,3,5,5,6,7]
```

Explanation:

```text
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### Example 2

Input:

```text
nums = [1], k = 1
```

Output:

```text
[1]
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
