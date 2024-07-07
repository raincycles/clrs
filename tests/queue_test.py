import pytest

from clrs.queue import Queue


class TestQueue:
    @pytest.mark.parametrize("input_list", [([5]), ([1, 2, 3, 4, 5])])
    def test_push_and_pop(self, input_list):
        queue = Queue()

        for x in input_list:
            queue.push(x)

        assert queue.front() == input_list[0]

        for x in input_list:
            assert x == queue.pop()

        assert len(queue) == 0

    @pytest.mark.parametrize("input_list", [([5]), ([1, 2, 3, 4, 5])])
    def test_iteration(self, input_list):
        queue = Queue()

        for x in input_list:
            queue.push(x)

        for a, b in zip(queue, input_list):
            assert a == b
