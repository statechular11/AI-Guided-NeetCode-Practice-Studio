# 152. Maximum Product Subarray

Problem: https://leetcode.com/problems/maximum-product-subarray/

## Study Lists

- NeetCode 150; order 107; section: 1-D Dynamic Programming

## Problem Description

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

## Signature

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
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
nums = [2,3,-2,4]
```

Output:

```text
6
```

Explanation:

[2,3] has the largest product 6.

### Example 2

Input:

```text
nums = [-2,0,-1]
```

Output:

```text
0
```

Explanation:

The result cannot be 2, because [-2,-1] is not a subarray.

## Constraints

- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
