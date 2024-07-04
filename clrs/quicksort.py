def lomuto_partition(data: list[int], start: int, end: int) -> int:
    pivot = data[end - 1]
    i = start - 1

    for j in range(start, end - 1):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    i += 1
    data[i], data[end - 1] = data[end - 1], data[i]
    return i


def lomuto_quicksort(data: list[int], start: int, end: int) -> None:
    if end - start <= 1:
        return

    pivot_index = lomuto_partition(data, start, end)
    lomuto_quicksort(data, start, pivot_index)
    lomuto_quicksort(data, pivot_index + 1, end)


def median3(a: int, b: int, c: int) -> int:
    if (a < b) != (a < c):
        return a
    elif (b > a) != (b > c):
        return b
    else:
        return c


def hoare_partition(data: list[int], start: int, end: int) -> int:
    mid = ((end - 1) + start) // 2
    pivot = median3(data[start], data[mid], data[end - 1])
    i = start - 1
    j = end

    while True:
        i += 1
        while data[i] < pivot:
            i += 1

        j -= 1
        while data[j] > pivot:
            j -= 1

        if i >= j:
            return j

        data[i], data[j] = data[j], data[i]


def hoare_quicksort(data: list[int], start: int, end: int) -> None:
    if end - start <= 1:
        return

    pivot_index = hoare_partition(data, start, end)
    hoare_quicksort(data, start, pivot_index + 1)
    hoare_quicksort(data, pivot_index + 1, end)


quicksort = hoare_quicksort
