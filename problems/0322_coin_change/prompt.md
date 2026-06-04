# 322. Coin Change

Problem: https://leetcode.com/problems/coin-change/

## Study Lists

- LeetCode Top Interview 150; order 140; section: 1D DP
- NeetCode 150; order 106; section: 1-D Dynamic Programming

## Problem Description

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

## Signature

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| coins | integer[] |
| amount | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
coins = [1,2,5], amount = 11
```

Output:

```text
3
```

Explanation:

11 = 5 + 5 + 1

### Example 2

Input:

```text
coins = [2], amount = 3
```

Output:

```text
-1
```

### Example 3

Input:

```text
coins = [1], amount = 0
```

Output:

```text
0
```

## Constraints

You may assume that you have an infinite number of each kind of coin.
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
