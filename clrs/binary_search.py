def binary_search(data: list[int], start: int, end: int, target: int) -> int:
    low = start
    high = end - 1

    while low <= high:
        mid = low + (high - low) // 2

        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


def binary_search_rec(data: list[int], start: int, end: int, target: int) -> int:
    low = start
    high = end - 1

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if data[mid] < target:
        return binary_search_rec(data, mid + 1, end, target)

    if data[mid] > target:
        return binary_search_rec(data, start, mid, target)

    return mid


def binary_search_leftmost(data: list[int], start: int, end: int, target: int) -> int:
    low = start
    high = end

    while low < high:
        mid = low + (high - low) // 2

        if data[mid] < target:
            low = mid + 1
        else:
            high = mid

    if low < end and data[low] == target:
        return low

    return -1


def binary_search_rightmost(data: list[int], start: int, end: int, target: int) -> int:
    low = start
    high = end

    while low < high:
        mid = low + (high - low) // 2

        if data[mid] <= target:
            low = mid + 1
        else:
            high = mid

    if high > start and data[high - 1] == target:
        return high - 1

    return -1
