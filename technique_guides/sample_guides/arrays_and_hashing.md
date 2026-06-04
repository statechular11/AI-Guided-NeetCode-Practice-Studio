# Arrays and Hashing - A Complete Guide for Coding Interviews

## 1. What Are Arrays and Hashing?

**Arrays** store ordered values and give O(1) access by index. In Python, the
usual interview "array" is a `list`.

**Hashing** uses a hash table to make lookup fast. In Python, the main hash
table tools are:

- `set`: stores unique values and answers "have I seen this value?"
- `dict`: maps a key to information, such as an index, count, list, or state
- `collections.Counter`: counts how many times each value appears
- `collections.defaultdict`: creates missing values automatically, often for
  grouping

The central idea is simple:

```text
Instead of searching the past again and again, remember the useful facts in a
hash table so future checks are O(1) on average.
```

That one move turns many O(n^2) brute-force solutions into O(n) solutions.

Example: Two Sum.

```text
Brute force:
For every pair (i, j), check nums[i] + nums[j].
Time: O(n^2)

Hash-map approach:
For each value x, ask whether target - x has already appeared.
Time: O(n)
```

Hashing is one of the first major interview accelerators because it replaces
"compare with everything" with "look up the one fact I need."

### 1.1 - What hashing gives you

A hash table uses a key's hash value to jump near where that key should live.
Python then confirms equality among any keys that land in the same area.

```text
key -> hash(key) -> table location -> equality check -> value / membership
```

For interview reasoning, the practical model is:

```text
I can ask "is this exact key present?" in O(1) average time.
```

Two details matter:

- The key must be hashable, which usually means immutable in Python.
- The key must represent exactly the identity you care about.

Examples:

```python
seen.add(42)                  # int is hashable
groups[("a", 1)].append(word) # tuple is hashable if its contents are hashable
groups[[1, 0, 2]].append(word) # list is mutable, so this is invalid
```

Hashing does not magically solve ordering. It makes exact lookup fast. If the
question needs sorted order, nearest values, or range queries, you may need
sorting, two pointers, binary search, a heap, or a tree-like structure instead.


---

## 2. The Core Mental Model

Before choosing a data structure, ask:

```text
What question do I need to answer quickly?
```

Then choose the smallest hash-based structure that answers that question.

| Question | Structure | Example |
| --- | --- | --- |
| Have I seen this value before? | `set` | Contains Duplicate |
| Where did I see this value? | `dict[value] = index` | Two Sum |
| How many times did each value appear? | `Counter` or `dict[value] += 1` | Valid Anagram |
| Which items share the same identity/key? | `defaultdict(list)` | Group Anagrams |
| Which state has already appeared in this scope? | `set` of markers | Valid Sudoku |
| Can this value start a unique structure? | `set` membership | Longest Consecutive Sequence |

This is the most important Arrays and Hashing habit: do not start by coding.
First name the fast question.

### 2.1 - Hash-state design worksheet

Before writing a hash-based solution, fill in the state explicitly.

| Design question | Common answer | Example |
| --- | --- | --- |
| What is the key? | value, character, tuple, normalized form | `target - x`, `tuple(counts)`, `(row, digit)` |
| What does the value store? | index, count, list, boolean, last position | `value -> index`, `char -> count` |
| What does the state mean before each iteration? | past only, current window, all input, one scope | Two Sum map contains earlier indices only |
| When do I update it? | before lookup, after lookup, after shrinking | lookup-before-insert for Two Sum |
| Can values repeat? | no, yes with counts, yes with lists | anagram counts, grouped words |
| Does order matter? | preserve input order, output arbitrary, sorted needed | Top K output often arbitrary |

This worksheet catches many quiet bugs. A `set` is enough when the answer only
depends on membership. A `dict` is needed when the key must retrieve more
information. A count map is needed when repeated values are part of the meaning.

Example:

```text
Two Sum
    key: previous number
    value: previous index
    state before i: values from indices < i
    update order: lookup complement first, then insert nums[i]

Group Anagrams
    key: canonical form of the word
    value: list of words in that group
    state meaning: groups built from words already processed

Longest Consecutive Sequence
    key/state: complete set of unique values
    update order: build the full set first, then scan for starts
```


---

## 3. Arrays vs Hash Tables

Arrays and hash tables solve different kinds of lookup.

### 3.1 - Array lookup

Array lookup is best when the key is already an index.

```python
nums[i]
```

Use array indexing when:

- the data is naturally positional
- you need neighbors like `i - 1` or `i + 1`
- you need a fixed-size count array, such as 26 lowercase letters
- you need prefix/suffix accumulation by position

Example: count lowercase English letters.

```python
counts = [0] * 26
for ch in s:
    counts[ord(ch) - ord("a")] += 1
```

