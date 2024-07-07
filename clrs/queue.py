from typing import Iterator, cast


class Queue:
    _buffer: list[int | None]
    _head: int
    _tail: int
    _size: int

    def __init__(self, capacity=4) -> None:
        self._buffer = [None] * capacity
        self._size = 0
        self._head = 0
        self._tail = 0

    @property
    def _capacity(self) -> int:
        return len(self._buffer)

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def _next_index(self, index: int) -> int:
        next_index = index + 1
        return next_index if next_index != self._capacity else 0

    def __iter__(self) -> Iterator[int]:
        i = self._head
        for _ in range(self._size):
            yield cast(int, self._buffer[i])
            i = self._next_index(i)

    def _grow(self) -> None:
        new_capacity = max(self._capacity * 2, 4)
        new_buffer: list[int | None] = [None] * new_capacity

        for i, value in enumerate(self):
            new_buffer[i] = value

        self._buffer = new_buffer
        self._head = 0
        self._tail = self._size

    def push(self, value: int) -> None:
        if self._size == self._capacity:
            self._grow()

        self._buffer[self._tail] = value
        self._tail = self._next_index(self._tail)
        self._size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("queue is empty")

        value = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = self._next_index(self._head)
        self._size -= 1
        return cast(int, value)

    def front(self) -> int:
        if self.is_empty():
            raise IndexError("queue is empty")

        return cast(int, self._buffer[self._head])

    def clear(self) -> None:
        i = self._head
        for _ in range(self._size):
            self._buffer[i] = None
            i = self._next_index(i)

        self._size = 0
        self._head = 0
        self._tail = 0
