# 90. Subsets II

Problem: https://leetcode.com/problems/subsets-ii/

## Study Lists

- NeetCode 150; order 71; section: Backtracking

## Problem Description

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Signature

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
nums = [1,2,2]
```

Output:

```text
[[],[1],[1,2],[1,2,2],[2],[2,2]]
```

### Example 2

Input:

```text
nums = [0]
```

Output:

```text
[[],[0]]
```

## Constraints

- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
