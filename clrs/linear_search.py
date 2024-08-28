# O(n)
def linear_search(data: list[int], target: int) -> int | None:
    for i, value in enumerate(data):
        if value == target:
            return i

    return None
