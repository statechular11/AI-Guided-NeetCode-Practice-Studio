# Binary Search - A Complete Guide for Coding Interviews

## Table of Contents

- [1. What Is Binary Search?](#1-what-is-binary-search)
- [2. The Boundary Design Worksheet](#2-the-boundary-design-worksheet)
- [3. Pattern 1: Exact Search in a Sorted Array](#3-pattern-1-exact-search-in-a-sorted-array)
- [4. Pattern 2: First True / Lower Bound](#4-pattern-2-first-true--lower-bound)
- [5. Pattern 3: Last True / Floor Search](#5-pattern-3-last-true--floor-search)
- [6. Lower Bound, Upper Bound, Floor, and Ceiling](#6-lower-bound-upper-bound-floor-and-ceiling)
- [7. Answer-Space Binary Search](#7-answer-space-binary-search)
- [8. Rotated Arrays](#8-rotated-arrays)
- [9. Virtual Index Binary Search](#9-virtual-index-binary-search)
- [10. Peak and Neighbor-Based Binary Search](#10-peak-and-neighbor-based-binary-search)
- [11. Python Implementation Details](#11-python-implementation-details)
- [12. Correctness Invariants](#12-correctness-invariants)
- [13. Failure Modes and Edge Cases](#13-failure-modes-and-edge-cases)
  - [13.3 - Infinite-loop patterns and progress invariants](#133---infinite-loop-patterns-and-progress-invariants)
- [14. Tradeoffs and Neighboring Techniques](#14-tradeoffs-and-neighboring-techniques)
- [15. Practice Progression](#15-practice-progression)
- [16. Interview Explanation Templates](#16-interview-explanation-templates)
- [17. Mastery Checklist](#17-mastery-checklist)
- [18. Quick Reference](#18-quick-reference)

## 1. What Is Binary Search?

Binary search is a way to use one comparison to discard a whole region of
impossible answers.

The primitive move is:

```text
Probe the middle.
Use sorted order or a monotonic predicate to prove one side cannot contain the
answer.
Keep only the side that can still contain the answer.
```

That is all binary search is. The hard part is not computing `mid`; the hard
part is knowing exactly what your interval means and whether `mid` is still a
candidate after the comparison.

There are two broad families:

| Family | Search space | Example |
| --- | --- | --- |
| Exact search | sorted positions | Find target in sorted array |
| Boundary search | monotonic truth pattern | First feasible speed, last timestamp <= query |

Exact search asks:

```text
Is nums[mid] the target?
```

Boundary search asks:

```text
Where does a monotonic condition change?
```

The second family is where most interview bugs live. It includes lower bounds,
upper bounds, answer-space search, rotated-array pivots, and floor lookups.

### 1.1 - Why binary search is O(log n)

Each step keeps at most half of the remaining candidates.

```text
n -> n/2 -> n/4 -> n/8 -> ... -> 1
```

The number of halvings needed to reach one candidate is `log2(n)`, so the time
is `O(log n)` when each predicate check is O(1). If each check costs O(k), the
total time is `O(k log n)`.

Example: Koko Eating Bananas checks all piles for each candidate speed, so the
time is `O(n log max(piles))`.

### 1.2 - The central mental model

Before coding, answer this:

```text
What fact lets one midpoint decision discard many candidates?
```

Examples:

| Problem shape | Discarding fact |
| --- | --- |
| Sorted array exact search | If `nums[mid] < target`, everything left of `mid` is too small |
| First true predicate | If `condition(mid)` is true, the first true is at `mid` or left |
| Last true predicate | If `condition(mid)` is true, the last true is at `mid` or right |
| Rotated minimum | If `nums[mid] > nums[right]`, the pivot is right of `mid` |
| TimeMap floor lookup | If `time[mid] <= query`, this value works but a later one may work too |
| Koko speed | If speed works, every larger speed also works |

The code should follow that fact directly.


---

## 2. The Boundary Design Worksheet

Use this worksheet before writing any binary search.

| Question | What to decide |
| --- | --- |
| What is the search space? | array indices, virtual indices, answer values, timestamps |
| Is it sorted or monotonic? | exact order, `F...T`, `T...F`, rotated structure |
| What does `left` mean? | first live candidate, first possible boundary, lower answer bound |
| What does `right` mean? | last live candidate or one-past-the-end |
| Is the interval closed or half-open? | `[left, right]` or `[left, right)` |
| Is `mid` still a candidate after the check? | keep it, discard it, or store it as best-so-far |
| What is returned? | index, value, boolean, insertion point, stored answer |
| How do updates guarantee progress? | use `mid +/- 1`, or use midpoint bias when keeping `mid` |

This worksheet matters because binary search has several correct templates.
Most bugs come from combining pieces from different templates.

### 2.1 - Template selection table

After writing the truth pattern, choose the template.

| Desired result | Truth shape | Natural template |
| --- | --- | --- |
| exact target index | equality check | closed exact search |
| first value satisfying condition | `F...T` | first-true / lower-bound |
| last value satisfying condition | `T...F` | explicit answer or upper-mid last-true |
| minimum feasible answer | `F...T` over answer values | first feasible |
| maximum feasible answer | `T...F` over answer values | last feasible |
| floor `<= x` in ascending data | `T...F` for `value <= x` | last true |
| ceiling `>= x` in ascending data | `F...T` for `value >= x` | first true |

If no valid answer may exist, prefer an explicit answer variable or a half-open
boundary with a final guard. Templates that return `left` directly need a valid
sentinel or a final verification step.

### 2.2 - Two interval conventions

Closed interval:

```text
[left, right]
left and right are both live candidates.
Loop while left <= right for exact search, or left < right for single-candidate
boundary narrowing.
```

Half-open interval:

```text
[left, right)
left is live, right is one past the last live index.
Loop while left < right.
```

Both are good. Pick one deliberately.

### 2.3 - Progress rule

Important:

```text
Every iteration must shrink the interval.
```

Safe ways to shrink:

```python
left = mid + 1
right = mid - 1

# ------------------------------------------------------------
# Keep mid only when midpoint bias still shrinks the interval.
# ------------------------------------------------------------
right = mid       # lower-mid; mid < old right when left < right
left = mid        # upper-mid; mid > old left when left < right
```

Midpoint bias means which side the midpoint formula chooses when there is no
single exact middle. When two candidates remain, lower-mid chooses the left
candidate and upper-mid chooses the right candidate.

Lower-mid:

```python
mid = left + (right - left) // 2
```

Upper-mid:

```python
mid = left + (right - left + 1) // 2
```

The bias matters when an update keeps `mid` as a possible answer. If you use
lower-mid and assign `left = mid`, two candidates can remain stuck because
`mid == left`. If you use upper-mid and assign `right = mid`, two candidates can
remain stuck because `mid == right`.

This is why first-true templates use lower-mid with `right = mid`, while
last-true templates use upper-mid with `left = mid`.

The deeper rule is covered in [13.3 - Infinite-loop patterns and progress
invariants](#133---infinite-loop-patterns-and-progress-invariants): every branch
must either terminate the search or make the live interval strictly smaller.


---

## 3. Pattern 1: Exact Search in a Sorted Array

Use exact search when the problem asks:

```text
Return the index of target if it exists, otherwise return -1.
```

Example: Binary Search.

### 3.1 - State and invariant

Use a closed interval.

```text
Invariant:
If target exists, its index is inside [left, right].
```

When `nums[mid] == target`, return immediately. Otherwise `mid` is ruled out, so
discard it with `mid + 1` or `mid - 1`.

### 3.2 - Template

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### 3.3 - Trace

```text
nums = [-1, 0, 3, 5, 9, 12], target = 9

left = 0, right = 5, mid = 2, nums[mid] = 3
3 is too small, so discard indices 0..2.

left = 3, right = 5, mid = 4, nums[mid] = 9
Found target.
```

### 3.4 - Correctness sketch

At every step, sorted order proves the discarded half cannot contain target.
When equality happens, the returned index is correct. If the loop exits, the
candidate interval is empty, so target does not exist.

### 3.5 - Failure modes

- Using `while left < right` for exact search and forgetting to check the final
  candidate.
- Updating `left = mid` or `right = mid` after `mid` has been proven not equal.
- Returning `left` after the loop without verifying equality.
- Mixing a half-open `right = len(nums)` initialization with closed-interval
  updates.


---

## 4. Pattern 2: First True / Lower Bound

Many problems are not asking for exact equality. They ask for the first position
where a condition becomes true.

Truth shape:

```text
F F F F T T T
        ^
        first true
```

Examples:

- first index with `nums[i] >= target`
- first feasible speed
- first bad version
- minimum answer satisfying a constraint

### 4.1 - Why the common template works

The common closed single-candidate narrowing template is:

```python
low, high = 0, size - 1
while low < high:
    mid = low + (high - low) // 2
    if condition(nums[mid]):
        high = mid
    else:
        low = mid + 1
return low
```

It works for `F...T` because:

```text
If condition(mid) is true:
    mid may be the first true.
    Keep mid with high = mid.

If condition(mid) is false:
    mid and everything left of it are false.
    Discard mid with low = mid + 1.
```

The lower midpoint is safe because the branch that keeps `mid` moves `high`,
not `low`. When two candidates remain, `mid == low`:

- if `condition(mid)` is false, `low = mid + 1` moves to `high`
- if `condition(mid)` is true, `high = mid` moves to `low`

Either way, the interval shrinks.

Important guard:

```text
If the search space may contain no true value, returning `low` directly is not
enough.
```

Use one of these two designs.

#### Option 1: use a sentinel answer position

Make the upper boundary a position that means "no real index satisfies the
condition." For array lower bound, this is exactly the half-open
`right = len(nums)` template in
[4.2 - Lower-bound template with half-open interval](#42---lower-bound-template-with-half-open-interval).
Use this design when returning an insertion point is useful.

#### Option 2: verify the final index

If the caller wants a real matching index, keep the original index range and
verify the final candidate before returning it.

```python
def first_ge_or_minus_one(nums, target):
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] >= target:
            high = mid
        else:
            low = mid + 1

    return low if nums[low] >= target else -1
```

Example:

```text
nums = [1, 3, 5], target = 9

The loop narrows to index 2 because it is the last remaining candidate.
But nums[2] = 5 is not >= 9, so the final verification returns -1.
```

This design is best when "not found" should be explicit rather than encoded as
`len(nums)`.

The two designs answer different questions:

| Design | Return when no true exists | Best for |
| --- | --- | --- |
| sentinel boundary | `len(nums)` or another sentinel position | insertion points and lower bounds |
| final verification | `-1`, `None`, or another not-found value | real-index search results |

### 4.2 - Lower-bound template with half-open interval

For arrays, the half-open lower-bound template is often cleaner:

```python
def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left
```

This template uses `len(nums)` as a sentinel answer position. It is not a valid
array index, but it is a valid insertion position. Conceptually,
`condition(len(nums))` is true, even though the code never reads
`nums[len(nums)]`.

Return meaning:

```text
left = first index i where nums[i] >= target
left may equal len(nums) if no such index exists
```

Example:

```text
nums = [1, 3, 5], target = 9

Truth pattern over real indices:
    F F F

Search space with sentinel:
    F F F T
          ^
          index 3 = len(nums)

The function returns 3, meaning "no element is >= 9; insert at the end."
```

Why `nums[mid]` is still safe:

```text
With left < right and right = len(nums), lower-mid always gives
mid < len(nums). The sentinel can be returned, but it is never indexed.
```

Exact search from lower bound:

```python
i = lower_bound(nums, target)
if i < len(nums) and nums[i] == target:
    return i
return -1
```

### 4.3 - Answer-space first true

The same idea works when the search space is values, not indices.

Example: Koko Eating Bananas.

```python
def min_eating_speed(piles, h):
    def can_finish(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

Predicate shape:

```text
speed:      1  2  3  4  5  6  ...
can_finish: F  F  F  T  T  T
                     ^
                     minimum feasible speed
```

### 4.4 - Correctness sketch

The predicate is monotonic. False means the answer is strictly to the right.
True means `mid` may be the first true, so keep it. When one candidate remains,
it is the first true.

### 4.5 - Failure modes

- Returning a feasible answer before proving smaller answers fail.
- Forgetting that `left == len(nums)` is a possible lower-bound result.
- Using an invalid answer-space bound, such as speed 0 for division problems.
- Failing to prove monotonicity before applying binary search.


---

## 5. Pattern 3: Last True / Floor Search

The mirror image of first true is last true.

Truth shape:

```text
T T T T F F F
      ^
      last true
```

Examples:

- largest number `<= target`
- last timestamp `<= query`
- last position satisfying a capacity or distance rule
- upper bound minus one

TimeMap is a clean example:

```text
timestamps = [1, 4, 9], query = 5
predicate: timestamp <= 5
truth:     T  T  F
answer:       index 1, timestamp 4
```

### 5.1 - Template with explicit answer

This is the safest template for last true:

```python
def last_true(values, condition):
    left, right = 0, len(values) - 1
    answer = -1

    while left <= right:
        mid = left + (right - left) // 2
        if condition(values[mid]):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
```

Why store `answer`?

```text
When condition(mid) is true, mid is valid.
But it might not be the last valid index.
Store it, then search right.
```

### 5.2 - TimeMap floor lookup

```python
def get(self, key: str, timestamp: int) -> str:
    values = self.lookup_table.get(key, [])
    left, right = 0, len(values) - 1
    result = ""

    while left <= right:
        mid = left + (right - left) // 2
        event_time, value = values[mid]
        if event_time <= timestamp:
            result = value
            left = mid + 1
        else:
            right = mid - 1

    return result
```

Return meaning:

```text
result = value at the largest event_time <= query
result remains "" if no event_time is valid
```

### 5.3 - Why the first-true template is not enough

The first-true template:

```python
while low < high:
    mid = low + (high - low) // 2
    if condition(nums[mid]):
        high = mid
    else:
        low = mid + 1
return low
```

assumes truth looks like:

```text
F F F T T T
```

For floor search, truth looks like:

```text
T T T F F F
```

If you use the first-true update on a `T...F` predicate, you move in the wrong
direction. A true `mid` is not an instruction to go left; it is a candidate and
an instruction to see whether there is a later true value.

This is the exact reason TimeMap needs an answer variable in the most robust
version:

```text
query before first timestamp:
    truth pattern is F F F
    there is no true value to return

query inside timeline:
    truth pattern is T T F
    each true value is valid, but only the last true is best
```

`result = ""` handles the no-true case. Updating `result` on true handles the
candidate case. Moving `left = mid + 1` keeps searching for a better candidate
without risking a stuck loop.

### 5.4 - Alternative last-true template with upper midpoint

You can avoid an explicit answer if you maintain a non-empty interval that is
known to contain the last true, but the update must use upper-mid when keeping
`mid` on the left side.

```python
def last_true_index(nums, condition):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left + 1) // 2
        if condition(nums[mid]):
            left = mid
        else:
            right = mid - 1

    return left
```

This only works cleanly when you know at least one true exists or you add guards.
For TimeMap, the explicit-answer version is more robust because no timestamp may
be `<= query`.

One clean guard is the mirror image of the `len(nums)` sentinel from
[4.2 - Lower-bound template with half-open interval](#42---lower-bound-template-with-half-open-interval):
use `left = -1` as a conceptual true sentinel.

```python
def last_true_index_or_minus_one(nums, condition):
    left, right = -1, len(nums) - 1

    while left < right:
        mid = left + (right - left + 1) // 2
        if condition(nums[mid]):
            left = mid
        else:
            right = mid - 1

    return left
```

Conceptually, `condition(-1)` is true: it represents "no real index works yet."
The code never reads `nums[-1]`. With upper-mid and `left < right`, `mid` is
always greater than `left`, so when `left = -1`, the smallest possible `mid` is
`0`.

Example with no true real index:

```text
nums = [5, 7, 9], condition(x) = x <= 3

Real truth pattern:
    F F F

Search space with sentinel:
    T F F F
    ^
    index -1 = no valid real index

The function returns -1.
```

### 5.5 - When to choose explicit answer vs upper-mid

Use explicit answer when:

- no valid answer may exist
- the return value is not just an index, such as TimeMap returning a string
- you want the easiest invariant to explain
- the predicate check produces useful payload, such as `(timestamp, value)`

Use upper-mid when:

- at least one valid answer is guaranteed, or a sentinel such as `left = -1`
  represents "no valid index"
- the answer is the final index or value at that index
- you want a compact single-candidate narrowing loop

The explicit-answer version is longer, but it is often the clearest interview
choice for floor lookups and maximum feasible answer problems.

### 5.6 - Why `left = mid` can hang

With lower-mid:

```python
mid = left + (right - left) // 2
```

If two candidates remain:

```text
left = 0, right = 1
mid = 0
```

Then `left = mid` leaves `left` unchanged. The next iteration repeats forever.

Fixes:

- discard `mid` after recording it: `answer = mid; left = mid + 1`
- or keep `mid` with upper-mid:

```python
mid = left + (right - left + 1) // 2
```


---

## 6. Lower Bound, Upper Bound, Floor, and Ceiling

These names are worth memorizing, but there is one naming trap:

```text
upper_bound(x) is not "the largest value <= x."
upper_bound(x) is the first insertion position after all values <= x.
```

So `upper_bound(x)` is a boundary position. The last actual index with
`nums[i] <= x` is the floor index, which is `upper_bound(x) - 1`.

Think of the concepts in two groups.

Boundary / insertion-position queries:

| Name | Meaning | Predicate shape |
| --- | --- | --- |
| lower bound | first index `i` with `nums[i] >= x` | `F...T` for `nums[i] >= x` |
| upper bound | first index `i` with `nums[i] > x` | `F...T` for `nums[i] > x` |

Actual-element queries:

| Name | Meaning | Boundary formula |
| --- | --- | --- |
| floor | largest value/index `<= x` | `upper_bound(x) - 1`, then guard |
| ceiling | smallest value/index `>= x` | `lower_bound(x)`, then guard |

Relationship:

```text
floor index = upper_bound(x) - 1
ceiling index = lower_bound(x)
last occurrence of x = upper_bound(x) - 1, then verify equality
first occurrence of x = lower_bound(x), then verify equality
```

Example with duplicates:

```text
nums = [1, 2, 2, 2, 4], x = 2

index:          0  1  2  3  4   5
value:          1  2  2  2  4  end

lower_bound(2) = 1   # first index with value >= 2
upper_bound(2) = 4   # first index with value > 2

ceiling index  = 1   # nums[1] = 2
floor index    = 3   # upper_bound(2) - 1, nums[3] = 2
first 2 index  = 1
last 2 index   = 3
```

Example without an exact match:

```text
nums = [1, 2, 2, 2, 4], x = 3

lower_bound(3) = 4   # first value >= 3 is 4
upper_bound(3) = 4   # first value > 3 is also 4

ceiling index  = 4   # nums[4] = 4
floor index    = 3   # nums[3] = 2
```

Guard edge cases:

```text
x smaller than everything:
    floor index = upper_bound(x) - 1 may be -1, so no floor exists.

x larger than everything:
    ceiling index = lower_bound(x) may be len(nums), so no ceiling exists.
```

### 6.1 - First and last occurrence

For a sorted array with duplicates:

```python
def first_occurrence(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    if left < len(nums) and nums[left] == target:
        return left
    return -1
```

```python
def last_occurrence(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    candidate = left - 1
    if candidate >= 0 and nums[candidate] == target:
        return candidate
    return -1
```

This is the cleanest way to solve "Find First and Last Position of Element in
Sorted Array": compute both boundaries and verify them.

### 6.2 - Python `bisect`

Python's `bisect` module implements these boundaries.

```python
from bisect import bisect_left, bisect_right

i = bisect_left(nums, target)   # first nums[i] >= target
j = bisect_right(nums, target)  # first nums[j] > target
```

Common recipes:

```python
# exact search
i = bisect_left(nums, target)
found = i < len(nums) and nums[i] == target

# first occurrence
first = bisect_left(nums, target)

# last occurrence
last = bisect_right(nums, target) - 1

# floor
floor_i = bisect_right(nums, x) - 1

# ceiling
ceil_i = bisect_left(nums, x)
```

Guards matter:

```python
if floor_i >= 0:
    floor_value = nums[floor_i]
else:
    floor_value = None

if ceil_i < len(nums):
    ceil_value = nums[ceil_i]
else:
    ceil_value = None
```

`bisect` returns an insertion point. It does not prove the target exists.

### 6.3 - What if the array is descending?

Descending arrays are not a new template. They only flip the monotonic
predicate.

Ascending floor:

```text
nums = [1, 4, 9], query = 5
condition nums[i] <= 5 gives T T F
answer is last true
```

Descending floor:

```text
nums = [9, 4, 1], query = 5
condition nums[i] <= 5 gives F T T
answer is first true
```

So do not memorize "floor always means last true." Instead, write the truth
pattern for the actual order, then choose first true or last true.

For TimeMap, timestamps are ascending because `set` appends increasing
timestamps, so `timestamp <= query` is a `T...F` predicate and the answer is
last true.


---

## 7. Answer-Space Binary Search

Sometimes the array is not sorted, but the answer space is monotonic.

Recognition signal:

```text
The problem asks for the minimum/maximum integer value satisfying a condition.
```

Examples:

- minimum eating speed
- minimum ship capacity
- minimum days to make bouquets
- maximum minimum distance
- square root floor

### 7.1 - Design worksheet for answer search

| Question | Example: Koko |
| --- | --- |
| What is the answer variable? | eating speed |
| What are safe bounds? | `1` to `max(piles)` |
| What is the predicate? | `can_finish(speed)` |
| Is it `F...T` or `T...F`? | `F...T` |
| Which boundary do we need? | first true |
| What is the cost of one check? | O(n) |

### 7.2 - First feasible answer template

```python
left, right = min_possible, max_possible

while left < right:
    mid = left + (right - left) // 2
    if feasible(mid):
        right = mid
    else:
        left = mid + 1

return left
```

Invariant:

```text
The minimum feasible answer stays inside [left, right].
```

### 7.3 - Maximum feasible answer

Sometimes feasibility is `T...F`, and you want the last true.

Example shape:

```text
distance:  1  2  3  4  5
can_place: T  T  T  F  F
answer:          3
```

Use either explicit answer:

```python
answer = min_possible
left, right = min_possible, max_possible

while left <= right:
    mid = left + (right - left) // 2
    if feasible(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

return answer
```

or upper-mid:

```python
left, right = min_possible, max_possible

while left < right:
    mid = left + (right - left + 1) // 2
    if feasible(mid):
        left = mid
    else:
        right = mid - 1

return left
```

Use explicit answer when it is possible that no value is feasible.

### 7.4 - Bound selection

Good bounds are correct first, tight second.

For Koko:

```text
lower bound: 1
upper bound: max(piles)
```

A tighter lower bound is:

```python
(sum(piles) + h - 1) // h
```

That bound is safe because total capacity must cover all bananas, but it is not
automatically the answer because each pile rounds up to full hours.

Common bound mistakes:

- starting from an invalid value, such as speed 0
- using a bound that can exclude the true answer
- optimizing the bound before proving the predicate


---

## 8. Rotated Arrays

Rotated sorted arrays are binary search problems where the array is not globally
sorted, but each midpoint still reveals a sorted side or a pivot boundary.

There are two common tasks:

| Problem | Core question |
| --- | --- |
| Search in Rotated Sorted Array | Which side of `mid` is sorted, and can target be there? |
| Find Minimum in Rotated Sorted Array | Which side contains the rotation drop? |

### 8.1 - Search in rotated array

State invariant:

```text
If target exists, it remains inside [left, right].
```

Template:

```python
left, right = 0, len(nums) - 1

while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid

    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

return -1
```

Boundary lesson:

```text
Use nums[left] <= nums[mid], not nums[left] < nums[mid].
```

Why? In a closed interval, a one-element side is still sorted. When
`left == mid`, the interval `[left, mid]` contains one value and is sorted.

The target range excludes `mid` because equality was already checked:

```text
left sorted side:  nums[left] <= target < nums[mid]
right sorted side: nums[mid] < target <= nums[right]
```

### 8.2 - Find minimum in rotated array

State invariant:

```text
The minimum index remains inside [left, right].
```

Template:

```python
left, right = 0, len(nums) - 1

while left < right:
    mid = left + (right - left) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

return nums[left]
```

Why `right = mid`?

If `nums[mid] <= nums[right]`, then `mid` may be the minimum. Do not discard it
with `right = mid - 1`.

### 8.3 - Duplicate caveat

The common rotated-array templates rely on uniqueness. With duplicates,
comparisons like `nums[mid] <= nums[right]` can become ambiguous. That usually
requires shrinking a boundary by one and accepting possible O(n) worst-case
behavior.


---

## 9. Virtual Index Binary Search

Sometimes the data is globally sorted if you view it through a different index
space.

Example: Search a 2D Matrix.

If each row is sorted and every row starts after the previous row ends, the
matrix is sorted in row-major order.

```text
matrix:
[
  [1,  3,  5],
  [7,  9, 11],
  [13,15,17]
]

virtual array:
[1, 3, 5, 7, 9, 11, 13, 15, 17]
```

Do not physically flatten it. Search virtual indices.

```python
rows, cols = len(matrix), len(matrix[0])
left, right = 0, rows * cols - 1

while left <= right:
    mid = left + (right - left) // 2
    row, col = divmod(mid, cols)
    value = matrix[row][col]

    if value == target:
        return True
    if value < target:
        left = mid + 1
    else:
        right = mid - 1

return False
```

Key rule:

```text
virtual index k maps to row = k // cols, col = k % cols
```

Common mistakes:

- dividing by rows instead of columns
- flattening the matrix and using O(m*n) extra space
- applying this to matrices that are only row-sorted and column-sorted but not
  row-major globally sorted


---

## 10. Peak and Neighbor-Based Binary Search

Some binary search problems do not look like `F...T` at first. They use a local
slope or neighbor comparison to prove a peak exists on one side.

Example: Find Peak Element.

```python
left, right = 0, len(nums) - 1

while left < right:
    mid = left + (right - left) // 2
    if nums[mid] < nums[mid + 1]:
        left = mid + 1
    else:
        right = mid

return left
```

Mental model:

```text
If nums[mid] < nums[mid + 1], the slope rises to the right, so there is a peak
on the right.
Otherwise there is a peak at mid or on the left.
```

This is still binary search because each neighbor comparison proves one side
contains at least one valid answer.

Rules:

- Use `while left < right` so `mid + 1` is safe.
- Keep `mid` with `right = mid` when `mid` can still be a peak.
- Discard `mid` with `left = mid + 1` when the right neighbor proves a peak is
  to the right.


---

## 11. Python Implementation Details

### 11.1 - Midpoint calculation

In Python, this is fine:

```python
mid = (left + right) // 2
```

But this version is portable to fixed-width integer languages:

```python
mid = left + (right - left) // 2
```

Use upper-mid only when the update keeps `mid` on the left side:

```python
mid = left + (right - left + 1) // 2
```

### 11.2 - Integer ceiling division

For positive integers:

```python
ceil(a / b) == (a + b - 1) // b
```

Koko uses:

```python
hours += (pile + speed - 1) // speed
```

Do not use `pile // speed`; it undercounts partial hours.

### 11.3 - `bisect` with keyless arrays

For simple sorted arrays, `bisect` is ideal:

```python
from bisect import bisect_left, bisect_right
```

For arrays of pairs, avoid clever tuple sentinels unless you can explain the
value constraints. A separate timestamp array is often clearer:

```python
times = [1, 4, 9]
values = ["bar", "bar2", "bar3"]

i = bisect_right(times, query) - 1
return "" if i < 0 else values[i]
```

### 11.4 - Empty inputs

Closed exact search handles empty arrays naturally:

```python
left, right = 0, len(nums) - 1
# if nums is empty, right = -1 and the loop does not run
```

Half-open lower bound handles empty arrays naturally:

```python
left, right = 0, len(nums)
# both are 0, loop does not run
```

But final indexing needs guards.


---

## 12. Correctness Invariants

A strong binary-search explanation has three parts.

### 12.1 - Invariant

Say what remains possible.

Examples:

```text
Exact search:
If target exists, its index is in [left, right].

First true:
The first true index is in [left, right].

TimeMap floor:
result is the best valid value seen so far; any unseen better value must be in
[left, right].

Rotated minimum:
The minimum index is in [left, right].
```

### 12.2 - Maintenance

Explain why each branch preserves the invariant.

Example for TimeMap:

```text
If event_time <= query:
    This value is valid, so store it.
    A later valid value may exist, so search right.

If event_time > query:
    This event and every later event is too late.
    Search left.
```

### 12.3 - Termination

Explain why the loop stops and why the returned value is correct.

Examples:

```text
Exact search:
The interval becomes empty, so target does not exist.

First true:
left == right, and the invariant says this single index is the first true.

Explicit answer floor search:
The interval is empty, and result stores the last valid candidate encountered.
```


---

## 13. Failure Modes and Edge Cases

### 13.1 - Mixed interval conventions

Bad combination:

```python
left, right = 0, len(nums)
while left <= right:
    ...
```

This starts half-open but loops like closed. It can index `len(nums)`.

### 13.2 - Keeping `mid` without midpoint bias

Danger:

```python
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        left = mid
```

If `right = left + 1`, `mid = left`, so the loop can freeze.

### 13.3 - Infinite-loop patterns and progress invariants

Infinite loops in binary search almost always come from one mistake:

```text
The code enters the next iteration with the same live interval it had before.
```

Use this progress invariant:

```text
After every branch:
    either the function returns,
    or the new interval is strictly smaller than the old interval.
```

For index intervals, "strictly smaller" means at least one live index is removed.

```text
closed interval [left, right]:
    new_left > old_left or new_right < old_right

half-open interval [left, right):
    new_left > old_left or new_right < old_right
```

When `mid` is discarded, progress is easy:

```python
left = mid + 1
right = mid - 1
```

When `mid` is kept as a possible answer, progress depends on midpoint bias:

```text
lower-mid: mid == left  when two candidates remain
upper-mid: mid == right when two candidates remain
```

So the safe pairings are:

| Goal | Midpoint | Keep-mid update | Why it shrinks |
| --- | --- | --- | --- |
| first true / lower bound | lower-mid | `right = mid` | when two remain, `mid == left`, so right moves left |
| last true / upper bound previous | upper-mid | `left = mid` | when two remain, `mid == right`, so left moves right |

#### Pattern A: lower-mid plus `left = mid`

This is the classic hang.

```python
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        left = mid
    else:
        right = mid - 1
```

Trace with two candidates:

```text
left = 0, right = 1
mid = 0
condition(0) is true
left = mid = 0

New interval is still [0, 1].
The next iteration repeats the same state forever.
```

Fix 1: keep `mid` with upper-mid.

```python
while left < right:
    mid = left + (right - left + 1) // 2
    if condition(mid):
        left = mid
    else:
        right = mid - 1
```

Fix 2: store `mid` as best-so-far, then discard it.

```python
answer = -1
while left <= right:
    mid = left + (right - left) // 2
    if condition(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
```

This second version is often clearer when no valid answer may exist. See
[5.5 - When to choose explicit answer vs upper-mid](#55---when-to-choose-explicit-answer-vs-upper-mid).

#### Pattern B: upper-mid plus `right = mid`

Upper-mid fixes last-true searches, but it is the wrong bias for first-true
searches that keep `mid` on the right.

```python
while left < right:
    mid = left + (right - left + 1) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
```

Trace with two candidates:

```text
left = 0, right = 1
mid = 1
condition(1) is true
right = mid = 1

New interval is still [0, 1].
The next iteration repeats forever.
```

Fix: use lower-mid for first true.

```python
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
```

When two candidates remain, `mid == left`. If `condition(mid)` is true,
`right = mid` shrinks to the left candidate. If false, `left = mid + 1` shrinks
to the right candidate.

#### Pattern C: equality branch does not remove `mid`

In exact search with a closed interval, `mid` is no longer a live candidate
after you compare it.

Bad:

```python
while left <= right:
    mid = left + (right - left) // 2

    if nums[mid] < target:
        left = mid
    elif nums[mid] > target:
        right = mid
    else:
        return mid
```

Trace:

```text
nums = [1, 3], target = 3
left = 0, right = 1
mid = 0, nums[mid] = 1
left = mid = 0

The interval is still [0, 1].
```

Fix:

```python
if nums[mid] < target:
    left = mid + 1
elif nums[mid] > target:
    right = mid - 1
else:
    return mid
```

The invariant is:

```text
If target exists, it is inside [left, right].
```

Once `nums[mid] < target`, `mid` and everything left of it are impossible, so
`mid` must be removed with `left = mid + 1`.

#### Pattern D: mixed interval convention hides the progress proof

This may not always loop forever, but it destroys the invariant that prevents
loop bugs.

Bad:

```python
left, right = 0, len(nums)
while left <= right:
    mid = left + (right - left) // 2
    ...
```

The initialization is half-open `[left, right)`, but the loop condition is
closed. The code may probe `nums[len(nums)]`, or force awkward updates that do
not match either template.

Pick one invariant:

```python
# Closed exact search: [left, right]
left, right = 0, len(nums) - 1
while left <= right:
    ...
```

or:

```python
# Half-open lower bound: [left, right)
left, right = 0, len(nums)
while left < right:
    ...
```

The habit to build:

```text
Before coding, state the live interval.
For each branch, say which indices are removed.
For any branch that keeps mid, check the two-candidate case by hand.
```

### 13.4 - Returning an insertion point as if it were a found target

Lower bound returns where the target would go.

```python
i = bisect_left(nums, target)
```

You still need:

```python
i < len(nums) and nums[i] == target
```

### 13.5 - No valid answer

Boundary searches often need a default:

```python
answer = -1
answer = ""
answer = None
```

Use this when no candidate might satisfy the predicate.

### 13.6 - Wrong monotonic direction

Before coding, write the truth pattern:

```text
F...T -> first true
T...F -> last true
```

Then choose the template. Do not force every problem into first true.

### 13.7 - Unproven answer-space bounds

Bounds must contain the answer.

For answer search:

```text
correct loose bound > incorrect tight-looking bound
```


---

## 14. Tradeoffs and Neighboring Techniques

Binary search is not the right tool just because data contains numbers.

| Need | Often better tool |
| --- | --- |
| Exact membership in unsorted data | hash set |
| All pairs in sorted array | two pointers |
| Contiguous window with changing validity | sliding window |
| Repeated min/max under updates | heap |
| Prefix/range sum queries | prefix sum |
| Graph reachability for one threshold check | BFS/DFS inside answer-space binary search |

Examples:

- Two Sum II is better with two pointers because you need a pair, not one
  boundary.
- Minimum Size Subarray Sum with positive numbers is usually sliding window,
  though prefix sums plus binary search can also work.
- Swim in Rising Water can be solved by binary searching time and checking
  reachability, but a heap/Dijkstra-style frontier is often more direct.


---

## 15. Practice Progression

Use this order to build the topic from mechanics to advanced recognition.

### 15.1 - Core mechanics

- Binary Search
- Search Insert Position
- Sqrt(x)

Practice goals:

- Write closed exact search from memory.
- Write lower-bound search from memory.
- Explain `left`, `right`, and return value.

### 15.2 - Boundary searches

- Find First and Last Position of Element in Sorted Array
- Time Based Key-Value Store
- Koko Eating Bananas

Practice goals:

- Distinguish `F...T` from `T...F`.
- Use `answer` for floor/last-true search.
- Use final guards for missing answers.

### 15.3 - Virtual and transformed spaces

- Search a 2D Matrix
- Longest Increasing Subsequence

Practice goals:

- Search a virtual index space.
- Search insertion positions inside a helper array.

### 15.4 - Rotated and structural variants

- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Find Peak Element

Practice goals:

- State why one side remains searchable.
- Know when `mid` must be kept.
- Handle one-element sides and boundary ownership.

### 15.5 - Advanced combinations

- Median of Two Sorted Arrays
- Swim in Rising Water
- Minimum Interval to Include Each Query

Practice goals:

- Recognize when binary search is only one part of the solution.
- Compare binary search against heaps, graph traversal, and two pointers.


---

## 16. Interview Explanation Templates

### 16.1 - Exact search

```text
I keep a closed interval of candidate indices. At each midpoint, if I find the
target I return it. If the midpoint value is too small, sorted order proves
everything at or left of mid is too small, so I move left to mid + 1. The large
case is symmetric. If the interval becomes empty, the target is absent.
```

### 16.2 - First true

```text
I define a monotonic predicate where false values come before true values. The
answer is the first true. When the midpoint is true, I keep it because it may be
the first true. When it is false, I discard it and everything before it. The
loop ends when the boundary is isolated.
```

### 16.3 - Last true / floor

```text
I define a monotonic predicate where true values come before false values. The
answer is the last true. When the midpoint is true, it is a valid candidate, so
I store it and search right for a later valid candidate. When it is false, I
search left. The stored answer is the best valid candidate seen.
```

### 16.4 - Answer-space search

```text
The array itself is not sorted, but the answer values have monotonic
feasibility. I choose bounds that contain the answer, define a predicate, and
binary search the first or last feasible value depending on the truth pattern.
```

### 16.5 - Rotated array

```text
Even though the whole array is rotated, each midpoint leaves at least one side
normally sorted or reveals which side contains the pivot. I use that sorted
side or pivot comparison to discard a half while preserving the invariant that
the answer remains in the interval.
```


---

## 17. Mastery Checklist

Before coding:

- Can I name the search space?
- Can I write the truth pattern: exact, `F...T`, or `T...F`?
- Can I state what `left` and `right` mean?
- Can I say whether the interval is closed or half-open?
- Can I say what the return value means?
- Can I prove the predicate is monotonic?

During coding:

- If I discard `mid`, do I use `mid + 1` or `mid - 1`?
- If I keep `mid`, does midpoint bias still guarantee progress?
- Do I need an `answer` variable?
- Do I handle no-answer cases?
- Do I guard final array access?

After coding:

- Test empty input if allowed.
- Test one element.
- Test two elements.
- Test target before first and after last.
- Test exact boundary hits.
- Test gaps between valid values.
- Test no valid answer.
- Test all false and all true predicate shapes.


---

## 18. Quick Reference

### Exact search, closed interval

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

### First true, half-open

```python
left, right = 0, n
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
return left
```

### First true, closed single-candidate narrowing

```python
left, right = 0, n - 1
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
return left
```

Use only when at least one true exists or when bounds include a sentinel true.

### Last true with explicit answer

```python
left, right = 0, n - 1
answer = -1
while left <= right:
    mid = left + (right - left) // 2
    if condition(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
return answer
```

### Last true with upper midpoint

```python
left, right = 0, n - 1  # use when at least one true exists
while left < right:
    mid = left + (right - left + 1) // 2
    if condition(mid):
        left = mid
    else:
        right = mid - 1
return left
```

Sentinel version when no real true may exist:

```python
left, right = -1, n - 1
while left < right:
    mid = left + (right - left + 1) // 2
    if condition(mid):
        left = mid
    else:
        right = mid - 1
return left
```

Here `-1` means "no valid real index." The loop never calls `condition(-1)`.

### Lower and upper bounds with `bisect`

```python
from bisect import bisect_left, bisect_right

first_ge = bisect_left(nums, x)
first_gt = bisect_right(nums, x)
floor_i = first_gt - 1
ceil_i = first_ge
```

### Decision prompt

```text
Am I finding:

1. exact target?
   -> closed exact search

2. first place a condition becomes true?
   -> lower-bound / first-true template

3. last place a condition remains true?
   -> explicit answer or upper-mid last-true template

4. minimum feasible answer?
   -> first true over answer space

5. maximum feasible answer?
   -> last true over answer space

6. a rotated pivot or sorted side?
   -> preserve the answer interval; keep mid when it may be the answer
```
