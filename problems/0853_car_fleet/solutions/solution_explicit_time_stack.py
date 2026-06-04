"""
853. Car Fleet - Explicit Arrival-Time Stack Reference

Return how many car fleets reach the target.

Variant role:
    Stack-shaped version of the standard arrival-time scan.

Core idea:
    Sort cars by position from closest to target to farthest. A car behind can
    only interact with the fleet directly ahead of it. If its arrival time is
    less than or equal to that fleet's time, it catches up and merges. If its
    arrival time is greater, it cannot catch up and starts a new fleet.

Stack meaning:
    The stack stores arrival times of fleets, ordered from closest fleet to
    farthest fleet among the cars processed so far.

Processing order:
    For each car after sorting by descending position:

    - compute its time to target,
    - if the stack is empty, this car starts the first fleet,
    - if its time is greater than the stack top, it cannot catch the fleet ahead
      and starts a new fleet,
    - otherwise, it merges into the stack-top fleet, so do not push anything.

Important equality case:
    If the current car reaches target at exactly the same time as the fleet
    ahead, it is still counted as part of that fleet. That is why the new-fleet
    condition is strictly:

        current_time > stack[-1]

Example:
    For:

        target = 10
        position = [6, 8]
        speed = [2, 1]

    arrival times after sorting by position descending:

        position 8 -> time 2
        position 6 -> time 2

    The second car catches the first exactly at target, so there is 1 fleet.

Complexity:
    Time:
        O(n log n), dominated by sorting.

    Space:
        O(n), for the sorted cars and stack.

When to choose this variant:
    Use this when you want the Stack tag to be explicit. The compact scan can
    store only the slowest fleet time so far, but the invariant is the same.
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_times: list[float] = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            arrival = (target - pos) / spd
            if not fleet_times or arrival > fleet_times[-1]:
                fleet_times.append(arrival)

        return len(fleet_times)
