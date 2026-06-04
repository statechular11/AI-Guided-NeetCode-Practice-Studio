# 416. Partition Equal Subset Sum

Problem: https://leetcode.com/problems/partition-equal-subset-sum/

## Study Lists

- NeetCode 150; order 110; section: 1-D Dynamic Programming

## Problem Description

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

## Signature

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
nums = [1,5,11,5]
```

Output:

```text
true
```

Explanation:

The array can be partitioned as [1, 5, 5] and [11].

### Example 2

Input:

```text
nums = [1,2,3,5]
```

Output:

```text
false
```

Explanation:

The array cannot be partitioned into equal sum subsets.

## Constraints

- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100
