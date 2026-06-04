"""
1. Two Sum - Brute Force Pair Scan

Variant role:
    learning baseline. This file is meant to be read as an educational reference, not just
    as accepted code.

Core idea:
    Use the target to turn a pair-search problem into a lookup problem: If `needed` has already appeared, the answer is the earlier index plus the current index.

    This specific variant uses: brute force pair scan.

Key invariant:
    The lookup/counting state contains exactly the facts needed from the portion of the input already processed, so later checks never rescan unnecessary earlier work.

Mechanics:
    1. Name the state carried through the loop or recursion.
    2. Update that state using the current input item or decision.
    3. Check the invariant before recording an answer.
    4. Return the value described by the problem's output contract.

Walkthrough:
    On the local case `example_1`, the input is `{"nums": [2, 7, 11, 15], "target": 9}` and the expected result is `[0, 1]`. Trace how the reference's state changes until that expected result is forced.

Common pitfalls:
    Return indices, not values. Look up the complement before storing the current index so one element is not reused. Duplicates are valid when they occur at different indices, e.g. `[3, 3]`. The output order is not important for the local comparator, but returning earlier index first is conventional.

Complexity:
    Time: O(n^2); Space: O(1)

When to choose this variant:
    Use this variant when its role matches the interview goal: learning baseline. Be ready
    to explain both the state invariant and why the update step preserves it.

Existing reference note:
    1. Two Sum - brute force reference Variant role: Learning baseline. This is the simplest correct solution and is useful for clarifying the contract before optimizing. Core idea: Try every pair of indices `(i, j)` with `i < j`. If their values sum to the target, return those indices. Walkthrough: For nums = [2, 7, 11, 15] and target = 9: - Check 2 + 7. - It equals 9, so return [0, 1]. Interview note: This is usually too slow for the final answer, but it is a good first explanation because it makes the uniqueness and index-return requirements explicit. Complexity: Time: O(n^2) Space: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
