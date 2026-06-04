# 494. Target Sum

Problem: https://leetcode.com/problems/target-sum/

## Study Lists

- NeetCode 150; order 115; section: 2-D Dynamic Programming

## Problem Description

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

- For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

## Signature

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |
| target | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
nums = [1,1,1,1,1], target = 3
```

Output:

```text
5
```

Explanation:

```text
There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

### Example 2

Input:

```text
nums = [1], target = 1
```

Output:

```text
1
```

## Constraints

- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000
