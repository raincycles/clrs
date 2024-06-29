class MinHeap:
    _data: list[int]

    def __init__(self) -> None:
        self._data = []

    def _sift_up(self, start: int) -> None:
        node = start

        while node > 0:
            parent = (node - 1) // 2

            if self._data[parent] <= self._data[node]:
                return

            self._data[parent], self._data[node] = self._data[node], self._data[parent]
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

            self._data[parent], self._data[child] = (
                self._data[child],
                self._data[parent],
            )
            parent = child

    def push(self, val: int) -> None:
        self._data.append(val)
        n = len(self._data)
        self._sift_up(n - 1)

    def pop(self) -> int:
        n = len(self._data)
        if n == 0:
            raise IndexError("pop from empty heap")

        self._data[0], self._data[n - 1] = self._data[n - 1], self._data[0]
        val = self._data.pop()
        self._sift_down(0)

        return val

    def peek(self) -> int:
        n = len(self._data)
        if n == 0:
            raise IndexError("peek on empty heap")

        return self._data[0]

    def clear(self) -> None:
        self._data = []

    def __len__(self) -> int:
        return len(self._data)
