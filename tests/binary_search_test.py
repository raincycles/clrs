import pytest

from clrs.binary_search import (
    binary_search,
    binary_search_leftmost,
    binary_search_rightmost,
    binary_search_rec,
)


test_params = [
    ([18, 13, 33, 34, 92, 97], 0, 5, 33, 2),
    ([15, 20, 41, 54, 70, 82], 0, 5, 99, -1),
    ([20, 28, 45, 80, 93, 95], 1, 4, 20, -1),
]


@pytest.mark.parametrize("test_data,start,end,target,expected", test_params)
def test_binary_search(test_data, start, end, target, expected):
    idx = binary_search(test_data, start, end, target)
    assert idx == expected


@pytest.mark.parametrize("test_data,start,end,target,expected", test_params)
def test_binary_search_rec(test_data, start, end, target, expected):
    idx = binary_search_rec(test_data, start, end, target)
    assert idx == expected


@pytest.mark.parametrize("test_data,start,end,target,expected", test_params)
def test_binary_search_leftmost(test_data, start, end, target, expected):
    idx = binary_search_leftmost(test_data, start, end, target)
    assert idx == expected


@pytest.mark.parametrize("test_data,start,end,target,expected", test_params)
def test_binary_search_rightmost(test_data, start, end, target, expected):
    idx = binary_search_rightmost(test_data, start, end, target)
    assert idx == expected
