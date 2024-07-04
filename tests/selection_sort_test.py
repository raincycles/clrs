import pytest

from clrs.selection_sort import selection_sort


@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([4, 5, 5, 2, 1, 4, 2], [1, 2, 2, 4, 4, 5, 5]),
    ],
)
def test_selection_sort(input_list, expected):
    a = list(input_list)
    selection_sort(a)
    assert a == expected
