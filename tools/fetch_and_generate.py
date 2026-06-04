from __future__ import annotations

import argparse
import ast
import csv
import html
import importlib.util
import json
import os
import plistlib
import re
import textwrap
import urllib.request
from collections import defaultdict
from copy import deepcopy
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REFERENCE_ROOT = ROOT / "reference_repos" / "LeetCode-Top-Interview-150"
LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"
LEETCODE_STUDY_PLAN_API_SLUG = "top-interview-150"
TOP_INTERVIEW_PLAN_SLUG = "leetcode-top-interview-150"
NEETCODE_PLAN_SLUG = "neetcode-150"
MERGED_PLAN_SLUG = "merged-leetcode-top-interview-150-neetcode-150"
PLAN_SLUG = TOP_INTERVIEW_PLAN_SLUG
PLAN_URL = f"https://leetcode.com/studyplan/{LEETCODE_STUDY_PLAN_API_SLUG}/"
NEETCODE_150_URL = "https://neetcode.io/practice/practice/neetcode150"


STUDY_PLAN_LABELS = {
    TOP_INTERVIEW_PLAN_SLUG: "LeetCode Top Interview 150",
    NEETCODE_PLAN_SLUG: "NeetCode 150",
    MERGED_PLAN_SLUG: "Merged LeetCode Top Interview 150 + NeetCode 150",
}


PLAN_QUERY = """
query studyPlanV2Detail($slug: String!) {
  studyPlanV2Detail(planSlug: $slug) {
    slug
    name
    questionNum
    planSubGroups {
      slug
      name
      questionNum
      questions {
        questionFrontendId
        id
        title
        titleSlug
        difficulty
        paidOnly
        topicTags {
          name
          slug
        }
      }
    }
  }
}
"""


QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    isPaidOnly
    content
    exampleTestcases
    hints
    metaData
    similarQuestions
    codeSnippets {
      lang
      langSlug
      code
    }
    topicTags {
      name
      slug
    }
  }
}
"""


SECTION_APPROACHES = {
    "Arrays & Hashing": "arrays_and_hashing",
    "Array / String": "array_string",
    "Two Pointers": "two_pointers",
    "Sliding Window": "sliding_window",
    "Matrix": "matrix_simulation",
    "Hashmap": "hash_map",
    "Intervals": "intervals",
    "Stack": "stack",
    "Linked List": "linked_list",
    "Trees": "tree_dfs",
    "Binary Tree General": "tree_dfs",
    "Binary Tree BFS": "tree_bfs",
    "Binary Search Tree": "bst",
    "Graphs": "graph",
    "Advanced Graphs": "advanced_graph",
    "Graph General": "graph",
    "Graph BFS": "bfs",
    "Tries": "trie",
    "Trie": "trie",
    "Backtracking": "backtracking",
    "Divide & Conquer": "divide_and_conquer",
    "Divide and Conquer": "divide_and_conquer",
    "Kadane's Algorithm": "kadane",
    "Binary Search": "binary_search",
    "Heap / Priority Queue": "heap",
    "Heap": "heap",
    "Bit Manipulation": "bit_manipulation",
    "Math & Geometry": "math_geometry",
    "Math": "math",
    "1D DP": "dynamic_programming",
    "1D Dynamic Programming": "dynamic_programming",
    "1-D Dynamic Programming": "dynamic_programming",
    "2-D Dynamic Programming": "multidimensional_dp",
    "Multidimensional DP": "multidimensional_dp",
    "Multidimensional Dynamic Programming": "multidimensional_dp",
    "Greedy": "greedy",
}


TAG_PITFALLS = {
    "array": "Check empty, single-item, duplicate, and all-equal arrays before trusting the main loop.",
    "two-pointers": "State what each pointer means. Most bugs come from moving the wrong pointer or skipping duplicates at the wrong time.",
    "sliding-window": "Keep the window invariant explicit. Decide whether the window is valid before or after each update.",
    "hash-table": "Be clear whether the map stores counts, last seen index, first seen index, or a representative object.",
    "dynamic-programming": "Define the state in a sentence before coding. Then verify base cases and iteration order.",
    "greedy": "Name the local choice and the reason it cannot hurt future choices.",
    "stack": "Know whether the stack stores values, indices, or partial computation frames.",
    "monotonic-stack": "Write down whether the stack is increasing or decreasing and whether equality should pop.",
    "binary-search": "Use half-open or closed intervals deliberately. Decide what `left` means when the loop ends.",
    "tree": "Be precise about whether information flows bottom-up, top-down, or both.",
    "binary-tree": "For recursion, define the return value of the helper before writing the recursive calls.",
    "graph": "Separate graph construction from traversal. Mark visited at enqueue time for BFS unless there is a reason not to.",
    "breadth-first-search": "Queue entries should contain exactly the state needed for one expansion step.",
    "depth-first-search": "Backtracking DFS needs a clear undo step for each mutation.",
    "trie": "Distinguish terminal-word state from prefix-continuation state.",
    "heap-priority-queue": "Remember Python has a min-heap; use negative values or tuple ordering when you need max behavior.",
    "linked-list": "Draw the predecessor node, not just the node being removed or moved.",
    "math": "List special cases first: zero, one, negative values, overflow-like boundaries, and divisibility.",
    "bit-manipulation": "Check whether the operation depends on Python's unbounded signed integers.",
    "prefix-sum": "Clarify whether the prefix at position `i` includes `nums[i]` or stops before it.",
    "sorting": "After sorting, track whether the answer needs original indices or only values.",
}


SECTION_MENTAL_MODELS = {
    "Array / String": "Most problems in this section are about maintaining compact state while scanning once, or rearranging an array in place without losing needed information.",
    "Two Pointers": "Two pointers are useful when sorted order or opposing movement lets one decision discard a whole family of impossible answers.",
    "Sliding Window": "A sliding window keeps a contiguous region plus enough summary state to expand or shrink without recomputing from scratch.",
    "Matrix": "Matrix problems usually become simpler once you name the traversal order, the boundary being consumed, or the in-place encoding rule.",
    "Hashmap": "Hash maps trade space for direct lookup: complements, counts, canonical forms, last seen positions, or membership.",
    "Intervals": "Sort intervals by start or end, then decide whether the current interval overlaps, extends, or starts a new group.",
    "Stack": "Stacks remember unresolved work. The top of the stack should represent the next thing that could be closed, matched, or resolved.",
    "Linked List": "Linked-list solutions are pointer choreography. Dummy nodes and predecessor pointers make edge cases boring.",
    "Trees": "Tree problems become simpler when you state exactly what each recursive call returns or what each BFS level represents.",
    "Binary Tree General": "Tree DFS is about choosing the helper's return value. Once that is fixed, the recursive structure usually writes itself.",
    "Binary Tree BFS": "Level-order traversal gives you natural access to per-level summaries such as rightmost value, average, or zigzag order.",
    "Binary Search Tree": "BST problems exploit inorder ordering or value bounds. Avoid treating it like a generic binary tree unless necessary.",
    "Graphs": "Graph problems are mostly about choosing the right state representation and traversal invariant: DFS, BFS, Union-Find, or topological order.",
    "Advanced Graphs": "Advanced graph problems usually add weights, ordering constraints, or reconstruction to ordinary graph traversal.",
    "Graph General": "Build an adjacency representation, choose DFS/BFS/Union-Find/topological sort, and be explicit about visited state.",
    "Graph BFS": "BFS is the default for shortest number of unweighted moves or transformations.",
    "Tries": "Tries turn a prefix relationship into a path through characters; keep terminal-word state separate from child existence.",
    "Trie": "Tries make prefix queries cheap by turning each character into a path decision.",
    "Backtracking": "Backtracking explores choices, records a candidate, recurses, and undoes the choice before trying the next branch.",
    "Divide & Conquer": "Split into smaller subproblems, solve recursively, then merge or connect the results.",
    "Kadane's Algorithm": "Kadane-style DP asks whether extending the previous subarray is better than starting fresh here.",
    "Binary Search": "Binary search works when you can define a monotonic predicate or exploit sorted structure after each midpoint decision.",
    "Heap": "Heaps are for repeated access to the current smallest/largest candidate without sorting everything every time.",
    "Bit Manipulation": "Bit tricks are compact set/count/parity manipulations. Keep the invariant in binary, not decimal.",
    "Math & Geometry": "Math and geometry problems reward writing the invariant first, then coding the transformation directly.",
    "Math": "Math problems often hinge on a derived invariant; code should follow the invariant rather than simulate blindly.",
    "1D DP": "One-dimensional DP usually asks for the best/count/feasible value up to an index or amount.",
    "1-D Dynamic Programming": "One-dimensional DP usually asks for the best/count/feasible value up to an index or amount.",
    "2-D Dynamic Programming": "Two-dimensional DP tracks two axes of state, such as positions in two strings or choices under an added constraint.",
    "Multidimensional DP": "Multi-dimensional DP tracks two or more positions/states at once; table dimensions should mirror the state definition.",
    "Greedy": "Greedy solutions need a short exchange argument: why the local choice preserves at least one optimal future.",
}


UNORDERED_RESULT_SLUGS = {
    "3sum",
    "group-anagrams",
    "letter-combinations-of-a-phone-number",
    "combinations",
    "permutations",
    "combination-sum",
    "combination-sum-ii",
    "generate-parentheses",
    "k-closest-points-to-origin",
    "n-queens",
    "pacific-atlantic-water-flow",
    "palindrome-partitioning",
    "substring-with-concatenation-of-all-words",
    "top-k-frequent-elements",
    "subsets",
    "subsets-ii",
    "word-search-ii",
}


PREFIX_JUDGE_SLUGS = {
    "remove-element": 0,
    "remove-duplicates-from-sorted-array": 0,
    "remove-duplicates-from-sorted-array-ii": 0,
}


IN_PLACE_ARG_SLUGS = {
    "merge-sorted-array": 0,
    "rotate-array": 0,
    "rotate-image": 0,
    "set-matrix-zeroes": 0,
    "game-of-life": 0,
    "surrounded-regions": 0,
    "flatten-binary-tree-to-linked-list": 0,
    "walls-and-gates": 0,
}


SOURCE_LICENSE = """# Third-Party Notices

This package does not include third-party reference-solution code under `problems/*/solutions/`.

