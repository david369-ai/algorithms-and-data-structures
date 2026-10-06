from src.sorting.bubble_sort import bubble_sort


def test_empty():
    assert bubble_sort([]) == []


def test_single():
    assert bubble_sort([5]) == [5]


def test_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_random():
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]


def test_duplicates():
    assert bubble_sort([3, 1, 3, 2, 1]) == [1, 1, 2, 3, 3]


def test_does_not_mutate():
    original = [3, 1, 2]
    bubble_sort(original)
    assert original == [3, 1, 2]
