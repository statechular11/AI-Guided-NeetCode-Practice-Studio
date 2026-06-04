# 332. Reconstruct Itinerary

Problem: https://leetcode.com/problems/reconstruct-itinerary/

## Study Lists

- NeetCode 150; order 94; section: Advanced Graphs

## Problem Description

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

## Signature

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| tickets | list<list<string>> |

Return type: `list<string>`

## Examples

### Example 1

Input:

```text
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
```

Output:

```text
["JFK","MUC","LHR","SFO","SJC"]
```

### Example 2

Input:

```text
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
```

Output:

```text
["JFK","ATL","JFK","SFO","ATL","SFO"]
```

Explanation:

Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

## Constraints

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- fromi.length == 3
- toi.length == 3
- fromi and toi consist of uppercase English letters.
- fromi != toi
