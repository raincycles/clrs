import pytest

from clrs.linked_list import LinkedList


# TODO: make more tests
class TestLinkedList:
    @pytest.mark.parametrize(
        "input_list",
        [
            ([5]),
            ([2, 5]),
            ([1, 2, 3, 4, 5]),
        ],
    )
    def test_reverse(self, input_list):
        linked_list = LinkedList()

        for x in input_list:
            linked_list.push_back(x)

        linked_list.reverse()

        for a, b in zip(linked_list, reversed(input_list)):
            assert a == b
