# Heap / Priority Queue - A Complete Guide for Coding Interviews

## 1. What Is a Heap?

A heap is a data structure for repeatedly answering this question:

```text
Which item has the highest priority right now?
```

In Python, `heapq` implements a **min heap**. That means:

```text
heap[0] = the smallest stored item
```

Only the root is guaranteed to be the smallest item. The rest of the list is
not sorted.

As a tree, the heap only promises that every parent is no larger than its
children:

```text
            1
          /   \
         3     8
        /
       5

heap list: [1, 3, 8, 5]
```

The root `1` is definitely smallest. The list representation is an
implementation detail, not a sorted order.

Example:

```python
import heapq

heap = [5, 1, 8, 3]
heapq.heapify(heap)

print(heap[0])  # 1
print(heap)     # heap-ordered, not fully sorted
```

Do not read `heap[1]`, `heap[2]`, and so on as sorted ranks. A heap gives fast
access to the best item, not fast access to every ordered position.

Why this matters in interviews:

```text
Sorting gives a complete order.
A heap gives the next best item, while allowing new items to be added.
```

Use a heap when the problem repeatedly changes the candidate set but only asks
for the current best candidate.

### 1.1 - How the list stores the tree

`heapq` stores the heap tree inside a Python list. For an item at index `i`:

```text
parent index      = (i - 1) // 2
left child index  = 2 * i + 1
right child index = 2 * i + 2
```

Example:

```text
index:      0   1   2   3   4   5   6
heap:      [1,  3,  8,  5,  4,  9, 10]

tree:
            1
          /   \
         3     8
        / \   / \
       5   4 9  10
```

The heap property is local:

```text
every parent <= each child
```

That local rule is enough to guarantee the root is the global minimum. If some
smaller value existed below the root, walking from that value upward would
eventually find a parent larger than its child, which violates the heap rule.

### 1.2 - Why push and pop are O(log n)

The heap tree is complete, so its height is `O(log n)`.

When pushing a value, Python appends it at the end and "sifts up" until the heap
property is restored.

```text
push 2 into [3, 5, 8, 9]

append:
            3
          /   \
         5     8
        / \
       9   2

2 < parent 5, swap:
            3
          /   \
         2     8
        / \
       9   5

2 < parent 3, swap:
            2
          /   \
         3     8
        / \
       9   5
```

When popping, Python removes the root, moves the final item to the root, then
"sifts down" by swapping with the smaller child until the heap property is
restored.

```text
pop from [1, 3, 8, 5, 4]

remove 1, move 4 to root:
            4
          /   \
         3     8
        /
       5

4 > smaller child 3, swap:
            3
          /   \
         4     8
        /
       5
```

You rarely implement sift-up or sift-down in Python interviews, but knowing this
mechanic explains why heaps expose only the root cheaply and why deleting from
the middle is not a built-in operation.


---

## 2. The Core Mental Model

The best heap solutions start by naming the frontier.

```text
frontier = candidates that are eligible to be chosen next
heap     = frontier ordered by the choice priority
```

Before coding, answer four questions:

| Question | Example answer |
| --- | --- |
| What does one heap entry represent? | `(sum, row, col)` for one pair candidate |
| What priority should the heap expose? | smallest sum, largest profit, earliest end time |
| When does an item become eligible? | capital requirement is affordable |
| What must be pushed after popping? | the next node from the same linked list |

This mental model prevents a common mistake: pushing everything into a heap just
because the tag says "heap". The heap should contain exactly the useful
frontier for the current pattern.

Example: Merge k Sorted Lists.

```text
Wrong frontier:
    all nodes from all lists

Better frontier:
    only the current head of each non-empty list

After popping a node:
    push node.next, because that node becomes the current head of the same list
```

The second version keeps heap size O(k), not O(N), where `k` is the number of
lists and `N` is the total number of nodes.

### 2.1 - Heap entry design worksheet

Most heap bugs come from under-specifying the entry. Before writing code, fill
in this worksheet:

| Field | Question | Example |
| --- | --- | --- |
| priority | What should the heap compare first? | `pair_sum`, `end_time`, `-profit` |
| payload | What value do I need to return or use? | `node`, `tweet_id`, `(x, y)` |
| source | Which stream/frontier did this come from? | `list_index`, `author_id`, `row` |
| position | How do I advance after popping? | `node.next`, `tweet_index - 1`, `col + 1` |
| validity | Can this entry expire or become stale? | window index, interval end, stored distance |

Examples:

```text
Merge k lists:
    (node.val, counter, node)
    priority = node value
    payload/position = node, because node.next is the continuation

Find k pairs:
    (nums1[i] + nums2[j], i, j)
    priority = pair sum
    source = row i
    position = column j, so the successor is (i, j + 1)

Sliding window max:
    (-nums[i], i)
    priority = larger value first through negation
    validity = index i must still be inside the window
```

If a popped entry needs to generate a successor but the entry does not carry the
source or position needed to find that successor, the heap state is incomplete.


---

## 3. Python `heapq` Fundamentals

### 3.1 - Common operations

