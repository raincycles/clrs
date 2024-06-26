def merge_sort(data: list[int], start: int, end: int) -> None:
    if end - start <= 1:
        return

    mid = start + (end - start) // 2

    merge_sort(data, start, mid)
    merge_sort(data, mid, end)

    left = data[start:mid]
    right = data[mid:end]

    ln = len(left)
    rn = len(right)

    li = 0
    ri = 0

    for i in range(start, end):
        if li < ln and (ri >= rn or left[li] <= right[ri]):
            data[i] = left[li]
            li += 1
        else:
            data[i] = right[ri]
            ri += 1
