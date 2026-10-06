def _partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_inplace(arr: list, low: int, high: int) -> None:
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_inplace(arr, low, pi - 1)
        _quick_sort_inplace(arr, pi + 1, high)


def quick_sort(arr: list) -> list:
    result = arr.copy()
    if len(result) > 1:
        _quick_sort_inplace(result, 0, len(result) - 1)
    return result