| Operation | Meaning | Time |
| --- | --- | --- |
| `heapq.heapify(a)` | turn list `a` into a heap in place | O(n) |
| `heapq.heappush(heap, x)` | add `x` | O(log n) |
| `heapq.heappop(heap)` | remove and return the smallest item | O(log n) |
| `heap[0]` | read the smallest item without removing it | O(1) |
| `heapq.heappushpop(heap, x)` | push `x`, then pop and return the smallest | O(log n) |
| `heapq.heapreplace(heap, x)` | pop smallest, then push `x` | O(log n) |
| `heapq.nsmallest(k, items)` | return k smallest items | roughly O(n log k) |
| `heapq.nlargest(k, items)` | return k largest items | roughly O(n log k) |

Important details:

- `heapify` mutates the list and returns `None`.
- `heap[0]` is the root/top priority item.
- Raw `heap.append(...)` and `heap.pop()` are normal list operations; they do
  not preserve heap order.
- A heap is not a deque. It does not have a meaningful head/tail model for
  queue order.
- Do not mutate the priority fields of items already inside a heap. `heapq`
  will not notice and repair the order for you.
- `nlargest` and `nsmallest` are convenient for Python practice, but in an
  interview you should still be able to explain the underlying heap or
  selection idea.

### 3.2 - Min heap vs max heap

Python's heap is a min heap. To simulate a max heap for numbers, store negative
priorities.

```python
import heapq

values = [8, 2, 7]
heap = [-x for x in values]
heapq.heapify(heap)

largest = -heapq.heappop(heap)  # 8
```

This works because:

```text
larger original value -> smaller negative value -> pops earlier

8  becomes -8
7  becomes -7
2  becomes -2

heap pops -8 first, which represents 8
```

When heap entries contain more state, negate only the priority field.

```python
# newest tweet first
heapq.heappush(heap, (-timestamp, author_id, tweet_index, tweet_id))

# highest profit first
heapq.heappush(heap, -profit)
```

### 3.3 - Tuple priorities and tie-breakers

Python compares tuples lexicographically:

```text
(priority, second, third)
```

If two priorities tie, Python compares the second field. This is useful when
the second field is an index or counter.

But it can break when the second field is a custom object, such as a `ListNode`.

```python
# Risky if node values tie:
heapq.heappush(heap, (node.val, node))

# Safer:
counter += 1
heapq.heappush(heap, (node.val, counter, node))
```

The counter is not part of the algorithmic priority. It only gives Python a
stable way to break ties without comparing node objects.

### 3.4 - Updating priorities

Python's `heapq` does not provide a direct "decrease key" or "increase key"
operation.

Avoid this:

```python
entry[0] = new_priority  # mutates an item already inside the heap
```

The list may still look like a heap-shaped object, but the heap property may be
wrong. The usual interview-safe options are:

- push a new entry and skip the old stale one when it reaches the root
- keep an external `best` map and ignore popped entries that no longer match it
- rebuild the heap with `heapq.heapify(...)` if the whole collection changed and
  that cost is acceptable

This is the same reason graph priority queues often allow duplicate entries for
the same node: pushing a better distance is cheaper and simpler than trying to
delete or mutate the older distance inside the heap.

### 3.5 - `heappushpop` vs `heapreplace`

These two helpers look similar but mean different things.

```python
heapq.heappushpop(heap, x)
```

Pushes `x`, then pops the smallest. If `x` is smaller than the current root, it
may return `x` immediately and leave the heap unchanged.

```python
heapq.heapreplace(heap, x)
```

Pops the current root first, then pushes `x`. Use this only when you already
know the root should be replaced.

For a size-k min heap that keeps the k largest values:

```python
if x > heap[0]:
    heapq.heapreplace(heap, x)
```

That condition matters. If `x <= heap[0]`, the new value is not in the top k and
should be ignored.


---

## 4. Complexity Basics

For a heap of size `H`:

```text
push: O(log H)
pop:  O(log H)
peek: O(1)
```

For a heap algorithm, complexity usually comes from counting pushes and pops:

```text
Time = O((number of pushes + number of pops) * log(max heap size))
Space = O(max heap size)
```

Special case:

```text
heapq.heapify(list_of_n_items) = O(n)
```

This is why "heapify all items, then pop k times" is:

```text
O(n + k log n)
```

not `O(n log n + k log n)`.


---

## 5. Recognition Signals

Reach for a heap when the problem has one or more of these signals:

| Signal | Heap interpretation |
| --- | --- |
| "k largest", "k smallest", "k closest" | Maintain top k or pop k best |
| "stream" | Keep a running frontier without sorting everything again |
| "merge k sorted ..." | Heap stores one current item from each sorted source |
| "minimum rooms", "next ending meeting" | Heap stores active intervals by end time |
| "available projects/tasks" | Heap stores currently eligible choices |
| "median from stream" | Two heaps store two halves around the median |
| "shortest path", "minimum effort" | Heap explores best current graph frontier |
| "sliding window max with heap" | Heap stores candidates plus indexes; delete stale roots lazily |

Do not stop at the signal. Also ask:

```text
What exactly is the frontier?
```

That question is the difference between a heap solution that passes and a heap
solution that times out.


---

## 6. Pattern 1: Size-k Heap

### 6.1 - When to use it

Use a size-k heap when:

- you only care about the best k items
- the input can be scanned once
- storing all items is unnecessary or too expensive
- the final answer does not require the whole input sorted

