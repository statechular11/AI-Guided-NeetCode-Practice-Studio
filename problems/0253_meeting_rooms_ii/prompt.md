# 253. Meeting Rooms II

Problem: https://neetcode.io/problems/meeting-schedule-ii/question
LeetCode: https://leetcode.com/problems/meeting-rooms-ii/

## Study Lists

- NeetCode 150; order 134; section: Intervals

## Problem Description

Statement source: NeetCode question page. The matching LeetCode page is Premium-only according to available metadata.

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

## Signature

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| intervals | integer[][] |

Return type: `integer`

## Examples

### Example 1

Input:

```text
intervals = [(0,40),(5,10),(15,20)]
```

Output:

```text
2
```

Explanation:

```text
room1: (0,40)
room2: (5,10),(15,20)
```

### Example 2

Input:

```text
intervals = [(4,9)]
```

Output:

```text
1
```

## Constraints

- 0 <= intervals.length <= 500
- 0 <= intervals[i].start < intervals[i].end <= 1,000,000
