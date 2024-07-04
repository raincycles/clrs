import pytest

from clrs.heapsort import heapsort


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
def test_heapsort(input_list, expected):
    a = list(input_list)
    heapsort(a)
    assert a == expected