Classic examples:

- Kth Largest Element in a Stream
- Kth Largest Element in an Array
- Top K Frequent Elements
- K Closest Points to Origin

### 6.2 - Keep k largest values with a min heap

The invariant:

```text
heap stores the k largest values seen so far
heap[0] is the weakest kept value
```

After scanning all values:

```text
heap[0] = kth largest value
```

Template:

```python
import heapq


def kth_largest(nums, k):
    heap = []

    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)

    return heap[0]
```

Walkthrough:

```text
nums = [4, 5, 8, 2], k = 3

scan 4:
    heap = [4]

scan 5:
    heap stores [4, 5]

scan 8:
    heap stores [4, 5, 8]
    heap[0] = 4, the 3rd largest among seen values

scan 2:
    2 <= heap[0], so 2 cannot be in the top 3
    ignore it

heap still stores [4, 5, 8]
heap[0] = 4
```

If a future value `10` appears:

```text
10 > heap[0]
replace 4 with 10

heap stores [5, 8, 10]
heap[0] = 5, the new 3rd largest
```

The heap does not need to remember values below the kth-largest boundary. They
cannot affect the answer unless they are larger than the current boundary, and
that is exactly what the comparison checks.

### 6.3 - Keep k smallest values with a max heap

For k closest points, a size-k heap can keep the k closest points seen so far.
The weakest kept item is the farthest among the kept points, so the heap must
expose the largest distance. In Python, simulate that with negative distance.

```python
import heapq


def k_closest(points, k):
    heap = []

    for x, y in points:
        dist = x * x + y * y
        item = (-dist, x, y)  # max heap by distance

        if len(heap) < k:
            heapq.heappush(heap, item)
        elif dist < -heap[0][0]:
            heapq.heapreplace(heap, item)

    return [[x, y] for _, x, y in heap]
```

Use squared distance:

```text
sqrt(x^2 + y^2) and x^2 + y^2 have the same ordering.
```

Avoid floating point and avoid sorting by the wrong expression, such as `x + y`.

### 6.4 - Size-k heap vs alternatives

| Strategy | Time | Space | Best when |
| --- | --- | --- | --- |
| Sort all items | O(n log n) | O(n) or O(1) depending on mutation | Simplicity matters |
| Heapify all, pop k | O(n + k log n) | O(n) | Need k best in sorted pop order |
| Size-k heap | O(n log k) | O(k) | `k` is much smaller than `n` |
| Quickselect | average O(n), worst O(n^2) | varies | Need unordered top k and interviewer wants selection |
| Bucket/counting | O(n) when bounded | O(n) or O(range) | Scores/frequencies have small bounded range |

For interviews, explain the tradeoff instead of pretending the heap is always
the final answer. Kth Largest and K Closest often invite a discussion of
sorting, heap, and quickselect.

Also be ready to say when a heap is not the best final tool:

```text
Fixed-size sliding window maximum:
    monotonic deque is O(n)
    heap with lazy deletion is O(n log n)

Top k frequent with small bounded frequencies:
    bucket/counting can be O(n)
    heap is still a clean general-purpose solution

Static kth element:
    quickselect can be average O(n)
    heap is simpler and more predictable to explain
```

The interview win is not "always use heap". It is naming the constraints and
choosing the simplest structure that satisfies them.

### 6.5 - Failure modes

- Using a max heap for kth largest stream. A max heap exposes the largest value,
  but the kth largest stream solution needs the boundary value among the k
  largest values.
- Dropping duplicates when the problem asks for kth largest by position.
  `nums = [5, 5, 4]`, `k = 2` returns `5`, not `4`.
- Replacing the root when `x <= heap[0]`. That admits values that are not in the
  top k.
- Assuming `heap` is sorted when returning multiple elements. If output order
  matters, pop repeatedly or sort the result.


---

## 7. Pattern 2: Heapify All, Then Pop the Best

### 7.1 - When to use it

Use this when the problem naturally starts with all candidates available and
each step asks for the next best candidate.

Classic examples:

- Last Stone Weight
- K Closest Points to Origin, direct heap variant
- Kth Largest Element in an Array, max-heap pop-k variant

Template:

```python
heap = build_entries(items)
heapq.heapify(heap)

for _ in range(k):
    best = heapq.heappop(heap)
    # use best
```

### 7.2 - Last Stone Weight

The problem repeatedly asks for the two heaviest stones. Python needs a
negative-value max heap.

```python
import heapq


def last_stone_weight(stones):
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    while len(heap) >= 2:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)

        if first != second:
            heapq.heappush(heap, -(first - second))

    return -heap[0] if heap else 0
```

Step trace:

```text
stones = [2, 7, 4, 1, 8, 1]

pop 8 and 7:
    leftover 1
    push 1

pop 4 and 2:
    leftover 2
    push 2

pop 2 and 1:
    leftover 1
    push 1

pop 1 and 1:
    equal, both disappear

pop 1:
    answer 1
```

The heap is helpful because every leftover stone changes the candidate set. A
single sort at the start would not be enough.


---

## 8. Pattern 3: K-way Merge and Frontier Heaps

### 8.1 - The idea

K-way merge appears whenever there are multiple sorted sources and you need the
best global items across them.

