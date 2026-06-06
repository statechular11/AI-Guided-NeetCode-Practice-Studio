# Binary Tree - A Complete Guide for Coding Interviews

## Table of Contents

- [1. What Is a Binary Tree?](#1-what-is-a-binary-tree)
- [2. The Core Mental Model](#2-the-core-mental-model)
- [3. Traversal Is the Primitive](#3-traversal-is-the-primitive)
- [4. The Binary Tree Design Worksheet](#4-the-binary-tree-design-worksheet)
- [5. Pattern 1: Simple Subtree Return](#5-pattern-1-simple-subtree-return)
- [6. Pattern 2: Bottom-Up Tree DP](#6-pattern-2-bottom-up-tree-dp)
- [7. Pattern 3: Top-Down Carried Context](#7-pattern-3-top-down-carried-context)
- [8. Pattern 4: Paired Subtree Traversal](#8-pattern-4-paired-subtree-traversal)
- [9. Pattern 5: Lowest Common Ancestor](#9-pattern-5-lowest-common-ancestor)
- [10. Pattern 6: BFS by Level](#10-pattern-6-bfs-by-level)
- [11. Pattern 7: BST Inorder and Ordered Search](#11-pattern-7-bst-inorder-and-ordered-search)
- [12. Pattern 8: Constructing Trees and Using Shape](#12-pattern-8-constructing-trees-and-using-shape)
- [13. Pattern 9: Serialization and Deserialization](#13-pattern-9-serialization-and-deserialization)
- [14. Pattern 10: Pointer Rewiring](#14-pattern-10-pointer-rewiring)
- [15. Iterative DFS Without Mystery](#15-iterative-dfs-without-mystery)
- [16. Correctness Invariants](#16-correctness-invariants)
- [17. Complexity Basics](#17-complexity-basics)
- [18. Failure Modes and Edge Cases](#18-failure-modes-and-edge-cases)
- [19. When Not to Use a Binary Tree Pattern](#19-when-not-to-use-a-binary-tree-pattern)
- [20. Practice Progression](#20-practice-progression)
- [21. Interview Explanation Templates](#21-interview-explanation-templates)
- [22. Quick Reference](#22-quick-reference)

## 1. What Is a Binary Tree?

A binary tree is a collection of nodes where each node has at most two child
pointers:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The important interview idea is not the class definition. The important idea is:

```text
Every node can be treated as the root of its own smaller tree.
```

That one sentence explains why recursion fits trees so naturally. If a problem
asks for a fact about the whole tree, you can often ask the same question about
the left subtree and the right subtree, then combine the answers at the current
node.

Example: Maximum Depth of Binary Tree.

```text
depth(node) = 1 + max(depth(node.left), depth(node.right))
depth(None) = 0
```

The function works because `node.left` and `node.right` are themselves roots of
smaller binary trees.

### 1.1 - Basic vocabulary

| Term | Meaning |
| --- | --- |
| root | the top node of the current tree or subtree |
| child | `node.left` or `node.right` |
| parent | the node that points to this node |
| leaf | a node with no children |
| subtree | a node together with all descendants below it |
| ancestor | a node on the path from the root to this node |
| descendant | a node below this node |
| depth | distance from the root to a node |
| height | distance from a node down to its deepest leaf |

Depth and height are common sources of off-by-one bugs. Some problems count
nodes, while others count edges.

```text
single-node tree:
node-count depth = 1
edge-count height/diameter contribution = 0
```

Always name the unit before writing code.

### 1.2 - Binary tree versus BST

A plain binary tree has only shape:

```text
left and right are just child pointers.
Values can appear anywhere unless the prompt says otherwise.
```

A binary search tree has ordering:

```text
all values in left subtree  < node.val
all values in right subtree > node.val
```

Do not use BST value logic on a general binary tree. Lowest Common Ancestor of a
Binary Search Tree can walk by value. Lowest Common Ancestor of a Binary Tree
must ask both subtrees what they contain.


---

## 2. The Core Mental Model

The strongest tree solutions start with two questions:

```text
1. What does one subtree need to report to its parent?
2. What context does one child need to receive from its ancestors?
```

Most tree problems are combinations of these two directions.

| Direction | State flow | Typical use |
| --- | --- | --- |
| bottom-up | child -> parent | height, balance, diameter, LCA, subtree hashes |
| top-down | parent -> child | path sum, good nodes, inherited BST bounds |
| level-order | level -> next level | level order, right side view, averages |
| ordered stream | left -> root -> right | BST validation, kth smallest |
| construction | traversal tokens -> nodes | build tree, serialize/deserialize |

Before coding, define the helper contract in plain English.

Bad starting point:

```text
I will do DFS.
```

Better starting point:

```text
dfs(node) returns the height of this subtree.
While computing that height, it updates `best` with every diameter candidate.
```

Or:

```text
dfs(node, path_max) receives the maximum ancestor value on the path to this
node. It returns how many good nodes appear in this subtree.
```

The traversal is the vehicle. The contract is the solution.


---

## 3. Traversal Is the Primitive

Almost every tree solution traverses nodes in some order. The order controls
when information is available.

### 3.1 - Discover versus visit

A node is discovered when the algorithm first identifies it as work to handle.
A node is visited when the algorithm performs the meaningful action for that
node, such as appending its value, updating an answer, checking a condition, or
creating output.

These are different events.

```text
Recursive DFS:
    a node is discovered when dfs(node) starts.

Iterative DFS:
    a node may be discovered when it is pushed onto a stack.

BFS:
    a node is usually discovered when it is enqueued.
```

In preorder traversal, discovery and visit are close together. In inorder and
postorder, a node can be discovered long before it is safe to visit.

### 3.2 - Three DFS timings

For a current node:

```text
       node
      /    \
   left   right
```

there are three natural moments to act:

| Traversal | Visit timing | Use when |
| --- | --- | --- |
| preorder | before children | pass context downward, clone/build, root-first output |
| inorder | between left and right | use BST sorted order |
| postorder | after children | combine child facts, mutate after preserving children |

Memory hook:

```text
preorder:  current node first
inorder:   current node in the middle
postorder: current node last
```

For many interview problems, traversal order is really update timing:

```text
Need child results before current decision? Use postorder.
Need ancestor context before child decision? Use preorder/top-down.
Need sorted BST values? Use inorder.
Need output by depth? Use BFS or DFS with depth.
```

### 3.3 - BFS timing

BFS processes a frontier one layer at a time.

```text
queue = nodes discovered but not yet processed
```

For level problems, decide how the algorithm knows where one level ends.

| Boundary model | State | When useful |
| --- | --- | --- |
| queue-size snapshot | `level_size = len(queue)` | clean level order, averages, last value |
| depth payload | `(node, depth)` | attach metadata, group by depth, vertical variants |
| sentinel marker | `None` marker between levels | teaching model, less common in interviews |

Queue-size snapshot is the default:

```python
from collections import deque

def level_order(root):
    if not root:
        return []

    levels = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        row = []

        for _ in range(level_size):
            node = queue.popleft()
            row.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels.append(row)

    return levels
```

Same boundary model, but without an intermediate `row` list:

```python
from collections import deque

def level_order_direct(root):
    if not root:
        return []

    levels = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        levels.append([])

        for _ in range(level_size):
            node = queue.popleft()
            levels[-1].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return levels
```

This version creates the output row first with `levels.append([])`, then writes
each popped node directly into the current row with `levels[-1].append(...)`.
It is still a queue-size snapshot solution; only the output-writing style
changed.

The invariant is:

```text
At the start of each outer loop, the queue contains exactly the nodes in the
current level.
```

Children appended during the loop belong to the next level, so they must not be
included in the current row.


---

## 4. The Binary Tree Design Worksheet

Before writing a tree solution, fill in this worksheet.

| Design question | Common answers |
| --- | --- |
| What is the helper contract? | returns height, returns count, returns found target, returns root |
| What is the null result? | `0`, `None`, `True`, `(0, True)`, empty list |
| What must flow downward? | depth, path sum, path max, low/high bounds |
| What must flow upward? | height, balance, min/max, best gain, found node |
| Is there a global answer? | diameter, max path sum, first LCA, right-side list |
| When should the node be processed? | before children, between children, after children, by level |
| Does state belong to a branch? | path list, path sum, ancestor max, BST bounds |
| Does mutation happen? | swap children, flatten pointers, build nodes, restore threads |
| What is measured in nodes or edges? | depth, height, diameter, path length |
| Is the tree ordered? | general tree or BST |

### 4.1 - Choosing the state shape

| Problem shape | Usually store |
| --- | --- |
| one fact per subtree | return a scalar |
| two facts per subtree | return a tuple or use sentinel |
| best answer anywhere | return local fact and update `best` |
| root-to-node path context | pass context as an argument or stack payload |
| output grouped by depth | BFS rows or DFS `levels[depth]` |
| BST order | inorder traversal with previous value or rank counter |
| reconstruct tree | traversal index plus ownership range |
| serialize tree | traversal tokens plus null markers |

The most common bug is using the scheduling structure as if it already stores
semantic state. A stack says what work remains. It does not automatically know
the current path, depth, bounds, or path maximum unless you attach those values
to each stack entry.

Example:

```python
stack = [(root, root.val)]  # node plus branch-local path maximum
```

Now each entry carries the context needed to judge that node.


---

## 5. Pattern 1: Simple Subtree Return

Use this when the parent needs exactly one fact from each child.

Recognition signals:

- "height of tree"
- "count nodes"
- "sum of all nodes"
- "invert tree and return root"
- "same tree"

### 5.1 - Maximum depth

Contract:

```text
depth(node) returns the maximum node-count depth inside node's subtree.
```

Template:

```python
def max_depth(root):
    def depth(node):
        if not node:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)
        return 1 + max(left_depth, right_depth)

    return depth(root)
```

Why postorder? The current node cannot know its depth until both child depths
are known.

Trace:

```text
        3
       / \
      9  20
         / \
        15  7

depth(9)  = 1
depth(15) = 1
depth(7)  = 1
depth(20) = 1 + max(1, 1) = 2
depth(3)  = 1 + max(1, 2) = 3
```

### 5.2 - Same tree

Contract:

```text
same(a, b) returns whether the two subtrees have identical shape and values.
```

Template:

```python
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
```

Null handling is the whole problem. Two missing nodes match. Exactly one missing
node fails.

### 5.3 - Invert binary tree

Contract:

```text
invert(node) returns the root of the inverted version of this subtree.
```

Template:

```python
def invert_tree(root):
    if not root:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

Mutation ownership matters. If you overwrite a pointer before saving the child
you still need, you can lose part of the tree. Tuple assignment in Python
evaluates the right side first, so this version is safe.


---

## 6. Pattern 2: Bottom-Up Tree DP

Tree DP means each subtree returns a summary. The current node combines child
summaries into its own summary.

Recognition signals:

- "for every node, check child heights"
- "longest path may be inside any subtree"
- "subtree is valid if children are valid"
- "return one fact upward, but answer may use another fact locally"

### 6.1 - Height plus global best

Some problems have two facts:

```text
1. the fact the parent can use
2. the best answer seen anywhere so far
```

Diameter of Binary Tree is the clean example.

Contract:

```text
height(node) returns the maximum node-count downward path from node to a leaf.
While returning height, it updates `best` with the largest edge-count diameter.
```

Template:

```python
def diameter_of_binary_tree(root):
    best = 0

    def height(node):
        nonlocal best
        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        best = max(best, left + right)
        return 1 + max(left, right)

    height(root)
    return best
```

Why two facts?

```text
The parent can extend only one downward branch.
The diameter candidate at this node may use both child branches.
```

At node `2` here:

```text
        1
       / \
      2   3
     / \
    4   5
```

the local diameter through `2` uses `4 -> 2 -> 5`, but node `1` cannot extend
both sides of `2` upward. Node `2` returns height `2`, while `best` can record
diameter `2`.

### 6.2 - Maximum path sum

Maximum Path Sum has the same shape as diameter, but with values and negative
gains.

Contract:

```text
gain(node) returns the best one-sided path sum that starts at node and can be
extended by its parent.
`best` stores the best complete path found anywhere.
```

Template:

```python
def max_path_sum(root):
    best = float("-inf")

    def gain(node):
        nonlocal best
        if not node:
            return 0

        left = max(0, gain(node.left))
        right = max(0, gain(node.right))

        best = max(best, node.val + left + right)
        return node.val + max(left, right)

    gain(root)
    return best
```

Why discard negative child gains?

```text
A path is allowed to stop. A negative branch makes any path worse, so it should
not be included in a path through the current node.
```

Why initialize `best` to negative infinity?

```text
All node values may be negative. Initializing to 0 would incorrectly allow an
empty path.
```

### 6.3 - Balanced tree sentinel

Balanced Binary Tree asks whether every subtree is height-balanced.

Naive but costly:

```text
For each node, recompute left height and right height.
```

Optimized contract:

```text
height(node) returns a non-negative height if this subtree is balanced.
height(node) returns -1 if this subtree is already unbalanced.
```

Template:

```python
def is_balanced(root):
    def height(node):
        if not node:
            return 0

        left = height(node.left)
        if left == -1:
            return -1

        right = height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return height(root) != -1
```

The sentinel keeps one return value instead of returning `(height, balanced)`.
Both designs are valid. The important part is that the parent receives enough
information to avoid recomputing subtrees.


---

## 7. Pattern 3: Top-Down Carried Context

Use top-down traversal when a node needs information from ancestors.

Recognition signals:

- "root-to-leaf"
- "path sum"
- "maximum seen so far"
- "all ancestor constraints"
- "depth of this node"

### 7.1 - Count good nodes

Contract:

```text
dfs(node, path_max) counts good nodes in node's subtree.
`path_max` is the maximum value seen from the root to node's parent.
```

Template:

```python
def good_nodes(root):
    def dfs(node, path_max):
        if not node:
            return 0

        good = 1 if node.val >= path_max else 0
        next_max = max(path_max, node.val)

        return (
            good
            + dfs(node.left, next_max)
            + dfs(node.right, next_max)
        )

    return dfs(root, root.val)
```

The key phrase is branch-local. The maximum on the left path is not the maximum
on the right path. In iterative code, attach the context to each entry:

```python
def good_nodes_iterative(root):
    if not root:
        return 0

    count = 0
    stack = [(root, root.val)]

    while stack:
        node, path_max = stack.pop()

        if node.val >= path_max:
            count += 1

        next_max = max(path_max, node.val)
        if node.left:
            stack.append((node.left, next_max))
        if node.right:
            stack.append((node.right, next_max))

    return count
```

The stack is not the path. The `(node, path_max)` payload carries the path
information.

### 7.2 - Path sum

For Path Sum, carry the remaining sum or accumulated sum.

Remaining-sum contract:

```text
dfs(node, remaining) returns whether there is a root-to-leaf path from node
whose values add to `remaining`.
```

Template:

```python
def has_path_sum(root, target_sum):
    def dfs(node, remaining):
        if not node:
            return False

        remaining -= node.val
        if not node.left and not node.right:
            return remaining == 0

        return dfs(node.left, remaining) or dfs(node.right, remaining)

    return dfs(root, target_sum)
```

Leaf detection matters. A partial path ending at an internal node is not a
root-to-leaf path.

### 7.3 - BST bounds

Validate Binary Search Tree can be solved top-down by passing open bounds.

Contract:

```text
valid(node, low, high) returns whether every value in node's subtree is inside
the open interval (low, high).
```

Template:

```python
def is_valid_bst(root):
    def valid(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return (
            valid(node.left, low, node.val)
            and valid(node.right, node.val, high)
        )

    return valid(root, float("-inf"), float("inf"))
```

The bounds come from all ancestors, not just the parent.

Counterexample for parent-child-only checks:

```text
        10
       /  \
      5    15
          /  \
         6    20
```

The node `6` is less than its parent `15`, but it is in the right subtree of
`10`, so it must be greater than `10`. Ancestor bounds catch this.


---

## 8. Pattern 4: Paired Subtree Traversal

Use paired traversal when the state is a pair of nodes.

Recognition signals:

- "same tree"
- "symmetric tree"
- "subtree of another tree"
- "compare two structures"

### 8.1 - Symmetric tree

A tree is symmetric if its left and right subtrees are mirrors.

Contract:

```text
mirror(a, b) returns whether subtree a and subtree b are mirror images.
```

Template:

```python
def is_symmetric(root):
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False

        return mirror(a.left, b.right) and mirror(a.right, b.left)

    return mirror(root.left, root.right) if root else True
```

The child pairing is crossed:

```text
left.left  compares with right.right
left.right compares with right.left
```

### 8.2 - Subtree of another tree

Subtree of Another Tree has two layers.

```text
Outer layer: scan candidate roots in the large tree.
Inner layer: compare candidate subtree with subRoot using Same Tree.
```

Template:

```python
def is_subtree(root, sub_root):
    def same(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return same(a.left, b.left) and same(a.right, b.right)

    if not sub_root:
        return True
    if not root:
        return False

    return (
        same(root, sub_root)
        or is_subtree(root.left, sub_root)
        or is_subtree(root.right, sub_root)
    )
```

Full shape matters. A candidate with extra descendants is not the same subtree.

Advanced alternatives serialize with null markers or compute structural
signatures, but the direct scan is the default interview answer unless the
constraints force optimization.


---

## 9. Pattern 5: Lowest Common Ancestor

LCA problems are about where two target searches first meet.

There are two separate versions:

| Problem | Property | Main idea |
| --- | --- | --- |
| LCA in Binary Tree | no ordering | ask both subtrees what target they found |
| LCA in BST | ordered values | walk to the first split point |

### 9.1 - General binary tree LCA

Contract:

```text
lca(node) returns:
- None if this subtree contains neither target
- p or q if this subtree contains exactly one target, or node is a target
- the LCA if this subtree contains both targets
```

Template:

```python
def lowest_common_ancestor(root, p, q):
    def dfs(node):
        if not node:
            return None
        if node is p or node is q:
            return node

        left = dfs(node.left)
        right = dfs(node.right)

        if left and right:
            return node
        return left or right

    return dfs(root)
```

Why postorder? The current node can only know whether it is the meeting point
after it hears from both children.

Trace:

```text
p = 7, q = 4

7 returns 7
4 returns 4
2 receives left=7 and right=4, so 2 is the LCA
```

Use node identity when the API passes nodes:

```python
node is p
```

Value equality can be misleading in other variants where values are not unique.

### 9.2 - BST LCA

In a BST, the current node tells you whether both targets lie on the same side.

Template:

```python
def lowest_common_ancestor_bst(root, p, q):
    low, high = sorted((p.val, q.val))
    node = root

    while node:
        if node.val > high:
            node = node.left
        elif node.val < low:
            node = node.right
        else:
            return node
```

The first node with:

```text
low <= node.val <= high
```

is the inclusive split point. Inclusive matters because one target may be an
ancestor of the other.


---

## 10. Pattern 6: BFS by Level

BFS is best when the problem is naturally organized by distance from the root.

Recognition signals:

- "level order"
- "right side view"
- "average of each level"
- "minimum depth"
- "zigzag level order"
- "next right pointer"

### 10.1 - Level order

State:

```text
queue holds current level at the start of each outer loop.
row collects values for that level.
```

Template:

```python
from collections import deque

def level_order(root):
    if not root:
        return []

    queue = deque([root])
    levels = []

    while queue:
        row = []

        for _ in range(len(queue)):
            node = queue.popleft()
            row.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels.append(row)

    return levels
```

In Python, `range(len(queue))` evaluates `len(queue)` once before the loop
starts, so it is a compact queue-size snapshot.

### 10.2 - Depth-pair BFS

Alternative state:

```text
each queue entry is (node, depth)
```

Template:

```python
from collections import deque

def level_order_depth_pairs(root):
    if not root:
        return []

    levels = []
    queue = deque([(root, 0)])

    while queue:
        node, depth = queue.popleft()

        if depth == len(levels):
            levels.append([])
        levels[depth].append(node.val)

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return levels
```

The invariant:

```text
depth tells this node which output row it belongs to.
```

This form is useful when future variants need more metadata, such as
`(node, row, col)` for vertical order traversal.

### 10.3 - Right side view

Right side view asks for the last visible node at each depth.

Do not follow only right pointers. A left-subtree node can be visible if there
is no node to its right at that depth.

BFS last-value template:

```python
from collections import deque

def right_side_view(root):
    if not root:
        return []

    ans = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                ans.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans
```

DFS right-first template:

```python
def right_side_view_dfs(root):
    ans = []

    def dfs(node, depth):
        if not node:
            return

        if depth == len(ans):
            ans.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return ans
```

Why `append` in right-first DFS?

```text
Because `depth == len(ans)` means this is the first node ever seen at this
depth. Right-first order makes that first node the rightmost one.
```

Do not assign `ans[depth] = node.val` before the slot exists.

### 10.4 - Zigzag level order

Zigzag is still normal BFS. Only the row output direction changes.

Template:

```python
from collections import deque

def zigzag_level_order(root):
    if not root:
        return []

    levels = []
    queue = deque([root])
    left_to_right = True

    while queue:
        row = []

        for _ in range(len(queue)):
            node = queue.popleft()
            row.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            row.reverse()
        levels.append(row)
        left_to_right = not left_to_right

    return levels
```

Keep child enqueue order stable left-to-right. Reverse the row for output if
needed. That avoids mixing traversal order with presentation order.


---

## 11. Pattern 7: BST Inorder and Ordered Search

BST problems are binary tree problems plus ordering.

The strongest BST mental model:

```text
Inorder traversal of a valid BST emits values in strictly increasing order.
```

### 11.1 - Iterative inorder stack

Template:

```python
def inorder_values(root):
    values = []
    stack = []
    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        values.append(node.val)
        node = node.right

    return values
```

Stack meaning:

```text
ancestors whose left subtree has been discovered, but whose value has not yet
been emitted.
```

This is why the loop condition is `while node or stack`. The cursor may still
be descending even when the stack is empty, especially at the start.

### 11.2 - Validate BST by inorder

Contract:

```text
Each inorder pop should emit a value greater than the previous emitted value.
```

Template:

```python
def is_valid_bst_inorder(root):
    stack = []
    node = root
    prev = None

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        if prev is not None and node.val <= prev:
            return False
        prev = node.val

        node = node.right

    return True
```

Use `None` for "no previous value yet" instead of numeric sentinels. Node values
can be very small or very large.

### 11.3 - Kth smallest

Contract:

```text
The first inorder pop is rank 1, the second pop is rank 2, and so on.
```

Template:

```python
def kth_smallest(root, k):
    stack = []
    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val

        node = node.right
```

Complexity for one query:

```text
O(h + k) time, O(h) space
```

For repeated kth queries, plain inorder repeats work. A follow-up is to store
subtree sizes and descend by rank:

```text
left_size = size(node.left)

if k <= left_size:
    go left
elif k == left_size + 1:
    return node
else:
    k -= left_size + 1
    go right
```

That turns selection into an order-statistic search in `O(h)` time after sizes
are available and kept updated.

### 11.4 - Minimum difference in BST

Because inorder values are sorted, the minimum absolute difference must occur
between adjacent inorder values.

Template:

```python
def get_minimum_difference(root):
    best = float("inf")
    prev = None
    stack = []
    node = root

    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        if prev is not None:
            best = min(best, node.val - prev)
        prev = node.val

        node = node.right

    return best
```

Do not compare every pair. Sorted order reduces the check to neighbors.

### 11.5 - BST iterator

Binary Search Tree Iterator is lazy inorder traversal.

Instead of producing the whole sorted list at once, maintain the stack state
between calls.

Invariant:

```text
The stack contains the path to the next smallest unvisited node, plus ancestors
waiting for their right subtree.
```

Template:

```python
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self):
        return bool(self.stack)
```

This is the same iterative inorder traversal, paused after each emitted value.
Each node is pushed and popped once across all calls, so `next()` is amortized
O(1), with O(h) stack space.


---

## 12. Pattern 8: Constructing Trees and Using Shape

Tree construction problems reverse the usual traversal process.

Recognition signals:

- "construct binary tree from preorder and inorder"
- "construct from inorder and postorder"
- "sorted array to BST"
- "deserialize"
- "complete binary tree"

### 12.1 - Preorder plus inorder

Core facts:

```text
preorder tells which root to create next.
inorder tells which values belong to the left and right subtrees.
```

For Construct Binary Tree from Preorder and Inorder Traversal:

```text
preorder = root, left subtree, right subtree
inorder  = left subtree, root, right subtree
```

Contract:

```text
build(left, right) builds the subtree whose values occupy inorder[left:right].
When build starts, `pre_i` points to that subtree's root in preorder.
```

Closed-boundary template:

```python
def build_tree(preorder, inorder):
    index = {value: i for i, value in enumerate(inorder)}
    pre_i = 0

    def build(left, right):
        nonlocal pre_i
        if left > right:
            return None

        value = preorder[pre_i]
        pre_i += 1

        root = TreeNode(value)
        mid = index[value]

        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    return build(0, len(inorder) - 1)
```

Why build left before right?

```text
After preorder consumes the root, the next values belong to the entire left
subtree before the right subtree.
```

Common boundary bugs:

- `left > right` is the empty interval.
- `left == right` is a leaf and must create a node.
- `left`, `right`, and `mid` are inorder positions, not preorder positions.

### 12.2 - Sorted array to balanced BST

Core idea:

```text
Choose the middle value as root so each side has about the same number of nodes.
Then recursively build left and right halves.
```

Template:

```python
def sorted_array_to_bst(nums):
    def build(left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    return build(0, len(nums) - 1)
```

This is divide and conquer. The sorted array gives inorder order. Choosing the
middle keeps the height balanced.

### 12.3 - Count complete tree nodes

A complete binary tree has every level full except possibly the last, and the
last level is filled from left to right.

That shape gives a shortcut:

```text
If the leftmost height and rightmost height of a subtree are equal, the subtree
is perfect and contains 2^height - 1 nodes.
Otherwise, recursively count the children.
```

Helper for edge-free node-height counting:

```python
def left_height(node):
    height = 0
    while node:
        height += 1
        node = node.left
    return height

def right_height(node):
    height = 0
    while node:
        height += 1
        node = node.right
    return height
```

Template:

```python
def count_nodes(root):
    if not root:
        return 0

    left = left_height(root)
    right = right_height(root)

    if left == right:
        return (1 << left) - 1

    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

Why this works:

```text
In a complete tree, equal leftmost and rightmost heights mean no gaps exist in
that subtree, so the subtree is perfect.
```

The time is often described as O(log^2 n) for the optimized complete-tree
approach, because at each level you compute heights of length O(log n). The
plain traversal is still O(n), but this shape-specific trick is the interview
point of Count Complete Tree Nodes.


---

## 13. Pattern 9: Serialization and Deserialization

Serialization turns a tree into tokens. Deserialization turns tokens back into
the same shape.

The key rule:

```text
Include enough information to reconstruct missing children.
```

Values alone are not enough.

```text
preorder values [1, 2] could mean:

  1        1
 /          \
2            2
```

Null markers distinguish these shapes.

### 13.1 - Preorder codec

Serialization contract:

```text
emit node value, then left subtree, then right subtree; emit # for None.
```

Template:

```python
class Codec:
    def serialize(self, root):
        tokens = []

        def dfs(node):
            if not node:
                tokens.append("#")
                return

            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data):
        tokens = iter(data.split(","))

        def build():
            value = next(tokens)
            if value == "#":
                return None

            node = TreeNode(int(value))
            node.left = build()
            node.right = build()
            return node

        return build()
```

The deserializer works because preorder with null markers is self-delimiting:
each node knows recursively how many tokens belong to its left and right
subtrees.

### 13.2 - Level-order codec

Level-order codecs read child slots from a queue.

Serialization outline:

```text
queue starts with root
pop a node slot
if slot is None, emit #
else emit value and enqueue left slot and right slot
```

Deserialization outline:

```text
create root from first token
queue holds parents waiting for children
read two tokens per parent: left then right
```

Template:

```python
from collections import deque

class Codec:
    def serialize(self, root):
        if not root:
            return ""

        tokens = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                tokens.append("#")
                continue

            tokens.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        while tokens and tokens[-1] == "#":
            tokens.pop()

        return ",".join(tokens)

    def deserialize(self, data):
        if not data:
            return None

        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(tokens):
            node = queue.popleft()

            if i < len(tokens) and tokens[i] != "#":
                node.left = TreeNode(int(tokens[i]))
                queue.append(node.left)
            i += 1

            if i < len(tokens) and tokens[i] != "#":
                node.right = TreeNode(int(tokens[i]))
                queue.append(node.right)
            i += 1

        return root
```

Trimming trailing null markers is safe for level-order serialization because
missing slots beyond the last real node add no new structure.


---

## 14. Pattern 10: Pointer Rewiring

Pointer-rewiring problems mutate the tree. The danger is losing access to a
child before it has been processed.

Recognition signals:

- "flatten binary tree"
- "connect next right pointers"
- "invert tree"
- "convert tree in-place"
- "Morris traversal"

### 14.1 - Flatten binary tree to linked list

Flatten wants preorder order using right pointers:

```text
root -> left preorder -> right preorder
```

Reverse-preorder trick:

```text
Process right, then left, then current.
Maintain `prev` as the already flattened suffix.
Point current.right to prev.
```

Template:

```python
def flatten(root):
    prev = None

    def dfs(node):
        nonlocal prev
        if not node:
            return

        dfs(node.right)
        dfs(node.left)

        node.right = prev
        node.left = None
        prev = node

    dfs(root)
```

Why reverse preorder works:

```text
Normal preorder output is root, left, right.
Building the linked list backward visits right, left, root.
When current is rewired, `prev` is exactly the suffix that should follow it.
```

### 14.2 - General mutation rules

Before rewiring pointers, answer:

| Question | Why it matters |
| --- | --- |
| Which child pointers do I still need to traverse? | avoid losing subtrees |
| Is the mutation preorder or postorder? | decide when children are safe |
| Does the prompt allow modifying the tree? | some variants require preserving input |
| Do I need to restore temporary threads? | Morris traversal must restore |

For Morris inorder, early return can leave temporary right pointers in the tree.
Use it only when the O(1) auxiliary-space constraint is important and you are
comfortable proving restoration.

### 14.3 - Next right pointers

Populating Next Right Pointers asks you to connect nodes across a level.

BFS version:

```python
from collections import deque

def connect(root):
    if not root:
        return None

    queue = deque([root])

    while queue:
        prev = None

        for _ in range(len(queue)):
            node = queue.popleft()

            if prev:
                prev.next = node
            prev = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        prev.next = None

    return root
```

The invariant is:

```text
Within one level, `prev` is the node immediately to the left of the current
node. After linking `prev.next = node`, advance `prev`.
```

The O(1) extra-space follow-up for general binary trees uses already-created
`next` pointers to scan the current level while building the next level with a
dummy head:

```text
current level: traverse using next pointers
next level: append children behind a tail pointer
```

That version is pointer-list construction, not ordinary BFS. The mental model
is "build the linked list for the next level while walking the linked list for
the current level."


---

## 15. Iterative DFS Without Mystery

Recursive DFS uses Python's call stack. Iterative DFS makes the stack explicit.

The word `stack` does not always mean the same thing.

| Iterative pattern | What the stack stores |
| --- | --- |
| simple preorder DFS | discovered nodes waiting to be processed |
| inorder BST traversal | ancestors waiting for left subtree completion |
| postorder simulation | nodes whose children may need to finish first |
| command stack | explicit commands such as process or visit |
| metadata stack | `(node, depth)`, `(node, path_max)`, `(node, low, high)` |

Always define what one stack entry represents.

### 15.1 - Simple preorder stack

Template:

```python
def preorder_values(root):
    if not root:
        return []

    values = []
    stack = [root]

    while stack:
        node = stack.pop()
        values.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return values
```

Push right before left because the stack is LIFO and you want left processed
first.

### 15.2 - Command stack

The command-stack model is the most general way to turn recursion into
iteration.

```text
(node, False) = process this node into smaller commands
(node, True)  = visit this node now
```

For inorder:

```python
def inorder_command_stack(root):
    values = []
    stack = [(root, False)]

    while stack:
        node, visit = stack.pop()
        if not node:
            continue

        if visit:
            values.append(node.val)
        else:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))

    return values
```

Commands are pushed in reverse execution order because the stack is LIFO.

This model is not always the most concise, but it is excellent for rebuilding
iterative traversals from first principles.

### 15.3 - Iterative postorder with computed facts

For postorder tree DP, you often need child facts before processing the parent.
One safe pattern uses a visited flag and a table.

Example: iterative heights.

```python
def max_depth_iterative(root):
    if not root:
        return 0

    height = {}
    stack = [(root, False)]

    while stack:
        node, seen = stack.pop()
        if not node:
            continue

        if seen:
            left = height.get(node.left, 0)
            right = height.get(node.right, 0)
            height[node] = 1 + max(left, right)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return height[root]
```

The first time a node appears, it schedules its children. The second time, child
heights are already known.


---

## 16. Correctness Invariants

Tree correctness arguments are usually short once the helper contract is clear.

### 16.1 - Structural induction

For recursive tree code, use structural induction:

```text
Base case:
    The helper returns the correct answer for None.

Inductive step:
    Assume the helper is correct for the left and right subtrees.
    Show that the current node combines those correct child results into the
    correct result for the current subtree.
```

Example: Maximum depth.

```text
Base: depth(None) = 0 is correct.
Step: if left and right child depths are correct, then the deepest path from
node uses one child path plus node itself, so 1 + max(left, right) is correct.
```

### 16.2 - Traversal invariant

For iterative traversals, state what the stack or queue means before each loop.

Examples:

```text
BFS level order:
At the start of each outer loop, the queue contains exactly the current level.
```

```text
BST inorder:
When a node is popped from the stack, every smaller reachable BST value has
already been emitted, and no larger value has been emitted yet.
```

```text
Right-first DFS right side view:
Before visiting a node at depth d, if len(ans) == d then no node at that depth
has been seen. Because traversal is right before left, this node is the
rightmost visible node for that depth.
```

### 16.3 - State ownership invariant

When state is carried downward, say who owns it.

```text
In Count Good Nodes, each stack entry owns its branch-local `path_max`.
Changing path_max for one child does not affect sibling branches.
```

When state is global, say why it is safe.

```text
In Diameter, `best` stores the maximum local diameter candidate observed among
all completed nodes. Each node contributes exactly one candidate,
left_height + right_height.
```


---

## 17. Complexity Basics

Most binary tree traversals visit each node once.

```text
Time: O(n)
```

Space depends on the shape and traversal.

| Method | Auxiliary space |
| --- | --- |
| recursive DFS | O(h) call stack |
| iterative DFS | O(h) average for many trees, O(n) worst case |
| BFS | O(w), where w is maximum width |
| serialization | O(n) tokens |
| construction with index map | O(n) map plus O(h) stack |

Tree height `h` can be:

```text
balanced tree: O(log n)
skewed tree:   O(n)
```

BFS width `w` can be `O(n)` in a wide last level.

Python recursion depth is a practical concern on skewed trees. If constraints
allow thousands of nodes and the platform does not raise the recursion limit,
keep an iterative variant in mind.


---

## 18. Failure Modes and Edge Cases

### 18.1 - Null and leaf confusion

`None` is an empty subtree. A leaf is a real node with no children.

```python
if not node:
    return 0       # empty

if not node.left and not node.right:
    return ...     # leaf
```

Path-sum problems often require root-to-leaf paths, so leaf detection matters.

### 18.2 - Node count versus edge count

Maximum Depth counts nodes in LeetCode 104. Diameter counts edges in LeetCode
543.

```text
leaf height in nodes = 1
diameter of single-node tree = 0
```

Write the unit in the helper contract.

### 18.3 - Returning the wrong fact

In Diameter and Maximum Path Sum:

```text
return upward: one branch
update answer: both branches may be used
```

Returning a path that already bends through both children to the parent is
wrong because the parent would create a forked path instead of a simple path.

### 18.4 - Global answer initialization

If node values can be negative:

```python
best = float("-inf")
```

not:

```python
best = 0
```

Maximum Path Sum must choose at least one real node.

### 18.5 - Shared mutable path state

When carrying a list path, either backtrack or copy.

Backtracking pattern:

```python
path.append(node.val)
dfs(node.left)
dfs(node.right)
path.pop()
```

Without `pop`, sibling branches see each other's values.

### 18.6 - Stack is not path

A DFS stack is a scheduling structure. It may contain nodes from different
branches at the same time.

If you need path context, store it explicitly:

```python
stack = [(root, [root.val])]
stack = [(root, current_sum)]
stack = [(root, path_max)]
```

### 18.7 - BFS level boundary mistakes

Wrong:

```python
while queue:
    node = queue.popleft()
    depth += 1
```

This increments per node, not per level.

Right:

```python
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        ...
    depth += 1
```

### 18.8 - BST parent-only checks

For BST validation, checking only immediate children misses ancestor
constraints.

Use either:

```text
open bounds inherited from ancestors
```

or:

```text
inorder strict increase
```

### 18.9 - Traversal order and update rule mismatch

Right side view examples:

| Traversal | Correct update |
| --- | --- |
| right-first DFS | append first value seen at each depth |
| left-first DFS | overwrite value at each depth |
| BFS left-to-right | take last value in each level |

If the traversal order changes, the update rule often changes too.

### 18.10 - Serialization without null markers

Traversal values alone do not preserve shape. Include null markers, separators,
or structural IDs.

### 18.11 - Losing children during rewiring

When mutating pointers, save anything you still need.

```python
left = node.left
right = node.right
```

or use an order that guarantees the needed child has already been processed.


---

## 19. When Not to Use a Binary Tree Pattern

Tree tags can be broad. Choose the technique based on the actual structure.

| Situation | Better tool or caution |
| --- | --- |
| parent pointers create cycles | graph DFS/BFS with `visited` |
| arbitrary edges, not parent-child tree | graph algorithms |
| sorted array to balanced tree | divide and conquer over indices |
| repeated kth queries in BST | subtree sizes or balanced tree structure |
| prefix lookup strings | trie, which is a different tree shape |
| nearest values/range queries in Python | maybe sorting plus binary search; built-in BST is absent |
| huge skewed tree in Python | iterative DFS/BFS may be safer than recursion |

A binary tree is acyclic by definition. Once the prompt adds parent pointers or
undirected edges, protect against revisiting nodes.


---

## 20. Practice Progression

Use this progression to build from mechanics to advanced patterns.

### 20.1 - Core mechanics

1. Maximum Depth of Binary Tree
2. Invert Binary Tree
3. Same Tree
4. Symmetric Tree

Focus:

```text
null base cases, leaf handling, simple return contracts, pointer swapping
```

### 20.2 - Postorder tree DP

1. Diameter of Binary Tree
2. Balanced Binary Tree
3. Binary Tree Maximum Path Sum

Focus:

```text
return local fact upward, update global answer or return tuple, distinguish
height/gain from final answer
```

### 20.3 - Top-down path context

1. Path Sum
2. Sum Root to Leaf Numbers
3. Count Good Nodes in Binary Tree

Focus:

```text
branch-local state, leaf conditions, iterative payloads
```

### 20.4 - BFS level patterns

1. Binary Tree Level Order Traversal
2. Average of Levels in Binary Tree
3. Binary Tree Right Side View
4. Binary Tree Zigzag Level Order Traversal

Focus:

```text
queue-size snapshot, depth payloads, output order, first-seen versus overwrite
```

### 20.5 - BST patterns

1. Validate Binary Search Tree
2. Kth Smallest Element in a BST
3. Minimum Absolute Difference in BST
4. Lowest Common Ancestor of a BST
5. Binary Search Tree Iterator

Focus:

```text
inorder sorted stream, strict increasing values, rank counting, split point
```

### 20.6 - Construction and serialization

1. Construct Binary Tree from Preorder and Inorder Traversal
2. Construct Binary Tree from Inorder and Postorder Traversal
3. Serialize and Deserialize Binary Tree
4. Flatten Binary Tree to Linked List

Focus:

```text
traversal ownership ranges, null markers, queue child slots, mutation order
```


---

## 21. Interview Explanation Templates

### 21.1 - Bottom-up DFS

```text
I will define a helper on a subtree. The helper returns the one fact the parent
needs. The base case is the empty subtree. For a real node, I first solve the
left and right subtrees, then combine their results at the current node. This
visits each node once, so the time is O(n), and the recursion stack is O(h).
```

### 21.2 - Global answer plus local return

```text
The parent can only use a one-sided value from a child, but the final answer may
be completed inside any subtree. So my helper returns the extendable value, and
I update a separate best answer at every node using the local candidate through
that node.
```

### 21.3 - Top-down context

```text
Each node needs information from its ancestors, so I pass that context down as a
parameter. The value is branch-local: each child receives an updated copy of the
context, and sibling branches do not share it.
```

### 21.4 - BFS by level

```text
I will use a queue. At the start of each outer loop, the queue contains exactly
one level. I save the queue size, process that many nodes into the current row,
and enqueue their children for the next row.
```

### 21.5 - BST inorder

```text
For a BST, inorder traversal emits values in sorted order. I can use that stream
directly: validate by checking strict increase, answer kth smallest by counting
inorder pops, or compare adjacent values for minimum difference.
```

### 21.6 - Tree construction

```text
Preorder gives me the next root. Inorder tells me which values belong to that
root's left and right subtrees. My recursive frame owns an inorder interval, and
the preorder pointer always points to the root of that interval.
```


---

## 22. Quick Reference

### 22.1 - Pattern selection table

| Prompt clue | Pattern |
| --- | --- |
| max depth, count, sum | simple subtree return |
| diameter, max path sum | postorder return plus global best |
| balanced tree | postorder height plus sentinel or tuple |
| path sum, good nodes | top-down carried context |
| same/symmetric/subtree | paired subtree traversal |
| LCA in general tree | postorder target bubbling |
| level order/averages/right view | BFS by level |
| validate BST | bounds DFS or inorder strict increase |
| kth smallest BST | inorder rank stream |
| construct from traversals | root source plus ownership ranges |
| count complete tree nodes | perfect-subtree height shortcut |
| serialize/deserialize | traversal tokens with null markers |
| flatten/invert/connect | pointer rewiring with ownership discipline |

### 22.2 - Helper contract prompts

Before coding, answer:

```text
What does dfs(node) return for None?
What does dfs(node) return for a leaf?
What exact fact does the parent need?
What answer, if any, is updated globally?
What context must be attached to each child call?
Does the current node act before, between, or after children?
```

### 22.3 - Traversal timing cheat sheet

```text
preorder:
    process node
    left
    right

inorder:
    left
    process node
    right

postorder:
    left
    right
    process node

BFS:
    process nodes by increasing depth
```

### 22.4 - Python implementation reminders

- Use `collections.deque` for BFS queues.
- Use `nonlocal best` when a nested helper updates a captured answer.
- Prefer `None` sentinels for "no previous value yet" in BST inorder checks.
- Avoid numeric sentinels when node values can cover the whole range.
- Attach metadata to stack/queue entries when context is branch-local.
- For recursive solutions on skewed trees, mention the O(h) call stack and
  Python recursion-depth risk.
- Do not mutate `node.val` to store computed helper state unless the prompt
  explicitly allows altering input values.

### 22.5 - Mastery checklist

You are ready for most binary-tree interviews when you can:

- define a helper contract before coding;
- explain the null base case and leaf behavior;
- choose preorder, inorder, postorder, or BFS based on information timing;
- distinguish state returned upward from context carried downward;
- use `nonlocal best` or tuple returns for global-answer tree DP;
- carry branch-local metadata in iterative DFS/BFS entries;
- use queue-size snapshots for BFS levels;
- use inorder as a sorted stream for BSTs;
- validate BSTs with ancestor bounds or strict inorder increase;
- build trees from traversal ranges without slicing;
- serialize with null markers;
- reason about O(h), O(w), and O(n) space;
- avoid losing subtrees during pointer rewiring;
- give a short structural-induction correctness proof.
