"""
853. Car Fleet - Integer Cross Multiplication For Exact Arrival Comparison

Variant role:
    precision-aware alternative. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Process cars from closest to target backward. A car with an arrival time less than or equal to the fleet ahead merges into it. The crucial simplification is to stop simulating positions over time. Once cars are sorted by starting position from closest to target to farthest, each farther car only needs its arrival time compared with the fleet directly ahead. If the farther car arrives earlier than or at the same time as the fleet ahead, it catches that fleet before or exactly at target. If it arrives later, it can never catch the fleet ahead and must start a new fleet.

    This specific variant uses: integer cross multiplication for exact arrival comparison.

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
    Use this variant when its role matches the interview goal: precision-aware alternative. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    853. Car Fleet - exact arrival-time comparison without floats. The usual solution computes: arrival_time = (target - position) / speed Python floats are fine for the official constraints, but the comparison can also be done exactly with integer cross multiplication. Core comparison: For two arrival times: a = distance_a / speed_a b = distance_b / speed_b a > b is equivalent to: distance_a * speed_b > distance_b * speed_a because all speeds are positive. Algorithm: Sort cars from closest to target to farthest. Track the arrival time of the last fleet as a fraction `(fleet_distance, fleet_speed)`. For a new car: - if its exact arrival time is greater than the current fleet's arrival time, it cannot catch that fleet and starts a new fleet - otherwise, it merges into the fleet ahead and the tracked fleet arrival time stays unchanged When to use: In an interview, the float version is short...
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        fleet_distance = 0
        fleet_speed = 1

        for pos, spd in sorted(zip(position, speed), reverse=True):
            distance = target - pos

            starts_new_fleet = (
                fleets == 0
                or distance * fleet_speed > fleet_distance * spd
            )

            if starts_new_fleet:
                fleets += 1
                fleet_distance = distance
                fleet_speed = spd

        return fleets
