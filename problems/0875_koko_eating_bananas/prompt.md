# 875. Koko Eating Bananas

Problem: https://leetcode.com/problems/koko-eating-bananas/

## Study Lists

- NeetCode 150; order 29; section: Binary Search

## Problem Description

Koko loves to eat bananas. There are n piles of bananas, the i^th pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

## Signature

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| piles | integer[] |
| h | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
piles = [3,6,7,11], h = 8
```

Output:

```text
4
```

### Example 2

Input:

```text
piles = [30,11,23,4,20], h = 5
```

Output:

```text
30
```

### Example 3

Input:

```text
piles = [30,11,23,4,20], h = 6
```

Output:

```text
23
```

## Constraints

- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
