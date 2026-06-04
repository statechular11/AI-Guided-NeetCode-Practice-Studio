# 121. Best Time to Buy and Sell Stock

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Study Lists

- LeetCode Top Interview 150; order 7; section: Array / String
- NeetCode 150; order 15; section: Sliding Window

## Problem Description

You are given an array prices where prices[i] is the price of a given stock on the i^th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Signature

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| prices | integer[] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
prices = [7,1,5,3,6,4]
```

Output:

```text
5
```

Explanation:

Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

## Constraints

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
