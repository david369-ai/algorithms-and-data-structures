import pytest
from src.data_structures.deque import Deque


def test_empty():
    d = Deque()
    assert d.is_empty()
    assert len(d) == 0


def test_push_front():
    d = Deque()
    d.push_front(1)
    d.push_front(2)
    assert d.to_list() == [2, 1]


def test_push_back():
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    assert d.to_list() == [1, 2]


def test_mixed():
    d = Deque()
    d.push_back(2)
    d.push_back(3)
    d.push_front(1)
    d.push_front(0)
    assert d.to_list() == [0, 1, 2, 3]


def test_pop_front():
    d = Deque()
    for x in [1, 2, 3]:
        d.push_back(x)
    assert d.pop_front() == 1
    assert d.to_list() == [2, 3]


def test_pop_back():
    d = Deque()
    for x in [1, 2, 3]:
        d.push_back(x)
    assert d.pop_back() == 3
    assert d.to_list() == [1, 2]


def test_pop_empty():
    d = Deque()
    with pytest.raises(IndexError):
        d.pop_front()
    with pytest.raises(IndexError):
        d.pop_back()


def test_peek():
    d = Deque()
    d.push_back(1)
    d.push_back(2)
    assert d.peek_front() == 1
    assert d.peek_back() == 2


def test_single_element():
    d = Deque()
    d.push_back(42)
    assert d.pop_back() == 42
    assert d.is_empty()
    assert d.peek_front() is None
    assert d.peek_back() is None
