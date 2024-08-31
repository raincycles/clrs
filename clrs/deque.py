from typing import Final, Iterator, cast


class Deque:
    DEFAULT_CAPACITY: Final = 8

    _buffer: list[int | None]
    _head: int
    _size: int

    def __init__(self) -> None:
        self._buffer = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._head = 0

    @property
    def _capacity(self) -> int:
        return len(self._buffer)

    # O(1)
    def __len__(self) -> int:
        return self._size

    # O(1)
    def is_empty(self) -> bool:
        return self._size == 0

    # NOTE: This is effectively the same as `(head + index) % capacity`.
    #
    # We translate the index like this to avoid unnecessarily converting to dynamically sized integers.
    # If you are implementing this in another language, this avoids overflow, which would break continuity.
    #
    def _translate_index(self, index: int) -> int:
        if index >= self._capacity - self._head:
            return index - (self._capacity - self._head)
        else:
            return self._head + index

    def __iter__(self) -> Iterator[int]:
        for i in range(self._size):
            actual_index = self._translate_index(i)
            yield cast(int, self._buffer[actual_index])

    # O(n)
    def _resize(self) -> None:
        new_capacity = self._capacity * 2
        new_buffer: list[int | None] = [None] * new_capacity

        for i, value in enumerate(self):
            new_buffer[i] = value

        self._buffer = new_buffer
        self._head = 0

    # O(1) or O(n) when full
    def push_back(self, value: int) -> None:
        if self._size == self._capacity:
            self._resize()

        index = self._translate_index(self._size)
        self._buffer[index] = value
        self._size += 1

    # O(1) or O(n) when full
    def push_front(self, value: int) -> None:
        if self._size == self._capacity:
            self._resize()

        if self._head == 0:
            self._head = self._capacity - 1
        else:
            self._head -= 1

        self._buffer[self._head] = value
        self._size += 1

    # O(1)
    def pop_back(self) -> int:
        if self.is_empty():
            raise IndexError("deque is empty")

        index = self._translate_index(self._size - 1)
        value = self._buffer[index]
        self._buffer[index] = None
        self._size -= 1

        return cast(int, value)

    # O(1)
    def pop_front(self) -> int:
        if self.is_empty():
            raise IndexError("deque is empty")

        value = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = self._translate_index(1)
        self._size -= 1

        return cast(int, value)

    # O(1)
    def back(self) -> int:
        if self.is_empty():
            raise IndexError("deque is empty")

        index = self._translate_index(self._size - 1)
        return cast(int, self._buffer[index])

    # O(1)
    def front(self) -> int:
        if self.is_empty():
            raise IndexError("deque is empty")

        return cast(int, self._buffer[self._head])

    # O(1)
    def get(self, index: int) -> int:
        if index >= self._size:
            raise IndexError("index out of range")

        actual_index = self._translate_index(index)
        return cast(int, self._buffer[actual_index])

    # O(1)
    def set(self, index: int, value: int) -> None:
        if index >= self._size:
            raise IndexError("index out of range")

        actual_index = self._translate_index(index)
        self._buffer[actual_index] = value

    # O(n)
    def clear(self) -> None:
        for i in range(self._size):
            actual_index = self._translate_index(i)
            self._buffer[actual_index] = None

        self._head = 0
        self._size = 0
