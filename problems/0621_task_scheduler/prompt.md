# 621. Task Scheduler

Problem: https://leetcode.com/problems/task-scheduler/

## Study Lists

- NeetCode 150; order 64; section: Heap / Priority Queue

## Problem Description

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

## Signature

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
```

## Input / Output Contract

| Parameter | Type |
| --- | --- |
| tasks | character[] |
| n | integer |

Return type: `integer`

## Examples

### Example 1

Input:

```text
tasks = ["A","A","A","B","B","B"], n = 2
```

Output:

```text
8
```

Explanation:

```text
A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3^rd interval, neither A nor B can be done, so you idle. By the 4^th interval, you can do A again as 2 intervals have passed.
```

### Example 2

Input:

```text
tasks = ["A","C","A","B","D","B"], n = 1
```

Output:

```text
6
```

Explanation:

```text
A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.
```

### Example 3

Input:

```text
tasks = ["A","A","A", "B","B","B"], n = 3
```

Output:

```text
10
```

Explanation:

```text
A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
```

## Constraints

- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter.
- 0 <= n <= 100
