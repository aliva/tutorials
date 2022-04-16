# python -m unittest selection_sort.py

from typing import List
from unittest import TestCase


def find_smallest_index(items: List[int]) -> int:
    smallest_index = 0
    smallest = items[smallest_index]

    for i in range(1, len(items)):
        if items[i] < smallest:
            smallest_index = i
            smallest = items[smallest_index]

    return smallest_index


def selection_sort(items: List[int]) -> List[int]:
    sorted_items = []

    while items:
        index = find_smallest_index(items)
        sorted_items.append(items.pop(index))

    return sorted_items


class TestSelectionSort(TestCase):
    def test_sort(self):
        items = [5, 3, 6, 2, 10]
        sorted_items = [2, 3, 5, 6, 10]
        self.assertEqual(selection_sort(items), sorted_items)

    def test_empty(self):
        items = []
        sorted_items = []

        self.assertEqual(selection_sort(items), sorted_items)
