# 46. Permutations

Problem: https://leetcode.com/problems/permutations/

## Study Lists

- LeetCode Top Interview 150; order 103; section: Backtracking
- NeetCode 150; order 70; section: Backtracking

## Problem Description

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

## Signature

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2

Input:

```text
nums = [0,1]
```

Output:

```text
[[0,1],[1,0]]
```

### Example 3

Input:

```text
nums = [1]
```

Output:

```text
[[1]]
```

## Constraints

- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.
