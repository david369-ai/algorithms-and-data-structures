from src.sorting.quick_sort import quick_sort


def test_empty():
    assert quick_sort([]) == []


def test_single():
    assert quick_sort([5]) == [5]


def test_sorted():
    assert quick_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse():
    assert quick_sort([3, 2, 1]) == [1, 2, 3]


def test_random():
    assert quick_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]


def test_duplicates():
    assert quick_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_does_not_mutate():
    original = [3, 1, 2]
    quick_sort(original)
    assert original == [3, 1, 2]
