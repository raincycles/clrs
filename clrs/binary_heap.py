class MinHeap:
    _data: list[int]

    def __init__(self) -> None:
        self._data = []

    # O(1)
    def __len__(self) -> int:
        return len(self._data)

    # O(1)
    def is_empty(self) -> bool:
        return len(self) == 0

    # O(1)
    def _swap(self, a: int, b: int) -> None:
        (self._data[a], self._data[b]) = (
            self._data[b],
            self._data[a],
        )

    # O(log(n))
    def _sift_up(self, start: int) -> None:
        index = start

        while index > 0:
            parent_index = (index - 1) // 2

            if not self._data[parent_index] > self._data[index]:
                return

            self._swap(parent_index, index)
            index = parent_index

    # O(log(n))
    def _sift_down(self, start: int) -> None:
        n = len(self._data)
        index = start

        while True:
            child_index = index * 2 + 1

            if child_index >= n:
                return

            if (
                child_index + 1 < n
                and self._data[child_index] > self._data[child_index + 1]
            ):
                child_index += 1

            if not self._data[index] > self._data[child_index]:
                return

            self._swap(index, child_index)
            index = child_index

    # O(log(n))
    def push(self, value: int) -> None:
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    # O(log(n))
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("heap is empty")

        self._swap(0, len(self._data) - 1)
        top_value = self._data.pop()
        self._sift_down(0)

        return top_value

    # O(log(n))
    def push_pop(self, value: int) -> int:
        if self.is_empty() or not value > self._data[0]:
            return value

        top_value = self._data[0]
        self._data[0] = value
        self._sift_down(0)

        return top_value

    # O(1)
    def top(self) -> int:
        if self.is_empty():
            raise IndexError("heap is empty")

        return self._data[0]

    # O(1)
    def clear(self) -> None:
        self._data = []