This is O(1) space because there are always only 26 possible lowercase letters.

### 3.2 - Hash-table lookup

Hash-table lookup is best when the key is not a compact index.

```python
seen.add(value)
index_by_value[value] = i
count[value] += 1
```

Use hash tables when:

- values can be large, negative, sparse, or strings
- you need membership checks
- you need to group by a computed key
- you need to preserve arbitrary relationships, such as value -> index

Example: count arbitrary integers.

```python
from collections import Counter

count = Counter(nums)
```

This uses O(k) space, where `k` is the number of distinct values.

### 3.3 - Fixed array vs hash map

When a key has a small known integer range, an array can be simpler and faster
than a hash map.

| Situation | Prefer | Why |
| --- | --- | --- |
| lowercase English letters | `[0] * 26` | compact fixed range |
| digits 1 through 9 | bitmask or `[False] * 10` | tiny fixed range |
| arbitrary integers | `dict` / `Counter` | sparse and possibly large/negative |
| arbitrary strings | `dict` / `Counter` | no compact numeric index |

The fixed-array version is an optimization built on a constraint. If the
constraint changes, the data structure may need to change too.

```text
Valid Anagram with lowercase English:
    26-count array works.

Valid Anagram with arbitrary Unicode:
    Counter is safer.
```


---

## 4. Complexity Basics

For Python `dict` and `set`:

| Operation | Average Time |
| --- | --- |
| Insert key | O(1) |
| Delete key | O(1) |
| Check membership | O(1) |
| Read value by key | O(1) |

Interview solutions normally state hash-table operations as O(1) average time.
The theoretical worst case can be worse if many keys collide, but that is not
usually the focus unless the interviewer asks about hash implementation details.

Space is usually O(k), where `k` is the number of distinct keys stored. In many
array problems, `k <= n`, so the answer is often written as O(n) space.

Important Python detail: hash-table keys must be hashable. Immutable types like
`int`, `str`, and `tuple` can be keys. Mutable types like `list`, `dict`, and
`set` cannot.

```python
key = tuple(counts)      # valid dictionary key
bad_key = counts         # invalid if counts is a list
```

Hashability has two interview consequences:

- Convert mutable state into an immutable key before storing it.
- Do not mutate an object after using it as part of a key.

For canonical keys, prefer building a fresh immutable representation:

```python
counts = [0] * 26
...
key = tuple(counts)
```

The tuple is a snapshot. Later changes to the `counts` list do not change keys
already stored in the dictionary.


---

## 5. Fundamental Pattern 1: Seen Set

**Problem shape:** Detect whether a value has appeared before.

**Core question:** Is the current value already in `seen`?

Template:

```python
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

Why the order matters:

```text
Check first, then add.
```

If the problem asks whether a duplicate already exists, the current value should
be compared against earlier values. After the check, it becomes part of the past
for later values.

### Application: Contains Duplicate

For 217. Contains Duplicate, sorting is a valid comparison point:

```python
def contains_duplicate_sorting(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
```

But the hash-set solution is the usual final answer:

```python
def contains_duplicate(nums):
    return len(set(nums)) != len(nums)
```

or the explicit early-return version:

```python
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

The explicit version is easier to extend when the interview problem has extra
conditions, such as distance or window constraints.


---

## 6. Fundamental Pattern 2: Complement Lookup

**Problem shape:** Find two values that satisfy an equation.

**Core question:** Given current value `x`, have I already seen the value that
would complete the answer?

For Two Sum:

```text
x + y = target
y = target - x
```

Template:

```python
def two_sum(nums, target):
    index_by_value = {}

    for i, x in enumerate(nums):
        need = target - x
        if need in index_by_value:
            return [index_by_value[need], i]
        index_by_value[x] = i
```

### Application: Two Sum

For 1. Two Sum, the key invariant is:

```text
index_by_value contains only values from earlier indices.
```

That is why the lookup happens before the insert. It prevents reusing the same
element twice.

Example:

```text
nums = [3, 3], target = 6

i = 0, x = 3, need = 3
3 not in map, store 3 -> 0

i = 1, x = 3, need = 3
3 is in map at index 0, return [0, 1]
```

The duplicate value is allowed because it appears at two different indices.

This pattern generalizes to many pair-search problems:

- target sum
- target difference
- matching prefix sums
- finding a previous state that makes the current state valid


---

## 7. Fundamental Pattern 3: Frequency Counts

**Problem shape:** Order does not matter, but multiplicity does.

**Core question:** Do two collections have the same counts?

### Application: Valid Anagram

For 242. Valid Anagram, these two strings are not equivalent:

```text
"aab" and "abb"
```

They have the same set of letters, but different counts.

Pythonic version:

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

Fixed lowercase-English version:

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    counts = [0] * 26

    for a, b in zip(s, t):
        counts[ord(a) - ord("a")] += 1
        counts[ord(b) - ord("a")] -= 1

    return all(count == 0 for count in counts)
```

The fixed-array version is only correct because the standard constraints limit
characters to lowercase English letters. If the input could contain arbitrary
Unicode characters, use `Counter`.

### Frequency-count checklist

When using counts, always clarify:

- Are values limited to a small alphabet? Use an array.
- Are values arbitrary? Use `Counter` or `dict`.
- Does multiplicity matter? Use counts, not a set.
- Is order irrelevant? Counts or canonical keys are likely useful.


---

## 8. Fundamental Pattern 4: Canonical Keys

**Problem shape:** Group items that are equivalent under some transformation.

**Core question:** Can I create the same key for all equivalent objects?

For anagrams, the actual string order differs, but the character multiset is the
same.

Two common canonical keys:

```text
"eat" -> "aet"                 sorted string key
"eat" -> (1, 0, 0, 0, 1, ...)   26-count tuple key
```

### Application: Group Anagrams

For 49. Group Anagrams, the simplest correct solution sorts each word:

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
```

Complexity:

```text
n = number of words
k = maximum word length

Time: O(n * k log k)
Space: O(n * k)
```

The optimized lowercase-English key uses counts:

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord("a")] += 1

        groups[tuple(counts)].append(word)

    return list(groups.values())
