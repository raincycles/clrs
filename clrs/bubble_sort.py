def bubble_sort(data: list[int]) -> None:
    n = len(data)

    for i in range(0, n - 1):
        swapped = False

        for j in range(1, n - i):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
                swapped = True

        if not swapped:
            return
