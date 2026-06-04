# 136. Single Number

Problem: https://leetcode.com/problems/single-number/

## Study Lists

- LeetCode Top Interview 150; order 128; section: Bit Manipulation
- NeetCode 150; order 144; section: Bit Manipulation

## Problem Description

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Signature

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
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
nums = [2,2,1]
```

Output:

```text
1
```

### Example 2

Input:

```text
nums = [4,1,2,1,2]
```

Output:

```text
4
```

### Example 3

Input:

```text
nums = [1]
```

Output:

```text
1
```

## Constraints

- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element in the array appears twice except for one element which appears only once.