```

Complexity:

```text
Time: O(n * k)
Space: O(n * k)
```

The important move is not the exact key. The important move is:

```text
Equivalent objects must map to exactly the same immutable key.
Non-equivalent objects should map to different keys.
```

Trace:

```text
strs = ["eat", "tea", "tan", "ate"]

word "eat":
    sorted key = "aet"
    groups["aet"] = ["eat"]

word "tea":
    sorted key = "aet"
    groups["aet"] = ["eat", "tea"]

word "tan":
    sorted key = "ant"
    groups["ant"] = ["tan"]

word "ate":
    sorted key = "aet"
    groups["aet"] = ["eat", "tea", "ate"]
```

The same trace works with a count-tuple key; only the representation changes.
The grouping logic stays the same.

### Canonical-key examples

| Problem type | Canonical key |
| --- | --- |
| Anagrams | sorted string or count tuple |
| Same slope | reduced fraction `(dy / g, dx / g)` |
| Same diagonal | `row - col` or `row + col` |
| Same 3x3 Sudoku box | `(row // 3, col // 3)` |
| Same graph state | tuple of normalized values |

If a key is wrong, the algorithm may still look clean while silently merging
states that should stay separate, or separating states that should be together.


---

## 9. Fundamental Pattern 5: Count, Then Select

**Problem shape:** Find the most frequent, least frequent, or top-k values.

**Core question:** Once I know every frequency, what is the best way to retrieve
the desired values?

The first phase is usually fixed:

```python
from collections import Counter

count = Counter(nums)
```

The second phase depends on the requirement.

Let:

```text
n = total number of input values
d = number of distinct values
m = number of values requested
```

| Selection method | Time | Best for |
| --- | --- | --- |
| Sort by frequency | O(d log d) | Simple and clear |
| Size-m heap | O(d log m) | Top `m` when `m` is small |
| Bucket sort | O(n + d) | Frequencies are bounded by `n` |
| Quickselect | Average O(d) | Advanced in-place selection |

### Application: Top K Frequent Elements

For 347. Top K Frequent Elements, bucket sort works because a frequency can only
be between `1` and `len(nums)`.

```python
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for value, freq in count.items():
        buckets[freq].append(value)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for value in buckets[freq]:
            result.append(value)
            if len(result) == k:
                return result
```

The bucket index is the frequency. By scanning buckets from high frequency to
low frequency, the first `k` values collected are top-k frequent values.

Trace:

```text
nums = [1, 1, 1, 2, 2, 3], k = 2

count:
    1 -> 3
    2 -> 2
    3 -> 1

buckets:
    freq 1: [3]
    freq 2: [2]
    freq 3: [1]

scan from high to low:
    freq 3 gives 1
    freq 2 gives 2

answer can be [1, 2]
```

The result order is usually not important for this problem. What matters is
that every returned value has one of the `k` highest frequencies.

### Heap version

Python's `heapq` is a min-heap.

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []

    for value, freq in count.items():
        heapq.heappush(heap, (freq, value))
        if len(heap) > k:
            heapq.heappop(heap)

    return [value for freq, value in heap]
```

This keeps only the best `k` candidates seen so far. The smallest frequency
among the kept candidates is at the top and gets removed when the heap grows too
large.

Use the bucket version when you want the optimized linear-time interview answer.
Use the heap version when you want a reusable top-k pattern.


---

## 10. Fundamental Pattern 6: Prefix and Suffix State

Arrays and Hashing sections often include array-state patterns that are not
hashing. Prefix and suffix accumulation is one of the most important.

**Problem shape:** The answer at index `i` depends on everything before `i` and
everything after `i`.

**Core question:** Can I split the answer into left contribution and right
contribution?

### Application: Product of Array Except Self

For 238. Product of Array Except Self:

```text
answer[i] = product(nums before i) * product(nums after i)
```

Canonical O(1)-extra-space version, excluding the output array:

```python
def product_except_self(nums):
    answer = [1] * len(nums)

    prefix = 1
    for i, x in enumerate(nums):
        answer[i] = prefix
        prefix *= x

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
```

The invariant is:

```text
When answer[i] is updated, prefix and suffix exclude nums[i].
```

This naturally handles zeros:

```text
[2, 0, 4] -> [0, 8, 0]
[0, 4, 0] -> [0, 0, 0]
```

No division is needed, and no special zero branches are needed.

Step trace:

```text
nums = [1, 2, 3, 4]

forward pass stores products strictly left of i:

i = 0, prefix = 1  -> answer[0] = 1, prefix becomes 1
i = 1, prefix = 1  -> answer[1] = 1, prefix becomes 2
i = 2, prefix = 2  -> answer[2] = 2, prefix becomes 6
i = 3, prefix = 6  -> answer[3] = 6, prefix becomes 24

answer after forward pass:
    [1, 1, 2, 6]

backward pass multiplies products strictly right of i:

i = 3, suffix = 1  -> answer[3] = 6,  suffix becomes 4
i = 2, suffix = 4  -> answer[2] = 8,  suffix becomes 12
i = 1, suffix = 12 -> answer[1] = 12, suffix becomes 24
i = 0, suffix = 24 -> answer[0] = 24, suffix becomes 24

final:
    [24, 12, 8, 6]
```

The important timing is:

```text
use prefix/suffix first, then multiply it by nums[i]
```

That keeps the current index excluded from its own answer.


---

## 11. Fundamental Pattern 7: Multiple Independent Scopes

**Problem shape:** Each value must be unique or valid across several scopes.

**Core question:** Which scopes does this value belong to, and has it appeared
in any of them?

### Application: Valid Sudoku

For 36. Valid Sudoku, every filled cell belongs to:

- one row
- one column
- one 3x3 box

Set-based version:

```python
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            digit = board[r][c]
            if digit == ".":
                continue

            box = (r // 3) * 3 + (c // 3)

            if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                return False

            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box].add(digit)

    return True
```

The box formula is worth making automatic:

```text
box = (row // 3) * 3 + (col // 3)
```

This maps:

```text
box index grid:

        cols
        0 1 2 | 3 4 5 | 6 7 8
rows 0    0   |   1   |   2
     1    0   |   1   |   2
     2    0   |   1   |   2
       -------+-------+-------
     3    3   |   4   |   5
     4    3   |   4   |   5
     5    3   |   4   |   5
       -------+-------+-------
     6    6   |   7   |   8
     7    6   |   7   |   8
     8    6   |   7   |   8
```

Bitmask variant:

```python
def is_valid_sudoku(board):
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9

    for r in range(9):
        for c in range(9):
            digit = board[r][c]
            if digit == ".":
                continue

            bit = 1 << (int(digit) - 1)
            box = (r // 3) * 3 + (c // 3)

            if rows[r] & bit or cols[c] & bit or boxes[box] & bit:
                return False

            rows[r] |= bit
            cols[c] |= bit
            boxes[box] |= bit

    return True
```

The bitmask version compresses each scope's set into one integer. For interviews,
the set version is often easier to write and explain. The bitmask version is a
nice optimization once the scope invariant is clear.


---

## 12. Fundamental Pattern 8: Start-Only Expansion

**Problem shape:** Values form chains or components, but expanding from every
value repeats work.

**Core question:** Which values are the unique starts?

### Application: Longest Consecutive Sequence

For 128. Longest Consecutive Sequence, the target is O(n), so sorting is not the
final answer.

The hash-set insight:

```text
x starts a sequence only if x - 1 is absent.
```

There are two distinct phases:

```text
1. Build values = set(nums).
2. Scan unique values and expand only from sequence starts.
```

The first phase matters. When the scan begins, the set already contains every
input value, no matter where it appeared in the original order. A start value can
find all later numeric values immediately by membership lookup; it does not wait
for those values to appear later in the scan.

Code:

```python
def longest_consecutive(nums):
    values = set(nums)
    best = 0

    for x in values:
        if x - 1 in values:
            continue

        y = x
        while y in values:
            y += 1

        best = max(best, y - x)

    return best
```

Why this is O(n):

- Each sequence is expanded only from its first value.
- Duplicates are removed by `set(nums)`.
- Across all while-loops, each unique value is visited as part of one forward
  expansion.

The key is to iterate over `values`, not the original `nums`. If the original
input has many duplicates, iterating over `nums` can repeat the same start check
and expansion work unnecessarily.

Example:

```text
nums = [100, 4, 200, 1, 3, 2]
values = {1, 2, 3, 4, 100, 200}

1 is a start because 0 is absent:
  count 1, 2, 3, 4 -> length 4

2, 3, 4 are not starts because predecessor exists.
100 is a start -> length 1
200 is a start -> length 1

answer = 4
```


---

## 13. Fundamental Pattern 9: Length-Prefix Encoding

Arrays and Hashing also includes design-style string problems where the main
skill is choosing a representation that can be decoded without ambiguity.

### Application: Encode and Decode Strings

For 271. Encode and Decode Strings, a simple delimiter is not robust:

```text
["a#b", "c"] joined with "#" becomes "a#b#c"
```

During decoding, there is no way to know which `#` characters are separators and
which are part of the payload.

Length-prefix encoding fixes that:

```text
<length>#<payload>
```

Example:

```text
["leet", "code", "", "a#b"]

encoded:
4#leet4#code0#3#a#b
```

Code:

```python
class Codec:
    def encode(self, strs):
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            result.append(s[start:start + length])
            i = start + length

        return result
```

The separator only separates the length field from the payload. The payload can
contain any character, including `#`, because the decoder uses the length to
know exactly how many characters to take.

Decode trace:

```text
encoded = "4#leet4#code0#3#a#b"

i = 0:
    read digits until # -> length 4
    take next 4 chars -> "leet"
    move i after payload

i = 6:
    read digits until # -> length 4
    take next 4 chars -> "code"

i = 12:
    read digits until # -> length 0
    take next 0 chars -> ""

i = 14:
    read digits until # -> length 3
    take next 3 chars -> "a#b"
```

The decoder never searches inside the payload for a separator. It trusts the
length.


---

## 14. Decision Framework

When you see a new problem, use this decision tree.

### 14.1 - Do I need membership?

Use a set.

```python
if x in seen:
    ...
seen.add(x)
```

Typical phrases:

- "contains duplicate"
- "has appeared before"
- "exists in array"
- "consecutive values"

### 14.2 - Do I need to retrieve associated information?

Use a dictionary.

```python
index_by_value[x] = i
count_by_value[x] += 1
group_by_key[key].append(x)
```

Typical phrases:

- "return indices"
- "find matching previous value"
- "group by"
- "count occurrences"

### 14.3 - Does order not matter, but counts matter?

Use a frequency map.

```python
Counter(a) == Counter(b)
```

Typical phrases:

- "anagram"
- "permutation"
- "same multiset"
- "top k frequent"

### 14.4 - Are equivalent items hidden behind different surface forms?

Create a canonical key.

```python
key = "".join(sorted(word))
key = tuple(counts)
```

Typical phrases:

- "group"
- "same pattern"
- "same normalized form"
- "equivalent under reordering"

### 14.5 - Does each index need left and right context?

Use prefix/suffix state.

```python
left contribution * right contribution
```

Typical phrases:

- "except self"
- "before and after"
- "without current element"
- "product/sum around each index"

### 14.6 - Does repeated expansion create O(n^2)?

Find unique starts.

```python
if x - 1 not in values:
    expand from x
```

Typical phrases:

- "longest consecutive"
- "sequence"
- "component"
- "chain"

### 14.7 - Would sorting or two pointers simplify the problem?

Hashing is powerful, but it is not always the final tool.

| Problem shape | Often consider | Why |
| --- | --- | --- |
| input is already sorted | two pointers / binary search | order is useful signal |
| need all answers in sorted order | sorting | hash table loses order |
| need nearest smaller/larger value | sorting or tree-like structure | exact lookup is not enough |
| static top-k by score | heap, bucket, quickselect | counting is only phase one |
| need contiguous window with deletions | sliding window map/deque | state must shrink as left moves |

Example: Two Sum and Two Sum II look similar but use different structure:

```text
unsorted Two Sum:
    hash map gives O(n) exact complement lookup

sorted Two Sum II:
    two pointers use sorted order and O(1) extra space
```

The right question is not "can I use a hash map?" The right question is "which
existing structure in the input gives me the cheapest useful lookup?"


---

## 15. Correctness Invariants

A good interview explanation should name the invariant, not just the code.

### Seen-set invariant

```text
Before processing nums[i], seen contains exactly the values from nums[0:i].
```

This supports duplicate detection and prevents accidentally treating the current
value as part of the past.

### Two Sum invariant

```text
Before storing nums[i], the map contains only earlier indices.
```

That is why one-pass Two Sum can never reuse the same element.

### Frequency invariant

```text
Two collections are equivalent only if every key has the same count.
```

A set is not enough when multiplicity matters.

### Canonical-key invariant

```text
All equivalent objects produce the same immutable key.
```

For Group Anagrams, every anagram of `"eat"` must produce the same key.

### Bucket-sort invariant

```text
Every value in buckets[f] appears exactly f times.
```

Scanning buckets from high to low frequency yields values in descending
frequency order.

### Prefix/suffix invariant

```text
When updating answer[i], the running prefix/suffix excludes nums[i].
```

Including the current value creates "product including self," which is the
opposite of the problem requirement.

### Scope invariant

```text
Each independent scope has its own seen state.
```

For Sudoku, rows, columns, and boxes must be checked independently.

### Start-only invariant

```text
Only the first value of a sequence is allowed to launch expansion.
```

For Longest Consecutive Sequence, `x` launches expansion only when `x - 1` is
absent.


---

## 16. Failure Modes to Guard Against

### 16.1 - Using a set when counts matter

Bad model:

```text
"aab" and "abb" both have letters {a, b}
```

Correct model:

```text
"aab" -> a:2, b:1
"abb" -> a:1, b:2
```

If multiplicity matters, use counts.

### 16.2 - Storing before lookup in one-pass Two Sum

If you store first, then `target = 2 * nums[i]` can accidentally match the
current element with itself.

Correct order:

```python
need = target - x
if need in index_by_value:
    return [index_by_value[need], i]
index_by_value[x] = i
```

### 16.3 - Using a mutable key

This fails:

```python
groups[counts].append(word)     # counts is a list
```

Use:

```python
groups[tuple(counts)].append(word)
```

### 16.4 - Forgetting constraints behind optimized keys

A 26-count array assumes lowercase English letters. If the problem allows
uppercase, punctuation, or arbitrary Unicode characters, use a more general key.

### 16.5 - Repeating expansion work

For Longest Consecutive Sequence, expanding from every number can become O(n^2).
Expand only from starts:

```python
if x - 1 not in values:
    ...
```

### 16.6 - Confusing output order requirements

Some hash-table problems do not care about order:

- Group Anagrams: order of groups does not matter
- Top K Frequent Elements: answer order usually does not matter

Other problems do care:

- Return original indices
- Preserve input order
- Encode/decode must round-trip exactly

Read the output contract carefully.

### 16.7 - Treating delimiters as always safe

If strings may contain any character, delimiter-only encoding is ambiguous.
Length-prefix encoding is robust because the decoder takes an exact number of
payload characters.

### 16.8 - Updating prefix/suffix in the wrong order

For Product of Array Except Self, update the running product after using it for
the current index.

```python
answer[i] *= suffix
suffix *= nums[i]
```

This keeps `suffix` strictly to the right of `i` when it is multiplied into the
answer.

### 16.9 - Accidentally depending on hash-table output order

Python dictionaries preserve insertion order, but many interview problem
contracts do not require hash-map output to be ordered. Do not add sorting work
unless the problem asks for a specific order.

Conversely, if the problem does require sorted output, a hash table alone is not
enough. Sort the final result or choose an order-aware approach.

### 16.10 - Letting `defaultdict` create keys during checks

Reading a missing key from `defaultdict` creates that key:

```python
from collections import defaultdict

count = defaultdict(int)
if count[x] == 0:   # this inserts x with value 0
    ...
```

This is usually harmless for simple counting, but it can pollute state during
membership-style logic. When you only want to ask whether a key exists, use:

```python
if x in count:
    ...
```


---

## 17. Python Tools to Know

### `set`

```python
seen = set()
seen.add(x)
if x in seen:
    ...
seen.remove(x)      # error if absent
seen.discard(x)     # no error if absent
```

Use `set` for membership and uniqueness.

### `dict`

```python
index_by_value = {}
index_by_value[x] = i

if x in index_by_value:
    ...
```

Use `dict` when the key needs associated information.

### `Counter`

```python
from collections import Counter

count = Counter(nums)
count[x] += 1
most_common = count.most_common(k)
```

Use `Counter` for clean frequency logic. Be ready to explain the manual version
if the interviewer wants fundamentals.

Manual count:

```python
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1
```

### `defaultdict`

```python
from collections import defaultdict

groups = defaultdict(list)
groups[key].append(value)
```

Use `defaultdict(list)` for grouping.

Use `defaultdict(int)` for counting when you do not need `Counter` features.

### `enumerate`

```python
for i, x in enumerate(nums):
    ...
```

Use `enumerate` when the answer needs indices.

### `zip`

```python
for a, b in zip(s, t):
    ...
```

Useful for paired scans after verifying equal lengths.

### Sorting as a baseline

Sorting often gives a simpler O(n log n) baseline:

- Contains Duplicate by adjacent comparison
- Valid Anagram by comparing sorted strings
- Group Anagrams by sorted-string key

Hashing often improves the final answer to O(n), but sorting baselines are good
for explaining tradeoffs.

### Hashing with windows

Later sliding-window problems reuse the same hash tools with a moving scope:

```python
count[ch] += 1      # right side enters
count[left_ch] -= 1 # left side leaves
```

The extra invariant is that the map describes only the current window, not the
whole prefix. Remove or ignore zero counts when equality of maps matters.


---

## 18. Typical Interview Applications

### 18.1 - Duplicate detection

Use a seen set.

Practice:

- 217. Contains Duplicate
- 219. Contains Duplicate II after sliding window

### 18.2 - Pair lookup

Use a map from value to index or count.

Practice:

- 1. Two Sum
- 167. Two Sum II as the sorted two-pointer contrast

### 18.3 - Multiset comparison

Use counts.

Practice:

- 242. Valid Anagram
- 567. Permutation in String after sliding window

### 18.4 - Grouping by normalized form

Use a canonical key and `defaultdict(list)`.

Practice:

- 49. Group Anagrams

### 18.5 - Top-k frequency

Count first, then select with bucket sort or heap.

Practice:

- 347. Top K Frequent Elements

### 18.6 - Delimiter-safe encoding

Use explicit lengths rather than trusting a separator.

Practice:

- 271. Encode and Decode Strings

### 18.7 - Prefix/suffix array state

Track left and right contributions separately.

Practice:

- 238. Product of Array Except Self

### 18.8 - Multi-scope validation

Maintain separate state for each independent scope.

Practice:

- 36. Valid Sudoku

### 18.9 - Hash-set sequence starts

Use set membership to identify unique starts.

Practice:

- 128. Longest Consecutive Sequence


---

## 19. Practice Progression

Use this order to build the technique from basic to interview-ready.

### Stage 1 - Basic membership and counts

1. 217. Contains Duplicate
2. 242. Valid Anagram
3. 1. Two Sum

Goal:

```text
Know exactly when to use set, dict, and Counter.
```

### Stage 2 - Canonical keys and grouping

4. 49. Group Anagrams

Goal:

```text
Convert an object into an immutable identity key.
```

### Stage 3 - Counting plus selection

5. 347. Top K Frequent Elements

Goal:

```text
Separate counting from retrieval, then choose sort, heap, bucket, or quickselect.
```

### Stage 4 - Array-state techniques

6. 238. Product of Array Except Self

Goal:

```text
Explain prefix/suffix state and exclude the current index correctly.
```

### Stage 5 - Multi-scope and compressed state

7. 36. Valid Sudoku

Goal:

```text
Maintain independent seen state for rows, columns, and boxes.
```

### Stage 6 - O(n) set invariants

8. 128. Longest Consecutive Sequence

Goal:

```text
Use set membership to identify unique starts and avoid repeated work.
```

### Stage 7 - Representation design

9. 271. Encode and Decode Strings

Goal:

```text
Design a representation that round-trips every allowed input.
```


---

## 20. Interview Explanation Templates

### Contains Duplicate

```text
I only need to know whether a value appeared before, so I keep a set of seen
values. For each number, if it is already in the set, I found a duplicate.
Otherwise I add it and continue. This is O(n) average time and O(n) space.
```

### Two Sum

```text
For each number x, the only partner that can complete the target is target - x.
I keep a map from previously seen value to index. I check the complement before
storing x, so I never reuse the same index. This is O(n) average time and O(n)
space.
```

### Valid Anagram

```text
Anagrams have the same character multiplicities. I can count each character in
both strings and compare the counts. Under lowercase-English constraints, I can
use a fixed 26-element array; otherwise I can use Counter.
```

### Group Anagrams

```text
I need all anagrams to share the same key. Sorting each word gives a canonical
key, so I group words by that key in a dictionary. If optimizing under
lowercase-English constraints, I can use a 26-count tuple instead of sorting.
```

### Top K Frequent Elements

```text
First I count every value. Since a frequency is between 1 and n, I can bucket
values by frequency and scan buckets from high to low until I collect k values.
This gives O(n) time and O(n) space.
```

### Product of Array Except Self

```text
The answer at each index is product of everything to the left times product of
everything to the right. I store left products in the output, then scan from
right to left with a running suffix product. I update the suffix after using it,
so the current value is excluded.
```

### Valid Sudoku

```text
Each filled digit must be unique in three scopes: its row, its column, and its
3x3 box. I keep separate seen state for each scope. For every digit, if it has
already appeared in any of those scopes, the board is invalid; otherwise I add
it to all three scopes.
```

### Longest Consecutive Sequence

```text
I put all values in a set for O(1) membership checks. A number starts a sequence
only if number - 1 is not present. I expand only from starts, so every sequence
is counted once and the total work is O(n).
```


---

## 21. Practice Checkpoints From This Track

These checkpoints are the high-signal details worth revisiting after finishing
the first Arrays and Hashing pass.

### 21.1 - Keep the structure as small as the question

For duplicate detection, a boolean question only needs a set. Counting every
frequency is correct, but it adds state the problem does not ask for.

Practice prompt:

```text
Can I answer the problem with membership only, or do I need associated data?
```

### 21.2 - Treat multiplicity as a separate requirement

For anagram-style problems, the same letters are not enough. The counts must
match.

Practice prompt:

```text
Would a set lose information that the problem needs?
```

### 21.3 - Look up before inserting when current index cannot be reused

For one-pass pair lookup, the map should represent the past, not the past plus
the current element.

Practice prompt:

```text
What exactly is inside my hash map before this iteration starts?
```

### 21.4 - Make canonical keys immutable and complete

For grouping, the key must contain all information needed to define the group,
and it must be hashable.

Practice prompt:

```text
Do all equivalent values produce the same key, and can that key be used in a dict?
```

### 21.5 - Separate counting from selection

Top-k frequency problems usually have two phases: count everything, then choose
how to retrieve the answer. The retrieval method is a separate design decision.

Practice prompt:

```text
After counting, is sort, heap, bucket, or quickselect the right selector?
```

### 21.6 - Use bounded ranges when they exist

Bucket sort becomes available when the bucket index has a known small range.
For Top K Frequent Elements, the frequency range is `1..len(nums)`.

Practice prompt:

```text
Is the value I am sorting by bounded enough to become an array index?
```

### 21.7 - Name whether running products include or exclude the current index

For prefix/suffix problems, most bugs come from updating the running value on the
wrong side of the current index.

Practice prompt:

```text
At the moment I write answer[i], does my running state include nums[i]?
```

### 21.8 - Isolate independent scopes

For Sudoku-style validation, a digit can be valid in one scope and invalid in
another. Rows, columns, and boxes need separate state.

Practice prompt:

```text
Which independent scopes does this value participate in?
```

### 21.9 - Count each structure from its unique start

For Longest Consecutive Sequence, the O(n) guarantee depends on expanding only
from sequence starts and iterating over unique values.

Practice prompt:

```text
What condition proves this value is the first element of the structure?
```

### 21.10 - Design encodings around decoding, not just joining

For string encoding, the encoded form must be unambiguous for every allowed
payload, including empty strings and strings containing separators.

Practice prompt:

```text
Can the decoder know exactly where each payload ends without guessing?
```


---

## 22. Mastery Checklist

You are interview-ready for Arrays and Hashing when you can do the following
without looking at a reference:

- Choose between `set`, `dict`, `Counter`, `defaultdict`, and fixed arrays.
- Explain why hash-table lookup changes many brute-force solutions from O(n^2)
  to O(n).
- Write one-pass Two Sum with lookup before insert.
- Explain why counts are different from membership.
- Build a canonical immutable key for grouping.
- Compare sorted-string and count-tuple anagram keys.
- Count first, then select top-k with either heap or bucket sort.
- Explain why bucket sort is valid when frequency is bounded by `n`.
- Write prefix/suffix Product Except Self with the current index excluded.
- Validate multiple independent scopes, such as rows, columns, and boxes.
- Use a set to identify unique starts and prevent repeated expansion.
- State time and space complexity in terms of `n`, distinct keys `k`, and word
  length when appropriate.


---

## 23. Quick Reference

```python
# Seen set
seen = set()
for x in nums:
    if x in seen:
        return True
    seen.add(x)

# Value -> index
index_by_value = {}
for i, x in enumerate(nums):
    if target - x in index_by_value:
        return [index_by_value[target - x], i]
    index_by_value[x] = i

# Count frequencies
from collections import Counter
count = Counter(nums)

# Manual count
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1

# Group by key
from collections import defaultdict
groups = defaultdict(list)
groups[key].append(value)

# Immutable count key
counts = [0] * 26
for ch in word:
    counts[ord(ch) - ord("a")] += 1
key = tuple(counts)

# Prefix/suffix excluding current index
answer = [1] * len(nums)
prefix = 1
for i, x in enumerate(nums):
    answer[i] = prefix
    prefix *= x

suffix = 1
for i in range(len(nums) - 1, -1, -1):
    answer[i] *= suffix
    suffix *= nums[i]

# Start-only expansion
values = set(nums)
for x in values:
    if x - 1 not in values:
        # expand from x
        ...
```

The most reliable path is:

```text
Name the fast question.
Choose the smallest structure that answers it.
State the invariant.
Check the edge cases created by duplicates, counts, ordering, and representation.
```
