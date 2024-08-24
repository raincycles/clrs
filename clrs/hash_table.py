from dataclasses import dataclass
from typing import Final, Iterator, cast


# FNV-1a 32 bit
def hash_str(value: str) -> int:
    OFFSET_BASIS: Final = 2166136261
    PRIME: Final = 16777619
    UINT32_MAX: Final = (1 << 32) - 1

    value_bytes = value.encode()
    result = OFFSET_BASIS

    for b in value_bytes:
        result ^= b
        result *= PRIME
        # handle overflow
        result &= UINT32_MAX

    return result


@dataclass
class Entry:
    key: str
    value: int
    offset: int


class HashTable:
    DEFAULT_CAPACITY: Final = 16
    MAX_LOAD_FACTOR: Final = 0.75

    _entries: list[Entry | None]
    _size: int

    def __init__(self) -> None:
        self._entries = [None] * self.DEFAULT_CAPACITY
        self._size = 0

    @property
    def _capacity(self) -> int:
        return len(self._entries)

    @property
    def _load_factor(self) -> float:
        return self._size / self._capacity

    # O(1)
    def __len__(self) -> int:
        return self._size

    # O(1)
    def is_empty(self) -> bool:
        return len(self) == 0

    # O(cap)
    def _resize(self) -> None:
        old_entries = self._entries

        new_capacity = self._capacity * 2
        self._entries = [None] * new_capacity
        self._size = 0

        for entry in old_entries:
            if entry is not None:
                self.insert(entry.key, entry.value)

    # Average: O(1)
    # Worst: O(n)
    def insert(self, key: str, value: int) -> None:
        index = hash_str(key) % self._capacity
        candidate = Entry(key, value, offset=0)

        while True:
            entry = self._entries[index]

            if entry is None:
                break

            if entry.key == key:
                entry.value = value
                return

            if candidate.offset > entry.offset:
                self._entries[index] = candidate
                candidate = entry

            candidate.offset += 1
            index = (index + 1) % self._capacity

        self._entries[index] = candidate
        self._size += 1

        if self._load_factor > self.MAX_LOAD_FACTOR:
            self._resize()

    # Average: O(1)
    # Worst: O(n)
    def _find_index(self, key: str) -> int | None:
        index = hash_str(key) % self._capacity
        offset = 0

        while True:
            entry = self._entries[index]

            if entry is None or offset > entry.offset:
                return None

            if entry.key == key:
                return index

            offset += 1
            index = (index + 1) % self._capacity

    # Average: O(1)
    # Worst: O(n)
    def get(self, key: str) -> int:
        index = self._find_index(key)
        if index is None:
            raise KeyError("key not found")

        return cast(Entry, self._entries[index]).value

    # Average: O(1)
    # Worst: O(n)
    def contains(self, key: str) -> bool:
        index = self._find_index(key)
        return index is not None

    # Average: O(1)
    # Worst: O(n)
    def remove(self, key: str) -> None:
        index = self._find_index(key)
        if index is None:
            return

        self._entries[index] = None
        self._size -= 1

        while True:
            next_index = (index + 1) % self._capacity
            next_entry = self._entries[next_index]

            if next_entry is None or next_entry.offset == 0:
                return

            self._entries[index] = next_entry
            self._entries[next_index] = None
            next_entry.offset -= 1

            index = next_index

    # results are unordered
    def __iter__(self) -> Iterator[tuple[str, int]]:
        for entry in self._entries:
            if entry is not None:
                yield (entry.key, entry.value)

    # O(cap)
    def clear(self) -> None:
        for i in range(self._capacity):
            self._entries[i] = None

        self._size = 0
