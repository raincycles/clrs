import pytest

from clrs.binary_search import (
    binary_search,
    binary_search_leftmost,
    binary_search_rec,
    binary_search_rightmost,
)


@pytest.mark.parametrize(
    "input_list,target,start,end,expected",
    [
        ([], 5, 0, 0, None),
        ([5], 5, 0, 1, 0),
        ([2, 5], 5, 0, 2, 1),
        ([1, 2, 3, 4, 5], 1, 0, 5, 0),
        ([1, 2, 3, 4, 5], 5, 0, 5, 4),
        ([1, 2, 3, 4, 5], 6, 0, 5, None),
        ([1, 2, 3, 4, 5], 2, 1, 4, 1),
        ([1, 2, 3, 4, 5], 5, 1, 4, None),
    ],
)
def test_binary_search(input_list, target, start, end, expected):
    i = binary_search(input_list, target, start, end)
    assert i == expected


@pytest.mark.parametrize(
    "input_list,target,start,end,expected",
    [
        ([], 5, 0, 0, None),
        ([5], 5, 0, 1, 0),
        ([2, 5], 5, 0, 2, 1),
        ([1, 2, 3, 4, 5], 1, 0, 5, 0),
        ([1, 2, 3, 4, 5], 5, 0, 5, 4),
        ([1, 2, 3, 4, 5], 6, 0, 5, None),
        ([1, 2, 3, 4, 5], 2, 1, 4, 1),
        ([1, 2, 3, 4, 5], 5, 1, 4, None),
    ],
)
def test_binary_search_rec(input_list, target, start, end, expected):
    i = binary_search_rec(input_list, target, start, end)
    assert i == expected


@pytest.mark.parametrize(
    "input_list,target,start,end,expected",
    [
        ([], 5, 0, 0, None),
        ([5], 5, 0, 1, 0),
        ([2, 5], 5, 0, 2, 1),
        ([1, 2, 3, 4, 5], 1, 0, 5, 0),
        ([1, 2, 3, 4, 5], 5, 0, 5, 4),
        ([1, 2, 3, 4, 5], 6, 0, 5, None),
        ([1, 2, 3, 4, 5], 2, 1, 4, 1),
        ([1, 2, 3, 4, 5], 5, 1, 4, None),
        ([1, 2, 2, 2, 3, 3, 5], 2, 0, 6, 1),
        ([1, 2, 2, 2, 3, 3, 5], 2, 2, 5, 2),
    ],
)
def test_binary_search_leftmost(input_list, target, start, end, expected):
    i = binary_search_leftmost(input_list, target, start, end)
    assert i == expected


@pytest.mark.parametrize(
    "input_list,target,start,end,expected",
    [
        ([], 5, 0, 0, None),
        ([5], 5, 0, 1, 0),
        ([2, 5], 5, 0, 2, 1),
        ([1, 2, 3, 4, 5], 1, 0, 5, 0),
        ([1, 2, 3, 4, 5], 5, 0, 5, 4),
        ([1, 2, 3, 4, 5], 6, 0, 5, None),
        ([1, 2, 3, 4, 5], 2, 1, 4, 1),
        ([1, 2, 3, 4, 5], 5, 1, 4, None),
        ([1, 2, 2, 2, 3, 3, 5], 2, 0, 6, 3),
        ([1, 2, 2, 2, 3, 3, 5], 2, 2, 5, 3),
    ],
)
def test_binary_search_rightmost(input_list, target, start, end, expected):
    i = binary_search_rightmost(input_list, target, start, end)
    assert i == expected
