import pytest

from clrs.linear_search import linear_search

test_params = [
    ([12, 75, 15, 48, 56, 91], 56, 4),
    ([57, 63, 93, 19], 999, -1),
]


@pytest.mark.parametrize("test_data,target,expected", test_params)
def test_linear_search(test_data, target, expected):
    idx = linear_search(test_data, target)
    assert idx == expected
