def linear_search(data: list[int], target: int) -> int:
    for i, value in enumerate(data):
        if value == target:
            return i

    return -1
