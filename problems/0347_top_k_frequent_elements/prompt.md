# 347. Top K Frequent Elements

Problem: https://leetcode.com/problems/top-k-frequent-elements/

## Study Lists

- NeetCode 150; order 5; section: Arrays & Hashing

## Problem Description

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Signature

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| nums | integer[] |
| k | integer |

Return type: `integer[]`

## Examples

### Example 1

Input:

```text
nums = [1,1,1,2,2,3], k = 2
```

Output:

```text
[1,2]
```

### Example 2

Input:

```text
nums = [1], k = 1
```

Output:

```text
[1]
```

### Example 3

Input:

```text
nums = [1,2,1,2,1,2,3,1,3,2], k = 2
```

Output:

```text
[1,2]
```

## Constraints

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

## Follow-up

Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
