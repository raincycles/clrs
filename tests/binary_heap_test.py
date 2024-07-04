import pytest

from clrs.binary_heap import MinHeap


class TestMinHeap:
    @pytest.mark.parametrize(
        "input_list,expected",
        [
            ([1], [1]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([4, 5, 5, 2, 1, 4, 2], [1, 2, 2, 4, 4, 5, 5]),
        ],
    )
    def test_push_and_pop(self, input_list, expected):
        heap = MinHeap()
        for x in input_list:
            heap.push(x)

        for x in expected:
            assert heap.pop() == x

    @pytest.mark.parametrize(
        "input_list,next_value,expected",
        [
            ([], 5, 5),
            ([4, 6, 2, 5], 7, 2),
            ([4, 6, 2, 5], 1, 1),
        ],
    )
    def test_push_pop(self, input_list, next_value, expected):
        heap = MinHeap()
        for x in input_list:
            heap.push(x)

        top = heap.push_pop(next_value)
        assert top == expected
