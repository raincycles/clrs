from typing import Final, Iterator, cast


class Deque:
    DEFAULT_CAPACITY: Final = 8

    _buffer: list[int | None]
    _head: int
    _tail: int
    _size: int

    def __init__(self) -> None:
        self._buffer = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._head = 0
        self._tail = 0

    @property
    def _capacity(self) -> int:
        return len(self._buffer)

    # O(1)
    def __len__(self) -> int:
        return self._size

    # O(1)
    def is_empty(self) -> bool:
        return self._size == 0

    # O(1)
    def _next_index(self, index: int) -> int:
        return index + 1 if index != self._capacity - 1 else 0

    # O(1)
    def _prev_index(self, index: int) -> int:
        return index - 1 if index != 0 else self._capacity - 1

    def __iter__(self) -> Iterator[int]:
        index = self._head
        while True:
            yield cast(int, self._buffer[index])

            index = self._next_index(index)
            if index == self._tail:
                break

    # O(n)
    def _expand(self) -> None:
        new_capacity = self._capacity * 2
        new_buffer: list[int | None] = [None] * new_capacity

        index = 0
        for value in self:
            new_buffer[index] = value
            index += 1

        self._buffer = new_buffer
        self._head = 0
        self._tail = self._size

    # O(1) or O(n) when full
    def push_back(self, value: int) -> None:
        if self._size == self._capacity:
            self._expand()

        self._buffer[self._tail] = value
        self._tail = self._next_index(self._tail)
        self._size += 1

    # O(1) or O(n) when full
    def push_front(self, value: int) -> None:
        if self._size == self._capacity:
            self._expand()

        self._head = self._prev_index(self._head)
        self._buffer[self._head] = value
        self._size += 1

    # O(1)
    def pop_back(self) -> int:
        if self.is_empty():
            raise IndexError("deque is empty")

        self._tail = self._prev_index(self._tail)
        value = self._buffer[self._tail]
        self._buffer[self._tail] = None
        self._size -= 1

        return cast(int, value)

    # O(1)
    def pop_front(self) -> int:
        if self.is_empty():
            raise IndexError("deque is empty")

        value = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = self._next_index(self._head)
        self._size -= 1

        return cast(int, value)

    # O(1)
    def back(self) -> int:
        if self.is_empty():
            raise IndexError("deque is empty")

        last_index = self._prev_index(self._tail)
        return cast(int, self._buffer[last_index])

    # O(1)
    def front(self) -> int:
        if self.is_empty():
            raise IndexError("deque is empty")

        return cast(int, self._buffer[self._head])

    # O(n)
    def clear(self) -> None:
        for i in range(self._capacity):
            self._buffer[i] = None

        self._head = 0
        self._tail = 0
        self._size = 0
