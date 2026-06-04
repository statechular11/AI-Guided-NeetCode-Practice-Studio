# 300. Longest Increasing Subsequence

Problem: https://leetcode.com/problems/longest-increasing-subsequence/

## Study Lists

- LeetCode Top Interview 150; order 141; section: 1D DP
- NeetCode 150; order 109; section: 1-D Dynamic Programming

## Problem Description

Given an integer array nums, return the length of the longest strictly increasing subsequence.

## Signature

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
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
nums = [10,9,2,5,3,7,101,18]
```

Output:

```text
4
```

Explanation:

The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

### Example 2

Input:

```text
nums = [0,1,0,3,2,3]
```

Output:

```text
4
```

### Example 3

Input:

```text
nums = [7,7,7,7,7,7,7]
```

Output:

```text
1
```

## Constraints

- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

## Follow-up

Can you come up with an algorithm that runs in O(n log(n)) time complexity?