```text
source A: a0, a1, a2, ...
source B: b0, b1, b2, ...
source C: c0, c1, c2, ...

heap stores:
    current best unused item from A
    current best unused item from B
    current best unused item from C
```

After popping from one source, advance only that source.

```text
pop A's current item
push A's next item
```

The invariant:

```text
The heap stores the best remaining candidate from each active source.
Therefore heap[0] is the next global best candidate.
```

### 8.2 - Merge k Sorted Lists

Each linked list is already sorted. The heap should store only one current node
per list.

```python
import heapq


def merge_k_lists(lists):
    heap = []
    counter = 0

    for node in lists:
        if node:
            counter += 1
            heapq.heappush(heap, (node.val, counter, node))

    dummy = ListNode(0)
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next:
            counter += 1
            heapq.heappush(heap, (node.next.val, counter, node.next))

    tail.next = None
    return dummy.next
```

Key details:

- The counter prevents Python from comparing `ListNode` objects on equal values.
- Push current heads, not every node.
- After popping a node, push `node.next` from the same list.
- If reusing original nodes, set the final `tail.next = None` to avoid stale
  links.

### 8.3 - Design Twitter

For a user's news feed:

```text
visible authors = user + followees
each author's tweets = one sorted stream, newest to oldest
feed = newest 10 tweets across those streams
```

Heap entry:

```text
(-timestamp, author_id, tweet_index, tweet_id)
```

Algorithm:

```text
1. For each visible author with at least one tweet:
       push the author's newest tweet.

2. Repeat until feed has 10 tweets or heap is empty:
       pop newest tweet
       append tweet_id to feed
       push the same author's next older tweet, if it exists
```

Common bug:

```text
following a user does not mean that user has tweets
```

Seed the heap only for non-empty tweet lists.

### 8.4 - Find K Pairs with Smallest Sums

If both arrays are sorted, pair sums form sorted rows:

```text
                 nums2[0]       nums2[1]       nums2[2]
nums1[0]     (0,0) sum <=   (0,1) sum <=   (0,2) sum
nums1[1]     (1,0) sum <=   (1,1) sum <=   (1,2) sum
nums1[2]     (2,0) sum <=   (2,1) sum <=   (2,2) sum
```

Each row is one sorted source:

```text
row i = (nums1[i], nums2[0]), (nums1[i], nums2[1]), ...
```

Use a row-frontier heap:

```python
import heapq


def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k == 0:
        return []

    heap = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    result = []
    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result
```

Why this version does not need `visited`:

```text
(i, 0) is seeded once
(i, 1) is pushed only after (i, 0) is popped
(i, 2) is pushed only after (i, 1) is popped

Each pair has exactly one creation path inside its row.
```

Contrast with best-first grid expansion:

```text
from (i, j), push both (i + 1, j) and (i, j + 1)
```

Then a cell like `(1, 1)` can be discovered from `(0, 1)` and `(1, 0)`, so that
variant needs a `seen` set.

Concrete row-frontier trace:

```text
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 4

seed one pair per row:
    row 0: (1, 2), sum 3   -> heap entry (3, 0, 0)
    row 1: (7, 2), sum 9   -> heap entry (9, 1, 0)
    row 2: (11, 2), sum 13 -> heap entry (13, 2, 0)

pop (3, 0, 0):
    output [1, 2]
    advance only row 0 -> push (1, 4), sum 5

pop (5, 0, 1):
    output [1, 4]
    advance only row 0 -> push (1, 6), sum 7

pop (7, 0, 2):
    output [1, 6]
    row 0 has no next column

pop (9, 1, 0):
    output [7, 2]
    advance only row 1 -> push (7, 4), sum 11

answer:
    [[1, 2], [1, 4], [1, 6], [7, 2]]
```

Notice what never happens: after popping from row 0, we do not push anything
from row 1. Row 1 already has exactly one frontier candidate in the heap.

### 8.5 - K-way merge checklist

For any k-way merge heap, define:

- source identity: list index, author id, row index
- position inside source: node pointer, tweet index, column index
- priority: value, timestamp, pair sum
- advance rule: what to push after popping
- stop rule: all items, first k items, or first 10 feed items

Complexity template:

```text
R = number of active sources
M = number of popped result items

Time: O(initial seeding + M log R)
Space: O(R)
```


---

## 9. Pattern 4: Two Heaps for a Moving Boundary

### 9.1 - The idea

Two heaps are useful when the answer is a boundary between lower values and
higher values.

The canonical example is Median Finder.

```text
low  = max heap for the lower half
high = min heap for the upper half

all values in low <= all values in high
sizes are balanced
```

Python implementation:

```text
low stores negative values
high stores normal values

max(low) = -low[0]
min(high) = high[0]
```

### 9.2 - Median Finder invariants

One valid convention:

```text
size invariant:
    len(low) == len(high)
    or len(low) == len(high) + 1

order invariant:
    every value in low <= every value in high

extra item:
    if the total count is odd, low owns the extra item
```

Then:

```text
odd count:
    median = -low[0]

even count:
    median = (-low[0] + high[0]) / 2
```

### 9.3 - A robust insertion template

