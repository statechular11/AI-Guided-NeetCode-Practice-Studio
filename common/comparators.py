from __future__ import annotations

import math


FLAT_UNORDERED_RESULT_SLUGS = {
    "generate-parentheses",
    "letter-combinations-of-a-phone-number",
    "substring-with-concatenation-of-all-words",
    "top-k-frequent-elements",
    "word-search-ii",
}


NESTED_UNORDERED_SORT_INNER_SLUGS = {
    "3sum",
    "combination-sum",
    "combination-sum-ii",
    "combinations",
    "subsets",
    "subsets-ii",
}


NESTED_UNORDERED_PRESERVE_INNER_SLUGS = {
    "find-k-pairs-with-smallest-sums",
    "k-closest-points-to-origin",
    "n-queens",
    "pacific-atlantic-water-flow",
    "palindrome-partitioning",
    "permutations",
}


UNORDERED_RESULT_SLUGS = (
    FLAT_UNORDERED_RESULT_SLUGS
    | NESTED_UNORDERED_SORT_INNER_SLUGS
    | NESTED_UNORDERED_PRESERVE_INNER_SLUGS
    | {"group-anagrams"}
)


def _freeze(value):
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def _normalize_flat_unordered(value):
    if not isinstance(value, list):
        return value
    return sorted((_freeze(item) for item in value), key=repr)


def _normalize_nested_sort_inner(value):
    if not isinstance(value, list):
        return value
    normalized = []
    for item in value:
        if isinstance(item, list):
            normalized.append(tuple(sorted((_freeze(part) for part in item), key=repr)))
        else:
            normalized.append(_freeze(item))
    return sorted(normalized, key=repr)


def _normalize_nested_preserve_inner(value):
    if not isinstance(value, list):
        return value
    return sorted((_freeze(item) for item in value), key=repr)


def _is_valid_course_order(order, raw_args, expected):
    if not isinstance(order, list):
        return False
    if expected == []:
        return order == []
    num_courses = raw_args.get("numCourses")
    prerequisites = raw_args.get("prerequisites", [])
    if not isinstance(num_courses, int) or len(order) != num_courses:
        return False
    if sorted(order) != list(range(num_courses)):
        return False
    position = {course: index for index, course in enumerate(order)}
    return all(position.get(before, -1) < position.get(after, -1) for after, before in prerequisites)


def _is_valid_alien_order(order, raw_args, expected):
    if not isinstance(order, str):
        return False
    if expected == "":
        return order == ""
    words = raw_args.get("words", [])
    letters = set("".join(words))
    if len(order) != len(letters) or set(order) != letters:
        return False
    position = {char: index for index, char in enumerate(order)}
    for first, second in zip(words, words[1:]):
        limit = min(len(first), len(second))
        for index in range(limit):
            if first[index] != second[index]:
                if position[first[index]] > position[second[index]]:
                    return False
                break
        else:
            if len(first) > len(second):
                return False
    return True


def _float_close(a, b):
    if isinstance(a, float) or isinstance(b, float):
        return math.isclose(float(a), float(b), rel_tol=1e-6, abs_tol=1e-6)
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        return all(_float_close(x, y) for x, y in zip(a, b))
    return a == b


def _is_valid_peak_index(index, raw_args):
    nums = raw_args.get("nums", [])
    if not isinstance(index, int) or index < 0 or index >= len(nums):
        return False
    left = float("-inf") if index == 0 else nums[index - 1]
    right = float("-inf") if index == len(nums) - 1 else nums[index + 1]
    return nums[index] > left and nums[index] > right


def _is_valid_balanced_bst(values, nums):
    if nums == []:
        return values in (None, [])
    if not isinstance(values, list):
        return False

    inorder = []
    balanced = True

    def walk(index):
        nonlocal balanced
        if index >= len(values) or values[index] is None:
            return 0
        left_height = walk(index * 2 + 1)
        inorder.append(values[index])
        right_height = walk(index * 2 + 2)
        if abs(left_height - right_height) > 1:
            balanced = False
        return max(left_height, right_height) + 1

    walk(0)
    return balanced and inorder == nums


def _is_valid_longest_palindrome(actual, expected, raw_args):
    s = raw_args.get("s", "")
    return (
        isinstance(actual, str)
        and actual == actual[::-1]
        and actual in s
        and len(actual) == len(expected)
    )


def _quad_equal(actual, expected):
    if actual is None or expected is None:
        return actual == expected
    if not isinstance(actual, list) or not isinstance(expected, list):
        return False
    if len(actual) != 6 or len(expected) != 6:
        return False
    if actual[0] != expected[0]:
        return False
    if actual[0]:
        return actual[1] == expected[1]
    return all(_quad_equal(a, e) for a, e in zip(actual[2:], expected[2:]))


def compare_values(slug, actual, expected, raw_args=None):
    raw_args = raw_args or {}
    if slug == "longest-palindromic-substring":
        return _is_valid_longest_palindrome(actual, expected, raw_args)
    if slug == "construct-quad-tree":
        return _quad_equal(actual, expected)
    if slug == "convert-sorted-array-to-binary-search-tree":
        return _is_valid_balanced_bst(actual, raw_args.get("nums", []))
    if slug == "course-schedule-ii":
        return _is_valid_course_order(actual, raw_args, expected)
    if slug == "alien-dictionary":
        return _is_valid_alien_order(actual, raw_args, expected)
    if slug in {"evaluate-division", "average-of-levels-in-binary-tree", "find-median-from-data-stream", "powx-n"}:
        return _float_close(actual, expected)
    if slug == "find-peak-element":
        return _is_valid_peak_index(actual, raw_args)
    if slug in {"two-sum", "two-sum-ii-input-array-is-sorted"}:
        if not isinstance(actual, list) or not isinstance(expected, list):
            return False
        return sorted(actual) == sorted(expected)
    if slug == "remove-element":
        if not isinstance(actual, list) or not isinstance(expected, list):
            return False
        return sorted(actual) == sorted(expected)
    if slug == "group-anagrams":
        if not isinstance(actual, list) or not isinstance(expected, list):
            return False
        normalize = lambda groups: sorted(sorted(group) for group in groups)
        return normalize(actual) == normalize(expected)
    if slug in FLAT_UNORDERED_RESULT_SLUGS:
        return _normalize_flat_unordered(actual) == _normalize_flat_unordered(expected)
    if slug in NESTED_UNORDERED_SORT_INNER_SLUGS:
        return _normalize_nested_sort_inner(actual) == _normalize_nested_sort_inner(expected)
    if slug in NESTED_UNORDERED_PRESERVE_INNER_SLUGS:
        return _normalize_nested_preserve_inner(actual) == _normalize_nested_preserve_inner(expected)
    return actual == expected
