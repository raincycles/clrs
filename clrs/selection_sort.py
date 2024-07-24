# O(n^2)
def selection_sort(data: list[int]) -> None:
    n = len(data)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j

        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
