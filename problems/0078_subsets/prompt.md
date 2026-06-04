# 78. Subsets

Problem: https://leetcode.com/problems/subsets/

## Study Lists

- NeetCode 150; order 67; section: Backtracking

## Problem Description

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Signature

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
nums = [1,2,3]
```

Output:

```text
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
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
- All the numbers of nums are unique.
