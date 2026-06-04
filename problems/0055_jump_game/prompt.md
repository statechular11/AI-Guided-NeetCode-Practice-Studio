# 55. Jump Game

Problem: https://leetcode.com/problems/jump-game/

## Study Lists

- LeetCode Top Interview 150; order 9; section: Array / String
- NeetCode 150; order 123; section: Greedy

## Problem Description

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## Signature

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
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
nums = [2,3,1,1,4]
```

Output:

```text
true
```

Explanation:

Jump 1 step from index 0 to 1, then 3 steps to the last index.

### Example 2

Input:

```text
nums = [3,2,1,0,4]
```

Output:

```text
false
```

Explanation:

You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

## Constraints

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5
