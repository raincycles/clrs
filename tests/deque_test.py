from clrs.deque import Deque


class TestDeque:
    def test_push_and_pop(self):
        dq = Deque()

        dq.push_back(3)
        dq.push_back(4)

        assert dq.front() == 3
        assert dq.back() == 4

        dq.push_front(2)
        dq.push_front(1)

        assert dq.front() == 1
        assert dq.back() == 4

        assert len(dq) == 4

    def test_iteration(self):
        dq = Deque()

        dq.push_back(3)
        dq.push_back(4)

        dq.push_front(2)
        dq.push_front(1)

        assert list(dq) == [1, 2, 3, 4]
