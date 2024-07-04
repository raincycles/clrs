def merge_sort(data: list[int], start: int, end: int) -> None:
    if end - start <= 1:
        return

    mid = ((end - 1) + start) // 2

    merge_sort(data, start, mid + 1)
    merge_sort(data, mid + 1, end)

    left = data[start : mid + 1]
    right = data[mid + 1 : end]

    left_length = len(left)
    right_length = len(right)

    i = 0
    j = 0
    for k in range(start, end):
        if i < left_length and (j >= right_length or left[i] <= right[j]):
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
