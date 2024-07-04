class MinHeap:
    _data: list[int]

    def __init__(self) -> None:
        self._data = []

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def _swap(self, a: int, b: int) -> None:
        self._data[a], self._data[b] = self._data[b], self._data[a]

    def _sift_up(self, start: int) -> None:
        node = start

        while node > 0:
            parent = (node - 1) // 2

            if self._data[parent] <= self._data[node]:
                return

            self._swap(parent, node)
            node = parent

    def _sift_down(self, start: int) -> None:
        n = len(self._data)
        parent = start

        while True:
            child = parent * 2 + 1
            if child >= n:
                return

            if child + 1 < n and self._data[child + 1] < self._data[child]:
                child += 1

            if self._data[parent] <= self._data[child]:
                return

            self._swap(parent, child)
            parent = child

    def push(self, value: int) -> None:
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("pop from empty heap")

        self._swap(0, len(self._data) - 1)
        value = self._data.pop()
        self._sift_down(0)

        return value

    def push_pop(self, value: int) -> int:
        if self.is_empty() or value <= self._data[0]:
            return value

        top = self._data[0]
        self._data[0] = value
        self._sift_down(0)

        return top

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek on empty heap")

        return self._data[0]

    def clear(self) -> None:
        self._data = []

    def __len__(self) -> int:
        return len(self._data)
