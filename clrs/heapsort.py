# O(log(n))
def max_sift_down(data: list[int], start: int, end: int) -> None:
    index = start

    while True:
        child_index = index * 2 + 1

        if child_index >= end:
            return

        if child_index + 1 < end and data[child_index] < data[child_index + 1]:
            child_index += 1

        if not data[index] < data[child_index]:
            return

        data[index], data[child_index] = data[child_index], data[index]
        index = child_index


# O(n)
def make_max_heap(data: list[int]) -> None:
    n = len(data)

    for i in range((n // 2) - 1, -1, -1):
        max_sift_down(data, i, n)


# O(n * log(n))
def heapsort(data: list[int]) -> None:
    n = len(data)
    make_max_heap(data)

    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        max_sift_down(data, 0, i)