```python
import heapq


class MedianFinder:
    def __init__(self):
        self.low = []   # max heap via negatives
        self.high = []  # min heap

    def addNum(self, num: int) -> None:
        # First put num into low, then move low's maximum to high.
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Keep low as the heap that may own the extra item.
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2
```

Why the transfer matters:

```text
If we only balance sizes, the heaps can still be partitioned incorrectly.
The transfer step repairs the order boundary.
```

Example:

```text
stream = [5, 1, 3]

After 5:
    low = [5], high = []
    median = 5

After 1:
    low = [1], high = [5]
    median = (1 + 5) / 2 = 3

After 3:
    low = [3, 1], high = [5]
    median = 3
```

The lower heap owns `[1, 3]`; the upper heap owns `[5]`. Both invariants hold.

### 9.4 - Failure modes

- Preserving size balance but not order balance.
- Forgetting that `low[0]` is negative.
- Switching which heap owns the extra item without updating `findMedian`.
- Trying to sort the stream after every insert. That is often O(n) or O(n log n)
  per insert instead of O(log n).


---

## 10. Pattern 5: Two-frontier Greedy

### 10.1 - The idea

Some greedy problems have two different meanings of "best":

```text
eligible soonest     -> min heap or sorted pointer
best among eligible  -> max heap
```

The algorithm has two phases each round:

```text
1. Move newly eligible items into the available heap.
2. Choose the best available item.
```

This appears in IPO and offline query interval problems.

### 10.2 - IPO

At each round, choose one affordable project with maximum profit.

Two frontiers:

```text
locked projects:
    not yet affordable, ordered by required capital

available projects:
    affordable now, ordered by maximum profit
```

Template:

```python
import heapq


def find_maximized_capital(k, w, profits, capital):
    locked = [(capital[i], profits[i]) for i in range(len(profits))]
    heapq.heapify(locked)  # min capital requirement

    available = []         # max profit via negatives

    for _ in range(k):
        while locked and locked[0][0] <= w:
            _, profit = heapq.heappop(locked)
            heapq.heappush(available, -profit)

        if not available:
            break

        w += -heapq.heappop(available)

    return w
```

Why it is efficient:

```text
Each project moves from locked to available at most once.
Each selected project is popped from available at most once.
No repeated full scan is needed.
```

Why the greedy choice is safe:

```text
Among affordable projects, choosing a larger profit leaves at least as much
capital as choosing any smaller profit. More capital cannot make future
affordable choices worse.
```

Step trace:

```text
k = 2, initial capital w = 0
capital = [0, 1, 1]
profits = [1, 2, 3]

locked by capital:
    (0, profit 1), (1, profit 2), (1, profit 3)
available by profit:
    empty

round 1:
    move all projects with capital <= 0 into available
    available = [profit 1]
    choose profit 1
    w = 1

round 2:
    move all newly affordable projects with capital <= 1
    available = [profit 3, profit 2]
    choose profit 3
    w = 4

answer = 4
```

The optimized implementation never rescans all projects in round 2. The sorted
pointer or capital min heap continues from the first still-locked project, so
each project moves into `available` at most once.

### 10.3 - Meeting Rooms II

Meeting Rooms uses a min heap of end times:

```text
Process meetings by start time.
Heap stores end times of rooms currently in use.
If the earliest ending room ends before or at the new meeting's start, reuse it.
Otherwise allocate a new room.
```

Template:

```python
import heapq


def min_meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    rooms = []
    max_rooms = 0

    for start, end in intervals:
        while rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)
        max_rooms = max(max_rooms, len(rooms))

    return max_rooms
```

The heap frontier is:

```text
active rooms, ordered by earliest end time
```

Endpoint convention matters: if one meeting ends at time `10` and another
starts at time `10`, they do not overlap, so `rooms[0] <= start` can reuse the
room.

### 10.4 - Minimum Interval to Include Each Query

This offline query pattern is another two-frontier idea:

```text
sort queries ascending
sort intervals by start

as query q increases:
    add intervals with start <= q
    remove heap roots whose end < q
    heap root is the smallest valid interval covering q
```

Heap entry:

```text
(interval_length, interval_end)
```

The sorted pointer handles eligibility by start; lazy deletion handles
expiration by end.


---

## 11. Pattern 6: Heap Simulation with Cooldown or Rounds

### 11.1 - Task Scheduler

Task Scheduler can be solved by a formula, but the heap simulation is a useful
way to understand the process.

The heap stores task labels by remaining count:

```text
max heap of remaining counts
```

One cycle has `n + 1` slots. During a cycle, you can run at most one copy of the
same task label.

```text
n = 2
cycle length = 3

A _ _ | A _ _ | A
```

Heap-cycle simulation:

```text
while heap has work:
    used = []
    slots = n + 1

    while slots remain and heap has work:
        pop most frequent task
        run it once
        if it still has remaining copies:
            hold it in used

    push all used tasks back after the cycle ends
    add either full cycle length or only used slots for the final partial cycle
```

The key invariant:

```text
Do not push a used task back into the heap until the cycle ends.
```

If you push it back immediately, the same task can be chosen again before its
cooldown is satisfied.

### 11.2 - Formula connection

The optimized counting formula comes from the most frequent task's gaps:

```text
frame = (max_freq - 1) * (n + 1) + max_count
answer = max(len(tasks), frame)
```

