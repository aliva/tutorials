from dataclasses import dataclass, field
from typing import Any, Optional
from unittest import TestCase


@dataclass
class Node:
    data: Any
    next: Optional["Node"] = field(default=None, init=False)


class LinkedList:
    def __init__(self) -> None:
        self._head: Optional[Node] = None

    def add_node(self, data):
        node = Node(data=data)

        if self._head is None:
            self._head = node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = node

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration()

        value = self._current.data
        self._current = self._current.next
        return value

class TestBinarySearch(TestCase):
    def test_list(self):
        items = [1, 5, 20]
        ll = LinkedList()
        for item in items:
            ll.add_node(item)

        list_items = list(ll)
        self.assertEqual(items, list_items)

    def test_empty(self):
        ll = LinkedList()
        list_items = list(ll)
        self.assertEqual(list_items, [])
