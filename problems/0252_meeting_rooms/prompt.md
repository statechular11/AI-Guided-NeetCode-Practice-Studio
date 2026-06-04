# 252. Meeting Rooms

Problem: https://neetcode.io/problems/meeting-schedule/question
LeetCode: https://leetcode.com/problems/meeting-rooms/

## Study Lists

- NeetCode 150; order 133; section: Intervals

## Problem Description

Statement source: NeetCode question page. The matching LeetCode page is Premium-only according to available metadata.

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

## Signature

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        pass
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| intervals | integer[][] |

Return type: `boolean`

## Examples

### Example 1

Input:

```text
intervals = [(0,30),(5,10),(15,20)]
```

Output:

```text
false
```

Explanation:

```text
- (0,30) and (5,10) will conflict
- (0,30) and (15,20) will conflict
```

### Example 2

Input:

```text
intervals = [(5,8),(9,15)]
```

Output:

```text
true
```

## Constraints

- 0 <= intervals.length <= 500
- 0 <= intervals[i].start < intervals[i].end <= 1,000,000