`max_count` is the number of task labels tied at the maximum frequency.

The `max(len(tasks), frame)` part matters because enough filler tasks can remove
all idle time.

Use the heap simulation to explain the process. Use the formula when the
interview asks only for the minimum interval count and wants the optimized
solution.


---

## 12. Pattern 7: Lazy Deletion

### 12.1 - The problem

A heap supports fast access to the root. It does not support fast deletion from
the middle.

Lazy deletion means:

```text
Leave expired entries in the heap.
Before using heap[0] as an answer, pop expired roots until the root is valid.
```

This is correct because buried stale entries cannot be returned as the answer.
Only the root can affect the current answer.

### 12.2 - Sliding Window Maximum with a heap

Use entries:

```text
(-value, index)
```

Before reading the maximum for a window ending at `right`, remove expired roots:

```python
while heap[0][1] <= right - k:
    heapq.heappop(heap)
```

Then:

```python
answer = -heap[0][0]
```

Step trace:

```text
nums = [9, 1, 2, 3], k = 2

right = 0, push 9 at index 0
    no full window yet

right = 1, push 1 at index 1
    window [0..1] = [9, 1]
    heap root is 9 at index 0, still valid
    answer 9

right = 2, push 2 at index 2
    window [1..2] = [1, 2]
    heap root is still 9 at index 0, but index 0 expired
    pop it
    new root is 2 at index 2
    answer 2

right = 3, push 3 at index 3
    window [2..3] = [2, 3]
    root is 3 at index 3
    answer 3
```

Why stale entries below the root are okay:

```text
nums = [1, 3, -1, -3, 5], k = 3

When 5 enters, it becomes the root.
The old 3 may now be expired, but it is below 5.
It cannot affect the answer while 5 is the root.
If the old 3 ever rises to the root later, the cleanup loop will remove it
before returning an answer.
```

Interview nuance:

```text
Sliding Window Maximum's best-known interview solution is usually a monotonic
deque, not a heap.
```

The heap version is still worth understanding because it teaches lazy deletion:
stale indexes remain in the heap until they threaten to become the answer. But
if the interviewer asks for the optimal sliding-window maximum solution, explain
that the deque keeps candidates in decreasing value order and achieves O(n)
time. The heap variant is a practical alternative with O(n log n) time.

### 12.3 - Lazy deletion in graph heaps

Dijkstra-style algorithms often use the same idea:

```text
heap entry = (known_distance, node)
```

If a shorter distance to a node is found later, the old larger entry remains in
the heap. When it eventually pops, skip it if it is no longer current.

```python
dist, node = heapq.heappop(heap)
if dist != best[node]:
    continue
```

This is not wasted correctness. It is a deliberate tradeoff:

```text
Avoid deleting from the middle of the heap.
Allow stale entries.
Skip them when they reach the root.
```

### 12.4 - Lazy deletion checklist

Use lazy deletion when:

- heap entries can expire
- you can test validity from the entry's stored state
- expired entries are harmless unless they reach the root

Every lazy-deletion heap needs:

- enough metadata in each entry, such as an index, end time, or distance
- a cleanup loop before using `heap[0]`
- a clear definition of "valid now"

Common mistake:

```text
using if instead of while
```

If multiple stale entries are stacked at the root, one pop is not enough. Keep
popping until the root is valid.


---

## 13. Pattern 8: Graph Priority Queues

Heaps show up in graph problems when the next node to explore should be the
currently cheapest frontier state.

Typical heap entry:

```text
(cost_so_far, node)
```

or:

```text
(time, row, col)
(effort, row, col)
(price, stops_used, city)
```

The core invariant for Dijkstra:

```text
When edge weights are non-negative, the not-yet-finalized node with the smallest
known distance is safe to process next.
```

Examples:

- Network Delay Time: shortest path from one source.
- Swim in Rising Water: minimax path; priority is the highest elevation seen so
  far on the path.
- Cheapest Flights Within K Stops: state includes city and stop count, so a
  plain single-distance Dijkstra mental model is not enough.

Graph heap warning:

```text
The heap frontier is not just "nodes".
It is often "states".
```

For constrained shortest paths, reaching the same city with different stops
used can be meaningfully different. The heap entry and visited/best structure
must preserve the state dimension required by the problem.

### 13.1 - Three graph heap shapes

Graph heap problems look similar in code, but the priority and state can mean
different things.

| Shape | Heap entry | Best map / visited rule |
| --- | --- | --- |
| Plain shortest path | `(distance, node)` | one best distance per node |
| Minimax path | `(max_cost_seen, row, col)` | one best effort/time per cell |
| Constrained route | `(cost, city, stops_used)` | state includes city and stops |

Plain Dijkstra example:

```python
dist, node = heapq.heappop(heap)
if dist != best[node]:
    continue
```

This skip is lazy deletion. A newer shorter distance was pushed later, so the
older entry is stale.

Minimax example, as in Swim in Rising Water:

```text
priority = highest elevation seen on this path
next_priority = max(current_priority, grid[nr][nc])
```

The heap still pops the safest current frontier state first, but "cost" is no
longer a sum.

Constrained route warning:

```text
Cheapest Flights Within K Stops:
    reaching city X with 1 stop used
    is not the same state as reaching city X with 4 stops used
```