Reference solutions are AI-authored educational implementations intended for interview practice and review. Problem prompts link to their source problem pages where applicable; those problem statements and platform materials remain owned by their respective providers.
"""


def request_graphql(query: str, variables: dict[str, Any], referer: str = PLAN_URL) -> dict[str, Any]:
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        LEETCODE_GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": referer,
            "Origin": "https://leetcode.com",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if data.get("errors"):
        raise RuntimeError(json.dumps(data["errors"], indent=2))
    return data["data"]


def request_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def extract_js_array(source: str, assignment: str) -> str:
    start = source.find(assignment)
    if start == -1:
        raise RuntimeError(f"Could not find {assignment!r} in NeetCode asset")
    pos = start + len(assignment) - 1
    depth = 0
    for index, char in enumerate(source[pos:], start=pos):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return source[pos + 1 : index]
    raise RuntimeError(f"Could not parse array assigned by {assignment!r}")


def extract_js_objects(array_body: str) -> list[str]:
    objects: list[str] = []
    current: list[str] = []
    depth = 0
    for char in array_body:
        if char == "{" and depth == 0:
            current = [char]
            depth = 1
            continue
        if not depth:
            continue
        current.append(char)
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                objects.append("".join(current))
                current = []
    return objects


def js_string_field(obj: str, key: str) -> str:
    match = re.search(rf"{re.escape(key)}:\"([^\"]*)\"", obj)
    return match.group(1) if match else ""


def fetch_neetcode_150() -> list[dict[str, Any]]:
    html_text = request_text(NEETCODE_150_URL)
    script_matches = re.findall(r'<script[^>]+src="([^"]*main\.[^"]+\.js)"', html_text)
    if not script_matches:
        raise RuntimeError("Could not find NeetCode main JavaScript asset")
    script_url = script_matches[-1]
    if script_url.startswith("//"):
        script_url = "https:" + script_url
    elif script_url.startswith("/"):
        script_url = "https://neetcode.io" + script_url
    elif not script_url.startswith("http"):
        script_url = "https://neetcode.io/" + script_url
    js_text = request_text(script_url)
    objects = extract_js_objects(extract_js_array(js_text, "ee=["))
    entries: list[dict[str, Any]] = []
    for obj in objects:
        if "neetcode150:!0" not in obj:
            continue
        link = js_string_field(obj, "link").rstrip("/")
        code = js_string_field(obj, "code")
        entries.append(
            {
                "order": len(entries) + 1,
                "title": js_string_field(obj, "problem"),
                "section": js_string_field(obj, "pattern"),
                "slug": link,
                "difficulty": js_string_field(obj, "difficulty"),
                "code": code,
                "leetcode_url": f"https://leetcode.com/problems/{link}/",
                "neetcode_url": f"https://neetcode.io/problems/{js_string_field(obj, 'ncLink').rstrip('/')}",
                "video": js_string_field(obj, "video"),
            }
        )
    if len(entries) != 150:
        raise RuntimeError(f"Expected 150 NeetCode entries, found {len(entries)}")
    return entries


def snake(text: str) -> str:
    cleaned = text.replace("&", "and")
    cleaned = re.sub(r"[^0-9A-Za-z]+", "_", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("_").lower()
    return cleaned or "untitled"


def title_case_difficulty(value: str) -> str:
    return value[:1].upper() + value[1:].lower()


def parse_jsonish(value: str) -> Any:
    return json.loads(value)


def params_from_metadata(meta: dict[str, Any]) -> list[dict[str, Any]]:
    if meta.get("systemdesign"):
        return []
    return meta.get("params", [])


def python_type(lc_type: str) -> str:
    mapping = {
        "integer": "int",
        "long": "int",
        "double": "float",
        "boolean": "bool",
        "string": "str",
        "void": "None",
        "integer[]": "List[int]",
        "integer[][]": "List[List[int]]",
        "string[]": "List[str]",
        "list<string>": "List[str]",
        "list<integer>": "List[int]",
        "list<boolean>": "List[bool]",
        "list<list<integer>>": "List[List[int]]",
        "ListNode": "Optional[ListNode]",
        "ListNode[]": "List[Optional[ListNode]]",
        "TreeNode": "Optional[TreeNode]",
        "Node": "Optional[Node]",
    }
    return mapping.get(lc_type, "Any")


def format_params(params: list[dict[str, Any]]) -> str:
    rendered = []
    for param in params:
        name = param.get("name", "arg")
        if name.endswith("Size") or param.get("lang") == "c":
            continue
        rendered.append(f"{name}: {python_type(param.get('type', 'Any'))}")
    return ", ".join(rendered)


def snippet_from_metadata(meta: dict[str, Any], slug: str = "") -> str:
    if slug == "encode-and-decode-strings":
        return "\n".join(
            [
                "class Solution:",
                "    def encode(self, strs: List[str]) -> str:",
                "        pass",
                "",
                "    def decode(self, s: str) -> List[str]:",
                "        pass",
            ]
        )
    if meta.get("systemdesign"):
        class_name = meta.get("classname", "DesignClass")
        lines = [f"class {class_name}:"]
        constructor_params = format_params(meta.get("constructor", {}).get("params", []))
        lines += [f"    def __init__(self{', ' + constructor_params if constructor_params else ''}):", "        pass", ""]
        for method in meta.get("methods", []):
            params = format_params(method.get("params", []))
            return_type = python_type(method.get("return", {}).get("type", "None"))
            lines += [
                f"    def {method.get('name', 'method')}(self{', ' + params if params else ''}) -> {return_type}:",
                "        pass",
                "",
            ]
        return "\n".join(lines).rstrip()
    params = format_params(meta.get("params", []))
    return_type = python_type(meta.get("return", {}).get("type", "Any"))
    method_name = meta.get("name", "solve")
    return f"class Solution:\n    def {method_name}(self{', ' + params if params else ''}) -> {return_type}:\n        pass"


def python3_snippet(question: dict[str, Any]) -> str:
    for snippet in question.get("codeSnippets") or []:
        if snippet.get("langSlug") == "python3":
            return "\n".join(line.rstrip() for line in snippet.get("code", "").rstrip().splitlines())
    meta = json.loads(question.get("metaData") or "{}")
    return snippet_from_metadata(meta, question.get("titleSlug", ""))


TYPING_IMPORT_NAMES = ("Any", "Callable", "Deque", "Dict", "List", "Optional", "Set", "Tuple")
COLLECTION_IMPORT_NAMES = ("Counter", "defaultdict", "deque")
LC_TYPE_IMPORT_NAMES = (
    "ListNode",
    "Node",
    "TreeNode",
    "GraphNode",
    "RandomPointerNode",
    "NextTreeNode",
    "QuadTreeNode",
)
LC_NODE_IMPORT_BY_SLUG = {
    "clone-graph": "GraphNode as Node",
    "copy-list-with-random-pointer": "RandomPointerNode as Node",
    "populating-next-right-pointers-in-each-node": "NextTreeNode as Node",
    "populating-next-right-pointers-in-each-node-ii": "NextTreeNode as Node",
    "construct-quad-tree": "QuadTreeNode as Node",
}
MODULE_IMPORT_NAMES = ("collections", "heapq", "math")
GENERATED_IMPORT_PREFIXES = (
    "from collections import ",
    "import collections",
    "import heapq",
    "import math",
    "from typing import ",
    "from common.lc_types import ",
)

LC_TYPE_DEFINITION_COMMENTS = {
    "ListNode": """# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next""",
    "TreeNode": """# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right""",
    "GraphNode": """# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []""",
    "RandomPointerNode": """# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random""",
    "NextTreeNode": """# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next""",
    "QuadTreeNode": """# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight""",
    "Node": """# Definition for a Node.
# class Node:
#     def __init__(self, val=0, neighbors=None, next=None, random=None, left=None, right=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
#         self.next = next
#         self.random = random
#         self.left = left
#         self.right = right""",
}


def referenced_names(body: str) -> set[str]:
    try:
        module = ast.parse(body)
    except SyntaxError:
        return set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", body))

    names: set[str] = set()

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node: ast.Name) -> None:
            names.add(node.id)

    Visitor().visit(module)
    return names


def import_requirements_for_body(body: str, slug: str | None = None) -> list[str]:
    try:
        module = ast.parse(body)
    except SyntaxError:
        names = set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", body))
        defined: set[str] = set()
    else:
        names: set[str] = set()
        defined = set()

        class Visitor(ast.NodeVisitor):
            def visit_annotation(self, annotation: ast.AST) -> None:
                if isinstance(annotation, ast.Constant) and isinstance(annotation.value, str):
                    names.update(re.findall(r"\b[A-Za-z_][A-Za-z0-9_]*\b", annotation.value))
                    return
                self.visit(annotation)

            def visit_Name(self, node: ast.Name) -> None:
                if isinstance(node.ctx, ast.Load):
                    names.add(node.id)
                elif isinstance(node.ctx, (ast.Store, ast.Del)):
                    defined.add(node.id)
                self.generic_visit(node)

            def visit_arg(self, node: ast.arg) -> None:
                if node.annotation:
                    self.visit_annotation(node.annotation)

            def visit_ClassDef(self, node: ast.ClassDef) -> None:
                defined.add(node.name)
                for decorator in node.decorator_list:
                    self.visit(decorator)
                for base in node.bases:
                    self.visit(base)
                for keyword in node.keywords:
                    self.visit(keyword)
                for stmt in node.body:
                    self.visit(stmt)

            def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
                defined.add(node.name)
                for decorator in node.decorator_list:
                    self.visit(decorator)
                self.visit(node.args)
                if node.returns:
                    self.visit_annotation(node.returns)
                for stmt in node.body:
                    self.visit(stmt)

            visit_AsyncFunctionDef = visit_FunctionDef

            def visit_Import(self, node: ast.Import) -> None:
                for alias in node.names:
                    defined.add(alias.asname or alias.name.split(".")[0])

            def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
                for alias in node.names:
                    defined.add(alias.asname or alias.name)

        Visitor().visit(module)

    imports = []
    collection_names = [name for name in COLLECTION_IMPORT_NAMES if name in names and name not in defined]
    if collection_names:
        imports.append(f"from collections import {', '.join(collection_names)}")
    for module_name in MODULE_IMPORT_NAMES:
        if module_name in names and module_name not in defined:
            imports.append(f"import {module_name}")
    typing_names = [name for name in TYPING_IMPORT_NAMES if name in names and name not in defined]
    if typing_names:
        imports.append(f"from typing import {', '.join(typing_names)}")
    lc_type_names = [
        name
        for name in LC_TYPE_IMPORT_NAMES
        if name != "Node" and name in names and name not in defined
    ]
    if "Node" in names and "Node" not in defined:
        lc_type_names.append(LC_NODE_IMPORT_BY_SLUG.get(slug or "", "Node"))
    if lc_type_names:
        imports.append(f"from common.lc_types import {', '.join(lc_type_names)}")
    return imports


def lc_type_definition_comments_for_imports(imports: list[str]) -> list[str]:
    comments = []
    imported_names: set[str] = set()
    for line in imports:
        if not line.startswith("from common.lc_types import "):
            continue
        imported = line.rsplit(" import ", 1)[1]
        for part in imported.split(","):
            part = part.strip()
            if " as " in part:
                original, _alias = part.split(" as ", 1)
                imported_names.add(original.strip())
            else:
                imported_names.add(part)
    for name in LC_TYPE_IMPORT_NAMES:
        if name in imported_names:
            comments.append(LC_TYPE_DEFINITION_COMMENTS[name])
    return comments


def lc_type_definition_comment_block(imports: list[str]) -> str:
    comments = lc_type_definition_comments_for_imports(imports)
    return "\n\n".join(comments)


def template_imports_for_body(body: str, slug: str | None = None) -> list[str]:
    return import_requirements_for_body(body, slug=slug)


def strip_template_imports(snippet: str) -> str:
    lines = []
    for line in snippet.splitlines():
        if line.startswith("import ") or line.startswith("from "):
            continue
        if line.startswith("# Definition for "):
            continue
        if line.startswith("# class "):
            continue
        if line.startswith("#     "):
            continue
        lines.append(line)
    return "\n".join(lines).strip("\n")


def add_template_imports(snippet: str, slug: str | None = None) -> str:
    body = strip_template_imports(snippet).rstrip()
    if body.endswith(":"):
        body += "\n        pass"
    body = re.sub(r"\n\s*$", "", body)
    if "pass" not in body and re.search(r":\n\s*$", body):
        body += "\n        pass"
    pattern = re.compile(r"(?m)^([ \t]+def [^\n]+:\n)([ \t]*\n)+(?=^[ \t]*(?:def |#|$))")

    def fill_empty_method(match: re.Match[str]) -> str:
        indent = match.group(1).split("def ")[0]
        return match.group(1) + indent + "    pass\n\n"

    body = pattern.sub(fill_empty_method, body)
    docstring_only_method = re.compile(r'(?ms)^([ \t]+def [^\n]+:\n([ \t]+)"""(?:.*?)"""\n)(?=^[ \t]*(?:def |class |\Z))')
    body = docstring_only_method.sub(lambda match: match.group(1) + match.group(2) + "pass\n", body)
    imports = template_imports_for_body(body, slug=slug)
    if imports:
        definition_comments = lc_type_definition_comment_block(imports)
        if definition_comments:
            return "\n".join(imports) + "\n\n\n" + definition_comments + "\n\n\n" + body + "\n"
        return "\n".join(imports) + "\n\n\n" + body + "\n"
    return body + "\n"


def is_blank_statement(stmt: Any) -> bool:
    if isinstance(stmt, ast.Pass):
        return True
    if isinstance(stmt, ast.Expr):
        value = stmt.value
        return isinstance(value, ast.Constant) and value.value in {None, Ellipsis}
    return False


def is_docstring_expr(stmt: Any) -> bool:
    return isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str)


def is_blank_function(node: ast.FunctionDef) -> bool:
    body = node.body[:]
    if body and is_docstring_expr(body[0]):
        body = body[1:]
    return bool(body) and all(is_blank_statement(stmt) for stmt in body)


def is_blank_class(node: ast.ClassDef) -> bool:
    if not node.body:
        return False
    for stmt in node.body:
        if is_blank_statement(stmt):
            continue
        if isinstance(stmt, ast.FunctionDef) and is_blank_function(stmt):
            continue
        return False
    return True


