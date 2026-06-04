# 704. Binary Search

Problem: https://leetcode.com/problems/binary-search/

## Study Lists

- NeetCode 150; order 27; section: Binary Search

## Problem Description

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

## Signature

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
nums = [-1,0,3,5,9,12], target = 9
```

Output:

```text
4
```

Explanation:

9 exists in nums and its index is 4

### Example 2

Input:

```text
nums = [-1,0,3,5,9,12], target = 2
```

Output:

```text
-1
```

Explanation:

2 does not exist in nums so return -1

## Constraints

- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.
