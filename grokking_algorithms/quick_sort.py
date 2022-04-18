# python -m unittest quick_sort.py

from typing import List
from unittest import TestCase




def quick_sort(items: List[int]) -> List[int]:
    if len(items) < 2:
        return items
    else:
        pivot = items[0]
        less = [i for i in items[1:] if  i <= pivot]
        greater = [i for i in items[1:] if  i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


class TestQuickSort(TestCase):
    def test_sort(self):
        items = [5, 3, 6, 2, 10]
        sorted_items = [2, 3, 5, 6, 10]
        self.assertEqual(quick_sort(items), sorted_items)

    def test_empty(self):
        items = []
        sorted_items = []

        self.assertEqual(quick_sort(items), sorted_items)