def is_untouched_solution_template(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        module = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError:
        return False
    saw_blank_class = False
    for stmt in module.body:
        if isinstance(stmt, (ast.Import, ast.ImportFrom)):
            continue
        if is_docstring_expr(stmt):
            continue
        if isinstance(stmt, ast.ClassDef) and is_blank_class(stmt):
            saw_blank_class = True
            continue
        return False
    return saw_blank_class


def parse_example_cases(example_testcases: str, meta: dict[str, Any]) -> list[dict[str, Any]]:
    if not example_testcases:
        return []
    lines = [line for line in example_testcases.splitlines() if line.strip()]
    if meta.get("systemdesign"):
        if len(lines) < 2:
            return []
        return [
            {
                "name": "example_1",
                "operations": parse_jsonish(lines[0]),
                "arguments": parse_jsonish(lines[1]),
            }
        ]
    params = params_from_metadata(meta)
    width = len(params)
    if width == 0:
        return []
    cases = []
    for i in range(0, len(lines), width):
        chunk = lines[i : i + width]
        if len(chunk) != width:
            continue
        cases.append(
            {
                "name": f"example_{len(cases) + 1}",
                "args": {param["name"]: parse_jsonish(raw) for param, raw in zip(params, chunk)},
            }
        )
    return cases


def judge_config(slug: str, meta: dict[str, Any]) -> dict[str, Any]:
    if slug == "encode-and-decode-strings":
        return {"mode": "codec"}
    if slug == "serialize-and-deserialize-binary-tree":
        return {"mode": "tree_codec"}
    if meta.get("systemdesign"):
        return {"mode": "design"}
    if slug in PREFIX_JUDGE_SLUGS:
        return {"mode": "returned_prefix", "arg_index": PREFIX_JUDGE_SLUGS[slug]}
    if slug in IN_PLACE_ARG_SLUGS:
        return {"mode": "in_place", "arg_index": IN_PLACE_ARG_SLUGS[slug]}
    output = meta.get("output") or {}
    if meta.get("return", {}).get("type") == "void" and "paramindex" in output:
        return {"mode": "in_place", "arg_index": int(output["paramindex"])}
    return {"mode": "return"}


def source_solution_path(reference_root: Path, frontend_id: int, folder_slug: str) -> Path | None:
    if not reference_root.exists():
        return None
    pattern = f"s{frontend_id:04d}_{folder_slug}"
    candidates = list((reference_root / "src" / "main" / "python").glob(f"**/{pattern}/*.py"))
    candidates = [path for path in candidates if path.name.lower() != "readme.md"]
    if candidates:
        return sorted(candidates)[0]
    loose = list((reference_root / "src" / "main" / "python").glob(f"**/s{frontend_id:04d}_*/*.py"))
    loose = [path for path in loose if path.name.lower() != "readme.md"]
    return sorted(loose)[0] if loose else None


def complexity_from_source(source: str) -> str:
    match = re.search(r"#Big_O_Time_([^#\n]+?)_Space_([^#\n]+)", source)
    if not match:
        return "See the reference solution and verify during review."
    time = match.group(1).replace("_", " ")
    space = match.group(2).replace("_", " ")
    return f"Time: {time}; Space: {space}"


SOLUTION_HEADER_APPROACH_IDEAS = {
    "arrays_and_hashing": "Track counts, membership, or last-seen state with hash-based structures so each update preserves the lookup invariant needed by the result.",
    "array_string": "Reduce the array/string contract to a small invariant, then update indices or accumulated state without losing information needed later.",
    "two_pointers": "Move two indices according to the sorted/order invariant so each step discards only candidates that can no longer improve the answer.",
    "sliding_window": "Maintain a valid window plus the state needed to expand or shrink it; each pointer moves forward at most once.",
    "matrix_simulation": "Map the matrix transformation to row/column boundaries or in-place swaps, then update cells without corrupting unread state.",
    "hash_map": "Use direct key-to-state mappings to avoid repeated scans and make the matching/counting condition explicit.",
    "intervals": "Sort or merge by interval boundaries so overlap decisions are local and the running interval/counter stays meaningful.",
    "stack": "Use the stack to store unresolved items; when the current item resolves the top, pop until the invariant is restored.",
    "linked_list": "Preserve pointer ownership with a dummy node or carefully ordered rewiring so no node is lost during mutation.",
    "tree_dfs": "Define the value each subtree returns to its parent, then combine left and right results while handling the root case explicitly.",
    "tree_bfs": "Process the tree level by level with a queue so level order, width, or nearest-node properties are explicit.",
    "bst": "Exploit the BST ordering invariant to discard one side or to traverse in sorted order.",
    "graph": "Model states as nodes and edges, then use visited state to avoid cycles while preserving reachability or component invariants.",
    "advanced_graph": "Use the graph algorithm that matches the edge property, such as topological order for prerequisites or a heap for weighted shortest paths.",
    "bfs": "Use a queue to explore states by distance/layer, marking visited states as soon as they are enqueued.",
    "trie": "Store shared prefixes in trie nodes so prefix and word queries become direct traversals.",
    "backtracking": "Build one partial candidate at a time, recurse only while constraints remain valid, and undo the choice before trying the next branch.",
    "divide_and_conquer": "Split the input into independent subproblems, solve each recursively, then combine the results at the boundary.",
    "kadane": "Carry the best subarray ending at the current position and the best answer seen so far.",
    "binary_search": "Define the monotonic predicate or sorted-side invariant first, then shrink the search range around that invariant.",
    "heap": "Use a heap when the next smallest/largest candidate must be retrieved repeatedly without sorting the entire remaining set.",
    "bit_manipulation": "Translate the invariant into bit operations so counts, parity, masks, or carries are updated directly.",
    "math_geometry": "Derive the numeric or geometric invariant first, then implement that invariant directly instead of simulating unnecessary state.",
    "math": "Use the derived arithmetic invariant to avoid brute-force simulation.",
    "dynamic_programming": "Choose a state that captures the best/count/feasible answer for a prefix or subproblem, then fill it from smaller states.",
    "multidimensional_dp": "Use a DP state with multiple indices or dimensions so every transition depends only on already solved smaller states.",
    "greedy": "Make a local choice that can be justified by an exchange argument and keep only the state needed for future feasibility.",
}


SOLUTION_HEADER_WALKTHROUGHS = {
    "arrays_and_hashing": [
        "Identify the value that must be remembered for each key, such as a count, index, complement, or bucket membership.",
        "Scan the input once or build the table first, updating that state immediately after each observation.",
        "Use O(1)-average lookups to decide whether the current item completes the condition or contributes to the final structure.",
        "Return the accumulated answer after the invariant has been maintained for every item.",
    ],
    "array_string": [
        "Translate the statement into the smallest state needed while scanning the array or string.",
        "Update that state in the same order the input is read, taking care with boundaries and empty cases.",
        "When the problem asks for mutation, write only the accepted prefix or final transformed positions.",
        "Return the requested value after the scan has preserved the stated contract.",
    ],
    "two_pointers": [
        "Start with two indices whose relative positions encode the search space still worth considering.",
        "Compare the values at the pointers to decide which side can no longer lead to a better or valid answer.",
        "Move only that pointer, preserving the invariant that no skipped candidate is needed later.",
        "Stop when the pointers cross or when the required pair/window has been found.",
    ],
    "sliding_window": [
        "Maintain a left boundary, a right boundary, and summary state for exactly the current window.",
        "Expand the right boundary to include new information.",
        "While the window violates or satisfies the target condition, move the left boundary and update the summary state.",
        "Record the best/count/valid answer only at the moment the window invariant matches the problem requirement.",
    ],
    "matrix_simulation": [
        "Choose a stable traversal order or a marker scheme before mutating cells.",
        "For each cell, derive the target row/column/neighbor state from the original information.",
        "When mutation is in-place, use temporary markers or boundary variables so unread state is not destroyed.",
        "Perform any final cleanup pass needed to convert markers into the required output values.",
    ],
    "hash_map": [
        "Define what each key maps to: count, index, representative object, or current best state.",
        "Process each item and update the map exactly once per observation.",
        "Use membership/count comparisons to detect matches without scanning prior items again.",
        "Return the stored answer or the map-derived grouping once all observations are incorporated.",
    ],
    "intervals": [
        "Sort intervals by the boundary that makes overlap decisions local.",
        "Keep the current merged interval, active end, or count of resources as the invariant.",
        "For each next interval, decide whether it overlaps the current state or starts a new independent block.",
        "Update the merged list, count, or best answer from that local overlap decision.",
    ],
    "stack": [
        "Use the stack to hold items whose answer is not known yet.",
        "For each new item, compare it with the stack top.",
        "Pop while the new item resolves the previous unresolved state, updating the answer or area/count as needed.",
        "Push the current item if it may be needed by a future element.",
    ],
    "linked_list": [
        "Use a dummy node or explicit previous/current pointers to make head changes safe.",
        "Save any next pointer before rewiring links.",
        "Perform pointer changes in an order that never loses access to the remainder of the list.",
        "Return the new head, usually `dummy.next` or the tracked head pointer.",
    ],
    "tree_dfs": [
        "Write the base case for an empty node first.",
        "Let each recursive call return exactly the information its parent needs.",
        "Combine left and right results at the current node.",
        "Update any global/nonlocal answer before returning the parent-facing value.",
    ],
    "tree_bfs": [
        "Push the root into a queue and process nodes level by level.",
        "For each level, snapshot the queue size so the level boundary is explicit.",
        "Collect or update the answer from nodes in that level.",
        "Append children for the next level in the order required by the problem.",
    ],
    "bst": [
        "Use the fact that left subtree values are smaller and right subtree values are larger.",
        "Move left or right when searching, or use inorder traversal when sorted order is needed.",
        "Keep only the previous node, candidate answer, or search interval required by the task.",
        "Return once the BST invariant has narrowed the answer enough.",
    ],
    "graph": [
        "Build an adjacency structure from the input relationships.",
        "Track visited state so each node/state is processed safely and cycles do not loop forever.",
        "Run DFS or BFS according to whether the problem needs reachability, components, ordering, or shortest unweighted distance.",
        "Update the answer from the traversal result, not from one arbitrary visit order.",
    ],
    "advanced_graph": [
        "Build the graph with the edge information the algorithm needs, such as weights, prerequisites, or directed edges.",
        "Choose the graph primitive that matches the requirement: heap for weighted shortest path, indegree for topological order, or union-find for connectivity.",
        "Maintain the algorithm's invariant at every pop/union/relaxation step.",
        "Return the value implied by that invariant once all reachable states or required nodes have been processed.",
    ],
    "bfs": [
        "Put the start state(s) in a queue and mark them visited immediately.",
        "Process the queue in layers when distance or minimum steps matters.",
        "Generate valid neighboring states and skip anything out of bounds or already visited.",
        "The first time the target layer/state is reached, the BFS distance is minimal.",
    ],
    "trie": [
        "Insert each word or key character by character into trie nodes.",
        "Store terminal markers so full words can be distinguished from prefixes.",
        "For a query, walk the trie according to the query characters.",
        "Return based on whether traversal ends at a terminal word, valid prefix, or wildcard-expanded branch.",
    ],
    "backtracking": [
        "Represent the partial candidate explicitly, along with any sets/counters that make validity checks fast.",
        "At each recursion level, try every valid next choice.",
        "Append the choice, recurse, then undo the choice before trying the next branch.",
        "Record a copy of the candidate only when it satisfies the full target condition.",
    ],
    "divide_and_conquer": [
        "Split the input around a midpoint or pivot into smaller independent subproblems.",
        "Solve each side recursively until reaching the base case.",
        "Combine the left and right answers with any crossing/boundary information.",
        "Return the combined result to the caller.",
    ],
    "kadane": [
        "Keep the best value ending exactly at the current position.",
        "At each item, choose between extending the previous run or starting fresh.",
        "Update the global best after the current-position value is known.",
        "Return the global best after the scan.",
    ],
    "binary_search": [
        "Choose search bounds that are guaranteed to contain the answer.",
        "Compute the midpoint and evaluate the sorted-side or monotonic condition.",
        "Discard the half that cannot contain a valid answer.",
        "Continue until the bounds identify the answer or prove it absent.",
    ],
    "heap": [
        "Push candidates into a heap using the tuple/key that makes the needed item appear at the top.",
        "Pop from the heap whenever the current best candidate is needed or stale.",
        "For fixed-size top-k problems, keep only k useful candidates by popping excess items.",
        "Build the return value from the heap or from the sequence of popped candidates.",
    ],
    "bit_manipulation": [
        "Encode the relevant state as bits, such as membership, parity, carry, or a rolling mask.",
        "Use shifts, masks, xor, and/or to update that state in O(1).",
        "Preserve only the bits that are still relevant to the current window or invariant.",
        "Decode or return the final bit state according to the problem contract.",
    ],
    "math_geometry": [
        "Derive the formula or invariant before writing loops.",
        "Normalize values when needed so equivalent cases have the same representation.",
        "Apply the formula directly while guarding special cases such as zero, duplicates, or vertical lines.",
        "Return the derived quantity rather than simulating unnecessary intermediate states.",
    ],
    "math": [
        "Identify the arithmetic property that determines the answer.",
        "Reduce the input using that property instead of brute-force enumeration.",
        "Handle sign, overflow-style boundaries, and zero/one edge cases explicitly.",
        "Return the computed value once the invariant is fully evaluated.",
    ],
    "dynamic_programming": [
        "Define `dp[i]` or an equivalent state as the answer for a prefix/subproblem.",
        "Initialize the base case(s) that do not depend on prior work.",
        "Fill states in an order where every transition reads already-computed values.",
        "Return the final state that corresponds to the full input.",
    ],
    "multidimensional_dp": [
        "Define a state with multiple coordinates, such as two indices, an interval, or a remaining capacity.",
        "Initialize boundary rows/columns or smallest intervals.",
        "Fill the table so every transition reads smaller or already-known states.",
        "Return the cell/state representing the complete problem.",
    ],
    "greedy": [
        "Sort or scan in the order that exposes the locally dominant choice.",
        "Keep the smallest state needed to preserve future feasibility.",
        "Make the local choice and update that state immediately.",
        "The exchange argument is that replacing an optimal solution's first differing choice with this local choice does not hurt the final answer.",
    ],
}


SOLUTION_HEADER_SLUG_WALKTHROUGHS = {
    "product-of-array-except-self": [
        "Create an answer array filled with 1s.",
        "Scan left to right with a running prefix product; store the product of values strictly left of each index.",
        "Scan right to left with a running suffix product; multiply each stored prefix by the product of values strictly right of that index.",
        "Update the running product only after using it at the current index so `nums[i]` is never included in its own answer.",
    ],
    "top-k-frequent-elements": [
        "Count how many times each number appears.",
        "Create frequency buckets where bucket `i` stores all values that appear exactly `i` times.",
        "Scan buckets from high frequency to low frequency and append values until k answers have been collected.",
        "This avoids sorting all unique values, so the bucket version reaches linear time in the input size.",
    ],
    "minimum-window-substring": [
        "Count the characters required by `t`, including duplicates.",
        "Move the right boundary across `s`, reducing the remaining need when a useful character enters the window.",
        "Once all required characters are covered, move the left boundary to make the window as small as possible while still valid.",
        "Record the smallest valid window seen during this expand-then-shrink process.",
    ],
    "find-median-from-data-stream": [
        "Maintain two heaps: a max-heap for the lower half and a min-heap for the upper half.",
        "Insert each new number into the heap whose range it belongs to.",
        "Rebalance so the heap sizes differ by at most one.",
        "The median is either the top of the larger heap or the average of both heap tops.",
    ],
    "course-schedule-ii": [
        "Build the prerequisite graph.",
        "Use DFS/BFS topological logic to ensure every prerequisite appears before the course that depends on it.",
        "Detect cycles; a cycle means no valid course order exists.",
        "Return any ordering that satisfies all prerequisite edges.",
    ],
    "alien-dictionary": [
        "Compare adjacent words to extract the first character ordering constraint where they differ.",
        "Reject invalid prefix cases, such as a longer word appearing before its own prefix.",
        "Topologically sort the character graph.",
        "Any order that satisfies all extracted constraints is valid.",
    ],
    "word-search-ii": [
        "Build a trie from all target words so shared prefixes are searched once.",
        "Start DFS from each board cell and follow trie edges that match neighboring characters.",
        "Mark cells as temporarily used during one path, then unmark them during backtracking.",
        "Whenever a trie terminal word is reached, add it to the result and avoid duplicate reporting.",
    ],
    "largest-rectangle-in-histogram": [
        "Maintain a monotonic increasing stack of bar indices/heights.",
        "When a shorter bar arrives, pop taller bars because their right boundary is now known.",
        "For each popped bar, compute area using the current index as the right boundary and the new stack top as the left boundary.",
        "Append a sentinel or finish with a cleanup pass so all remaining bars are evaluated.",
    ],
    "sliding-window-maximum": [
        "Maintain a deque of indices whose values are decreasing from front to back.",
        "Remove indices that fall out of the current window.",
        "Before adding a new index, remove smaller values from the back because they can never become the maximum while the new value remains.",
        "The front of the deque is the maximum for each complete window.",
    ],
    "trapping-rain-water": [
        "Track the highest wall seen from the left and from the right.",
        "Move the pointer on the side with the smaller current boundary.",
        "That smaller boundary limits the water level at that side, independent of farther bars on the larger side.",
        "Accumulate positive differences between the boundary and current bar height.",
    ],
    "regular-expression-matching": [
        "Let a DP/recursive state represent whether `s[i:]` matches `p[j:]`.",
        "A direct character match succeeds when characters are equal or the pattern has `.`.",
        "When the next pattern character is `*`, branch between skipping the `x*` token or consuming one matching character.",
        "Memoization or bottom-up filling prevents exponential recomputation.",
    ],
    "edit-distance": [
        "Let `dp[i][j]` be the minimum edits to convert the first i characters of one word to the first j of the other.",
        "Initialize empty-prefix conversions with insertions/deletions.",
        "If the current characters match, inherit the diagonal state.",
        "Otherwise take one plus the best insert, delete, or replace transition.",
    ],
    "serialize-and-deserialize-binary-tree": [
        "Serialize with a traversal that records both node values and null markers.",
        "During deserialization, consume tokens in the same order they were produced.",
        "Null markers are what make the tree shape unambiguous.",
        "Rebuild child pointers recursively or iteratively according to that token stream.",
    ],
}


def solution_header_description(problem: dict[str, Any], detail: dict[str, Any] | None) -> str:
    if detail:
        sections = split_problem_content(detail.get("content"))
        neetcode_question = detail.get("neetcode_question") or {}
        if not sections["description"] and neetcode_question:
            sections = neetcode_question.get("sections", sections)
        for line in sections.get("description", []):
            if line and not line.startswith("Statement source:"):
                return line[:320]
    return f"Solve {problem['title']} using the local problem contract."


def solution_header_example(detail: dict[str, Any] | None) -> tuple[str, str]:
    if not detail:
        return "", ""
    examples = extract_official_examples(detail.get("content"))
    neetcode_question = detail.get("neetcode_question") or {}
    if not examples and neetcode_question:
        examples = neetcode_question.get("examples", examples)
    if not examples:
        return "", ""
    return examples[0].get("input", ""), examples[0].get("output", "")


def solution_header_follow_up(detail: dict[str, Any] | None) -> str:
    if not detail:
        return ""
    sections = split_problem_content(detail.get("content"))
    neetcode_question = detail.get("neetcode_question") or {}
    if not sections["follow_up"] and neetcode_question:
        sections = neetcode_question.get("sections", sections)
    return sections["follow_up"][0] if sections.get("follow_up") else ""


def solution_header_optimization_note(problem: dict[str, Any]) -> str:
    tags = set(problem.get("tags", []))
    if "bucket-sort" in tags:
        return "Here, frequency/count buckets can avoid a full sort when counts are bounded by input length."
    if "quickselect" in tags:
        return "Quickselect is another useful comparison point when only the top-k boundary matters."
    if "heap-priority-queue" in tags:
        return "A heap variant is often simpler for top-k or repeated min/max access, but may add a log factor."
    if "topological-sort" in tags:
        return "For ordering problems, compare the exact output against the dependency constraints rather than one fixed ordering."
    return ""


def solution_header_walkthrough(problem: dict[str, Any], approach: str) -> str:
    steps = SOLUTION_HEADER_SLUG_WALKTHROUGHS.get(problem.get("slug")) or SOLUTION_HEADER_WALKTHROUGHS.get(approach) or [
        "Identify the invariant that the solution maintains.",
        "Update the state in the order implied by the input.",
        "Record or return the answer once the invariant proves the required condition.",
    ]
    return "\n".join(f"{index}. {step}" for index, step in enumerate(steps, start=1))


def solution_header_why_it_works(problem: dict[str, Any], approach: str) -> str:
    slug = problem.get("slug")
    if slug in {"course-schedule-ii", "alien-dictionary"}:
        return "The output is checked by constraints rather than by one fixed ordering: every directed edge must place its prerequisite/source before its dependent/target, and cycle detection protects impossible cases."
    if slug == "top-k-frequent-elements":
        return "Every value is placed in the bucket equal to its exact frequency. Scanning buckets from highest to lowest frequency visits candidates in the only order that matters for top-k."
    if slug == "product-of-array-except-self":
        return "For each index, the wanted product is product(values left of i) times product(values right of i). The two passes compute exactly those two pieces without division, so zeros are handled naturally."
    if slug == "minimum-window-substring":
        return "The window is expanded until it covers all required characters, then shrunk until removing the left character would break validity. Every valid minimal candidate is considered at the moment it becomes tight."
    if slug == "find-median-from-data-stream":
        return "The heaps partition the stream into lower and upper halves. Balancing keeps the median at one or both heap tops, so no full sort is needed after each insertion."
    if slug == "word-search-ii":
        return "The trie prunes any board path that is not a prefix of a target word, while the visited markers enforce the no-cell-reuse rule for the current DFS path."
    if approach in {"sliding_window", "two_pointers"}:
        return "Each pointer only moves forward, and the maintained state describes exactly the current candidate range. Anything skipped has been proven unable to improve or satisfy the answer."
    if approach in {"dynamic_programming", "multidimensional_dp"}:
        return "Each state is defined in terms of smaller states that have already been solved, so the final state composes all required choices without recomputing subproblems."
    if approach in {"backtracking", "tree_dfs", "graph", "advanced_graph", "bfs"}:
        return "The traversal explores only valid next states and records visited/used state where needed, so every feasible candidate is considered without reusing forbidden state."
    if approach == "heap":
        return "The heap invariant keeps the next best candidate at the top after every push/pop, which is exactly the repeated choice the algorithm needs."
    return "The maintained state is updated after every relevant input item, so when the scan/traversal finishes it represents the full problem rather than a local snapshot."


def solution_header_example_walkthrough(problem: dict[str, Any], approach: str, example_input: str, example_output: str) -> str:
    if not example_input and not example_output:
        return "Use the first example in prompt.md and trace the state variables named in the walkthrough above."
    slug = problem.get("slug")
    if slug == "top-k-frequent-elements":
        return "For the sample, the counts are 1 -> 3, 2 -> 2, and 3 -> 1. The bucket scan starts at frequency 3, then frequency 2, producing the two most frequent values."
    if slug == "product-of-array-except-self":
        return "For [1,2,3,4], the left-products pass produces [1,1,2,6]. The right-products pass multiplies by suffixes [24,12,4,1], producing [24,12,8,6]."
    if slug == "minimum-window-substring":
        return "For the sample, the window first becomes valid at `ADOBEC`. The left boundary then advances, and the best tight window eventually becomes `BANC`."
    if slug == "find-median-from-data-stream":
        return "After adding 1 and 2, the two heap tops are 1 and 2, so the median is 1.5. After adding 3, the upper half has one extra item and its top is 2."
    if slug == "word-search-ii":
        return "In the sample board, DFS paths following trie prefixes can complete `oath` and `eat`; paths toward `pea` or `rain` fail because some required next character is not adjacent in the board."
    if approach == "backtracking":
        return "Trace the first example as a recursion tree: each level adds one choice, invalid branches stop early, and complete valid candidates are copied into the result."
    if approach in {"dynamic_programming", "multidimensional_dp"}:
        return "Trace the first example by writing the base states first, then filling later states from earlier ones until the cell/state for the full input gives the shown output."
    if approach in {"graph", "advanced_graph", "bfs"}:
        return "Trace the first example by drawing nodes and edges, then follow the queue/stack/heap order while marking visited state to see why the shown output is reached."
    if approach in {"sliding_window", "two_pointers"}:
        return "Trace the first example by moving the boundaries one step at a time and checking when the maintained invariant first matches the expected output."
    return f"For the sample input `{example_input}`, the maintained invariant described above leads to `{example_output}`."


LOCAL_REFERENCE_OVERRIDES: dict[str, dict[str, str]] = {
    "product-of-array-except-self": {
        "complexity": "Time: O(n); Space: O(1) extra, excluding the output array.",
        "source_note": "Local prefix/suffix reference implementation.",
        "body": '''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            answer[i] = prefix
            prefix *= num

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
''',
    }
}


def build_solution_header(
    problem: dict[str, Any],
    approach: str,
    complexity: str,
    source_path: Path | None,
    detail: dict[str, Any] | None = None,
) -> str:
    source_note = problem.get("reference_source_note") or "AI-authored educational reference solution pending."
    description = solution_header_description(problem, detail)
    idea = SOLUTION_HEADER_APPROACH_IDEAS.get(approach, "Use the invariant in the problem statement to guide each update.")
    optimization_note = solution_header_optimization_note(problem)
    follow_up = solution_header_follow_up(detail)
    example_input, example_output = solution_header_example(detail)
    walkthrough = solution_header_walkthrough(problem, approach)
    why_it_works = solution_header_why_it_works(problem, approach)
    example_walkthrough = solution_header_example_walkthrough(problem, approach, example_input, example_output)
    tags = ", ".join(tag.get("name", tag) if isinstance(tag, dict) else tag for tag in problem.get("topic_tags", [])[:6]) or "None"
    extra_lines = []
    if optimization_note:
        extra_lines.append(f"- Optimization note: {optimization_note}")
    if follow_up:
        extra_lines.append(f"- Follow-up target: {follow_up}")
    extra_text = "\n".join(extra_lines) + "\n" if extra_lines else ""
    if example_input or example_output:
        example_lines = f"- Input: {example_input}\n- Output: {example_output}"
    else:
        example_lines = "- See prompt.md for the local examples and expected outputs."
    return f'''"""
{problem["id"]}. {problem["title"]} - {approach.replace("_", " ").title()} Reference

What this reference demonstrates:
- Problem focus: {description}
- Core idea: {idea}
{extra_text}- Tags to connect while studying: {tags}

Example to keep in mind:
{example_lines}

Algorithm walkthrough:
{walkthrough}

Why this works:
{why_it_works}

Example walkthrough:
{example_walkthrough}

Review use:
- First make your own `solution.py` pass the local tests.
- Then compare against this reference for the invariant, edge-case coverage, and asymptotic complexity.
- If your solution is simpler but asymptotically slower, keep that tradeoff explicit in your notes.

Complexity: {complexity}
Source: {source_note}

For your own attempt, edit ../solution.py instead of this file.
"""

'''


def strip_generated_reference_imports(source: str) -> str:
    lines = []
    for line in source.rstrip().splitlines():
        stripped = line.strip()
        if any(stripped.startswith(prefix) for prefix in GENERATED_IMPORT_PREFIXES):
            continue
        lines.append(line.rstrip())
    return "\n".join(lines).strip("\n") + "\n"


def reference_imports_for_body(body: str, slug: str | None = None) -> str:
    imports = import_requirements_for_body(body, slug=slug)
    if not imports:
        return ""
    definition_comments = lc_type_definition_comment_block(imports)
    if definition_comments:
        return "\n".join(imports) + "\n\n\n" + definition_comments + "\n\n\n"
    return "\n".join(imports) + "\n\n"


def format_signature_snippet(snippet: str) -> str:
    text = "\n".join(line.rstrip() for line in snippet.rstrip().splitlines())
    text = re.sub(
        r"(?m)(^# Definition for[^\n]*\n(?:^#.*\n)+)\n*(?=^class )",
        lambda match: match.group(1).rstrip() + "\n\n\n",
        text,
    )
    text = re.sub(
        r'(?ms)("""\n# Definition for.*?\n""")\n*(?=class )',
        lambda match: match.group(1).rstrip() + "\n\n\n",
        text,
    )
    return text


def normalize_neetcode_source(slug: str, source: str) -> str:
    lines = [line.rstrip() for line in source.rstrip().splitlines()]
    lines = [line for line in lines if not line.lstrip().startswith("print(")]
    body = "\n".join(lines)
    if slug == "graph-valid-tree":
        body = body.split("# alternative solution", 1)[0].rstrip()
    if slug == "walls-and-gates":
        body = body.replace("def walls_and_gates(self, rooms", "def wallsAndGates(self, rooms")
    if body.lstrip().startswith("def "):
        body = "class Solution:\n" + textwrap.indent(body, "    ")
    return body + "\n"


def approach_for(problem: dict[str, Any]) -> str:
    section = problem["section"]
    if problem["slug"] in {"two-sum", "isomorphic-strings", "word-pattern", "valid-anagram", "group-anagrams"}:
        return "hash_map"
    if problem["slug"] in {"minimum-window-substring", "longest-substring-without-repeating-characters"}:
        return "sliding_window"
    if problem["slug"] in {"search-insert-position", "search-a-2d-matrix", "find-peak-element"}:
        return "binary_search"
    return SECTION_APPROACHES.get(section, snake(section))


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        write(path, content)


def write_solution_template(path: Path, content: str) -> None:
    if not path.exists() or is_untouched_solution_template(path):
        write(path, content)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def markdown_table(rows: list[list[str]], headers: list[str]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    out += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(out)


class LeetCodeHTMLTextParser(HTMLParser):
    BLOCK_TAGS = {"p", "div", "pre", "ul", "ol", "li", "table", "tr", "blockquote"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[tuple[str, bool]] = []
        self.skip_depth = 0
        self.pre_depth = 0

    def append(self, text: str) -> None:
        self.parts.append((text, self.pre_depth > 0))

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "pre":
            self.append("\n")
            self.pre_depth += 1
            return
        if tag == "br":
            self.append("\n")
        elif tag == "li":
            self.append("\n- ")
        elif tag == "sup":
            self.append("^")
        elif tag in self.BLOCK_TAGS:
            self.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "pre" and self.pre_depth:
            self.pre_depth -= 1
            self.append("\n")
            return
        if tag in self.BLOCK_TAGS:
            self.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        self.append(data)


def html_to_lines(raw_html: str | None) -> list[str]:
    if not raw_html:
        return []
    parser = LeetCodeHTMLTextParser()
    parser.feed(raw_html)
    lines = []
    pending: list[str] = []
    preserve_pending = False

    def flush() -> None:
        nonlocal pending, preserve_pending
        raw_line = html.unescape("".join(pending)).replace("\xa0", " ").replace("\u200b", "")
        if preserve_pending:
            line = raw_line.rstrip()
        else:
            line = re.sub(r"[ \t]+", " ", raw_line).strip()
        if line:
            lines.append(line)
        pending = []
        preserve_pending = False

    for text, preserve in parser.parts:
        for chunk in text.splitlines(keepends=True):
            has_newline = chunk.endswith(("\n", "\r"))
            pending.append(chunk.rstrip("\r\n"))
            preserve_pending = preserve_pending or preserve
            if has_newline:
                flush()
    if pending:
        flush()
    return lines


def similar_questions_from_detail(detail: dict[str, Any]) -> list[dict[str, str]]:
    raw = detail.get("similarQuestions")
    if not raw:
        return []
    try:
        items = json.loads(raw)
    except json.JSONDecodeError:
        return []
    cleaned = []
    for item in items:
        if not isinstance(item, dict):
            continue
        cleaned.append(
            {
                "title": item.get("title", ""),
                "titleSlug": item.get("titleSlug", ""),
                "difficulty": title_case_difficulty(str(item.get("difficulty", "")).lower()),
            }
        )
    return cleaned


def question_detail_for_index(detail: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in detail.items() if key != "content"}


def strip_label(line: str, label: str) -> str:
    return re.sub(rf"^{label}\s*:?\s*", "", line, flags=re.IGNORECASE).strip()


def split_problem_lines(lines: list[str]) -> dict[str, list[str]]:
    description: list[str] = []
    constraints: list[str] = []
    follow_up: list[str] = []
    mode = "description"
    for line in lines:
        if re.match(r"^Example(?:\s+\d+)?\s*:?", line, flags=re.IGNORECASE):
            mode = "examples"
            continue
        if re.match(r"^Constraints\s*:?", line, flags=re.IGNORECASE):
            mode = "constraints"
            rest = strip_label(line, "Constraints")
            if rest:
                constraints.append(rest)
            continue
        if mode == "description" and re.match(r"^(For simplicity sake, )?you may assume\b", line, flags=re.IGNORECASE):
            mode = "constraints"
            constraints.append(line)
            continue
        if re.match(r"^Follow[- ]?up\s*:?", line, flags=re.IGNORECASE):
            mode = "follow_up"
            rest = re.sub(r"^Follow[- ]?up\s*:?\s*", "", line, flags=re.IGNORECASE).strip()
            if rest:
                follow_up.append(rest)
            continue
        if mode == "description":
            description.append(line)
        elif mode == "constraints":
            constraints.append(line)
        elif mode == "follow_up":
            follow_up.append(line)
    return {
        "description": description,
        "constraints": constraints,
        "follow_up": follow_up,
    }


def split_problem_content(raw_html: str | None) -> dict[str, list[str]]:
    return split_problem_lines(html_to_lines(raw_html))


EXAMPLE_HEADING_PATTERN = re.compile(r"^Example(?:\s+(\d+))?\s*:?", re.IGNORECASE)
EXAMPLE_LABEL_PATTERN = re.compile(r"^(Input|Output|Explanation)\s*:?\s*(.*)$", re.IGNORECASE)
EXAMPLE_INPUT_INTRO_PATTERN = re.compile(
    r"^(Assume that|If\b.*\bhas the following content|Given\b.*\bfollowing content)",
    re.IGNORECASE,
)
EXAMPLE_OUTPUT_INTRO_PATTERN = re.compile(
    r"^(Your script should output|Output the following|The output should be)",
    re.IGNORECASE,
)


def append_example_line(example: dict[str, str], label: str, line: str) -> None:
    separator = "\n" if example.get(label) else ""
    example[label] = example.get(label, "") + separator + line


def examples_from_lines(lines: list[str]) -> list[dict[str, str]]:
    examples: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    current_label: str | None = None
    next_index = 1

    def flush() -> None:
        nonlocal current
        if current and any(current.get(key) for key in ("input", "output", "explanation")):
            examples.append(current)
        current = None

    for line in lines:
        heading = EXAMPLE_HEADING_PATTERN.match(line)
        if heading:
            flush()
            index = heading.group(1) or str(next_index)
            next_index += 1
            current = {"name": f"Example {index}"}
            current_label = None
            continue
        if current is None:
            continue
        if re.match(r"^(Constraints|Follow[- ]?up|Note)\s*:?", line, flags=re.IGNORECASE):
            flush()
            break
        match = EXAMPLE_LABEL_PATTERN.match(line)
        if match:
            current_label = match.group(1).lower()
            value = match.group(2).strip()
            if value:
                example_label = current_label
                current[example_label] = value
        elif EXAMPLE_INPUT_INTRO_PATTERN.match(line):
            current_label = "input"
            append_example_line(current, current_label, line)
        elif EXAMPLE_OUTPUT_INTRO_PATTERN.match(line):
            current_label = "output"
            append_example_line(current, current_label, line)
        elif current_label and line:
            append_example_line(current, current_label, line)
    flush()
    return examples


def extract_official_examples(raw_html: str | None) -> list[dict[str, str]]:
    if not raw_html:
        return []
    return examples_from_lines(html_to_lines(raw_html))


NEETCODE_CONTENT_STOP_PATTERN = re.compile(
    r"^(Topics|Recommended Time|Hint\s+\d+|Company Tags|Seen this question|Acceptance Rate|Python|Java|C\+\+|"
    r"JavaScript|TypeScript|Auto|Solution\s+\d+|Test Case|Output|Console|Run Submit)$",
    re.IGNORECASE,
)

NEETCODE_UI_LINES = {
    "Pro",
    "Sign in",
    "×",
    "ESC",
    "- Question",
    "- Solution",
    "- Submissions",
    "- Discuss",
    "Question",
    "Solution",
    "Submissions",
    "Discuss",
}


def neetcode_question_url(url: str) -> str:
    base = url.rstrip("/")
    if base.endswith("/question"):
        return base
    return f"{base}/question"


def neetcode_content_start(lines: list[str], title: str) -> int:
    for index, line in enumerate(lines):
        if line == title and any(
            re.match(r"^(Easy|Medium|Hard)\b", candidate, flags=re.IGNORECASE)
            for candidate in lines[index + 1 : index + 5]
        ):
            return index + 1
    for index, line in enumerate(lines):
        if line == title:
            return index + 1
    for index, line in enumerate(lines):
        if line in {"- Discuss", "Discuss"}:
            start = index + 1
            while start < len(lines) and (lines[start] in NEETCODE_UI_LINES or lines[start].endswith("- NeetCode")):
                start += 1
            return min(start + 1, len(lines))
    return 0


def split_neetcode_topics(topic_lines: list[str]) -> list[str]:
    topics: list[str] = []
    known_topics = [
        "Heap (Priority Queue)",
        "Two Pointers",
        "Prefix Sum",
        "Dynamic Programming",
        "Depth First Search",
        "Breadth First Search",
        "Union Find",
        "Hash Table",
        "Linked List",
        "Binary Search",
        "Bit Manipulation",
        "Topological Sort",
        "Array",
        "String",
        "Design",
        "Graph",
        "Sorting",
        "Greedy",
        "Matrix",
        "Trie",
        "Stack",
        "Tree",
    ]
    for line in topic_lines:
        remaining = line
        for topic in known_topics:
            if topic in remaining and topic not in topics:
                topics.append(topic)
                remaining = remaining.replace(topic, " ")
        for part in re.split(r"\s{2,}|,\s*", remaining):
            cleaned = part.strip()
            if cleaned and cleaned not in topics:
                topics.append(cleaned)
    return topics


def clean_neetcode_content_line(line: str) -> str:
    # NeetCode pages can expose visible MathJax, raw TeX, and rendered MathJax text together.
    return line.replace("m×nm \\times nm×n", "m x n")


def parse_neetcode_question_html(raw_html: str, title: str, url: str) -> dict[str, Any] | None:
    lines = html_to_lines(raw_html)
    start = neetcode_content_start(lines, title)
    content_lines: list[str] = []
    topic_lines: list[str] = []
    collecting_topics = False
    for line in lines[start:]:
        if collecting_topics:
            if NEETCODE_CONTENT_STOP_PATTERN.match(line):
                break
            topic_lines.append(line)
            continue
        if line == "Topics":
            collecting_topics = True
            continue
        if NEETCODE_CONTENT_STOP_PATTERN.match(line):
            break
        if line in NEETCODE_UI_LINES or line.endswith("- NeetCode"):
            continue
        if re.match(r"^(Easy|Medium|Hard)\b", line, flags=re.IGNORECASE):
            continue
        content_lines.append(clean_neetcode_content_line(line))
    sections = split_problem_lines(content_lines)
    examples = examples_from_lines(content_lines)
    if not sections["description"] and not examples:
        return None
    return {
        "url": url,
        "source": "neetcode",
        "sections": sections,
        "examples": examples,
        "topics": split_neetcode_topics(topic_lines),
    }


def fetch_neetcode_question(entry: dict[str, Any] | None, title: str) -> dict[str, Any] | None:
    url = (entry or {}).get("neetcode_url", "")
    if not url:
        return None
    question_url = neetcode_question_url(url)
    neetcode_title = (entry or {}).get("title") or title
    try:
        return parse_neetcode_question_html(request_text(question_url), neetcode_title, question_url)
    except Exception:
        return None


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(", ", ": "))


def study_plan_names(problem: dict[str, Any]) -> list[str]:
    return [STUDY_PLAN_LABELS.get(plan, plan) for plan in problem.get("study_plans", [])]


def study_plan_lines(problem: dict[str, Any]) -> list[str]:
    sections = problem.get("sections_by_plan", {})
    orders = problem.get("study_plan_orders", {})
    lines = []
    for plan in problem.get("study_plans", []):
        label = STUDY_PLAN_LABELS.get(plan, plan)
        parts = [label]
        if plan in orders:
            parts.append(f"order {orders[plan]}")
        if sections.get(plan):
            parts.append(f"section: {sections[plan]}")
        lines.append("- " + "; ".join(parts))
    return lines


def markdown_text_block(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    text_lines = text.splitlines()
    if len(text_lines) == 1:
        return [text]
    return ["```text", *text_lines, "```"]


def markdown_description_lines(lines: list[str]) -> list[str]:
    rendered: list[str] = []
    in_list = False

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue

        is_list_item = bool(re.match(r"^(?:[-*]|\d+\.)\s+", line))
        if is_list_item:
            if rendered and rendered[-1] != "" and not in_list:
                rendered.append("")
            rendered.append(line)
            in_list = True
            continue

        if rendered and rendered[-1] != "":
            rendered.append("")
        rendered.append(line)
        rendered.append("")
        in_list = False

    while rendered and rendered[-1] == "":
        rendered.pop()
    return rendered


def problem_links(problem: dict[str, Any], neetcode_question: dict[str, Any] | None = None) -> list[str]:
    question_url = (neetcode_question or {}).get("url") or problem.get("neetcode", {}).get("question_url", "")
    if problem.get("content_source") == "neetcode" and question_url:
        links = [f"Problem: {question_url}", f"LeetCode: {problem['url']}"]
        return links
    return [f"Problem: {problem['url']}"]


def prompt_md(problem: dict[str, Any], meta: dict[str, Any], cases: list[dict[str, Any]], snippet: str, detail: dict[str, Any]) -> str:
    params = params_from_metadata(meta)
    content_sections = split_problem_content(detail.get("content"))
    official_examples = extract_official_examples(detail.get("content"))
    neetcode_question = detail.get("neetcode_question") or {}
    if not content_sections["description"] and neetcode_question:
        content_sections = neetcode_question.get("sections", content_sections)
        official_examples = neetcode_question.get("examples", official_examples)
    lines = [
        f"# {problem['id']}. {problem['title']}",
        "",
        *problem_links(problem, neetcode_question),
        "",
        "## Study Lists",
        "",
        *study_plan_lines(problem),
        "",
        "## Problem Description",
        "",
    ]
    if content_sections["description"]:
        if neetcode_question:
            lines += [
                "Statement source: NeetCode question page. The matching LeetCode page is Premium-only according to available metadata.",
                "",
            ]
        lines += markdown_description_lines(content_sections["description"]) + [""]
    elif problem.get("is_paid_only"):
        lines += [
            "This appears to be a LeetCode Premium problem. Public LeetCode metadata exposes the signature and example test cases, but not the full statement text.",
            "Open the official LeetCode page if you have Premium access, then use the local signature and tests below for practice.",
            "",
        ]
    else:
        lines += [
            "Implement the interface below for the named LeetCode problem. Use the official link for exact wording nuance.",
            "",
        ]
    lines += [
        "## Signature",
        "",
        "```python",
        format_signature_snippet(snippet),
        "```",
        "",
    ]
    if meta.get("systemdesign"):
        class_name = meta.get("classname", "DesignClass")
        methods = meta.get("methods", [])
        lines += [
            "## Class Contract",
            "",
            f"Implement `{class_name}` with its constructor and public methods.",
            "",
        ]
        for method in methods:
            params_text = ", ".join(f"{p['name']}: {p['type']}" for p in method.get("params", [])) or "no arguments"
            return_type = method.get("return", {}).get("type", "void")
            lines.append(f"- `{method['name']}({params_text}) -> {return_type}`")
        lines.append("")
    elif params:
        rows = [[p["name"], p["type"]] for p in params]
        ret = meta.get("return", {}).get("type", "unknown")
        lines += [
            "## Input / Output Contract",
            "",
            markdown_table(rows, ["Parameter", "Type"]),
            "",
            f"Return type: `{ret}`",
            "",
        ]
    if official_examples:
        lines += ["## Examples", ""]
        for example in official_examples:
            lines.append(f"### {example['name']}")
            lines.append("")
            if example.get("input"):
                lines += ["Input:", "", "```text", example["input"], "```", ""]
            if example.get("output"):
                lines += ["Output:", "", "```text", example["output"], "```", ""]
            if example.get("explanation"):
                lines += ["Explanation:", "", *markdown_text_block(example["explanation"]), ""]
    elif cases:
        lines += ["## Example Inputs", ""]
        for case in cases:
            lines.append(f"### {case['name']}")
            lines.append("")
            lines.append("```json")
            payload = {k: v for k, v in case.items() if k != "name"}
            lines.append(compact_json(payload))
            lines.append("```")
            lines.append("")
        lines.append("Expected outputs are produced by the local reference solution when you run the tests.")
        lines.append("")
    if content_sections["constraints"]:
        lines += ["## Constraints", ""]
        for constraint in content_sections["constraints"]:
            lines.append(constraint)
        lines.append("")
    if content_sections["follow_up"]:
        lines += ["## Follow-up", ""]
        lines += content_sections["follow_up"]
        lines.append("")
    return "\n".join(lines)


def readme_md(problem: dict[str, Any], solution_file: str | None, complexity: str) -> str:
    tags = ", ".join(f"`{tag['slug']}`" for tag in problem["topic_tags"])
    similar_questions = problem.get("similar_questions") or []
    study_lists = ", ".join(f"**{name}**" for name in study_plan_names(problem))
    reference_entries = problem.get("reference_solutions") or []
    if reference_entries:
        primary = Path(problem.get("reference_solution", "")).name
        reference_file_line = f"- `solutions/`: AI-authored reference variants. Primary: `{primary}`."
        reference_section = markdown_table(
            [
                [
                    Path(item.get("file", "")).name,
                    item.get("approach", ""),
                    item.get("complexity", ""),
                ]
                for item in reference_entries
            ],
            ["File", "Approach", "Complexity"],
        )
    else:
        reference_file_line = (
            f"- `solutions/{solution_file}`: reference implementation to study when stuck."
            if solution_file
            else "- `solutions/`: optional reference implementations. Add a legally usable reference before relying on local expected outputs."
        )
        reference_section = (
            markdown_table([[solution_file, problem["approach"].replace("_", " "), complexity]], ["File", "Approach", "Complexity"])
            if solution_file
            else "No reference implementation is available yet."
        )
    reference_run = (
        f"""
Run the reference implementation instead:

```bash
python -m tools.run_problem problems/{problem['folder']} --reference
```
"""
        if solution_file
        else ""
    )
    similar_section = ""
    if similar_questions:
        rows = []
        for item in similar_questions[:10]:
            title = item.get("title") or item.get("translatedTitle") or item.get("titleSlug", "")
            slug = item.get("titleSlug") or ""
            difficulty = item.get("difficulty", "")
            link = f"https://leetcode.com/problems/{slug}/" if slug else problem["url"]
            rows.append([f"[{title}]({link})", difficulty])
        similar_section = f"""
## Similar Questions

{markdown_table(rows, ["Problem", "Difficulty"])}
"""
    links_text = "\n".join(problem_links(problem))
    return f"""# {problem['id']}. {problem['title']}

{links_text}

Difficulty: **{problem['difficulty']}**

Study-plan section: **{problem['section']}**

Study lists: {study_lists}

Tags: {tags}

Status: `{problem['status']}`

## Files

- `prompt.md`: local prompt with description, signature, examples, constraints, follow-up, and study-list membership.
- `solution.py`: your blank attempt file.
{reference_file_line}
- `tests/cases.json`: local example test inputs.
- `notes.md`: pre-filled mental model plus your future review log.

## Reference Solutions

{reference_section}
{similar_section}

## Run

```bash
python -m tools.run_problem problems/{problem['folder']}
```
{reference_run}
"""


def notes_md(problem: dict[str, Any], solution_file: str | None, complexity: str) -> str:
    section_model = SECTION_MENTAL_MODELS.get(problem["section"], "Identify the problem invariant before writing code.")
    pitfalls = []
    for tag in problem["topic_tags"]:
        pitfall = TAG_PITFALLS.get(tag["slug"])
        if pitfall and pitfall not in pitfalls:
            pitfalls.append(pitfall)
    if not pitfalls:
        pitfalls.append("Write down edge cases before coding, especially empty inputs, duplicates, and boundary sizes.")
    pitfalls_text = "\n".join(f"- {item}" for item in pitfalls[:6])
    tags_text = ", ".join(tag["name"] for tag in problem["topic_tags"]) or "TBD"
    reference_text = (
        f"- `{solution_file}`: {problem['approach'].replace('_', ' ')} reference implementation.\n\nComplexity: {complexity}"
        if solution_file
        else "No reference implementation is available yet. Add a legally usable reference before using the local runner as an expected-output oracle."
    )
    return f"""# Notes - {problem['id']}. {problem['title']}

## Core Idea

Primary section: **{problem['section']}**

Tags: {tags_text}

{section_model}

Start by making the invariant explicit in one sentence. Then code the smallest version that maintains that invariant on every iteration or recursive call.

## Reference Solution

{reference_text}

## Pitfalls To Watch

{pitfalls_text}

## Edge Cases

- Minimum input size.
- Repeated values or repeated characters.
- Already-sorted, reverse-sorted, or already-valid inputs when relevant.
- Cases where the answer is empty, zero, or impossible.
- For in-place problems, verify both the returned value and the mutated prefix/object state.

## Interview Explanation Checklist

- State the data structure or invariant first.
- Explain why the loop/recursion makes progress.
- Explain why the chosen update cannot discard a valid answer.
- Give time and space complexity without relying on LeetCode runtime numbers.

## Review Log

Add review observations here after Codex reviews your `solution.py`.
"""


def root_readme(plan: dict[str, Any]) -> str:
    return (ROOT / "README.md").read_text(encoding="utf-8")


def workflow_md() -> str:
    return (ROOT / "WORKFLOW.md").read_text(encoding="utf-8")


def pyproject_toml() -> str:
    return """[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["problems", "tests"]
"""


def lc_types_py() -> str:
    return '''from __future__ import annotations

from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


_UNSET = object()


class GraphNode:
    def __init__(self, val: int = 0, neighbors: Optional[list["GraphNode"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class RandomPointerNode:
    def __init__(
        self,
        x=_UNSET,
        next: Optional["RandomPointerNode"] = None,
        random: Optional["RandomPointerNode"] = None,
        *,
        val=_UNSET,
    ):
        if x is _UNSET:
            x = 0 if val is _UNSET else val
        self.val = int(x)
        self.next = next
        self.random = random


class NextTreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["NextTreeNode"] = None,
        right: Optional["NextTreeNode"] = None,
        next: Optional["NextTreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class QuadTreeNode:
    def __init__(
        self,
        val: bool = False,
        isLeaf: bool = False,
        topLeft: Optional["QuadTreeNode"] = None,
        topRight: Optional["QuadTreeNode"] = None,
        bottomLeft: Optional["QuadTreeNode"] = None,
        bottomRight: Optional["QuadTreeNode"] = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Node:
    """Backward-compatible catch-all Node.

    New generated problem files should import a problem-specific node class as
    `Node`. This compatibility class remains for older local solutions and
    scratch work that still import `Node` directly.
    """

    def __init__(
        self,
        val=_UNSET,
        neighbors: Optional[list["Node"]] = None,
        next: Optional["Node"] = None,
        random: Optional["Node"] = None,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        isLeaf: bool = False,
        topLeft: Optional["Node"] = None,
        topRight: Optional["Node"] = None,
        bottomLeft: Optional["Node"] = None,
        bottomRight: Optional["Node"] = None,
        x=_UNSET,
    ):
        if val is _UNSET:
            val = 0 if x is _UNSET else x
        if isinstance(neighbors, bool):
            isLeaf = neighbors
            topLeft, topRight, bottomLeft, bottomRight = next, random, left, right
            neighbors = None
            next = random = left = right = None
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        self.next = next
        self.random = random
        self.left = left
        self.right = right
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next


def build_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def list_to_values(head):
    values = []
    seen = set()
    while head is not None:
        ident = id(head)
        if ident in seen:
            raise ValueError("cycle detected while serializing ListNode")
        seen.add(ident)
        values.append(head.val)
        head = head.next
    return values


def build_tree(values):
    if not values:
        return None
    nodes = [None if value is None else TreeNode(value) for value in values]
    kids = deque(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        if kids:
            node.left = kids.popleft()
        if kids:
            node.right = kids.popleft()
    return nodes[0]


def tree_to_values(root):
    if root is None:
        return []
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(getattr(node, "left", None))
        queue.append(getattr(node, "right", None))
    while values and values[-1] is None:
        values.pop()
    return values


def find_tree_node(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    return find_tree_node(root.left, target) or find_tree_node(root.right, target)


def build_graph(adjacency):
    if not adjacency:
        return None
    nodes = [GraphNode(i + 1) for i in range(len(adjacency))]
    for i, neighbors in enumerate(adjacency):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def graph_to_adjacency(node):
    if node is None:
        return []
    seen = {}
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        if cur.val in seen:
            continue
        seen[cur.val] = cur
        for nxt in getattr(cur, "neighbors", []):
            if nxt.val not in seen:
                queue.append(nxt)
    return [[neighbor.val for neighbor in seen[i].neighbors] for i in sorted(seen)]


def build_random_list(values):
    if not values:
        return None
    nodes = [RandomPointerNode(pair[0]) for pair in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for node, pair in zip(nodes, values):
        random_idx = pair[1]
        node.random = None if random_idx is None else nodes[random_idx]
    return nodes[0]


def random_list_to_values(head):
    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    index = {id(node): i for i, node in enumerate(nodes)}
    out = []
    for node in nodes:
        random = getattr(node, "random", None)
        out.append([node.val, None if random is None else index.get(id(random))])
    return out


def build_next_tree(values):
    if not values:
        return None
    nodes = [None if value is None else NextTreeNode(value) for value in values]
    kids = deque(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        if kids:
            node.left = kids.popleft()
        if kids:
            node.right = kids.popleft()
    return nodes[0]


def next_tree_to_levels(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if getattr(node, "left", None):
                queue.append(node.left)
            if getattr(node, "right", None):
                queue.append(node.right)
        result.extend(level)
        result.append("#")
    return result


def quad_tree_to_values(node):
    if node is None:
        return None
    return [
        bool(getattr(node, "isLeaf", False)),
        bool(getattr(node, "val", False)),
        quad_tree_to_values(getattr(node, "topLeft", None)),
        quad_tree_to_values(getattr(node, "topRight", None)),
        quad_tree_to_values(getattr(node, "bottomLeft", None)),
        quad_tree_to_values(getattr(node, "bottomRight", None)),
    ]
'''


def comparators_py() -> str:
    return (ROOT / "common" / "comparators.py").read_text(encoding="utf-8")


def runner_py() -> str:
    return (ROOT / "common" / "runner.py").read_text(encoding="utf-8")


def run_problem_py() -> str:
    return '''from common.runner import main


if __name__ == "__main__":
    main()
'''


def apply_macos_tags_py() -> str:
    return (ROOT / "tools" / "apply_macos_tags.py").read_text(encoding="utf-8")


def generate_indexes_py() -> str:
    return '''from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    problems = []
    tag_map = defaultdict(list)
    for metadata_path in sorted((ROOT / "problems").glob("*/metadata.json")):
        metadata = json.loads(metadata_path.read_text())
        problems.append(metadata)
        for tag in metadata["tags"]:
            tag_map[tag].append(metadata)

    (ROOT / "indexes").mkdir(exist_ok=True)
    (ROOT / "indexes" / "problems.json").write_text(json.dumps(problems, indent=2) + "\\n")
    (ROOT / "indexes" / "tags.json").write_text(json.dumps({k: [p["folder"] for p in v] for k, v in tag_map.items()}, indent=2) + "\\n")

    with (ROOT / "indexes" / "status.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "difficulty", "section", "tags", "status", "last_reviewed"])
        for p in problems:
            writer.writerow([p["id"], p["title"], p["difficulty"], p["section"], "|".join(p["tags"]), p["status"], ""])

    for tag, items in tag_map.items():
        tag_dir = ROOT / "tags" / tag
        tag_dir.mkdir(parents=True, exist_ok=True)
        rows = ["| ID | Problem | Difficulty | Section | Status |", "| --- | --- | --- | --- | --- |"]
        for p in sorted(items, key=lambda x: x["id"]):
            rows.append(f"| {p['id']:04d} | [{p['title']}](../../problems/{p['folder']}) | {p['difficulty']} | {p['section']} | {p['status']} |")
        (tag_dir / "problems.md").write_text(f"# {tag.replace('-', ' ').title()}\\n\\n" + "\\n".join(rows) + "\\n")


if __name__ == "__main__":
    main()
'''


def test_solution_py() -> str:
    return '''from pathlib import Path

from common.runner import run_problem


def test_solution():
    assert run_problem(Path(__file__).resolve().parents[1]) == 0
'''


def vscode_tasks(root: Path) -> str:
    return f'''{{
  "version": "2.0.0",
  "tasks": [
    {{
      "label": "LeetCode: Test Current Problem",
      "type": "shell",
      "command": "python -m tools.run_problem ${{fileDirname}}",
      "options": {{
        "cwd": "{root.parents[1]}"
      }},
      "problemMatcher": []
    }},
    {{
      "label": "LeetCode: Test Current Problem Reference",
      "type": "shell",
      "command": "python -m tools.run_problem ${{fileDirname}} --reference",
      "options": {{
        "cwd": "{root.parents[1]}"
      }},
      "problemMatcher": []
    }}
  ]
}}
'''


def build_problem_record(
    q: dict[str, Any],
    section: str,
    order: int,
    detail: dict[str, Any],
    study_plans: list[str],
    study_plan_orders: dict[str, int],
    sections_by_plan: dict[str, str],
    neetcode_entry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    pid = int(detail.get("questionFrontendId") or q["questionFrontendId"])
    title = detail.get("title") or q["title"]
    slug = detail.get("titleSlug") or q["titleSlug"]
    folder = f"{pid:04d}_{snake(slug)}"
    topic_tags = detail.get("topicTags") or q.get("topicTags", [])
    meta = json.loads(detail["metaData"]) if detail.get("metaData") else {}
    function: dict[str, Any]
    if meta.get("systemdesign"):
        function = {
            "class_name": meta.get("classname"),
            "methods": [
                {
                    "name": m.get("name"),
                    "params": m.get("params", []),
                    "return_type": m.get("return", {}).get("type", "void"),
                }
                for m in meta.get("methods", [])
            ],
        }
    else:
        function = {
            "class_name": "Solution",
            "method_name": meta.get("name"),
            "params": meta.get("params", []),
            "return_type": meta.get("return", {}).get("type", "unknown"),
        }
    problem = {
        "id": pid,
        "title": title,
        "slug": slug,
        "folder": folder,
        "difficulty": title_case_difficulty((q.get("difficulty") or detail.get("difficulty") or "").lower()),
        "section": section,
        "order": order,
        "url": f"https://leetcode.com/problems/{slug}/",
        "problem_url": f"https://leetcode.com/problems/{slug}/",
        "problem_source": "leetcode",
        "topic_tags": topic_tags,
        "tags": [tag["slug"] for tag in topic_tags],
        "function": function,
        "judge": judge_config(slug, meta),
        "status": "todo",
        "source": "leetcode",
        "study_plans": study_plans,
        "study_plan_orders": study_plan_orders,
        "sections_by_plan": sections_by_plan,
        "is_paid_only": bool(detail.get("isPaidOnly")),
        "content_available": bool(detail.get("content")),
        "leetcode_content_available": bool(detail.get("content")),
        "content_source": "leetcode" if detail.get("content") else "unavailable",
        "similar_questions": similar_questions_from_detail(detail),
        "approach": "",
    }
    if neetcode_entry:
        problem["neetcode"] = {
            "code": neetcode_entry.get("code", ""),
            "url": neetcode_entry.get("neetcode_url", ""),
            "video": neetcode_entry.get("video", ""),
        }
    problem["approach"] = approach_for(problem)
    return problem


def top_interview_entries(plan_data: dict[str, Any]) -> list[dict[str, Any]]:
    entries = []
    order = 0
    for group in plan_data["planSubGroups"]:
        for q in group["questions"]:
            order += 1
            entries.append(
                {
                    "slug": q["titleSlug"],
                    "title": q["title"],
                    "difficulty": q["difficulty"],
                    "questionFrontendId": q["questionFrontendId"],
                    "topicTags": q.get("topicTags", []),
                    "section": group["name"],
                    "order": order,
                    "source_plan": TOP_INTERVIEW_PLAN_SLUG,
                    "raw": q,
                }
            )
    return entries


def merged_problem_entries(top_entries: list[dict[str, Any]], neetcode_entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_slug: dict[str, dict[str, Any]] = {}
    for entry in top_entries:
        by_slug[entry["slug"]] = {
            "slug": entry["slug"],
            "title": entry["title"],
            "difficulty": entry["difficulty"],
            "questionFrontendId": entry["questionFrontendId"],
            "topicTags": entry.get("topicTags", []),
            "study_plans": [TOP_INTERVIEW_PLAN_SLUG],
            "study_plan_orders": {TOP_INTERVIEW_PLAN_SLUG: entry["order"]},
            "sections_by_plan": {TOP_INTERVIEW_PLAN_SLUG: entry["section"]},
            "top_entry": entry,
            "neetcode_entry": None,
        }
    for entry in neetcode_entries:
        record = by_slug.setdefault(
            entry["slug"],
            {
                "slug": entry["slug"],
                "title": entry["title"],
                "difficulty": entry["difficulty"],
                "questionFrontendId": entry.get("code", "").split("-", 1)[0].lstrip("0") or "",
                "topicTags": [],
                "study_plans": [],
                "study_plan_orders": {},
                "sections_by_plan": {},
                "top_entry": None,
                "neetcode_entry": None,
            },
        )
        if NEETCODE_PLAN_SLUG not in record["study_plans"]:
            record["study_plans"].append(NEETCODE_PLAN_SLUG)
        record["study_plan_orders"][NEETCODE_PLAN_SLUG] = entry["order"]
        record["sections_by_plan"][NEETCODE_PLAN_SLUG] = entry["section"]
        record["neetcode_entry"] = entry

    ordered: list[dict[str, Any]] = []
    seen: set[str] = set()
    for entry in neetcode_entries:
        ordered.append(by_slug[entry["slug"]])
        seen.add(entry["slug"])
    for entry in top_entries:
        if entry["slug"] not in seen:
            ordered.append(by_slug[entry["slug"]])
            seen.add(entry["slug"])
    for order, entry in enumerate(ordered, start=1):
        entry["merged_order"] = order
    return ordered


def primary_section(entry: dict[str, Any]) -> str:
    sections = entry["sections_by_plan"]
    return sections.get(NEETCODE_PLAN_SLUG) or sections.get(TOP_INTERVIEW_PLAN_SLUG) or "Uncategorized"


def generate(args: argparse.Namespace) -> None:
    reference_root = Path(args.reference_root)
    top_entries: list[dict[str, Any]] = []
    neetcode_entries = fetch_neetcode_150()
    combined_entries = merged_problem_entries(top_entries, neetcode_entries)
    write_json(ROOT / "study_plans" / "neetcode_150_raw.json", neetcode_entries)

    details: dict[str, Any] = {}
    generated: list[dict[str, Any]] = []
    by_tag: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_section: dict[str, list[dict[str, Any]]] = defaultdict(list)
    missing_sources: list[str] = []
    preserved_reference_sources: list[str] = []

    write(ROOT / "README.md", root_readme({"name": "NeetCode 150"}))
    write(ROOT / "WORKFLOW.md", workflow_md())
    write(ROOT / "pyproject.toml", pyproject_toml())
    write(ROOT / "THIRD_PARTY_NOTICES.md", SOURCE_LICENSE)
    write(ROOT / "common" / "__init__.py", "")
    write(ROOT / "common" / "lc_types.py", lc_types_py())
    write(ROOT / "common" / "comparators.py", comparators_py())
    write(ROOT / "common" / "runner.py", runner_py())
    write(ROOT / "tools" / "__init__.py", "")
    write(ROOT / "tools" / "run_problem.py", run_problem_py())
    write(ROOT / "tools" / "apply_macos_tags.py", apply_macos_tags_py())
    write(ROOT / "tools" / "generate_indexes.py", generate_indexes_py())
    write(ROOT / "templates" / "solution.py", add_template_imports("class Solution:\n    pass"))
    write(ROOT / "templates" / "test_solution.py", test_solution_py())
    write(ROOT / "templates" / "notes.md", notes_md({"id": 0, "title": "Template", "section": "Template", "topic_tags": [], "approach": "reference"}, "solution_reference.py", "TBD"))
    write(ROOT / "templates" / "prompt.md", "# Prompt Template\n")
    write(ROOT / "templates" / "README.md", "# Problem README Template\n")

    for entry in combined_entries:
        slug = entry["slug"]
        detail = request_graphql(
            QUESTION_QUERY,
            {"titleSlug": slug},
            referer=f"https://leetcode.com/problems/{slug}/",
        )["question"]
        q = {
            "questionFrontendId": detail.get("questionFrontendId") or entry.get("questionFrontendId"),
            "title": detail.get("title") or entry["title"],
            "titleSlug": detail.get("titleSlug") or slug,
            "difficulty": detail.get("difficulty") or entry.get("difficulty", ""),
            "topicTags": detail.get("topicTags") or entry.get("topicTags", []),
        }
        problem = build_problem_record(
            q,
            primary_section(entry),
            entry["merged_order"],
            detail,
            entry["study_plans"],
            entry["study_plan_orders"],
            entry["sections_by_plan"],
            entry.get("neetcode_entry"),
        )
        if not detail.get("content"):
            neetcode_question = fetch_neetcode_question(entry.get("neetcode_entry"), problem["title"])
            if neetcode_question:
                detail["neetcode_question"] = neetcode_question
                problem["content_available"] = True
                problem["content_source"] = "neetcode"
                problem["problem_url"] = neetcode_question["url"]
                problem["problem_source"] = "neetcode"
                if "neetcode" in problem:
                    problem["neetcode"]["question_url"] = neetcode_question["url"]
                    problem["neetcode"]["topics"] = neetcode_question.get("topics", [])
        details[slug] = question_detail_for_index(detail)
        problem_dir = ROOT / "problems" / problem["folder"]
        existing_metadata_path = problem_dir / "metadata.json"
        existing_metadata: dict[str, Any] = {}
        if existing_metadata_path.exists():
            try:
                existing_metadata = json.loads(existing_metadata_path.read_text(encoding="utf-8"))
                problem["status"] = existing_metadata.get("status", problem["status"])
            except json.JSONDecodeError:
                existing_metadata = {}
        meta = json.loads(detail["metaData"]) if detail.get("metaData") else {}
        cases = parse_example_cases(detail.get("exampleTestcases") or "", meta)
        snippet = python3_snippet(detail)
        solution_template = add_template_imports(snippet, slug=problem["slug"])
        approach = problem["approach"]
        existing_ref_rel = existing_metadata.get("reference_solution", "")
        solution_name = Path(existing_ref_rel).name if existing_ref_rel else f"solution_{approach}.py"
        source_path = None
        existing_reference_path = problem_dir / "solutions" / solution_name
        existing_reference_entries = existing_metadata.get("reference_solutions") or []
        existing_is_ai_authored = (
            str(existing_metadata.get("reference_source_note", "")).startswith("AI-authored")
            and isinstance(existing_reference_entries, list)
            and bool(existing_reference_entries)
        )
        local_reference_override = LOCAL_REFERENCE_OVERRIDES.get(problem["slug"])
        if existing_is_ai_authored:
            problem["reference_source_note"] = existing_metadata["reference_source_note"]
            problem["reference_solution"] = existing_metadata.get("reference_solution", "")
            problem["reference_solutions"] = existing_reference_entries
            primary_ref = problem["reference_solution"]
            primary_entry = next(
                (item for item in existing_reference_entries if item.get("file") == primary_ref),
                existing_reference_entries[0],
            )
            complexity = primary_entry.get("complexity", "See reference solution and notes.")
            ref_code = None
            preserved_reference_sources.append(problem["folder"])
        elif local_reference_override:
            complexity = local_reference_override["complexity"]
            source_header = "# Local reference implementation for package learning use.\n\n"
            problem["reference_source_note"] = local_reference_override["source_note"]
            reference_body = local_reference_override["body"]
            ref_code = (
                source_header
                + build_solution_header(problem, approach, complexity, None, detail)
                + reference_imports_for_body(reference_body, slug=problem["slug"])
                + reference_body.rstrip()
                + "\n"
            )
            problem["reference_solution"] = f"solutions/{solution_name}"
        elif source_path:
            complexity = "AI-authored reference pending"
            ref_code = None
            missing_sources.append(problem["folder"])
        elif existing_reference_path.exists():
            source_code = existing_reference_path.read_text(encoding="utf-8")
            complexity = complexity_from_source(source_code)
            ref_code = None
            problem["reference_solution"] = f"solutions/{solution_name}"
            preserved_reference_sources.append(problem["folder"])
        else:
            complexity = "TBD"
            ref_code = None
            missing_sources.append(problem["folder"])
        generated.append(problem)
        by_section[problem["section"]].append(problem)
        for tag in problem["tags"]:
            by_tag[tag].append(problem)

        reference_solution_name = solution_name if problem.get("reference_solution") else None
        write(problem_dir / "README.md", readme_md(problem, reference_solution_name, complexity))
        write(problem_dir / "prompt.md", prompt_md(problem, meta, cases, snippet, detail))
        write_json(problem_dir / "metadata.json", problem)
        write_solution_template(problem_dir / "solution.py", solution_template)
        write_if_missing(problem_dir / "notes.md", notes_md(problem, reference_solution_name, complexity))
        if ref_code is not None:
            write(problem_dir / "solutions" / solution_name, ref_code)
        write_json(
            problem_dir / "tests" / "cases.json",
            {
                "source": "leetcode_example_testcases",
                "expected": "computed_by_reference_solution" if reference_solution_name else "reference_solution_missing",
                "cases": cases,
            },
        )
        write(problem_dir / "tests" / "test_solution.py", test_solution_py())

    write_json(ROOT / "indexes" / "source_leetcode_questions.json", details)
    write_json(ROOT / "indexes" / "problems.json", generated)
    write_json(ROOT / "indexes" / "tags.json", {tag: [p["folder"] for p in items] for tag, items in sorted(by_tag.items())})

    with (ROOT / "indexes" / "status.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "difficulty", "section", "tags", "status", "last_reviewed"])
        for p in sorted(generated, key=lambda item: item["order"]):
            writer.writerow([p["id"], p["title"], p["difficulty"], p["section"], "|".join(p["tags"]), p["status"], ""])

    def write_study_plan(slug: str, filename: str, title: str, items: list[dict[str, Any]]) -> None:
        rows = []
        ordered = sorted(items, key=lambda item: item.get("study_plan_orders", {}).get(slug, item["order"]))
        for p in ordered:
            order_value = p.get("study_plan_orders", {}).get(slug, p["order"])
            section_value = p.get("sections_by_plan", {}).get(slug, p["section"])
            rows.append([str(order_value), f"{p['id']:04d}", f"[{p['title']}](../problems/{p['folder']})", p["difficulty"], section_value, p["status"]])
        write(
            ROOT / "study_plans" / f"{filename}.md",
            f"# {title}\n\n"
            + markdown_table(rows, ["Order", "ID", "Problem", "Difficulty", "Section", "Status"])
            + "\n",
        )
        write_json(
            ROOT / "study_plans" / f"{filename}.json",
            [
                {
                    "order": p.get("study_plan_orders", {}).get(slug, p["order"]),
                    "id": p["id"],
                    "title": p["title"],
                    "folder": p["folder"],
                    "section": p.get("sections_by_plan", {}).get(slug, p["section"]),
                }
                for p in ordered
            ],
        )

    write_study_plan(
        NEETCODE_PLAN_SLUG,
        "neetcode_150",
        "NeetCode 150",
        [p for p in generated if NEETCODE_PLAN_SLUG in p["study_plans"]],
    )

    write(ROOT / "tags" / "README.md", "# Tags\n\nGenerated tag-to-problem mappings. Full learning materials will be added one tag at a time.\n")
    for tag, items in sorted(by_tag.items()):
        rows = []
        for p in sorted(items, key=lambda item: (item["difficulty"], item["id"])):
            rows.append([f"{p['id']:04d}", f"[{p['title']}](../../problems/{p['folder']})", p["difficulty"], p["section"], p["status"]])
        write(ROOT / "tags" / tag / "problems.md", f"# {tag.replace('-', ' ').title()}\n\n" + markdown_table(rows, ["ID", "Problem", "Difficulty", "Section", "Status"]) + "\n")

    if args.vscode:
        vscode_dir = ROOT.parents[1] / ".vscode"
        vscode_dir.mkdir(exist_ok=True)
        write(vscode_dir / "tasks.json", vscode_tasks(ROOT))

    write_json(
        ROOT / "indexes" / "generation_report.json",
        {
            "problem_count": len(generated),
            "missing_reference_sources": missing_sources,
            "missing_count": len(missing_sources),
            "preserved_reference_sources": preserved_reference_sources,
            "preserved_count": len(preserved_reference_sources),
        },
    )
    print(
        json.dumps(
            {
                "problem_count": len(generated),
                "missing_reference_sources": missing_sources[:10],
                "missing_count": len(missing_sources),
                "preserved_reference_sources": preserved_reference_sources[:10],
                "preserved_count": len(preserved_reference_sources),
            },
            indent=2,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch source metadata and regenerate this standalone NeetCode practice package.")
    parser.add_argument("--reference-root", default=str(DEFAULT_REFERENCE_ROOT), help="Deprecated compatibility option; reference solutions are AI-authored and preserved from solutions/")
    parser.add_argument("--vscode", action="store_true", help="Create VS Code tasks under the coding workspace root")
    args = parser.parse_args()
    generate(args)


if __name__ == "__main__":
    main()
