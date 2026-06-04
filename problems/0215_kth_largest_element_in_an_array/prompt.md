# 215. Kth Largest Element in an Array

Problem: https://leetcode.com/problems/kth-largest-element-in-an-array/

## Study Lists

- LeetCode Top Interview 150; order 121; section: Heap
- NeetCode 150; order 63; section: Heap / Priority Queue

## Problem Description

Given an integer array nums and an integer k, return the k^th largest element in the array.

Note that it is the k^th largest element in the sorted order, not the k^th distinct element.

Can you solve it without sorting?

## Signature

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |
| k | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
nums = [3,2,1,5,6,4], k = 2
```

Output:

```text
5
```

### Example 2

Input:

```text
nums = [3,2,3,1,2,4,5,5,6], k = 4
```

Output:

```text
4
```

## Constraints

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
