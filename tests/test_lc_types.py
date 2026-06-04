from common.lc_types import (
    GraphNode,
    NextTreeNode,
    Node,
    QuadTreeNode,
    RandomPointerNode,
    build_graph,
    build_next_tree,
    build_random_list,
    graph_to_adjacency,
    next_tree_to_levels,
    quad_tree_to_values,
    random_list_to_values,
)


def test_random_pointer_node_accepts_leetcode_and_local_keywords():
    by_x = RandomPointerNode(x=7)
    by_val = RandomPointerNode(val=13)

    by_x.next = by_val
    by_val.random = by_x

    assert by_x.val == 7
    assert by_val.val == 13
    assert random_list_to_values(by_x) == [[7, None], [13, 0]]


def test_build_random_list_returns_specific_node_type():
    head = build_random_list([[1, 1], [2, 0]])

    assert isinstance(head, RandomPointerNode)
    assert isinstance(head.next, RandomPointerNode)
    assert head.random is head.next
    assert head.next.random is head


def test_graph_node_builder_uses_graph_shape():
    node = build_graph([[2], [1]])

    assert isinstance(node, GraphNode)
    assert node.neighbors[0].neighbors[0] is node
    assert graph_to_adjacency(node) == [[2], [1]]


def test_next_tree_node_builder_uses_tree_next_shape():
    root = build_next_tree([1, 2, 3])

    assert isinstance(root, NextTreeNode)
    assert isinstance(root.left, NextTreeNode)
    assert next_tree_to_levels(root) == [1, "#", 2, 3, "#"]


def test_quad_tree_node_serialization_shape():
    root = QuadTreeNode(
        True,
        False,
        QuadTreeNode(True, True),
        QuadTreeNode(False, True),
        QuadTreeNode(True, True),
        QuadTreeNode(False, True),
    )

    assert quad_tree_to_values(root) == [
        False,
        True,
        [True, True, None, None, None, None],
        [True, False, None, None, None, None],
        [True, True, None, None, None, None],
        [True, False, None, None, None, None],
    ]


def test_legacy_node_remains_backward_compatible():
    random_style = Node(x=5)
    child = Node(False, True)
    quad_style = Node(True, False, child, None, None, None)

    assert random_style.val == 5
    assert quad_style.val is True
    assert quad_style.isLeaf is False
    assert quad_style.topLeft is child
