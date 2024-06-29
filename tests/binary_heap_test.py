import pytest

from clrs.binary_heap import MinHeap


class TestMinHeap:
    def test_push(self):
        heap = MinHeap()
        heap.push(3)
        heap.push(2)
        heap.push(5)
        assert heap.peek() == 2

    def test_pop(self):
        heap = MinHeap()
        heap.push(3)
        heap.push(2)
        heap.push(5)

        assert heap.pop() == 2
        assert heap.pop() == 3
        assert heap.pop() == 5

    def test_peek(self):
        heap = MinHeap()

        with pytest.raises(IndexError):
            heap.peek()

        heap.push(5)
        assert heap.peek() == 5
        heap.push(2)
        assert heap.peek() == 2
        heap.push(3)
        assert heap.peek() == 2
