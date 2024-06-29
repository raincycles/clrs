def max_sift_down(data: list[int], start: int, end: int) -> None:
    parent = start

    while True:
        child = parent * 2 + 1
        if child >= end:
            return

        if child + 1 < end and data[child + 1] > data[child]:
            child += 1

        if data[parent] >= data[child]:
            return

        data[parent], data[child] = data[child], data[parent]
        parent = child


def make_max_heap(data: list[int]) -> None:
    n = len(data)
    for i in range((n // 2) - 1, -1, -1):
        max_sift_down(data, i, n)


def heapsort(data: list[int]) -> None:
    n = len(data)
    make_max_heap(data)
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        max_sift_down(data, 0, i)
