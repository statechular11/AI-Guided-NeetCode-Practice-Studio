# 238. Product of Array Except Self

Problem: https://leetcode.com/problems/product-of-array-except-self/

## Study Lists

- LeetCode Top Interview 150; order 13; section: Array / String
- NeetCode 150; order 7; section: Arrays & Hashing

## Problem Description

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Signature

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |

Return type: `integer[]`

## Examples

### Example 1

Input:

```text
nums = [1,2,3,4]
```

Output:

```text
[24,12,8,6]
```

### Example 2

Input:

```text
nums = [-1,1,0,-3,3]
```

Output:

```text
[0,0,9,0,0]
```

## Constraints

- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

## Follow-up

Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
