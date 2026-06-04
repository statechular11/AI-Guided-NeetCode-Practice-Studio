# 1. Two Sum

Problem: https://leetcode.com/problems/two-sum/

## Study Lists

- LeetCode Top Interview 150; order 44; section: Hashmap
- NeetCode 150; order 3; section: Arrays & Hashing

## Problem Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

## Signature

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |
| target | integer |

Return type: `integer[]`

## Examples

### Example 1

Input:

```text
nums = [2,7,11,15], target = 9
```

Output:

```text
[0,1]
```

Explanation:

Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2

Input:

```text
nums = [3,2,4], target = 6
```

Output:

```text
[1,2]
```

### Example 3

Input:

```text
nums = [3,3], target = 6
```

Output:

```text
[0,1]
```

## Constraints

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

## Follow-up

Can you come up with an algorithm that is less than O(n^2) time complexity?
