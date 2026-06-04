# Notes - 355. Design Twitter

## Core Idea

Store tweets with an explicit timestamp/counter. A feed is the 10 newest tweets
from the visible author set: the requesting user plus everyone they follow.

There are three useful ways to think about the design:

- Global timeline scan: store all tweets in one chronological log and scan it
  backward, filtering by visible authors.
- Per-user candidate sorting: store tweets by author, gather all visible tweets,
  sort by timestamp, and take the first 10.
- Heap k-way merge: store tweets by author and keep only each visible author's
  newest not-yet-returned tweet in a heap.

The heap approach is the interview target because each user's tweet list is
already sorted by posting order, so `getNewsFeed` can merge visible lists only
as far as the 10-item feed needs.

## Reference Solutions

| File | Role | Complexity |
| --- | --- | --- |
| `solution_heap_merge_feeds.py` | primary optimized design solution | post/follow O(1), getNewsFeed O(U log U + 10 log U) |
| `solution_global_timeline_scan.py` | simple design baseline | post/follow O(1), getNewsFeed O(T) worst case |
| `solution_sort_visible_tweets.py` | baseline bridge to heap merge | post/follow O(1), getNewsFeed O(M log M) |

## Heap Merge Mental Model

For each visible author, push only their newest tweet. The heap root is the
newest tweet among all visible authors. After popping a tweet from author A,
push A's next older tweet. This preserves the invariant that the heap always
contains the best remaining candidate from each author.

In symbols:

```text
visible authors = {self} union followees
heap candidate for author u = newest unreturned tweet in tweets[u]
next feed item = max candidate by timestamp
```

## Pitfalls To Watch

- Tweet IDs are unique but are not guaranteed to encode recency. Use a separate
  timestamp/counter.
- The requester always sees their own tweets. Add the requester to the visible
  author set inside `getNewsFeed`.
- Python's `heapq` is a min-heap; negate timestamps to pop newest first.
- Store followees in a set so repeated `follow` calls do not duplicate authors.
- A heap merge entry needs enough information to continue that author's list,
  usually `(negative_time, author, index, tweet_id)`.
- Stop after 10 feed items; older visible tweets do not matter for this call.

## Review Log

Add review observations here after NeetCode Prep Coach reviews your `solution.py`.