A plain `visited = {city}` can be wrong because the more expensive route to a
city may leave more stops available, or the cheaper route may use too many
stops to finish. Preserve the state dimension that affects future choices.

When the state has extra dimensions, say the dominance rule out loud:

```text
I can skip this popped state only if I already know another state that is at
least as cheap and at least as flexible for all future moves.
```

That sentence protects against applying single-node Dijkstra too broadly.


---

## 14. Choosing the Right Heap Shape

| Problem shape | Heap shape | Heap contains | Root means |
| --- | --- | --- | --- |
| kth largest stream | size-k min heap | k largest values seen | kth largest |
| k closest points | size-k max heap or all-point min heap | kept closest or all candidates | farthest kept or next closest |
| last stone weight | max heap | current stones | heaviest stone |
| merge k lists | min heap frontier | one current node per list | next output node |
| Design Twitter | max heap frontier | newest unreturned tweet per author | next feed tweet |
| k pairs smallest sums | min heap row frontier | one current pair per row | next pair |
| median stream | two heaps | lower half and upper half | median boundary |
| IPO | two frontiers | locked by capital, available by profit | best affordable profit |
| meeting rooms | min heap | active room end times | earliest room to free |
| sliding window max | max heap with indexes | seen candidates, some stale | max if root is valid |
| Dijkstra | min heap | discovered states | cheapest state to process |

Neighboring tools to compare against:

| Need | Often better than heap | Why |
| --- | --- | --- |
| Complete sorted order once | sorting | simpler and often same asymptotic cost |
| Static kth element only | quickselect | average O(n), no heap space |
| Fixed sliding-window max/min | monotonic deque | O(n), deletes expired items naturally |
| Frequent arbitrary deletion plus order | balanced tree / sorted list | heap deletes only the root efficiently |
| Small bounded integer priorities | buckets/counting | can avoid log factor |

This comparison is often where interviewers see whether you understand the heap
as a tool rather than a tag.


---

## 15. Correctness Invariants by Pattern

When explaining a heap solution, use the invariant that matches the pattern.

### Size-k heap

```text
After processing each item, the heap stores exactly the best k candidates seen
so far. The root is the weakest kept candidate.
```

### K-way merge

```text
The heap stores the best remaining candidate from each active source. Since each
source is internally sorted, the smallest/largest heap root is the next global
answer.
```

### Two heaps

```text
The lower heap and upper heap partition all values around the median. Their
sizes are balanced, and every lower value is <= every upper value.
```

### Two-frontier greedy

```text
All currently eligible choices are in the available heap. The heap root is the
best eligible choice. Items move into availability exactly once.
```

### Lazy deletion

```text
Before using the root, stale roots are removed. After cleanup, the root is both
best by priority and valid for the current state.
```

### Graph priority queue

```text
The heap stores discovered states ordered by best known cost. Stale or dominated
states are skipped when popped.
```


---

## 16. Common Failure Modes

### 16.1 - Confusing heap root with sorted order

`heap[0]` is meaningful. The rest of the list is only heap-ordered.

If you need sorted output:

```python
result = [heapq.heappop(heap) for _ in range(len(heap))]
```

or sort the final result if mutation is acceptable.

### 16.2 - Using raw list operations

These preserve heap order:

```python
heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heapreplace(heap, item)
```

These do not:

```python
heap.append(item)
heap.pop()
```

### 16.3 - Forgetting Python is min-heap only

For maximum priority:

```python
heapq.heappush(heap, -priority)
```

For tuple entries:

```python
heapq.heappush(heap, (-priority, extra_state))
```

Negate the priority, not the whole state.

### 16.4 - Missing tie-breakers

If priorities can tie and payloads are not naturally comparable, add a counter.

```python
heapq.heappush(heap, (priority, counter, payload))
```

### 16.5 - Rescanning instead of advancing the frontier

IPO can time out if every round rescans all projects. K-way merge can waste
space if it pushes every item from every source. The optimized heap solution
usually moves each item into the heap only when it becomes the next relevant
candidate.

### 16.6 - Not storing enough state

A heap entry must carry enough information to continue after popping.

Examples:

```text
Merge k lists:
    need the node, because node.next is the continuation

Find k pairs:
    need row and column, because (i, j + 1) is the continuation

Design Twitter:
    need author and tweet index, because the next older tweet is in the same
    author's stream

Sliding window:
    need index, because values expire by position
```

### 16.7 - Lazy deletion without cleanup

If entries can expire, always clean before reading the root.

```python
while heap and is_stale(heap[0]):
    heapq.heappop(heap)
```

Use `while`, not `if`, when multiple stale entries can accumulate.

### 16.8 - Pushing a cooldown item back too early

In Task Scheduler heap simulation, a task used in the current cycle must be held
outside the heap until the cycle ends. Otherwise the heap may choose it again
before the cooldown is satisfied.

### 16.9 - Treating a graph node as the full state

For constrained graph problems, the heap state might include remaining stops,
time, effort, keys, or another dimension. A `visited` set of only nodes can
discard valid future states.


---

## 17. Interview Explanation Templates

### 17.1 - Size-k heap

