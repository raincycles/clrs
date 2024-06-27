import pytest

from clrs.binary_search import (
    binary_search,
    binary_search_rec,
    binary_search_leftmost,
    binary_search_rightmost,
)


@pytest.mark.parametrize(
    "input_list,start,end,target,expected",
    [
        ([], 0, 0, 5, -1),
        ([5], 0, 1, 5, 0),
        ([2, 5], 0, 2, 5, 1),
        ([1, 2, 3, 4, 5], 0, 5, 1, 0),
        ([1, 2, 3, 4, 5], 0, 5, 5, 4),
        ([1, 2, 3, 4, 5], 0, 5, 6, -1),
        ([1, 2, 3, 4, 5], 1, 4, 2, 1),
        ([1, 2, 3, 4, 5], 1, 4, 5, -1),
    ],
)
def test_binary_search(input_list, start, end, target, expected):
    i = binary_search(input_list, start, end, target)
    assert i == expected


@pytest.mark.parametrize(
    "input_list,start,end,target,expected",
    [
        ([], 0, 0, 5, -1),
        ([5], 0, 1, 5, 0),
        ([2, 5], 0, 2, 5, 1),
        ([1, 2, 3, 4, 5], 0, 5, 1, 0),
        ([1, 2, 3, 4, 5], 0, 5, 5, 4),
        ([1, 2, 3, 4, 5], 0, 5, 6, -1),
        ([1, 2, 3, 4, 5], 1, 4, 2, 1),
        ([1, 2, 3, 4, 5], 1, 4, 5, -1),
    ],
)
def test_binary_search_rec(input_list, start, end, target, expected):
    i = binary_search_rec(input_list, start, end, target)
    assert i == expected


@pytest.mark.parametrize(
    "input_list,start,end,target,expected",
    [
        ([], 0, 0, 5, -1),
        ([5], 0, 1, 5, 0),
        ([2, 5], 0, 2, 5, 1),
        ([1, 2, 3, 4, 5], 0, 5, 1, 0),
        ([1, 2, 3, 4, 5], 0, 5, 5, 4),
        ([1, 2, 3, 4, 5], 0, 5, 6, -1),
        ([1, 2, 3, 4, 5], 1, 4, 2, 1),
        ([1, 2, 3, 4, 5], 1, 4, 5, -1),
        ([1, 2, 2, 2, 3, 3, 5], 0, 6, 2, 1),
        ([1, 2, 2, 2, 3, 3, 5], 2, 5, 2, 2),
    ],
)
def test_binary_search_leftmost(input_list, start, end, target, expected):
    i = binary_search_leftmost(input_list, start, end, target)
    assert i == expected


@pytest.mark.parametrize(
    "input_list,start,end,target,expected",
    [
        ([], 0, 0, 5, -1),
        ([5], 0, 1, 5, 0),
        ([2, 5], 0, 2, 5, 1),
        ([1, 2, 3, 4, 5], 0, 5, 1, 0),
        ([1, 2, 3, 4, 5], 0, 5, 5, 4),
        ([1, 2, 3, 4, 5], 0, 5, 6, -1),
        ([1, 2, 3, 4, 5], 1, 4, 2, 1),
        ([1, 2, 3, 4, 5], 1, 4, 5, -1),
        ([1, 2, 2, 2, 3, 3, 5], 0, 6, 2, 3),
        ([1, 2, 2, 2, 3, 3, 5], 2, 5, 2, 3),
    ],
)
def test_binary_search_rightmost(input_list, start, end, target, expected):
    i = binary_search_rightmost(input_list, start, end, target)
    assert i == expected
