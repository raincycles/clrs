def linear_search(data: list[int], target: int) -> int:
    for i, x in enumerate(data):
        if x == target:
            return i

    return -1
