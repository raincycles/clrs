from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator


@dataclass
class Node:
    value: int
    prev: Node | None = None
    next: Node | None = None


class LinkedList:
    _head: Node | None
    _tail: Node | None
    _size: int

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    # O(1)
    def __len__(self) -> int:
        return self._size

    # O(1)
    def is_empty(self) -> bool:
        return self._head is None

    # O(1)
    def push_front(self, value: int) -> None:
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._size += 1

    # O(1)
    def push_back(self, value: int) -> None:
        new_node = Node(value)

        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    # O(1)
    def pop_front(self) -> int:
        if self._head is None:
            raise IndexError("list is empty")

        value = self._head.value
        next_node = self._head.next

        if next_node is not None:
            next_node.prev = None
        else:
            self._tail = None

        self._head = next_node
        self._size -= 1

        return value

    # O(1)
    def pop_back(self) -> int:
        if self._tail is None:
            raise IndexError("list is empty")

        value = self._tail.value
        prev_node = self._tail.prev

        if prev_node is not None:
            prev_node.next = None
        else:
            self._head = None

        self._tail = prev_node
        self._size -= 1

        return value

    # O(1)
    def front(self) -> int:
        if self._head is None:
            raise IndexError("list is empty")

        return self._head.value

    # O(1)
    def back(self) -> int:
        if self._tail is None:
            raise IndexError("list is empty")

        return self._tail.value

    # O(n)
    def reverse(self) -> None:
        node = self._head
        while node is not None:
            next_node = node.next
            node.next = node.prev
            node.prev = next_node
            node = next_node

        head_node = self._head
        self._head = self._tail
        self._tail = head_node

    # O(n)
    def _node_at(self, index: int) -> Node:
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")

        count = 0
        node = self._head
        while node is not None:
            if count == index:
                return node

            count += 1
            node = node.next

        assert False, "unreachable"

    # O(n)
    def insert_after(self, index: int, value: int) -> None:
        node = self._node_at(index)
        new_node = Node(value, prev=node, next=node.next)

        next_node = node.next
        node.next = new_node

        if next_node is not None:
            next_node.prev = new_node
        else:
            self._tail = new_node

        self._size += 1

    # O(n)
    def insert_before(self, index: int, value: int) -> None:
        node = self._node_at(index)
        new_node = Node(value, prev=node.prev, next=node)

        prev_node = node.prev
        node.prev = new_node

        if prev_node is not None:
            prev_node.next = new_node
        else:
            self._head = new_node

        self._size += 1

    # O(1)
    def _remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        if prev_node is None:
            self.pop_front()
            return

        if next_node is None:
            self.pop_back()
            return

        prev_node.next = next_node
        next_node.prev = prev_node
        self._size -= 1

    # O(n)
    def remove_at(self, index: int) -> None:
        node = self._node_at(index)
        self._remove_node(node)

    def __iter__(self) -> Iterator[int]:
        node = self._head
        while node is not None:
            yield node.value
            node = node.next

    # O(1)
    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
