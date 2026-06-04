# 787. Cheapest Flights Within K Stops

Problem: https://leetcode.com/problems/cheapest-flights-within-k-stops/

## Study Lists

- NeetCode 150; order 98; section: Advanced Graphs

## Problem Description

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

## Signature

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| n | integer |
| flights | integer[][] |
| src | integer |
| dst | integer |
| k | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
```

Output:

```text
700
```

Explanation:

```text
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
```

## Constraints

- 2 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 10^4
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst
