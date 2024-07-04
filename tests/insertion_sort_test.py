import pytest

from clrs.insertion_sort import (
    insertion_sort,
    insertion_sort_rec,
)


@pytest.mark.parametrize(
    "input_list,start,end,expected",
    [
        ([], 0, 0, []),
        ([1], 0, 1, [1]),
        ([1, 2, 3, 4, 5], 0, 5, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 0, 5, [1, 2, 3, 4, 5]),
        ([4, 5, 5, 2, 1, 4, 2], 0, 7, [1, 2, 2, 4, 4, 5, 5]),
        ([4, 3, 7, 8, 1, 2, 6, 5], 2, 6, [4, 3, 1, 2, 7, 8, 6, 5]),
    ],
)
def test_insertion_sort(input_list, start, end, expected):
    a = list(input_list)
    insertion_sort(a, start, end)
    assert a == expected


@pytest.mark.parametrize(
    "input_list,start,end,expected",
    [
        ([], 0, 0, []),
        ([1], 0, 1, [1]),
        ([1, 2, 3, 4, 5], 0, 5, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 0, 5, [1, 2, 3, 4, 5]),
        ([4, 3, 7, 8, 1, 2, 6, 5], 2, 6, [4, 3, 1, 2, 7, 8, 6, 5]),
        ([4, 3, 7, 8, 1, 2, 6, 5], 2, 6, [4, 3, 1, 2, 7, 8, 6, 5]),
    ],
)
def test_insertion_sort_rec(input_list, start, end, expected):
    a = list(input_list)
    insertion_sort_rec(a, start, end)
    assert a == expected