```text
I only need the top k candidates, so I keep a heap of size at most k. For kth
largest, I use a min heap: the root is the smallest among the k largest values
seen so far. When a new value is larger than the root, it belongs in the top k,
so I replace the root. Otherwise it cannot affect the answer. After scanning all
values, the root is the kth largest.
```

### 17.2 - K-way merge

```text
Each input source is already sorted, so I do not need to push all items. I push
only the current best item from each source. The heap root is the best candidate
globally. After popping from one source, I push that same source's next item.
That preserves one frontier candidate per active source.
```

### 17.3 - Two heaps for median

```text
I split the stream into a lower half and an upper half. The lower half is a max
heap and the upper half is a min heap. I maintain two invariants: sizes differ
by at most one, and every lower-half value is <= every upper-half value. Then
the median is either the top of the larger heap or the average of the two tops.
```

### 17.4 - Two-frontier greedy

```text
I separate eligibility from priority. First I move every newly eligible item into
an available heap. Then I choose the best item from that available heap. Each
item becomes available once, so the algorithm avoids repeated scans.
```

### 17.5 - Lazy deletion

```text
The heap may contain expired entries because deleting from the middle is not
efficient. That is okay because only the root can become the answer. Before I
use the root, I pop stale roots until the root is valid. Stale entries buried
below the root cannot affect the current answer.
```


---

## 18. Practice Progression

Use this order to build heap intuition from mechanics to harder frontier
problems.

### Stage 1 - Heap mechanics

Focus:

- Python min-heap behavior
- negative-value max heap
- root vs sorted order
- heapify, push, pop

Problems:

- Last Stone Weight
- Kth Largest Element in a Stream

Checkpoint:

```text
Can you explain why heap[0] is the answer boundary, even though the heap list is
not sorted?
```

### Stage 2 - Top k tradeoffs

Focus:

- size-k heap
- heapify-all-and-pop-k
- sorting vs heap vs quickselect
- duplicate/rank semantics

Problems:

- Kth Largest Element in an Array
- K Closest Points to Origin
- Top K Frequent Elements

Checkpoint:

```text
Can you choose between O(n log k), O(n + k log n), O(n log n), and quickselect,
and explain the tradeoff?
```

### Stage 3 - Frontier and k-way merge

Focus:

- one candidate per source
- advancing only the popped source
- tuple state
- tie-breakers

Problems:

- Merge k Sorted Lists
- Design Twitter
- Find K Pairs with Smallest Sums

Checkpoint:

```text
Can you name exactly what one heap entry means and what gets pushed after a pop?
```

### Stage 4 - Boundary maintenance

Focus:

- two heaps
- size invariant
- order invariant
- median boundary

Problems:

- Find Median from Data Stream

Checkpoint:

```text
Can you prove both invariants after every insertion, not just size balance?
```

### Stage 5 - Greedy availability

Focus:

- eligibility frontier
- available-choice heap
- moving each item once
- early stop when no available item exists

Problems:

- IPO
- Meeting Rooms II
- Minimum Interval to Include Each Query

Checkpoint:

```text
Can you explain why rescanning is unnecessary and why the greedy heap root is
safe to choose?
```

### Stage 6 - Simulation and lazy deletion

Focus:

- cooldown cycles
- stale entries
- cleanup before reading root

Problems:

- Task Scheduler
- Sliding Window Maximum, heap variant

Checkpoint:

```text
Can you explain why stale entries below the root are harmless?
```

### Stage 7 - Graph heaps

Focus:

- priority queue as exploration frontier
- stale distance entries
- node vs state
- constrained shortest paths

Problems:

- Network Delay Time
- Swim in Rising Water
- Cheapest Flights Within K Stops

Checkpoint:

```text
Can you define the heap state and the dominance rule for skipping stale states?
```


---

## 19. Quick Reference: Pattern Selection

| If the problem says... | Think... | First implementation idea |
| --- | --- | --- |
| kth largest in a stream | boundary of top k | size-k min heap |
| k closest / k smallest | top k by score | sort, heap, or quickselect |
| repeatedly take largest/smallest | dynamic best candidate | heapify all and pop |
| merge k sorted sources | one frontier per source | k-way heap merge |
| median from stream | boundary between halves | two heaps |
| choose best affordable/eligible item | eligibility + priority | sorted/min frontier plus max heap |
| active intervals by end | earliest finishing active item | min heap of end times |
| window max with heap | values expire by index | max heap plus lazy deletion |
| shortest path / minimum effort | best exploration frontier | min heap of states |


---

## 20. Final Checklist Before Submitting

Before calling a heap solution done, verify:

- The heap entry stores all state needed after a pop.
- The priority matches what should be chosen next.
- Python min-heap vs max-heap sign conventions are correct.
- Tuple tie cases cannot compare unsupported payload objects.
- The heap size is intentional: O(k), O(number of sources), O(n), or another
  justified bound.
- Lazy deletion cleanup runs before reading `heap[0]`.
- Each item is pushed/popped the expected number of times.
- Edge cases are covered: empty input, `k = 0`, `k = 1`, `k = n`, duplicates,
  ties, negative values, and initially fewer than k stream values when relevant.
- The explanation includes the invariant, not only the code mechanics.

Heap interview success is mostly about naming the frontier. Once the frontier is
clear, `heapq` is just the tool that keeps the best candidate reachable.
