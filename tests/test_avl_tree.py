from src.data_structures.avl_tree import AVLTree


def test_empty():
    tree = AVLTree()
    assert tree.root is None
    assert tree.inorder() == []


def test_insert_single():
    tree = AVLTree()
    tree.insert(10)
    assert tree.contains(10)
    assert tree.inorder() == [10]


def test_insert_sorted():
    tree = AVLTree()
    for x in [1, 2, 3, 4, 5]:
        tree.insert(x)
    assert tree.inorder() == [1, 2, 3, 4, 5]
    assert tree.height() <= 3


def test_insert_reverse():
    tree = AVLTree()
    for x in [5, 4, 3, 2, 1]:
        tree.insert(x)
    assert tree.inorder() == [1, 2, 3, 4, 5]
    assert tree.height() <= 3


def test_insert_duplicates():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(5)
    assert tree.inorder() == [5]


def test_contains():
    tree = AVLTree()
    for x in [10, 5, 15, 3, 7]:
        tree.insert(x)
    assert tree.contains(7)
    assert not tree.contains(99)


def test_many_elements():
    tree = AVLTree()
    values = list(range(100))
    for v in values:
        tree.insert(v)
    assert tree.inorder() == values
    assert tree.height() <= 10
