# 309. Best Time to Buy and Sell Stock with Cooldown

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

## Study Lists

- NeetCode 150; order 113; section: 2-D Dynamic Programming

## Problem Description

You are given an array prices where prices[i] is the price of a given stock on the i^th day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

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
prices = [1,2,3,0,2]
```

Output:

```text
3
```

Explanation:

transactions = [buy, sell, cooldown, buy, sell]

### Example 2

Input:

```text
prices = [1]
```

Output:

```text
0
```

## Constraints

- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000
