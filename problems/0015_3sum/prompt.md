# 15. 3Sum

Problem: https://leetcode.com/problems/3sum/

## Study Lists

- LeetCode Top Interview 150; order 29; section: Two Pointers
- NeetCode 150; order 12; section: Two Pointers

## Problem Description

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Signature

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |

Return type: `list<list<integer>>`

## Examples

### Example 1

Input:

```text
nums = [-1,0,1,2,-1,-4]
```

Output:

```text
[[-1,-1,2],[-1,0,1]]
```

Explanation:

```text
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

### Example 2

Input:

```text
nums = [0,1,1]
```

Output:

```text
[]
```

Explanation:

The only possible triplet does not sum up to 0.

### Example 3

Input:

```text
nums = [0,0,0]
```

Output:

```text
[[0,0,0]]
```

Explanation:

The only possible triplet sums up to 0.

## Constraints

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
