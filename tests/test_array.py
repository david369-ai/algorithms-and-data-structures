import pytest
from src.data_structures.array import Array


def test_empty_array():
    arr = Array()
    assert len(arr) == 0


def test_push_and_get():
    arr = Array()
    arr.push(10)
    arr.push(20)
    assert len(arr) == 2
    assert arr[0] == 10
    assert arr[1] == 20


def test_resize():
    arr = Array(capacity=2)
    for i in range(10):
        arr.push(i)
    assert len(arr) == 10
    assert arr[9] == 9


def test_pop():
    arr = Array()
    arr.push(1)
    arr.push(2)
    assert arr.pop() == 2
    assert len(arr) == 1


def test_pop_empty():
    arr = Array()
    with pytest.raises(IndexError):
        arr.pop()


def test_insert():
    arr = Array()
    arr.push(1)
    arr.push(3)
    arr.insert(1, 2)
    assert list(arr[i] for i in range(len(arr))) == [1, 2, 3]


def test_remove():
    arr = Array()
    for x in [1, 2, 3]:
        arr.push(x)
    assert arr.remove(1) == 2
    assert list(arr[i] for i in range(len(arr))) == [1, 3]


def test_index_out_of_range():
    arr = Array()
    arr.push(1)
    with pytest.raises(IndexError):
        _ = arr[5]


def test_find():
    arr = Array()
    for x in [10, 20, 30]:
        arr.push(x)
    assert arr.find(20) == 1
    assert arr.find(99) == -1
