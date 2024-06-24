def insertion_sort(data: list[int], start: int, end: int) -> None:
    for i in range(start + 1, end):
        j = i
        while j > start and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1


def insertion_sort_rec(data: list[int], start: int, end: int) -> None:
    if end - start <= 1:
        return

    i = end - 1
    insertion_sort_rec(data, start, i)

    j = i
    while j > start and data[j] < data[j - 1]:
        data[j], data[j - 1] = data[j - 1], data[j]
        j -= 1
