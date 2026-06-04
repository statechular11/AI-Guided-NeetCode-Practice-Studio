"""
853. Car Fleet - Arrival Times From Front To Back

Variant role:
    primary solution. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Process cars from closest to target backward. A car with an arrival time less than or equal to the fleet ahead merges into it. The crucial simplification is to stop simulating positions over time. Once cars are sorted by starting position from closest to target to farthest, each farther car only needs its arrival time compared with the fleet directly ahead. If the farther car arrives earlier than or at the same time as the fleet ahead, it catches that fleet before or exactly at target. If it arrives later, it can never catch the fleet ahead and must start a new fleet.

    This specific variant uses: arrival times from front to back.

Key invariant:
    The stack stores unresolved items in the order needed to resolve the next closing, warmer, smaller, or structurally related event.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"target": 12, "position": [10, 8, 0, 5, 3], "speed": [2, 4, 1, 1, 3]}` and the expected result is `3`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Sort by position, not by speed or arrival time alone. Road order determines which cars can catch which fleets. Process from closest to target to farthest. Reversing that mental direction is the most common source of wrong merges. Use a strict `>` check for new fleets. Equal arrival time means the car catches the fleet exactly at target and should merge. The stack, if used, stores fleet arrival times rather than raw cars.

Complexity:
    Time: O(n log n); Space: O(n)

When to choose this variant:
    Use this variant when its role matches the interview goal: primary solution. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    853. Car Fleet - compact arrival-time scan. Return the number of fleets that eventually reach target. Core idea: Sort cars by position from closest to target to farthest. Once cars are in that order, a farther car only needs to compare itself with the fleet directly ahead. If it would arrive earlier than or at the same time as that fleet, it catches the fleet and merges into it. If it would arrive later, it can never catch the fleet ahead, so it starts a new fleet. Arrival time: time = (target - position) / speed Why scanning from front to back works: A car cannot pass the car or fleet ahead of it. Therefore, after sorting by decreasing position, the only state we need is the latest arrival time among fleets already seen. That latest arrival time acts like a barrier: - current_time <= latest_fleet_time: current car catches that fleet - current_time > latest_fleet_time: current car bec...
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest_arrival_ahead = 0.0

        for pos, spd in cars:
            arrival = (target - pos) / spd
            if arrival > slowest_arrival_ahead:
                fleets += 1
                slowest_arrival_ahead = arrival

        return fleets
