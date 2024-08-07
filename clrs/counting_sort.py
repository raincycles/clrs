# O(n)
def counting_sort(data: list[int], min_value: int, max_value: int) -> None:
    prefix_sums = [0] * (max_value - min_value + 1)
    data_copy = list(data)

    for value in data:
        prefix_sums[value - min_value] += 1

    for i in range(1, len(prefix_sums)):
        prefix_sums[i] += prefix_sums[i - 1]

    for value in reversed(data_copy):
        prefix_sums[value - min_value] -= 1
        actual_index = prefix_sums[value - min_value]
        data[actual_index] = value
