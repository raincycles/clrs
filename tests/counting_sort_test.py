import pytest

from clrs.counting_sort import counting_sort


@pytest.mark.parametrize(
    "input_list,max_value,expected",
    [
        ([], 1, []),
        ([1], 1, [1]),
        ([5, 5, 5], 5, [5, 5, 5]),
        ([3, 4, 2, 5], 10, [2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 5, [1, 2, 3, 4, 5]),
        ([4, 5, 5, 2, 1, 4, 2], 5, [1, 2, 2, 4, 4, 5, 5]),
    ],
)
def test_counting_sort(input_list, max_value, expected):
    a = list(input_list)
    counting_sort(a, max_value)
    assert a == expected
