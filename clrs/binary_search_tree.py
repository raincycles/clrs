from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator


@dataclass
class BSTNode:
    value: int
    left: BSTNode | None = None
    right: BSTNode | None = None


# Worst: h = n
# Average: h = log(n)
class BinarySearchTree:
    _root: BSTNode | None
    _size: int

    def __init__(self) -> None:
        self._root = None
        self._size = 0

    # O(1)
    def is_empty(self) -> bool:
        return self._root is None

    # O(1)
    def __len__(self) -> int:
        return self._size

    # O(h)
    def insert(self, value: int) -> None:
        parent: BSTNode | None = None
        node = self._root
        was_left_child = False

        while node is not None:
            parent = node

            if node.value > value:
                node = node.left
                was_left_child = True
            elif node.value < value:
                node = node.right
                was_left_child = False
            else:
                return

        new_node = BSTNode(value)
        self._size += 1

        if parent is None:
            self._root = new_node
            return

        if was_left_child:
            parent.left = new_node
        else:
            parent.right = new_node

    # O(h)
    def contains(self, value: int) -> bool:
        node = self._root

        while node is not None:
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
            else:
                return True

        return False

    # O(n)
    def __iter__(self) -> Iterator[int]:
        stack: list[BSTNode] = []
        node = self._root

        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            yield node.value
            node = node.right

    # O(h)
    def _find_min_node(self, start: BSTNode) -> BSTNode:
        node = start
        while node.left is not None:
            node = node.left

        return node

    # O(h)
    def min(self) -> int:
        if self._root is None:
            raise IndexError("tree is empty")

        node = self._find_min_node(self._root)
        return node.value

    # O(h)
    def _find_max_node(self, start: BSTNode) -> BSTNode:
        node = start
        while node.right is not None:
            node = node.right

        return node

    # O(h)
    def max(self) -> int:
        if self._root is None:
            raise IndexError("tree is empty")

        node = self._find_max_node(self._root)
        return node.value

    # O(1)
    def _replace_node(
        self,
        parent: BSTNode | None,
        source: BSTNode,
        target: BSTNode | None,
    ) -> None:
        if parent is None:
            self._root = target
        elif source is parent.left:
            parent.left = target
        else:
            parent.right = target

    # O(h)
    def remove(self, value: int) -> None:
        parent: BSTNode | None = None
        node = self._root

        while node is not None and node.value != value:
            parent = node

            if node.value > value:
                node = node.left
            else:
                node = node.right

        if node is None:
            return

        self._size -= 1

        if node.left is None:
            self._replace_node(parent, node, node.right)
        elif node.right is None:
            self._replace_node(parent, node, node.left)
        else:
            next_parent: BSTNode = node
            next = node.right

            while next.left is not None:
                next_parent = next
                next = next.left

            node.value = next.value
            self._replace_node(next_parent, next, next.right)

    # O(h)
    def next_nearest(self, value: int) -> int | None:
        nearest: BSTNode | None = None
        node = self._root

        while node is not None:
            if node.value > value:
                nearest = node
                node = node.left
            else:
                node = node.right

        if nearest is None:
            return None

        return nearest.value

    # O(h)
    def prev_nearest(self, value: int) -> int | None:
        nearest: BSTNode | None = None
        node = self._root

        while node is not None:
            if node.value < value:
                nearest = node
                node = node.right
            else:
                node = node.left

        if nearest is None:
            return None

        return nearest.value

    # O(1)
    def clear(self) -> None:
        self._root = None
        self._size = 0
