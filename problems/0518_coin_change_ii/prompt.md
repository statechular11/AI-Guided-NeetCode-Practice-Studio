# 518. Coin Change II

Problem: https://leetcode.com/problems/coin-change-ii/

## Study Lists

- NeetCode 150; order 114; section: 2-D Dynamic Programming

## Problem Description

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

## Signature

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| amount | integer |
| coins | integer[] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
amount = 5, coins = [1,2,5]
```

Output:

```text
4
```

Explanation:

```text
there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

### Example 2

Input:

```text
amount = 3, coins = [2]
```

Output:

```text
0
```

Explanation:

the amount of 3 cannot be made up just with coins of 2.

### Example 3

Input:

```text
amount = 10, coins = [10]
```

Output:

```text
1
```

## Constraints

You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All the values of coins are unique.
- 0 <= amount <= 5000
