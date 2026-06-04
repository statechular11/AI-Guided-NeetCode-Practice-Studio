# 53. Maximum Subarray

Problem: https://leetcode.com/problems/maximum-subarray/

## Study Lists

- LeetCode Top Interview 150; order 112; section: Kadane's Algorithm
- NeetCode 150; order 122; section: Greedy

## Problem Description

Given an integer array nums, find the subarray with the largest sum, and return its sum.

## Signature

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

Output:

```text
6
```

Explanation:

The subarray [4,-1,2,1] has the largest sum 6.

### Example 2

Input:

```text
nums = [1]
```

Output:

```text
1
```

Explanation:

The subarray [1] has the largest sum 1.

### Example 3

Input:

```text
nums = [5,4,-1,7,8]
```

Output:

```text
23
```

Explanation:

The subarray [5,4,-1,7,8] has the largest sum 23.

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Follow-up

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
