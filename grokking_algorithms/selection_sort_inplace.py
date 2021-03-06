# python -m unittest selection_sort_inplace.py

from typing import List
from unittest import TestCase


def selection_sort(items: List[int]) -> List[int]:
    for i in range(len(items)):
        smallest_index = i

        for j in range(i+1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j

        items[i], items[smallest_index] = items[smallest_index], items[i]

    return items


class TestSelectionSort(TestCase):
    def test_sort(self):
        items = [5, 3, 6, 2, 10]
        sorted_items = [2, 3, 5, 6, 10]
        self.assertEqual(selection_sort(items), sorted_items)

    def test_empty(self):
        items = []
        sorted_items = []

        self.assertEqual(selection_sort(items), sorted_items)
