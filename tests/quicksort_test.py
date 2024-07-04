import pytest

from clrs.quicksort import (
    hoare_quicksort,
    lomuto_quicksort,
)


@pytest.mark.parametrize(
    "input_list,start,end,expected",
    [
        ([], 0, 0, []),
        ([1], 0, 1, [1]),
        ([5, 2], 0, 2, [2, 5]),
        ([5, 5, 5], 0, 3, [5, 5, 5]),
        ([1, 2, 3, 4, 5], 0, 5, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 0, 5, [1, 2, 3, 4, 5]),
        ([4, 5, 5, 2, 1, 4, 2], 0, 7, [1, 2, 2, 4, 4, 5, 5]),
        ([4, 3, 7, 8, 1, 2, 6, 5], 2, 6, [4, 3, 1, 2, 7, 8, 6, 5]),
    ],
)
def test_lomuto_quicksort(input_list, start, end, expected):
    a = list(input_list)
    lomuto_quicksort(a, start, end)
    assert a == expected


@pytest.mark.parametrize(
    "input_list,start,end,expected",
    [
        ([], 0, 0, []),
        ([1], 0, 1, [1]),
        ([5, 2], 0, 2, [2, 5]),
        ([5, 5, 5], 0, 3, [5, 5, 5]),
        ([1, 2, 3, 4, 5], 0, 5, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 0, 5, [1, 2, 3, 4, 5]),
        ([4, 5, 5, 2, 1, 4, 2], 0, 7, [1, 2, 2, 4, 4, 5, 5]),
        ([4, 3, 7, 8, 1, 2, 6, 5], 2, 6, [4, 3, 1, 2, 7, 8, 6, 5]),
    ],
)
def test_hoare_quicksort(input_list, start, end, expected):
    a = list(input_list)
    hoare_quicksort(a, start, end)
    assert a == expected
