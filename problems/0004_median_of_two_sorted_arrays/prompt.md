# 4. Median of Two Sorted Arrays

Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/

## Study Lists

- LeetCode Top Interview 150; order 120; section: Binary Search
- NeetCode 150; order 33; section: Binary Search

## Problem Description

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

## Signature

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums1 | integer[] |
| nums2 | integer[] |

Return type: `double`

## Examples

### Example 1

Input:

```text
nums1 = [1,3], nums2 = [2]
```

Output:

```text
2.00000
```

Explanation:

merged array = [1,2,3] and median is 2.

### Example 2

Input:

```text
nums1 = [1,2], nums2 = [3,4]
```

Output:

```text
2.50000
```

Explanation:

merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

## Constraints

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
