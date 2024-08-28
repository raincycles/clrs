import pytest

from clrs.linear_search import linear_search


@pytest.mark.parametrize(
    "input_list,target,expected",
    [
        ([], 5, None),
        ([5], 5, 0),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 4, 4, 7, 5, 4, 6], 4, 1),
        ([1, 4, 4, 7, 5, 4, 6], 8, None),
    ],
)
def test_linear_search(input_list, target, expected):
    i = linear_search(input_list, target)
    assert i == expected
