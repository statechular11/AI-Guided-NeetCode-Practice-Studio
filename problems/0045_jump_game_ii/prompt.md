# 45. Jump Game II

Problem: https://leetcode.com/problems/jump-game-ii/

## Study Lists

- LeetCode Top Interview 150; order 10; section: Array / String
- NeetCode 150; order 124; section: Greedy

## Problem Description

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

## Signature

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
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
nums = [2,3,1,1,4]
```

Output:

```text
2
```

Explanation:

The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

### Example 2

Input:

```text
nums = [2,3,0,1,4]
```

Output:

```text
2
```

## Constraints

- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1].
