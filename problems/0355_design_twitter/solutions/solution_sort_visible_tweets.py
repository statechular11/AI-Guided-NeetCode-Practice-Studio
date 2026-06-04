"""
355. Design Twitter - collect and sort visible tweets

Variant role:
    Baseline bridge between the global scan and the optimized heap merge. It
    stores tweets per user, which is the same state shape the heap solution
    needs, but it still answers a feed request by sorting all visible tweets.

Core idea:
    Maintain:

        tweets[user] = [(time, tweetId), ...]
        following[user] = {followee1, followee2, ...}

    For a feed request, gather every tweet from the requester and followees,
    sort by descending time, and return the first 10 tweet IDs.

Why this is useful:
    It makes the desired result very explicit:

        "top 10 by timestamp among visible authors"

    Once that is clear, the heap merge optimization becomes natural: instead of
    sorting all visible tweets, keep only the best current candidate from each
    visible author's already-sorted tweet list.

Concrete example:
    If user 1 follows user 2:

        user 1 tweets: [(1, 101), (4, 104)]
        user 2 tweets: [(2, 202), (3, 203)]

    Candidate tweets are:

        [(1, 101), (4, 104), (2, 202), (3, 203)]

    Sort by time descending:

        [(4, 104), (3, 203), (2, 202), (1, 101)]

    Feed:

        [104, 203, 202, 101]

Common pitfalls:
    - Sorting by tweet ID instead of timestamp.
    - Forgetting to include the requester's own tweets.
    - Returning more than 10 results.
    - Treating duplicate `follow` calls as duplicate authors. Use a set.

Complexity:
    Let M be the number of tweets written by visible authors.

    postTweet: O(1)
    follow/unfollow: O(1) average
    getNewsFeed: O(M log M)
    space: O(T + F), plus O(M) temporary feed candidates

When to choose this variant:
    Use it to validate your state model and correctness story. In an interview,
    present it briefly as a baseline, then optimize to the heap merge when the
    interviewer asks for better feed performance.
"""

from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        visible_users = set(self.following[userId])
        visible_users.add(userId)

        candidates: list[tuple[int, int]] = []
        for author in visible_users:
            candidates.extend(self.tweets[author])

        candidates.sort(reverse=True)
        return [tweet_id for _time, tweet_id in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
