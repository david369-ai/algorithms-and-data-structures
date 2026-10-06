import pytest
from src.data_structures.linked_list import LinkedList


def test_empty():
    lst = LinkedList()
    assert lst.is_empty()
    assert len(lst) == 0


def test_push_front():
    lst = LinkedList()
    lst.push_front(1)
    lst.push_front(2)
    assert lst.to_list() == [2, 1]


def test_push_back():
    lst = LinkedList()
    lst.push_back(1)
    lst.push_back(2)
    assert lst.to_list() == [1, 2]


def test_pop_front():
    lst = LinkedList()
    for x in [1, 2, 3]:
        lst.push_back(x)
    assert lst.pop_front() == 1
    assert lst.to_list() == [2, 3]


def test_pop_front_empty():
    lst = LinkedList()
    with pytest.raises(IndexError):
        lst.pop_front()


def test_find():
    lst = LinkedList()
    for x in [10, 20, 30]:
        lst.push_back(x)
    assert lst.find(20).value == 20
    assert lst.find(99) is None


def test_remove():
    lst = LinkedList()
    for x in [1, 2, 3]:
        lst.push_back(x)
    assert lst.remove(2) is True
    assert lst.to_list() == [1, 3]
    assert lst.remove(99) is False


def test_remove_head():
    lst = LinkedList()
    for x in [1, 2]:
        lst.push_back(x)
    lst.remove(1)
    assert lst.to_list() == [2]


def test_iter():
    lst = LinkedList()
    for x in [1, 2, 3]:
        lst.push_back(x)
    assert list(lst) == [1, 2, 3]
