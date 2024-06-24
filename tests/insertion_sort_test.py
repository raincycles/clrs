import pytest

from clrs.insertion_sort import (
    insertion_sort,
    insertion_sort_rec,
)

test_params = [
    ([3, 4, 6, 5, 1, 2], 0, 6, [1, 2, 3, 4, 5, 6]),
    ([4, 6, 2, 1, 3, 5], 2, 5, [4, 6, 1, 2, 3, 5]),
]


@pytest.mark.parametrize("test_data,start,end,expected", test_params)
def test_insertion_sort(test_data, start, end, expected):
    data = list(test_data)
    insertion_sort(data, start, end)
    assert data == expected


@pytest.mark.parametrize("test_data,start,end,expected", test_params)
def test_insertion_sort_rec(test_data, start, end, expected):
    data = list(test_data)
    insertion_sort_rec(data, start, end)
    assert data == expected
