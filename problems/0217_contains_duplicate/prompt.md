# 217. Contains Duplicate

Problem: https://leetcode.com/problems/contains-duplicate/

## Study Lists

- NeetCode 150; order 1; section: Arrays & Hashing

## Problem Description

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Signature

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
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
nums = [1,2,3,1]
```

Output:

```text
true
```

Explanation:

The element 1 occurs at the indices 0 and 3.

### Example 2

Input:

```text
nums = [1,2,3,4]
```

Output:

```text
false
```

Explanation:

All elements are distinct.

### Example 3

Input:

```text
nums = [1,1,1,3,3,4,3,2,4,2]
```

Output:

```text
true
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
